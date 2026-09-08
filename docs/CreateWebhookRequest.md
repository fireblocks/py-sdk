# CreateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The url of the webhook where notifications will be sent. URL must be valid, unique and https. | 
**description** | **str** | description of the webhook. should not contain special characters. | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | event types the webhook will subscribe to | 
**enabled** | **bool** | The status of the webhook. If false, the webhook will not receive notifications. | [optional] [default to True]
**mtls** | [**WebhookMtls**](WebhookMtls.md) |  | [optional] 
**oauth** | [**WebhookOAuth**](WebhookOAuth.md) |  | [optional] 
**custom_headers** | **Dict[str, object]** | Custom HTTP headers attached to every notification delivered by this webhook. A value is a string, sent as one header line, or an array of strings, sent as one header line per element under the same name. &#x60;Cookie&#x60; accepts only a string. An empty array is rejected — leave the name out instead. At most 10 header lines in total, counted per array element rather than per name. Names must be valid HTTP header tokens, are case-insensitive, and are at most 128 characters. Values are at most 1024 characters and may be empty. Reserved names: &#x60;Host&#x60;, &#x60;Content-Type&#x60;, &#x60;Content-Length&#x60;, &#x60;Transfer-Encoding&#x60;, &#x60;Connection&#x60;, &#x60;User-Agent&#x60;, &#x60;Accept&#x60;, &#x60;Accept-Encoding&#x60;, &#x60;Fireblocks-Signature&#x60;, &#x60;Fireblocks-Webhook-Signature&#x60;, &#x60;Authorization&#x60;. &#x60;Authorization&#x60; is reserved whether or not this webhook has OAuth credentials attached, because Fireblocks sets it once it does. Values are write-only; responses return only the header names. | [optional] 

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


