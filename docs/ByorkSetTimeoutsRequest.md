# ByorkSetTimeoutsRequest

Request body for setting BYORK timeout values. At least one of incomingTimeoutSeconds or outgoingTimeoutSeconds is required. Allowed range per direction is returned in GET config (timeoutRangeIncoming, timeoutRangeOutgoing).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incoming_timeout_seconds** | **int** | Timeout in seconds for incoming BYORK wait-for-response. Allowed range in GET config (timeoutRangeIncoming). | [optional] 
**outgoing_timeout_seconds** | **int** | Timeout in seconds for outgoing BYORK wait-for-response. Allowed range in GET config (timeoutRangeOutgoing). | [optional] 

## Example

```python
from fireblocks.models.byork_set_timeouts_request import ByorkSetTimeoutsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ByorkSetTimeoutsRequest from a JSON string
byork_set_timeouts_request_instance = ByorkSetTimeoutsRequest.from_json(json)
# print the JSON string representation of the object
print(ByorkSetTimeoutsRequest.to_json())

# convert the object into a dict
byork_set_timeouts_request_dict = byork_set_timeouts_request_instance.to_dict()
# create an instance of ByorkSetTimeoutsRequest from a dict
byork_set_timeouts_request_from_dict = ByorkSetTimeoutsRequest.from_dict(byork_set_timeouts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


