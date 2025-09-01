# IbanPaymentInfo

IBAN payment information for European bank transfers

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
**iban** | **str** | The International Bank Account Number (IBAN) | 
**iban_city** | **str** | The city associated with the IBAN | 
**iban_country** | **str** | The country associated with the IBAN (ISO 3166-1 alpha-2 code) | 

## Example

```python
from fireblocks.models.iban_payment_info import IbanPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IbanPaymentInfo from a JSON string
iban_payment_info_instance = IbanPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(IbanPaymentInfo.to_json())

# convert the object into a dict
iban_payment_info_dict = iban_payment_info_instance.to_dict()
# create an instance of IbanPaymentInfo from a dict
iban_payment_info_from_dict = IbanPaymentInfo.from_dict(iban_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


