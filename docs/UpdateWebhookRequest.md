# UpdateWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The url of the webhook where notifications will be sent. URL must be valid, unique and https. | [optional] 
**description** | **str** | description of the webhook of what it is used for.should not contain special characters. | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | The events that the webhook will be subscribed to | [optional] 
**enabled** | **bool** | The status of the webhook | [optional] 
**mtls** | [**WebhookMtls**](WebhookMtls.md) |  | [optional] 
**oauth** | [**WebhookOAuth**](WebhookOAuth.md) |  | [optional] 
**custom_headers** | **Dict[str, Optional[str]]** | Custom headers delta: entries with a string value are added or updated, entries with a &#x60;null&#x60; value delete that header (no-op if absent), and header names omitted from the payload are left untouched. The resulting set is limited to 10 headers. Header names are case-insensitive, up to 128 characters, and limited to valid HTTP header name characters. Some system header names are reserved and cannot be used. Values are write-only — never returned in responses. | [optional] 

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


