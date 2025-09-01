# MomoPaymentInfo

Mobile Money (MOMO) payment information for African mobile payment services

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for mobile money transfers | 
**addressing_system** | **str** | The addressing system used for mobile money transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**mobile_phone_number** | **str** | The mobile phone number associated with the mobile money account | 
**provider** | **str** | The mobile money service provider | 
**beneficiary_document_id** | **str** | The document ID of the beneficiary | [optional] 
**beneficiary_relationship** | **str** | The relationship between sender and beneficiary | [optional] 

## Example

```python
from fireblocks.models.momo_payment_info import MomoPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MomoPaymentInfo from a JSON string
momo_payment_info_instance = MomoPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(MomoPaymentInfo.to_json())

# convert the object into a dict
momo_payment_info_dict = momo_payment_info_instance.to_dict()
# create an instance of MomoPaymentInfo from a dict
momo_payment_info_from_dict = MomoPaymentInfo.from_dict(momo_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


