# TransferPeerPath


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_peer_path import TransferPeerPath

# TODO update the JSON string below
json = "{}"
# create an instance of TransferPeerPath from a JSON string
transfer_peer_path_instance = TransferPeerPath.from_json(json)
# print the JSON string representation of the object
print TransferPeerPath.to_json()

# convert the object into a dict
transfer_peer_path_dict = transfer_peer_path_instance.to_dict()
# create an instance of TransferPeerPath from a dict
transfer_peer_path_form_dict = transfer_peer_path.from_dict(transfer_peer_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


