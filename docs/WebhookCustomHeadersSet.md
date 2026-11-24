# WebhookCustomHeadersSet

A stored set of custom HTTP headers, referenced by webhooks and by OAuth credentials through their `webhookCustomHeadersId`. On a webhook the headers go out with every notification; on OAuth credentials they go out on the token request to your authorization server. Header values are write-only: only the names are returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the custom headers set. Pass this as a webhook&#39;s, or OAuth credentials&#39;, &#x60;webhookCustomHeadersId&#x60; to attach it. | 
**name** | **str** | The label given to this set. | 
**header_names** | **List[str]** | Names of the headers in the set, lowercased. Header values are never returned. | 
**created_at** | **int** | The date and time the set was created, in milliseconds. | 
**updated_at** | **int** | The date and time the set was last updated, in milliseconds. | 

## Example

```python
from fireblocks.models.webhook_custom_headers_set import WebhookCustomHeadersSet

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCustomHeadersSet from a JSON string
webhook_custom_headers_set_instance = WebhookCustomHeadersSet.from_json(json)
# print the JSON string representation of the object
print(WebhookCustomHeadersSet.to_json())

# convert the object into a dict
webhook_custom_headers_set_dict = webhook_custom_headers_set_instance.to_dict()
# create an instance of WebhookCustomHeadersSet from a dict
webhook_custom_headers_set_from_dict = WebhookCustomHeadersSet.from_dict(webhook_custom_headers_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


