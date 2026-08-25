from pathlib import Path
import pytest
from gltest import get_contract_factory
from gltest.assertions import tx_execution_succeeded
from gltest.types import TransactionStatus
from gltest.utils import extract_contract_address

ARGS = ["Northwind supplied a helmet and paid a fixed fee while leaving editorial control with the reviewer.", "A disclosure must plainly identify payment or a free product and appear with the endorsement.", "Paid partnership with Northwind. Northwind supplied this helmet and paid a fixed fee. After three weeks, the straps slipped."]

@pytest.mark.integration
def test_studionet_revision_review(default_account):
    factory = get_contract_factory(contract_file_path=Path(__file__).resolve().parents[2] / "contracts" / "ad_disclosure_check.py")
    deployed = factory.deploy_contract_tx(args=ARGS, account=default_account, wait_transaction_status=TransactionStatus.FINALIZED)
    assert tx_execution_succeeded(deployed)
    address = extract_contract_address(deployed)
    contract = factory.build_contract(address, account=default_account)
    reviewed = contract.review_current_revision(args=[]).transact(wait_transaction_status=TransactionStatus.FINALIZED)
    assert tx_execution_succeeded(reviewed)
    state = contract.get_state(args=[]).call()
    assert state["decision"] in ("CLEAR_DISCLOSURE", "AMBIGUOUS_DISCLOSURE", "MISSING_DISCLOSURE")
    assert contract.get_policy(args=[]).call()["schema"] == "ad-disclosure-check/policy/v2"
    print(f"STUDIONET_ADDRESS={address}")
    print(f"STUDIONET_DEPLOY_TX={deployed['hash']}")
    print(f"STUDIONET_WRITE_TX={reviewed['hash']}")
    print(f"STUDIONET_RESULT={state['decision']}")

