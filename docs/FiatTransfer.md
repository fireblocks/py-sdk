# FiatTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**amount** | **str** | The amount of the fiat transfer. | 
**reference_id** | **str** | The reference ID for the fiat transfer. | [optional] 

## Example

```python
from fireblocks.models.fiat_transfer import FiatTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of FiatTransfer from a JSON string
fiat_transfer_instance = FiatTransfer.from_json(json)
# print the JSON string representation of the object
print(FiatTransfer.to_json())

# convert the object into a dict
fiat_transfer_dict = fiat_transfer_instance.to_dict()
# create an instance of FiatTransfer from a dict
fiat_transfer_from_dict = FiatTransfer.from_dict(fiat_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


