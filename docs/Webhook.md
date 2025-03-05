# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the webhook | [optional] 
**url** | **str** | The url of the webhook where notifications will be sent. Must be a valid URL and https. | [optional] 
**description** | **str** | description of the webhook of what it is used for | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | The events that the webhook will be subscribed to | [optional] 
**status** | **str** | The status of the webhook | [optional] 
**created_at** | **datetime** | The date and time the webhook was created | [optional] 
**updated_at** | **datetime** | The date and time the webhook was last updated | [optional] 

## Example

```python
from fireblocks.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


