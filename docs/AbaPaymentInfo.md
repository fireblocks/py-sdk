# AbaPaymentInfo

ABA payment information for US bank transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | [optional] 
**account_holder_city** | **str** | The city where the account holder resides | 
**account_holder_country** | **str** | The country where the account holder resides (ISO 3166-1 alpha-2 code) | 
**account_holder_address1** | **str** | The primary address line of the account holder | 
**account_holder_address2** | **str** | The secondary address line of the account holder (optional) | [optional] 
**account_holder_district** | **str** | The district or region where the account holder resides | [optional] 
**account_holder_postal_code** | **str** | The postal code of the account holder&#39;s address | 
**aba_routing_number** | **str** | The ABA routing number for the bank | 
**aba_account_number** | **str** | The account number at the bank | 
**aba_country** | **str** | The country for the ABA transfer (ISO 3166-1 alpha-2 code) | 

## Example

```python
from fireblocks.models.aba_payment_info import AbaPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AbaPaymentInfo from a JSON string
aba_payment_info_instance = AbaPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(AbaPaymentInfo.to_json())

# convert the object into a dict
aba_payment_info_dict = aba_payment_info_instance.to_dict()
# create an instance of AbaPaymentInfo from a dict
aba_payment_info_from_dict = AbaPaymentInfo.from_dict(aba_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


