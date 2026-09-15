# CreateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The url of the webhook where notifications will be sent. URL must be valid, unique and https. | 
**description** | **str** | description of the webhook. should not contain special characters. | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | event types the webhook will subscribe to | 
**enabled** | **bool** | The status of the webhook. If false, the webhook will not receive notifications. | [optional] [default to True]
**mtls** | [**WebhookMtls**](WebhookMtls.md) |  | [optional] 
**webhook_oauth_id** | **str** | The id of the OAuth credentials this webhook authenticates with, from &#x60;/v1/webhooks_settings/oauth&#x60;. Several webhooks may share one credential set, so rotating its client secret covers all of them at once. Send &#x60;null&#x60; to stop using OAuth for this webhook. | [optional] 
**custom_headers** | **Dict[str, object]** | Custom HTTP headers attached to every notification delivered by this webhook. A value is a string, sent as one header line, or an array of strings, sent as one header line per element under the same name. &#x60;Cookie&#x60; accepts only a string. An empty array is rejected — leave the name out instead. At most 10 header lines in total, counted per array element rather than per name. Names must be valid HTTP header tokens, are case-insensitive, and are at most 128 characters. A value may be empty and has no length limit of its own; the whole object must be under 16 KB when serialized as UTF-8. A value that large may still be refused by your own endpoint, since web servers commonly cap the whole request header block at around 8 KB. Reserved names: &#x60;Host&#x60;, &#x60;Content-Type&#x60;, &#x60;Content-Length&#x60;, &#x60;Transfer-Encoding&#x60;, &#x60;Connection&#x60;, &#x60;User-Agent&#x60;, &#x60;Accept&#x60;, &#x60;Accept-Encoding&#x60;, &#x60;Fireblocks-Signature&#x60;, &#x60;Fireblocks-Webhook-Signature&#x60;. When this webhook has OAuth credentials attached, an &#x60;Authorization&#x60; value you set and the bearer token are both sent as separate header lines. Values are write-only; responses return only the header names. | [optional] 

## Example

```python
from fireblocks.models.create_webhook_request import CreateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookRequest from a JSON string
create_webhook_request_instance = CreateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookRequest.to_json())

# convert the object into a dict
create_webhook_request_dict = create_webhook_request_instance.to_dict()
# create an instance of CreateWebhookRequest from a dict
create_webhook_request_from_dict = CreateWebhookRequest.from_dict(create_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


