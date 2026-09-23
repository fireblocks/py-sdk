# UpdateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The url of the webhook where notifications will be sent. URL must be valid, unique and https. | [optional] 
**description** | **str** | description of the webhook of what it is used for.should not contain special characters. | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | The events that the webhook will be subscribed to | [optional] 
**enabled** | **bool** | The status of the webhook | [optional] 
**mtls** | [**WebhookMtls**](WebhookMtls.md) |  | [optional] 
**webhook_oauth_id** | **str** | The id of the OAuth credentials this webhook authenticates with, from &#x60;/v1/webhooks_settings/oauth&#x60;. Several webhooks may share one credential set, so rotating its client secret covers all of them at once. Send &#x60;null&#x60; to stop using OAuth for this webhook. Cannot be combined with an &#x60;authorization&#x60; custom header on the same webhook; a request that would leave both set is rejected. | [optional] 
**custom_headers** | **Dict[str, object]** | A delta applied to the delivery headers. A header with a value is added or replaced, a header with &#x60;null&#x60; is deleted, and one you leave out is untouched. A value replaces what is stored under that name rather than adding to it, so an array is the complete new set of lines for that header. Send &#x60;customHeaders: null&#x60; to clear every header in one call. That does not collide with a &#x60;null&#x60; value on a name: one names the header to delete, the other names the whole field. Names are case-insensitive, so a &#x60;null&#x60; under one casing deletes a header stored under another. Same rules as on create: string or non-empty array, &#x60;Cookie&#x60; and &#x60;Authorization&#x60; string-only, 10 headers and under 16 KB in the resulting set, the same reserved names, and values write-only. Entries set to &#x60;null&#x60; do not count towards the limit. &#x60;Authorization&#x60; cannot be combined with &#x60;webhookOauthId&#x60;, though one request may add it and detach the credentials together. | [optional] 

## Example

```python
from fireblocks.models.update_webhook_request import UpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookRequest from a JSON string
update_webhook_request_instance = UpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookRequest.to_json())

# convert the object into a dict
update_webhook_request_dict = update_webhook_request_instance.to_dict()
# create an instance of UpdateWebhookRequest from a dict
update_webhook_request_from_dict = UpdateWebhookRequest.from_dict(update_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


