# SpeiBasicPaymentInfo

Basic SPEI payment information for Mexican bank transfers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spei_clabe** | **str** | The CLABE (Clave Bancaria Estandarizada) number for SPEI transfers | 
**spei_name** | **str** | The name associated with the SPEI account | [optional] 

## Example

```python
from fireblocks.models.spei_basic_payment_info import SpeiBasicPaymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SpeiBasicPaymentInfo from a JSON string
spei_basic_payment_info_instance = SpeiBasicPaymentInfo.from_json(json)
# print the JSON string representation of the object
print(SpeiBasicPaymentInfo.to_json())

# convert the object into a dict
spei_basic_payment_info_dict = spei_basic_payment_info_instance.to_dict()
# create an instance of SpeiBasicPaymentInfo from a dict
spei_basic_payment_info_from_dict = SpeiBasicPaymentInfo.from_dict(spei_basic_payment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


