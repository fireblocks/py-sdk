# ValidateLayerZeroChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correct** | **bool** | Indicates whether the LayerZero channel configuration is valid. | 
**errors** | **List[str]** | List of errors found during validation. An empty array indicates no errors. | 

## Example

```python
from fireblocks.models.validate_layer_zero_channel_response import ValidateLayerZeroChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateLayerZeroChannelResponse from a JSON string
validate_layer_zero_channel_response_instance = ValidateLayerZeroChannelResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateLayerZeroChannelResponse.to_json())

# convert the object into a dict
validate_layer_zero_channel_response_dict = validate_layer_zero_channel_response_instance.to_dict()
# create an instance of ValidateLayerZeroChannelResponse from a dict
validate_layer_zero_channel_response_from_dict = ValidateLayerZeroChannelResponse.from_dict(validate_layer_zero_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


