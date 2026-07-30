# InstaPayPaymentInfo

InstaPay payment information for Philippine instant payment transfers (PHP)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for InstaPay transfers | 
**addressing_system** | **str** | The addressing system used for InstaPay transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**account_number** | **str** | Recipient bank account or wallet number | 
**bank_name** | **str** | Name of the recipient&#39;s bank or wallet (e.g. BDO, BPI, GCash, Maya) | 

## Example

```python
from fireblocks.models.insta_pay_payment_info import InstaPayPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InstaPayPaymentInfo from a JSON string
insta_pay_payment_info_instance = InstaPayPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(InstaPayPaymentInfo.to_json())

# convert the object into a dict
insta_pay_payment_info_dict = insta_pay_payment_info_instance.to_dict()
# create an instance of InstaPayPaymentInfo from a dict
insta_pay_payment_info_from_dict = InstaPayPaymentInfo.from_dict(insta_pay_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


