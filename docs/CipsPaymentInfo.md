# CipsPaymentInfo

CIPS payment information for Cross-Border Interbank Payment System transfers (CNY)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for CIPS transfers | 
**addressing_system** | **str** | The addressing system used for CIPS transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | [optional] 
**bank_name** | **str** | Name of the recipient&#39;s bank | 
**bank_country** | **str** | ISO 3166-1 alpha-2 country code of the bank | 
**swift_code** | **str** | SWIFT/BIC code of the recipient bank | 
**account_number** | **str** | Recipient bank account number | 
**reference_id** | **str** | Optional payment reference | [optional] 

## Example

```python
from fireblocks.models.cips_payment_info import CipsPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CipsPaymentInfo from a JSON string
cips_payment_info_instance = CipsPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(CipsPaymentInfo.to_json())

# convert the object into a dict
cips_payment_info_dict = cips_payment_info_instance.to_dict()
# create an instance of CipsPaymentInfo from a dict
cips_payment_info_from_dict = CipsPaymentInfo.from_dict(cips_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


