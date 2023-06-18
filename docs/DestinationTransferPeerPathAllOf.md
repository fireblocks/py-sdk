# DestinationTransferPeerPathAllOf

The destination of the transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_time_address** | [**OneTimeAddress**](OneTimeAddress.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.destination_transfer_peer_path_all_of import DestinationTransferPeerPathAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationTransferPeerPathAllOf from a JSON string
destination_transfer_peer_path_all_of_instance = DestinationTransferPeerPathAllOf.from_json(json)
# print the JSON string representation of the object
print DestinationTransferPeerPathAllOf.to_json()

# convert the object into a dict
destination_transfer_peer_path_all_of_dict = destination_transfer_peer_path_all_of_instance.to_dict()
# create an instance of DestinationTransferPeerPathAllOf from a dict
destination_transfer_peer_path_all_of_form_dict = destination_transfer_peer_path_all_of.from_dict(destination_transfer_peer_path_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


