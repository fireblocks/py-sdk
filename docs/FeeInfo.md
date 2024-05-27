# FeeInfo

Details of the transaction's fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_fee** | **str** | The fee paid to the network | [optional] 
**service_fee** | **str** | The total fee deducted by the exchange from the actual requested amount (serviceFee &#x3D; amount - netAmount) | [optional] 
**gas_price** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.fee_info import FeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FeeInfo from a JSON string
fee_info_instance = FeeInfo.from_json(json)
# print the JSON string representation of the object
print FeeInfo.to_json()

# convert the object into a dict
fee_info_dict = fee_info_instance.to_dict()
# create an instance of FeeInfo from a dict
fee_info_form_dict = fee_info.from_dict(fee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


