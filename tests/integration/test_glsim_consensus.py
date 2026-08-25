from __future__ import annotations
import json
from pathlib import Path
from gltest import get_contract_factory, get_validator_factory
from gltest.assertions import tx_execution_succeeded
from gltest.types import TransactionStatus
from gltest.utils import extract_contract_address

PROMPT = "independently review sponsored-content disclosure"
ARGS = ["Northwind supplied a helmet and paid a fixed fee while leaving editorial control with the reviewer.", "A disclosure must plainly identify payment or a free product and appear with the endorsement.", "Paid partnership with Northwind. I tested its helmet for three weeks and the straps slipped."]

def context():
    validators = get_validator_factory().batch_create_mock_validators(5, mock_llm_response={"nondet_exec_prompt": {PROMPT: json.dumps({"decision": "CLEAR_DISCLOSURE"})}})
    return {"validators": [v.to_dict() for v in validators]}

def test_five_validator_clearance_lifecycle():
    factory = get_contract_factory(contract_file_path=Path(__file__).resolve().parents[2] / "contracts" / "ad_disclosure_check.py")
    deployed = factory.deploy_contract_tx(args=ARGS, wait_transaction_status=TransactionStatus.FINALIZED)
    assert tx_execution_succeeded(deployed)
    contract = factory.build_contract(extract_contract_address(deployed))
    reviewed = contract.review_current_revision(args=[]).transact(transaction_context=context(), wait_transaction_status=TransactionStatus.FINALIZED)
    assert tx_execution_succeeded(reviewed)
    assert contract.get_state(args=[]).call()["phase"] == "CLEARED"

