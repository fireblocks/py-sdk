# LegacyPublishDraftRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_id** | **str** | draft unique identifier | [optional] 

## Example

```python
from fireblocks.models.legacy_publish_draft_request import LegacyPublishDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPublishDraftRequest from a JSON string
legacy_publish_draft_request_instance = LegacyPublishDraftRequest.from_json(json)
# print the JSON string representation of the object
print(LegacyPublishDraftRequest.to_json())

# convert the object into a dict
legacy_publish_draft_request_dict = legacy_publish_draft_request_instance.to_dict()
# create an instance of LegacyPublishDraftRequest from a dict
legacy_publish_draft_request_from_dict = LegacyPublishDraftRequest.from_dict(legacy_publish_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


