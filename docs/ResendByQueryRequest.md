# ResendByQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**List[NotificationStatus]**](NotificationStatus.md) | (optional) List of notification statuses to resend     - Default if missing: &#x60;[\&quot;FAILED\&quot;, \&quot;ON_HOLD\&quot;]&#x60;  | [optional] 
**start_time** | **float** | (optional) Start time for the resend window in milliseconds since epoch, within the last 72 hours - Default if missing means 24 hours before the current time in milliseconds since epoch - Maximum value is current time in milliseconds since epoch - Minimum value is 72 hours before the current time in milliseconds since epoch  | [optional] 
**end_time** | **float** | (optional) End time for the resend window in milliseconds since epoch, within the last 72 hours - Default if missing means current time in milliseconds since epoch - Requires startTime to be provided - Must be after startTime - Time window between startTime and endTime must not exceed 24 hours  | [optional] 
**events** | [**List[WebhookEvent]**](WebhookEvent.md) | (optional) Event types to resend, default is all event types     - Default if missing means all events will be included     - Empty array means all events will be included  | [optional] 
**resource_id** | **str** | (optional) Resource ID to filter notifications by  | [optional] 

## Example

```python
from fireblocks.models.resend_by_query_request import ResendByQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResendByQueryRequest from a JSON string
resend_by_query_request_instance = ResendByQueryRequest.from_json(json)
# print the JSON string representation of the object
print(ResendByQueryRequest.to_json())

# convert the object into a dict
resend_by_query_request_dict = resend_by_query_request_instance.to_dict()
# create an instance of ResendByQueryRequest from a dict
resend_by_query_request_from_dict = ResendByQueryRequest.from_dict(resend_by_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


