# FpsUkPaymentInfo

FPS UK payment information for UK Faster Payments transfers (GBP)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for UK Faster Payments transfers | 
**addressing_system** | **str** | The addressing system used for UK Faster Payments transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**account_number** | **str** | UK bank account number | 
**sort_code** | **str** | UK sort code (format XX-XX-XX) | 
**bank_account_country** | **str** | ISO 3166-1 alpha-2 country code of the bank account | [optional] 

## Example

```python
from fireblocks.models.fps_uk_payment_info import FpsUkPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FpsUkPaymentInfo from a JSON string
fps_uk_payment_info_instance = FpsUkPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(FpsUkPaymentInfo.to_json())

# convert the object into a dict
fps_uk_payment_info_dict = fps_uk_payment_info_instance.to_dict()
# create an instance of FpsUkPaymentInfo from a dict
fps_uk_payment_info_from_dict = FpsUkPaymentInfo.from_dict(fps_uk_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


