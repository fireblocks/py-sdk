# DestinationTransferPeerPathResponseAllOf

The transaction’s destination. **Note:** In case the transaction is sent to multiple destinations, the `destinations` parameter is be used instead of this.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sub_type** | **str** | The specific exchange, fiat account or unmanaged wallet (either INTERNAL / EXTERNAL) | [optional] 

## Example

```python
from fireblocks_client.models.destination_transfer_peer_path_response_all_of import DestinationTransferPeerPathResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationTransferPeerPathResponseAllOf from a JSON string
destination_transfer_peer_path_response_all_of_instance = DestinationTransferPeerPathResponseAllOf.from_json(json)
# print the JSON string representation of the object
print DestinationTransferPeerPathResponseAllOf.to_json()

# convert the object into a dict
destination_transfer_peer_path_response_all_of_dict = destination_transfer_peer_path_response_all_of_instance.to_dict()
# create an instance of DestinationTransferPeerPathResponseAllOf from a dict
destination_transfer_peer_path_response_all_of_form_dict = destination_transfer_peer_path_response_all_of.from_dict(destination_transfer_peer_path_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


