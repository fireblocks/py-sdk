# UnspentInputsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**UnspentInput**](UnspentInput.md) |  | [optional] 
**address** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 
**confirmations** | **float** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.unspent_inputs_response import UnspentInputsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnspentInputsResponse from a JSON string
unspent_inputs_response_instance = UnspentInputsResponse.from_json(json)
# print the JSON string representation of the object
print(UnspentInputsResponse.to_json())

# convert the object into a dict
unspent_inputs_response_dict = unspent_inputs_response_instance.to_dict()
# create an instance of UnspentInputsResponse from a dict
unspent_inputs_response_from_dict = UnspentInputsResponse.from_dict(unspent_inputs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


