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
**custom_headers** | **Dict[str, str]** | Custom HTTP headers attached to every notification delivered by this webhook (max 10). Header names must be valid RFC 7230 tokens (printable ASCII, no separators), are treated case-insensitively (duplicate names differing only in case are rejected), and may not exceed 128 characters. The following names are reserved and cannot be used: Host, Content-Type, Content-Length, Transfer-Encoding, Connection, User-Agent, Accept, Accept-Encoding, Fireblocks-Signature, Fireblocks-Webhook-Signature. Header values are write-only — never returned in responses. | [optional] 

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


