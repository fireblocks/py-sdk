# DraftResponse

Response object for draft operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Operation status | 
**rules** | [**List[PolicyRule]**](PolicyRule.md) | Draft rules | 
**draft_id** | **str** | Draft unique id | 
**metadata** | [**PolicyMetadata**](PolicyMetadata.md) |  | 

## Example

```python
from fireblocks.models.draft_response import DraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DraftResponse from a JSON string
draft_response_instance = DraftResponse.from_json(json)
# print the JSON string representation of the object
print(DraftResponse.to_json())

# convert the object into a dict
draft_response_dict = draft_response_instance.to_dict()
# create an instance of DraftResponse from a dict
draft_response_from_dict = DraftResponse.from_dict(draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


