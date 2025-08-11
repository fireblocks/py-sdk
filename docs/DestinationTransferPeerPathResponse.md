# DestinationTransferPeerPathResponse

Destination of the transaction.  **Note:** In case the transaction is sent to multiple destinations, the `destinations` parameter is be used instead of this.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransferPeerPathType**](TransferPeerPathType.md) |  | 
**sub_type** | **str** | In case the type is set to &#x60;EXCHANGE_ACCOUNT&#x60; or &#x60;FIAT_ACCOUNT&#x60;, the specific exchange vendor name or fiat vendor name.In case the type is set to &#x60;INTERNAL_WALLET&#x60; or &#x60;EXTERNAL_WALLET&#x60;, the subType is set to &#x60;Internal&#x60; or &#x60;External&#x60;. | [optional] 
**id** | **str** | The ID of the peer. You can retrieve the ID of each venue object using the endpoints for [listing vault accounts](https://developers.fireblocks.com/reference/getpagedvaultaccounts), [listing exchange account](https://developers.fireblocks.com/reference/getexchangeaccounts), [listing fiat accounts](https://developers.fireblocks.com/reference/getfiataccounts), [listing internal wallets](https://developers.fireblocks.com/reference/getinternalwallets), [listing external wallets](https://developers.fireblocks.com/reference/getexternalwallets), [listing network connections](https://developers.fireblocks.com/reference/getnetworkconnections). For the other types, this parameter is not needed. | [optional] 
**name** | **str** | The name of the peer. | [optional] 
**wallet_id** | **str** |  | [optional] 
**trading_account** | **str** | If this transaction is an exchange internal transfer, this field will be populated with the type of that trading account. | [optional] 

## Example

```python
from fireblocks.models.destination_transfer_peer_path_response import DestinationTransferPeerPathResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationTransferPeerPathResponse from a JSON string
destination_transfer_peer_path_response_instance = DestinationTransferPeerPathResponse.from_json(json)
# print the JSON string representation of the object
print(DestinationTransferPeerPathResponse.to_json())

# convert the object into a dict
destination_transfer_peer_path_response_dict = destination_transfer_peer_path_response_instance.to_dict()
# create an instance of DestinationTransferPeerPathResponse from a dict
destination_transfer_peer_path_response_from_dict = DestinationTransferPeerPathResponse.from_dict(destination_transfer_peer_path_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


