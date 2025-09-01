# PixPaymentInfo

PIX payment information for Brazilian instant payments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for PIX transfers | 
**addressing_system** | **str** | The addressing system used for PIX transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**country** | **str** | The country for the transfer (ISO 3166-1 alpha-2 code) | 
**pix_key** | **str** | The PIX key used for the transfer | 
**bank_name** | **str** | The name of the bank | [optional] 
**bank_code** | **str** | The bank code (ISPB - Identificador do Sistema de Pagamentos Brasileiros) | [optional] 
**key_type** | **str** | The type of PIX key being used | 

## Example

```python
from fireblocks.models.pix_payment_info import PixPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PixPaymentInfo from a JSON string
pix_payment_info_instance = PixPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(PixPaymentInfo.to_json())

# convert the object into a dict
pix_payment_info_dict = pix_payment_info_instance.to_dict()
# create an instance of PixPaymentInfo from a dict
pix_payment_info_from_dict = PixPaymentInfo.from_dict(pix_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


