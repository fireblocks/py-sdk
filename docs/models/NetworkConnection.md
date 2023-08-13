# fireblocks_client.model.network_connection.NetworkConnection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**localNetworkId** | str,  | str,  | The network ID of the profile trying to create the connection. | 
**remoteNetworkId** | str,  | str,  | The network ID the profile is attempting to connect to. | 
**routingPolicy** | [**NetworkConnectionRoutingPolicy**](NetworkConnectionRoutingPolicy.md) | [**NetworkConnectionRoutingPolicy**](NetworkConnectionRoutingPolicy.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

