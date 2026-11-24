# DeleteWebhookCustomHeadersResponse

The deleted custom headers set, plus the ids of any webhooks and OAuth credentials the delete detached from it. Things are only detached by `forceDelete=true`; without it a delete is refused with `409` while anything still uses the set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the custom headers set. Pass this as a webhook&#39;s, or OAuth credentials&#39;, &#x60;webhookCustomHeadersId&#x60; to attach it. | 
**name** | **str** | The label given to this set. | 
**header_names** | **List[str]** | Names of the headers in the set, lowercased. Header values are never returned. | 
**created_at** | **int** | The date and time the set was created, in milliseconds. | 
**updated_at** | **int** | The date and time the set was last updated, in milliseconds. | 
**detached_webhook_ids** | **List[str]** | Webhooks whose &#x60;webhookCustomHeadersId&#x60; was cleared. The webhooks themselves are not deleted and keep delivering, just without these headers. Empty unless &#x60;forceDelete&#x3D;true&#x60; detached something. | 
**detached_webhook_oauth_ids** | **List[str]** | OAuth credentials whose &#x60;webhookCustomHeadersId&#x60; was cleared. The credentials themselves are not deleted; their token requests just no longer carry these headers. Empty unless &#x60;forceDelete&#x3D;true&#x60; detached something. | 

## Example

```python
from fireblocks.models.delete_webhook_custom_headers_response import DeleteWebhookCustomHeadersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWebhookCustomHeadersResponse from a JSON string
delete_webhook_custom_headers_response_instance = DeleteWebhookCustomHeadersResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteWebhookCustomHeadersResponse.to_json())

# convert the object into a dict
delete_webhook_custom_headers_response_dict = delete_webhook_custom_headers_response_instance.to_dict()
# create an instance of DeleteWebhookCustomHeadersResponse from a dict
delete_webhook_custom_headers_response_from_dict = DeleteWebhookCustomHeadersResponse.from_dict(delete_webhook_custom_headers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


