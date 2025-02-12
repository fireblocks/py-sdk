# NotificationAttempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent_time** | **int** | The time when the attempt was sent in milliseconds. | 
**duration** | **int** | The duration of the attempt in milliseconds. | 
**response_code** | **int** | The response code of the attempt, when missing refer to failureReason. | [optional] 
**failure_reason** | **str** | The request failure reason in case responseCode is missing. | [optional] 

## Example

```python
from fireblocks.models.notification_attempt import NotificationAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationAttempt from a JSON string
notification_attempt_instance = NotificationAttempt.from_json(json)
# print the JSON string representation of the object
print(NotificationAttempt.to_json())

# convert the object into a dict
notification_attempt_dict = notification_attempt_instance.to_dict()
# create an instance of NotificationAttempt from a dict
notification_attempt_from_dict = NotificationAttempt.from_dict(notification_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


