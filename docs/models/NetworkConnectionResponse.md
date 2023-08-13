# fireblocks_client.model.network_connection_response.NetworkConnectionResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**localNetworkId** | [**NetworkId**](NetworkId.md) | [**NetworkId**](NetworkId.md) |  | 
**remoteNetworkId** | [**NetworkId**](NetworkId.md) | [**NetworkId**](NetworkId.md) |  | 
**id** | str,  | str,  |  | 
**routingPolicy** | [**NetworkConnectionRoutingPolicy**](NetworkConnectionRoutingPolicy.md) | [**NetworkConnectionRoutingPolicy**](NetworkConnectionRoutingPolicy.md) |  | 
**status** | [**ConfigChangeRequestStatus**](ConfigChangeRequestStatus.md) | [**ConfigChangeRequestStatus**](ConfigChangeRequestStatus.md) |  | 
**[localChannel](#localChannel)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Deprecated - Replaced by &#x60;localNetworkId&#x60; | [optional] 
**[remoteChannel](#remoteChannel)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Deprecated - Replaced by &#x60;remoteNetworkId&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# localChannel

Deprecated - Replaced by `localNetworkId`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Deprecated - Replaced by &#x60;localNetworkId&#x60; | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NetworkChannel](NetworkChannel.md) | [**NetworkChannel**](NetworkChannel.md) | [**NetworkChannel**](NetworkChannel.md) |  | 

# remoteChannel

Deprecated - Replaced by `remoteNetworkId`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Deprecated - Replaced by &#x60;remoteNetworkId&#x60; | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NetworkChannel](NetworkChannel.md) | [**NetworkChannel**](NetworkChannel.md) | [**NetworkChannel**](NetworkChannel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

