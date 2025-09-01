# SepaPaymentInfo

SEPA payment information for European Single Euro Payments Area transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for SEPA transfers | 
**addressing_system** | **str** | The addressing system used for SEPA transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**account_holder_country** | **str** | The country where the account holder resides (ISO 3166-1 alpha-2 code) | [optional] 
**account_holder_address** | **str** | The address of the account holder | [optional] 
**iban** | **str** | The International Bank Account Number (IBAN) | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**bic** | **str** | The Bank Identifier Code (BIC/SWIFT code) | [optional] 
**bank_name** | **str** | The name of the bank | [optional] 
**bank_branch** | **str** | The bank branch information | [optional] 
**bank_address** | **str** | The address of the bank | [optional] 
**purpose_code** | **str** | The purpose code for the transfer | [optional] 
**tax_id** | **str** | The tax identification number | [optional] 

## Example

```python
from fireblocks.models.sepa_payment_info import SepaPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SepaPaymentInfo from a JSON string
sepa_payment_info_instance = SepaPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(SepaPaymentInfo.to_json())

# convert the object into a dict
sepa_payment_info_dict = sepa_payment_info_instance.to_dict()
# create an instance of SepaPaymentInfo from a dict
sepa_payment_info_from_dict = SepaPaymentInfo.from_dict(sepa_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


