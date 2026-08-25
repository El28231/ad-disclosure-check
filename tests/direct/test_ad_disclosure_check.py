from pathlib import Path
import json

CONTRACT = Path(__file__).resolve().parents[2] / "contracts" / "ad_disclosure_check.py"
SDK = "v0.2.16"
PROMPT = "independently review sponsored-content disclosure"
ARGS = (
    "Northwind supplied a helmet and paid a fixed fee while leaving editorial control with the reviewer.",
    "A disclosure must plainly identify payment or a free product and appear with the endorsement.",
    "I tested the Northwind helmet for three weeks. The ventilation was good, but the straps slipped.",
)


def deploy(vm, direct_deploy, alice):
    vm.sender = alice
    return direct_deploy(str(CONTRACT), *ARGS, sdk_version=SDK)


def test_revision_clearance_lifecycle_and_validator_replay(direct_vm, direct_deploy, direct_alice):
    contract = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.mock_llm(PROMPT, json.dumps({"decision": "MISSING_DISCLOSURE"}))
    contract.review_current_revision()
    assert contract.get_state()["phase"] == "NEEDS_REVISION"
    contract.submit_revision("Paid partnership with Northwind. I tested its helmet for three weeks and found that the straps slipped.")
    direct_vm.clear_mocks()
    direct_vm.mock_llm(PROMPT, json.dumps({"decision": "CLEAR_DISCLOSURE"}))
    contract.review_current_revision()
    assert contract.get_state()["phase"] == "CLEARED"
    assert contract.get_revision(1).startswith("Paid partnership")
    leader = direct_vm._captured_validators[-1][0]
    assert direct_vm.run_validator(leader_result=leader) is True
    direct_vm.clear_mocks()
    direct_vm.mock_llm(PROMPT, json.dumps({"decision": "AMBIGUOUS_DISCLOSURE"}))
    assert direct_vm.run_validator(leader_result=leader) is False


def test_only_creator_can_submit_requested_revision(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.mock_llm(PROMPT, json.dumps({"decision": "MISSING_DISCLOSURE"}))
    contract.review_current_revision()
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("only_creator"):
        contract.submit_revision("Paid partnership. This replacement text is long enough for contract validation.")


def test_malformed_model_output_fails_closed(direct_vm, direct_deploy, direct_alice):
    contract = deploy(direct_vm, direct_deploy, direct_alice)
    direct_vm.mock_llm(PROMPT, json.dumps({"decision": "CLEAR_DISCLOSURE", "reason": "extra"}))
    with direct_vm.expect_revert("invalid_response_shape"):
        contract.review_current_revision()
    assert contract.get_state()["phase"] == "READY_FOR_REVIEW"

