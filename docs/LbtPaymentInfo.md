# LbtPaymentInfo

LBT (Lebanese Bank Transfer) payment information for Lebanese bank transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for Lebanese bank transfers | 
**addressing_system** | **str** | The addressing system used for Lebanese bank transfers (Bank Account Number) | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**account_number** | **str** | The bank account number | 
**bank_name** | **str** | The name of the bank | 
**bank_code** | **str** | The bank code or identifier | 

## Example

```python
from fireblocks.models.lbt_payment_info import LbtPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LbtPaymentInfo from a JSON string
lbt_payment_info_instance = LbtPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(LbtPaymentInfo.to_json())

# convert the object into a dict
lbt_payment_info_dict = lbt_payment_info_instance.to_dict()
# create an instance of LbtPaymentInfo from a dict
lbt_payment_info_from_dict = LbtPaymentInfo.from_dict(lbt_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


