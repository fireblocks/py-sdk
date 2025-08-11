# NotificationAttemptsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NotificationAttempt]**](NotificationAttempt.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.notification_attempts_paginated_response import NotificationAttemptsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationAttemptsPaginatedResponse from a JSON string
notification_attempts_paginated_response_instance = NotificationAttemptsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationAttemptsPaginatedResponse.to_json())

# convert the object into a dict
notification_attempts_paginated_response_dict = notification_attempts_paginated_response_instance.to_dict()
# create an instance of NotificationAttemptsPaginatedResponse from a dict
notification_attempts_paginated_response_from_dict = NotificationAttemptsPaginatedResponse.from_dict(notification_attempts_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


