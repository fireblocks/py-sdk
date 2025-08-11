# ResendFailedNotificationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | The total number of failed notifications that are scheduled to be resent. | [optional] 

## Example

```python
from fireblocks.models.resend_failed_notifications_response import ResendFailedNotificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResendFailedNotificationsResponse from a JSON string
resend_failed_notifications_response_instance = ResendFailedNotificationsResponse.from_json(json)
# print the JSON string representation of the object
print(ResendFailedNotificationsResponse.to_json())

# convert the object into a dict
resend_failed_notifications_response_dict = resend_failed_notifications_response_instance.to_dict()
# create an instance of ResendFailedNotificationsResponse from a dict
resend_failed_notifications_response_from_dict = ResendFailedNotificationsResponse.from_dict(resend_failed_notifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


