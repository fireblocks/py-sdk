# DestinationTransferPeerPath

The destination of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransferPeerPathType**](TransferPeerPathType.md) |  | 
**sub_type** | [**TransferPeerPathSubType**](TransferPeerPathSubType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**one_time_address** | [**OneTimeAddress**](OneTimeAddress.md) |  | [optional] 
**is_collateral** | **bool** | indicate if the destination is collateral account | [optional] 

## Example

```python
from fireblocks.models.destination_transfer_peer_path import DestinationTransferPeerPath

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationTransferPeerPath from a JSON string
destination_transfer_peer_path_instance = DestinationTransferPeerPath.from_json(json)
# print the JSON string representation of the object
print(DestinationTransferPeerPath.to_json())

# convert the object into a dict
destination_transfer_peer_path_dict = destination_transfer_peer_path_instance.to_dict()
# create an instance of DestinationTransferPeerPath from a dict
destination_transfer_peer_path_from_dict = DestinationTransferPeerPath.from_dict(destination_transfer_peer_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


