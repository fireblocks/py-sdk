# PesonetPaymentInfo

PesoNet payment information for Philippine batch payment transfers (PHP)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for PesoNet transfers | 
**addressing_system** | **str** | The addressing system used for PesoNet transfers | 
**account_holder_given_name** | **str** | The given name (first name) of the account holder | 
**account_holder_surname** | **str** | The surname (last name) of the account holder | 
**account_number** | **str** | Recipient bank account number | 
**bank_name** | **str** | Name of the recipient&#39;s bank | 

## Example

```python
from fireblocks.models.pesonet_payment_info import PesonetPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PesonetPaymentInfo from a JSON string
pesonet_payment_info_instance = PesonetPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(PesonetPaymentInfo.to_json())

# convert the object into a dict
pesonet_payment_info_dict = pesonet_payment_info_instance.to_dict()
# create an instance of PesonetPaymentInfo from a dict
pesonet_payment_info_from_dict = PesonetPaymentInfo.from_dict(pesonet_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


