# fireblocks_client.model.destination_transfer_peer_path_response.DestinationTransferPeerPathResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TransferPeerPath](TransferPeerPath.md) | [**TransferPeerPath**](TransferPeerPath.md) | [**TransferPeerPath**](TransferPeerPath.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Destination of the transaction.  **Note:** In case the transaction is sent to multiple destinations, the &#x60;destinations&#x60; parameter is be used instead of this. | 

# all_of_1

Destination of the transaction.  **Note:** In case the transaction is sent to multiple destinations, the `destinations` parameter is be used instead of this.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Destination of the transaction.  **Note:** In case the transaction is sent to multiple destinations, the &#x60;destinations&#x60; parameter is be used instead of this. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | [optional] 
**subType** | str,  | str,  | In case the type is set to &#x60;EXCHANGE_ACCOUNT&#x60; or &#x60;FIAT_ACCOUNT&#x60;, the specific exchange vendor name or fiat vendor name.In case the type is set to &#x60;INTERNAL_WALLET&#x60; or &#x60;EXTERNAL_WALLET&#x60;, the subType is set to &#x60;Internal&#x60; or &#x60;External&#x60;. | [optional] 
**id** | str,  | str,  | The ID of the peer. You can retrieve the ID of each venue object using the endpoints for [listing vault accounts](https://developers.fireblocks.com/reference/get_vault-accounts-paged), [listing exchange account](https://developers.fireblocks.com/reference/get_exchange-accounts), [listing fiat accounts](https://developers.fireblocks.com/reference/get_fiat-accounts), [listing internal wallets](https://developers.fireblocks.com/reference/get_internal-wallets), [listing external wallets](https://developers.fireblocks.com/reference/get_external-wallets), [listing network connections](https://developers.fireblocks.com/reference/get_network-connections). For the other types, this parameter is not needed. | [optional] 
**name** | str,  | str,  | The name of the peer. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

