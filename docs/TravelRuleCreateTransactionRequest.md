# TravelRuleCreateTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator_vas_pdid** | **str** | The VASP ID of the transaction originator | [optional] 
**beneficiary_vas_pdid** | **str** | The VASP ID of the transaction beneficiary | [optional] 
**beneficiary_vas_pname** | **str** | The name of the VASP acting as the beneficiary | [optional] 
**transaction_blockchain_info** | [**TravelRuleTransactionBlockchainInfo**](TravelRuleTransactionBlockchainInfo.md) | Information about the blockchain transaction | [optional] 
**originator** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | Information about the originator of the transaction | 
**beneficiary** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | Information about the beneficiary of the transaction | 
**encrypted** | **str** | Encrypted data related to the transaction | [optional] 
**protocol** | **str** | The protocol used to perform the travel rule | [optional] 
**skip_beneficiary_data_validation** | **bool** | Whether to skip validation of beneficiary data | [optional] 
**travel_rule_behavior** | **bool** | Whether to check if the transaction is a TRAVEL_RULE in the beneficiary VASP&#39;s jurisdiction | [optional] 
**originator_proof** | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) | Ownership proof related to the originator of the transaction | [optional] 
**beneficiary_proof** | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) | Ownership proof related to the beneficiary of the transaction | [optional] 
**pii** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) | Personal identifiable information related to the transaction | [optional] 

## Example

```python
from fireblocks_client.models.travel_rule_create_transaction_request import TravelRuleCreateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleCreateTransactionRequest from a JSON string
travel_rule_create_transaction_request_instance = TravelRuleCreateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TravelRuleCreateTransactionRequest.to_json())

# convert the object into a dict
travel_rule_create_transaction_request_dict = travel_rule_create_transaction_request_instance.to_dict()
# create an instance of TravelRuleCreateTransactionRequest from a dict
travel_rule_create_transaction_request_from_dict = TravelRuleCreateTransactionRequest.from_dict(travel_rule_create_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


