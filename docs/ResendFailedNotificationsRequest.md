# ResendFailedNotificationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **float** | (optional) Start time for the resend window in milliseconds since epoch up to 24 hours before the current time - Default if missing means 24 hours before the current time in milliseconds since epoch - Maximum value is current time in milliseconds since epoch - Minimum value is 24 hours before the current time in milliseconds since epoch  | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | (optional) Event types to resend, default is all event types     - Default if missing means all events will be included     - Empty array means all events will be included  | [optional] 

## Example

```python
from fireblocks.models.resend_failed_notifications_request import ResendFailedNotificationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendFailedNotificationsRequest from a JSON string
resend_failed_notifications_request_instance = ResendFailedNotificationsRequest.from_json(json)
# print the JSON string representation of the object
print(ResendFailedNotificationsRequest.to_json())

# convert the object into a dict
resend_failed_notifications_request_dict = resend_failed_notifications_request_instance.to_dict()
# create an instance of ResendFailedNotificationsRequest from a dict
resend_failed_notifications_request_from_dict = ResendFailedNotificationsRequest.from_dict(resend_failed_notifications_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


