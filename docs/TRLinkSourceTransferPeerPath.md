# TRLinkSourceTransferPeerPath

Source peer path for transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Source peer type (e.g., VAULT_ACCOUNT, UNKNOWN) | 
**id** | **str** | Source peer ID | [optional] 
**wallet_id** | **str** | Source wallet ID | [optional] 

## Example

```python
from fireblocks.models.tr_link_source_transfer_peer_path import TRLinkSourceTransferPeerPath

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkSourceTransferPeerPath from a JSON string
tr_link_source_transfer_peer_path_instance = TRLinkSourceTransferPeerPath.from_json(json)
# print the JSON string representation of the object
print(TRLinkSourceTransferPeerPath.to_json())

# convert the object into a dict
tr_link_source_transfer_peer_path_dict = tr_link_source_transfer_peer_path_instance.to_dict()
# create an instance of TRLinkSourceTransferPeerPath from a dict
tr_link_source_transfer_peer_path_from_dict = TRLinkSourceTransferPeerPath.from_dict(tr_link_source_transfer_peer_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


