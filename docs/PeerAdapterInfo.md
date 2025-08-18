# PeerAdapterInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_token_link_id** | **str** | The token link id of the adapter | 
**adapter_address** | **str** | The adapter address | 
**base_asset_id** | **str** | The base asset id for the base asset that the adapter is deployed on | 

## Example

```python
from fireblocks.models.peer_adapter_info import PeerAdapterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PeerAdapterInfo from a JSON string
peer_adapter_info_instance = PeerAdapterInfo.from_json(json)
# print the JSON string representation of the object
print(PeerAdapterInfo.to_json())

# convert the object into a dict
peer_adapter_info_dict = peer_adapter_info_instance.to_dict()
# create an instance of PeerAdapterInfo from a dict
peer_adapter_info_from_dict = PeerAdapterInfo.from_dict(peer_adapter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


