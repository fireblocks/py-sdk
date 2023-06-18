# SourceTransferPeerPathResponseAllOf

The transaction’s source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sub_type** | **str** | The specific exchange, fiat account or unmanaged wallet (either INTERNAL / EXTERNAL) | [optional] 

## Example

```python
from fireblocks_client.models.source_transfer_peer_path_response_all_of import SourceTransferPeerPathResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SourceTransferPeerPathResponseAllOf from a JSON string
source_transfer_peer_path_response_all_of_instance = SourceTransferPeerPathResponseAllOf.from_json(json)
# print the JSON string representation of the object
print SourceTransferPeerPathResponseAllOf.to_json()

# convert the object into a dict
source_transfer_peer_path_response_all_of_dict = source_transfer_peer_path_response_all_of_instance.to_dict()
# create an instance of SourceTransferPeerPathResponseAllOf from a dict
source_transfer_peer_path_response_all_of_form_dict = source_transfer_peer_path_response_all_of.from_dict(source_transfer_peer_path_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


