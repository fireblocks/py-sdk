# LegacyDraftResponse

Response object for draft operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Operation status | 
**rules** | [**List[LegacyPolicyRule]**](LegacyPolicyRule.md) | Draft rules | 
**draft_id** | **str** | Draft unique id | 
**metadata** | [**LegacyPolicyMetadata**](LegacyPolicyMetadata.md) |  | 

## Example

```python
from fireblocks.models.legacy_draft_response import LegacyDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyDraftResponse from a JSON string
legacy_draft_response_instance = LegacyDraftResponse.from_json(json)
# print the JSON string representation of the object
print(LegacyDraftResponse.to_json())

# convert the object into a dict
legacy_draft_response_dict = legacy_draft_response_instance.to_dict()
# create an instance of LegacyDraftResponse from a dict
legacy_draft_response_from_dict = LegacyDraftResponse.from_dict(legacy_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


