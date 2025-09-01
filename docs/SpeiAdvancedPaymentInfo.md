# SpeiAdvancedPaymentInfo

Advanced SPEI payment information for Mexican bank transfers with full details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for SPEI transfers | 
**addressing_system** | **str** | The addressing system used for SPEI transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**bank_name** | **str** | The name of the bank | [optional] 
**beneficiary_rfc** | **str** | The RFC (Registro Federal de Contribuyentes) of the beneficiary | [optional] 
**sender_document_id** | **str** | The document ID of the sender | [optional] 
**clabe** | **str** | The CLABE (Clave Bancaria Estandarizada) number | 

## Example

```python
from fireblocks.models.spei_advanced_payment_info import SpeiAdvancedPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SpeiAdvancedPaymentInfo from a JSON string
spei_advanced_payment_info_instance = SpeiAdvancedPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(SpeiAdvancedPaymentInfo.to_json())

# convert the object into a dict
spei_advanced_payment_info_dict = spei_advanced_payment_info_instance.to_dict()
# create an instance of SpeiAdvancedPaymentInfo from a dict
spei_advanced_payment_info_from_dict = SpeiAdvancedPaymentInfo.from_dict(spei_advanced_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


