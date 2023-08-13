# fireblocks_client.model.transaction_response_destination.TransactionResponseDestination

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**destinationAddress** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Address where the asset was transferred. | [optional] 
**destinationAddressDescription** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Description of the address. | [optional] 
**amount** | str,  | str,  | The amount to be sent to this destination. | [optional] 
**amountUSD** | str,  | str,  | The USD value of the requested amount. | [optional] 
**amlScreeningResult** | [**AmlScreeningResult**](AmlScreeningResult.md) | [**AmlScreeningResult**](AmlScreeningResult.md) |  | [optional] 
**destination** | [**DestinationTransferPeerPathResponse**](DestinationTransferPeerPathResponse.md) | [**DestinationTransferPeerPathResponse**](DestinationTransferPeerPathResponse.md) |  | [optional] 
**authorizationInfo** | [**AuthorizationInfo**](AuthorizationInfo.md) | [**AuthorizationInfo**](AuthorizationInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

