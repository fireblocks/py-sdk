# TRLinkTransferPeerPath

Transfer peer path for destination matching

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Peer type | [optional] 
**id** | **str** | Peer ID | [optional] 
**sub_type** | **str** | Peer subtype | [optional] 
**address** | **str** | Peer address | [optional] 

## Example

```python
from fireblocks.models.tr_link_transfer_peer_path import TRLinkTransferPeerPath

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkTransferPeerPath from a JSON string
tr_link_transfer_peer_path_instance = TRLinkTransferPeerPath.from_json(json)
# print the JSON string representation of the object
print(TRLinkTransferPeerPath.to_json())

# convert the object into a dict
tr_link_transfer_peer_path_dict = tr_link_transfer_peer_path_instance.to_dict()
# create an instance of TRLinkTransferPeerPath from a dict
tr_link_transfer_peer_path_from_dict = TRLinkTransferPeerPath.from_dict(tr_link_transfer_peer_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


