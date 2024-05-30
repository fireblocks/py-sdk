# SetNetworkIdDiscoverabilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_discoverable** | **bool** |  | 

## Example

```python
from fireblocks.models.set_network_id_discoverability_request import SetNetworkIdDiscoverabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetNetworkIdDiscoverabilityRequest from a JSON string
set_network_id_discoverability_request_instance = SetNetworkIdDiscoverabilityRequest.from_json(json)
# print the JSON string representation of the object
print(SetNetworkIdDiscoverabilityRequest.to_json())

# convert the object into a dict
set_network_id_discoverability_request_dict = set_network_id_discoverability_request_instance.to_dict()
# create an instance of SetNetworkIdDiscoverabilityRequest from a dict
set_network_id_discoverability_request_from_dict = SetNetworkIdDiscoverabilityRequest.from_dict(set_network_id_discoverability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


