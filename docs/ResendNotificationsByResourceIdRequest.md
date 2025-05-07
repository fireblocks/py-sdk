# ResendNotificationsByResourceIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource id to resend notifications for | 
**exclude_statuses** | [**List[NotificationStatus]**](NotificationStatus.md) | (optional) List of notification statuses to exclude from the resend operation     - Empty array means all statuses will be included     - If you want to exclude some statuses, you can use the following example: [ IN_PROGRESS, FAILED ]     - Default if missing, means all statuses other than \&quot;COMPLETED\&quot; will be included  | [optional] 

## Example

```python
from fireblocks.models.resend_notifications_by_resource_id_request import ResendNotificationsByResourceIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendNotificationsByResourceIdRequest from a JSON string
resend_notifications_by_resource_id_request_instance = ResendNotificationsByResourceIdRequest.from_json(json)
# print the JSON string representation of the object
print(ResendNotificationsByResourceIdRequest.to_json())

# convert the object into a dict
resend_notifications_by_resource_id_request_dict = resend_notifications_by_resource_id_request_instance.to_dict()
# create an instance of ResendNotificationsByResourceIdRequest from a dict
resend_notifications_by_resource_id_request_from_dict = ResendNotificationsByResourceIdRequest.from_dict(resend_notifications_by_resource_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


