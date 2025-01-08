# SplitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the new staking position | 

## Example

```python
from fireblocks.models.split_response import SplitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SplitResponse from a JSON string
split_response_instance = SplitResponse.from_json(json)
# print the JSON string representation of the object
print(SplitResponse.to_json())

# convert the object into a dict
split_response_dict = split_response_instance.to_dict()
# create an instance of SplitResponse from a dict
split_response_from_dict = SplitResponse.from_dict(split_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


