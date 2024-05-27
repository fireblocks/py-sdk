# PublishDraftRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft_id** | **str** | draft unique identifier | [optional] 

## Example

```python
from fireblocks_client.models.publish_draft_request import PublishDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishDraftRequest from a JSON string
publish_draft_request_instance = PublishDraftRequest.from_json(json)
# print the JSON string representation of the object
print PublishDraftRequest.to_json()

# convert the object into a dict
publish_draft_request_dict = publish_draft_request_instance.to_dict()
# create an instance of PublishDraftRequest from a dict
publish_draft_request_form_dict = publish_draft_request.from_dict(publish_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


