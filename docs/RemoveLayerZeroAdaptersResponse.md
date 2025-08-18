# RemoveLayerZeroAdaptersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deactivated** | **List[str]** | List of successfully deactivated adapter token link IDs | 
**failed** | [**List[RemoveLayerZeroAdapterFailedResult]**](RemoveLayerZeroAdapterFailedResult.md) | List of adapter token link IDs that failed to be removed | 

## Example

```python
from fireblocks.models.remove_layer_zero_adapters_response import RemoveLayerZeroAdaptersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveLayerZeroAdaptersResponse from a JSON string
remove_layer_zero_adapters_response_instance = RemoveLayerZeroAdaptersResponse.from_json(json)
# print the JSON string representation of the object
print(RemoveLayerZeroAdaptersResponse.to_json())

# convert the object into a dict
remove_layer_zero_adapters_response_dict = remove_layer_zero_adapters_response_instance.to_dict()
# create an instance of RemoveLayerZeroAdaptersResponse from a dict
remove_layer_zero_adapters_response_from_dict = RemoveLayerZeroAdaptersResponse.from_dict(remove_layer_zero_adapters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


