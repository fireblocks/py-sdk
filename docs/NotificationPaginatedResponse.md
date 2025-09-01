# NotificationPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Notification]**](Notification.md) | The data of the current page | 
**total** | **float** | The total number of notifications after all filters applied (not returned when &#39;pageCursor&#39; parameter is used) | [optional] 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.notification_paginated_response import NotificationPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationPaginatedResponse from a JSON string
notification_paginated_response_instance = NotificationPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationPaginatedResponse.to_json())

# convert the object into a dict
notification_paginated_response_dict = notification_paginated_response_instance.to_dict()
# create an instance of NotificationPaginatedResponse from a dict
notification_paginated_response_from_dict = NotificationPaginatedResponse.from_dict(notification_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


