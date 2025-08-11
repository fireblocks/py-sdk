# NotificationWithData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **int** | The creation date of the notification in milliseconds | 
**updated_at** | **int** | The date when the notification was updated in milliseconds | 
**status** | [**NotificationStatus**](NotificationStatus.md) |  | 
**event_type** | [**WebhookEvent**](WebhookEvent.md) |  | 
**resource_id** | **str** | The resource id of the event which the Notification is listen to | [optional] 
**data** | **object** | notification data | [optional] 

## Example

```python
from fireblocks.models.notification_with_data import NotificationWithData

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationWithData from a JSON string
notification_with_data_instance = NotificationWithData.from_json(json)
# print the JSON string representation of the object
print(NotificationWithData.to_json())

# convert the object into a dict
notification_with_data_dict = notification_with_data_instance.to_dict()
# create an instance of NotificationWithData from a dict
notification_with_data_from_dict = NotificationWithData.from_dict(notification_with_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


