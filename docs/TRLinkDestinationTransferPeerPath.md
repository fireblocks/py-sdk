# TRLinkDestinationTransferPeerPath

Destination peer path for transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Destination peer type (e.g., ONE_TIME_ADDRESS, VAULT_ACCOUNT) | 
**id** | **str** | Destination peer ID | [optional] 
**wallet_id** | **str** | Destination wallet ID | [optional] 
**one_time_address** | [**TRLinkOneTimeAddress**](TRLinkOneTimeAddress.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_destination_transfer_peer_path import TRLinkDestinationTransferPeerPath

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkDestinationTransferPeerPath from a JSON string
tr_link_destination_transfer_peer_path_instance = TRLinkDestinationTransferPeerPath.from_json(json)
# print the JSON string representation of the object
print(TRLinkDestinationTransferPeerPath.to_json())

# convert the object into a dict
tr_link_destination_transfer_peer_path_dict = tr_link_destination_transfer_peer_path_instance.to_dict()
# create an instance of TRLinkDestinationTransferPeerPath from a dict
tr_link_destination_transfer_peer_path_from_dict = TRLinkDestinationTransferPeerPath.from_dict(tr_link_destination_transfer_peer_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


