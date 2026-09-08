# AllocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the allocation request. | 

## Example

```python
from fireblocks.models.allocation_response import AllocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationResponse from a JSON string
allocation_response_instance = AllocationResponse.from_json(json)
# print the JSON string representation of the object
print(AllocationResponse.to_json())

# convert the object into a dict
allocation_response_dict = allocation_response_instance.to_dict()
# create an instance of AllocationResponse from a dict
allocation_response_from_dict = AllocationResponse.from_dict(allocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


