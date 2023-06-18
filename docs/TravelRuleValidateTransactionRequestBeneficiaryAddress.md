# TravelRuleValidateTransactionRequestBeneficiaryAddress

Beneficiary  name

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Street address | 
**city** | **str** | City | 
**state** | **str** | State or province | 
**postal_code** | **str** | Postal or ZIP code | 

## Example

```python
from fireblocks_client.models.travel_rule_validate_transaction_request_beneficiary_address import TravelRuleValidateTransactionRequestBeneficiaryAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateTransactionRequestBeneficiaryAddress from a JSON string
travel_rule_validate_transaction_request_beneficiary_address_instance = TravelRuleValidateTransactionRequestBeneficiaryAddress.from_json(json)
# print the JSON string representation of the object
print TravelRuleValidateTransactionRequestBeneficiaryAddress.to_json()

# convert the object into a dict
travel_rule_validate_transaction_request_beneficiary_address_dict = travel_rule_validate_transaction_request_beneficiary_address_instance.to_dict()
# create an instance of TravelRuleValidateTransactionRequestBeneficiaryAddress from a dict
travel_rule_validate_transaction_request_beneficiary_address_form_dict = travel_rule_validate_transaction_request_beneficiary_address.from_dict(travel_rule_validate_transaction_request_beneficiary_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


