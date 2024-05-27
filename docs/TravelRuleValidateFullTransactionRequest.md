# TravelRuleValidateFullTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_asset** | **str** | The asset involved in the transaction | [optional] 
**transaction_amount** | **str** | The amount of the transaction | [optional] 
**originator_did** | **str** | The DID of the transaction originator | [optional] 
**beneficiary_did** | **str** | The DID of the transaction beneficiary | [optional] 
**originator_vas_pdid** | **str** | The VASP ID of the transaction originator | [optional] 
**beneficiary_vas_pdid** | **str** | The VASP ID of the transaction beneficiary | [optional] 
**beneficiary_vas_pname** | **str** | The name of the VASP acting as the beneficiary | [optional] 
**transaction_blockchain_info** | [**TravelRuleTransactionBlockchainInfo**](TravelRuleTransactionBlockchainInfo.md) | Information about the blockchain transaction | [optional] 
**originator** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | Information about the originator of the transaction | 
**beneficiary** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | Information about the beneficiary of the transaction | 
**encrypted** | **str** | Encrypted data related to the transaction | [optional] 
**protocol** | **str** | The protocol used to perform the travel rule | [optional] 
**notification_email** | **str** | The email address where a notification should be sent upon completion of the travel rule | [optional] 
**skip_beneficiary_data_validation** | **bool** | Whether to skip validation of beneficiary data | [optional] 
**travel_rule_behavior** | **bool** | Whether to check if the transaction is a TRAVEL_RULE in the beneficiary VASP&#39;s jurisdiction | [optional] 
**originator_proof** | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) | Ownership proof related to the originator of the transaction | [optional] 
**beneficiary_proof** | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) | Ownership proof related to the beneficiary of the transaction | [optional] 
**pii** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | Personal identifiable information related to the transaction | [optional] 

## Example

```python
from fireblocks_client.models.travel_rule_validate_full_transaction_request import TravelRuleValidateFullTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateFullTransactionRequest from a JSON string
travel_rule_validate_full_transaction_request_instance = TravelRuleValidateFullTransactionRequest.from_json(json)
# print the JSON string representation of the object
print TravelRuleValidateFullTransactionRequest.to_json()

# convert the object into a dict
travel_rule_validate_full_transaction_request_dict = travel_rule_validate_full_transaction_request_instance.to_dict()
# create an instance of TravelRuleValidateFullTransactionRequest from a dict
travel_rule_validate_full_transaction_request_form_dict = travel_rule_validate_full_transaction_request.from_dict(travel_rule_validate_full_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


