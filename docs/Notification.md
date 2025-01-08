# Notification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the Notification | 
**created_at** | **datetime** | The creation date of the notification | 
**updated_at** | **datetime** | The date when the notification was updated | 
**status** | [**NotificationStatus**](NotificationStatus.md) |  | 
**event_type** | [**WebhookEvent**](WebhookEvent.md) |  | 
**event_version** | **float** | The event version of the Notification | 
**resource_id** | **str** | The resource id of the event which the Notification is listen to | [optional] 
**attempts** | **List[str]** | The attempts related to Notification | [optional] [default to []]

## Example

```python
from fireblocks.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print(Notification.to_json())

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_from_dict = Notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


