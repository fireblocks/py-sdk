# AllocationResponseReject

Reject a CIP-56 allocation request. Carries no arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the allocation request. | 

## Example

```python
from fireblocks.models.allocation_response_reject import AllocationResponseReject

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationResponseReject from a JSON string
allocation_response_reject_instance = AllocationResponseReject.from_json(json)
# print the JSON string representation of the object
print(AllocationResponseReject.to_json())

# convert the object into a dict
allocation_response_reject_dict = allocation_response_reject_instance.to_dict()
# create an instance of AllocationResponseReject from a dict
allocation_response_reject_from_dict = AllocationResponseReject.from_dict(allocation_response_reject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


