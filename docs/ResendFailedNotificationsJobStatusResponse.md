# ResendFailedNotificationsJobStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Bulk resend job ID | 
**status** | **str** | Bulk resend job status | 
**processed** | **float** | Number of notifications processed | 
**total** | **float** | Total number of notifications to process | 

## Example

```python
from fireblocks.models.resend_failed_notifications_job_status_response import ResendFailedNotificationsJobStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResendFailedNotificationsJobStatusResponse from a JSON string
resend_failed_notifications_job_status_response_instance = ResendFailedNotificationsJobStatusResponse.from_json(json)
# print the JSON string representation of the object
print(ResendFailedNotificationsJobStatusResponse.to_json())

# convert the object into a dict
resend_failed_notifications_job_status_response_dict = resend_failed_notifications_job_status_response_instance.to_dict()
# create an instance of ResendFailedNotificationsJobStatusResponse from a dict
resend_failed_notifications_job_status_response_from_dict = ResendFailedNotificationsJobStatusResponse.from_dict(resend_failed_notifications_job_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


