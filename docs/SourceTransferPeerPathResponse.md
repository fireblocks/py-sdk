# SourceTransferPeerPathResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sub_type** | **str** | The specific exchange, fiat account or unmanaged wallet (either INTERNAL / EXTERNAL) | [optional] 

## Example

```python
from fireblocks_client.models.source_transfer_peer_path_response import SourceTransferPeerPathResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SourceTransferPeerPathResponse from a JSON string
source_transfer_peer_path_response_instance = SourceTransferPeerPathResponse.from_json(json)
# print the JSON string representation of the object
print SourceTransferPeerPathResponse.to_json()

# convert the object into a dict
source_transfer_peer_path_response_dict = source_transfer_peer_path_response_instance.to_dict()
# create an instance of SourceTransferPeerPathResponse from a dict
source_transfer_peer_path_response_form_dict = source_transfer_peer_path_response.from_dict(source_transfer_peer_path_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


