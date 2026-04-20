# ByorkConfigResponse

BYORK Light configuration for the tenant: wait-for-response timeouts, active flag, provider, last update time, and allowed timeout ranges for validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incoming_timeout_seconds** | **int** | Timeout in seconds for incoming BYORK wait-for-response | [optional] 
**outgoing_timeout_seconds** | **int** | Timeout in seconds for outgoing BYORK wait-for-response | [optional] 
**active** | **bool** | Whether BYORK Light is active for the tenant | [optional] 
**provider** | **str** | Provider identifier | [optional] 
**last_update** | **datetime** | Last update timestamp of the configuration | [optional] 
**timeout_range_incoming** | [**ByorkTimeoutRange**](ByorkTimeoutRange.md) |  | [optional] 
**timeout_range_outgoing** | [**ByorkTimeoutRange**](ByorkTimeoutRange.md) |  | [optional] 

## Example

```python
from fireblocks.models.byork_config_response import ByorkConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ByorkConfigResponse from a JSON string
byork_config_response_instance = ByorkConfigResponse.from_json(json)
# print the JSON string representation of the object
print(ByorkConfigResponse.to_json())

# convert the object into a dict
byork_config_response_dict = byork_config_response_instance.to_dict()
# create an instance of ByorkConfigResponse from a dict
byork_config_response_from_dict = ByorkConfigResponse.from_dict(byork_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


