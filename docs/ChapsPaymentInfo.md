# ChapsPaymentInfo

CHAPS payment information for UK pound sterling same-day transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for CHAPS transfers | 
**addressing_system** | **str** | The addressing system used for CHAPS transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**sort_code** | **str** | UK bank sort code (format XX-XX-XX) | 
**account_number** | **str** | UK bank account number | 
**bank_name** | **str** | The name of the bank | [optional] 
**bank_account_country** | **str** | CHAPS bank account holder name | 
**bank_account_holder_name** | **str** | CHAPS bank account holder name | 

## Example

```python
from fireblocks.models.chaps_payment_info import ChapsPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChapsPaymentInfo from a JSON string
chaps_payment_info_instance = ChapsPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(ChapsPaymentInfo.to_json())

# convert the object into a dict
chaps_payment_info_dict = chaps_payment_info_instance.to_dict()
# create an instance of ChapsPaymentInfo from a dict
chaps_payment_info_from_dict = ChapsPaymentInfo.from_dict(chaps_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


