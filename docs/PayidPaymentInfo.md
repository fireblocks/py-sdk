# PayidPaymentInfo

PayID payment information for Australian dollar transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for PayID transfers | 
**addressing_system** | **str** | The addressing system used for PayID transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**value** | **str** | The PayID identifier (email, phone, ABN, or organization ID) | 
**type** | **str** | The type of PayID being used | 
**bsb** | **str** | Bank State Branch (BSB) number (6 digits, format XXX-XXX) | [optional] 
**account_number** | **str** | Australian bank account number | 

## Example

```python
from fireblocks.models.payid_payment_info import PayidPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayidPaymentInfo from a JSON string
payid_payment_info_instance = PayidPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(PayidPaymentInfo.to_json())

# convert the object into a dict
payid_payment_info_dict = payid_payment_info_instance.to_dict()
# create an instance of PayidPaymentInfo from a dict
payid_payment_info_from_dict = PayidPaymentInfo.from_dict(payid_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


