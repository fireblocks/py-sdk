# NequiPaymentInfo

NEQUI payment information for Colombian mobile payment transfers (COP)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rail** | **str** | The payment rail type for NEQUI transfers | 
**addressing_system** | **str** | The addressing system used for NEQUI transfers | 
**phone** | **str** | Recipient phone number in E.164 format | 

## Example

```python
from fireblocks.models.nequi_payment_info import NequiPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NequiPaymentInfo from a JSON string
nequi_payment_info_instance = NequiPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(NequiPaymentInfo.to_json())

# convert the object into a dict
nequi_payment_info_dict = nequi_payment_info_instance.to_dict()
# create an instance of NequiPaymentInfo from a dict
nequi_payment_info_from_dict = NequiPaymentInfo.from_dict(nequi_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


