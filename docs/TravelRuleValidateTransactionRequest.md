# TravelRuleValidateTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_asset** | **str** | Transaction asset symbol BTC,ETH) | 
**destination** | **str** | Transaction destination address | 
**transaction_amount** | **str** | Transaction amount in the transaction asset | 
**originator_vas_pdid** | **str** | This is the identifier assigned to your VASP | 
**originator_equals_beneficiary** | **bool** | \&quot;True\&quot; if the originator and beneficiary is the same person and you therefore do not need to collect any information. \&quot;False\&quot; if it is a third-party transfer. | 
**travel_rule_behavior** | **bool** | This will also check if the transaction is a TRAVEL_RULE in the beneficiary VASP&#39;s jurisdiction | [optional] 
**beneficiary_vas_pdid** | **str** | This is the identifier assigned to the VASP the funds are being sent to | [optional] 
**beneficiary_vas_pname** | **str** | Beneficiary VASP name | [optional] 
**beneficiary_name** | **str** | Beneficiary  name | [optional] 
**beneficiary_account_number** | **str** | Beneficiary  name | [optional] 
**beneficiary_address** | [**TravelRuleAddress**](TravelRuleAddress.md) | Beneficiary  name | [optional] 

## Example

```python
from fireblocks_client.models.travel_rule_validate_transaction_request import TravelRuleValidateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateTransactionRequest from a JSON string
travel_rule_validate_transaction_request_instance = TravelRuleValidateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateTransactionRequest.to_json())

# convert the object into a dict
travel_rule_validate_transaction_request_dict = travel_rule_validate_transaction_request_instance.to_dict()
# create an instance of TravelRuleValidateTransactionRequest from a dict
travel_rule_validate_transaction_request_from_dict = TravelRuleValidateTransactionRequest.from_dict(travel_rule_validate_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


