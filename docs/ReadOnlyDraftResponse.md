# ReadOnlyDraftResponse

Response object for the read-only draft operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Operation status | 
**rules** | [**List[PolicyRule]**](PolicyRule.md) | Draft rules | 
**draft_id** | **str** | Draft unique id. null when no draft is stored; the active policy is returned | 
**metadata** | [**Dict[str, PolicyMetadataEntry]**](PolicyMetadataEntry.md) | Policy metadata keyed by policy type | 

## Example

```python
from fireblocks.models.read_only_draft_response import ReadOnlyDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOnlyDraftResponse from a JSON string
read_only_draft_response_instance = ReadOnlyDraftResponse.from_json(json)
# print the JSON string representation of the object
print(ReadOnlyDraftResponse.to_json())

# convert the object into a dict
read_only_draft_response_dict = read_only_draft_response_instance.to_dict()
# create an instance of ReadOnlyDraftResponse from a dict
read_only_draft_response_from_dict = ReadOnlyDraftResponse.from_dict(read_only_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


