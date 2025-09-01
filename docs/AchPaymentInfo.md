# AchPaymentInfo

ACH payment information for US Automated Clearing House transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for ACH transfers | 
**addressing_system** | **str** | The addressing system used for ACH transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**account_number** | **str** | The bank account number | 
**routing_number** | **str** | The bank routing number (ABA routing number) | 
**account_type** | **str** | The type of bank account | 

## Example

```python
from fireblocks.models.ach_payment_info import AchPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AchPaymentInfo from a JSON string
ach_payment_info_instance = AchPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(AchPaymentInfo.to_json())

# convert the object into a dict
ach_payment_info_dict = ach_payment_info_instance.to_dict()
# create an instance of AchPaymentInfo from a dict
ach_payment_info_from_dict = AchPaymentInfo.from_dict(ach_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


