# SourceTransferPeerPathResponse

Source of the transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransferPeerPathType**](TransferPeerPathType.md) |  | 
**sub_type** | **str** | In case the type is set to &#x60;EXCHANGE_ACCOUNT&#x60; or &#x60;FIAT_ACCOUNT&#x60;, the specific exchange vendor name or fiat vendor name. In case the type is set to &#x60;INTERNAL_WALLET&#x60; or &#x60;EXTERNAL_WALLET&#x60;, the subType is set to &#x60;Internal&#x60; or &#x60;External&#x60;. | [optional] 
**id** | **str** | The ID of the peer. You can retrieve the ID of each venue object using the endpoints for [listing vault accounts](https://developers.fireblocks.com/reference/get_vault-accounts-paged), [listing exchange account](https://developers.fireblocks.com/reference/get_exchange-accounts), [listing fiat accounts](https://developers.fireblocks.com/reference/get_fiat-accounts), [listing internal wallets](https://developers.fireblocks.com/reference/get_internal-wallets), [listing external wallets](https://developers.fireblocks.com/reference/get_external-wallets), [listing network connections](https://developers.fireblocks.com/reference/get_network-connections). For the other types, this parameter is not needed. | [optional] 
**name** | **str** | The name of the peer. | [optional] 
**wallet_id** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.source_transfer_peer_path_response import SourceTransferPeerPathResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SourceTransferPeerPathResponse from a JSON string
source_transfer_peer_path_response_instance = SourceTransferPeerPathResponse.from_json(json)
# print the JSON string representation of the object
print(SourceTransferPeerPathResponse.to_json())

# convert the object into a dict
source_transfer_peer_path_response_dict = source_transfer_peer_path_response_instance.to_dict()
# create an instance of SourceTransferPeerPathResponse from a dict
source_transfer_peer_path_response_from_dict = SourceTransferPeerPathResponse.from_dict(source_transfer_peer_path_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


