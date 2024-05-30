# SourceTransferPeerPath

The source of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransferPeerPathType**](TransferPeerPathType.md) |  | 
**sub_type** | [**TransferPeerPathSubType**](TransferPeerPathSubType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.source_transfer_peer_path import SourceTransferPeerPath

# TODO update the JSON string below
json = "{}"
# create an instance of SourceTransferPeerPath from a JSON string
source_transfer_peer_path_instance = SourceTransferPeerPath.from_json(json)
# print the JSON string representation of the object
print(SourceTransferPeerPath.to_json())

# convert the object into a dict
source_transfer_peer_path_dict = source_transfer_peer_path_instance.to_dict()
# create an instance of SourceTransferPeerPath from a dict
source_transfer_peer_path_from_dict = SourceTransferPeerPath.from_dict(source_transfer_peer_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


