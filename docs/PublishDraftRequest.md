# PublishDraftRequest

Request schema for publishing draft with policy types and draft ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_types** | [**List[PolicyType]**](PolicyType.md) |  | 
**draft_id** | **str** | The ID of the draft to publish | 

## Example

```python
from fireblocks.models.publish_draft_request import PublishDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishDraftRequest from a JSON string
publish_draft_request_instance = PublishDraftRequest.from_json(json)
# print the JSON string representation of the object
print(PublishDraftRequest.to_json())

# convert the object into a dict
publish_draft_request_dict = publish_draft_request_instance.to_dict()
# create an instance of PublishDraftRequest from a dict
publish_draft_request_from_dict = PublishDraftRequest.from_dict(publish_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


