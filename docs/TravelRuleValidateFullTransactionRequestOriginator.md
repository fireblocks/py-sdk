# TravelRuleValidateFullTransactionRequestOriginator

Information about the originator of the transaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**date_of_birth** | **str** |  | 
**place_of_birth** | **str** |  | 
**address** | **str** |  | 
**identification_number** | **str** |  | 
**nationality** | **str** |  | 
**country_of_residence** | **str** |  | 
**tax_identification_number** | **str** |  | 
**customer_number** | **str** |  | 

## Example

```python
from fireblocks_client.models.travel_rule_validate_full_transaction_request_originator import TravelRuleValidateFullTransactionRequestOriginator

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateFullTransactionRequestOriginator from a JSON string
travel_rule_validate_full_transaction_request_originator_instance = TravelRuleValidateFullTransactionRequestOriginator.from_json(json)
# print the JSON string representation of the object
print TravelRuleValidateFullTransactionRequestOriginator.to_json()

# convert the object into a dict
travel_rule_validate_full_transaction_request_originator_dict = travel_rule_validate_full_transaction_request_originator_instance.to_dict()
# create an instance of TravelRuleValidateFullTransactionRequestOriginator from a dict
travel_rule_validate_full_transaction_request_originator_form_dict = travel_rule_validate_full_transaction_request_originator.from_dict(travel_rule_validate_full_transaction_request_originator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


