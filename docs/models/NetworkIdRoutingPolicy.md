# fireblocks_client.model.network_id_routing_policy.NetworkIdRoutingPolicy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[crypto](#crypto)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[sen](#sen)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[signet](#signet)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[sen_test](#sen_test)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[signet_test](#signet_test)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# crypto

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CustomCryptoRoutingDest](CustomCryptoRoutingDest.md) | [**CustomCryptoRoutingDest**](CustomCryptoRoutingDest.md) | [**CustomCryptoRoutingDest**](CustomCryptoRoutingDest.md) |  | 
[NoneNetworkRoutingDest](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) |  | 

# sen

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CustomFiatRoutingDest](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) |  | 
[NoneNetworkRoutingDest](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) |  | 

# signet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CustomFiatRoutingDest](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) |  | 
[NoneNetworkRoutingDest](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) |  | 

# sen_test

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NoneNetworkRoutingDest](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) |  | 
[CustomFiatRoutingDest](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) |  | 

# signet_test

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NoneNetworkRoutingDest](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) | [**NoneNetworkRoutingDest**](NoneNetworkRoutingDest.md) |  | 
[CustomFiatRoutingDest](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) | [**CustomFiatRoutingDest**](CustomFiatRoutingDest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

