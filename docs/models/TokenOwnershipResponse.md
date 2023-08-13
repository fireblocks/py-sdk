# fireblocks_client.model.token_ownership_response.TokenOwnershipResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**standard** | str,  | str,  | ERC721 / ERC1155 | 
**blockchainDescriptor** | str,  | str,  |  | must be one of ["ETH", "ETH_TEST3", "POLYGON", "POLYGON_TEST_MUMBAI", ] 
**balance** | str,  | str,  |  | 
**tokenId** | str,  | str,  | Token id within the contract/collection | 
**ownershipStartTime** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**vaultAccountId** | str,  | str,  |  | 
**id** | str,  | str,  | The Fireblocks NFT asset id | 
**[media](#media)** | list, tuple,  | tuple,  | Media items extracted from metadata JSON | 
**ownershipLastUpdateTime** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**metadataURI** | str,  | str,  | URL of the original token JSON metadata | [optional] 
**cachedMetadataURI** | str,  | str,  | URL of the cached token JSON metadata | [optional] 
**[collection](#collection)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Parent collection information | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# media

Media items extracted from metadata JSON

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Media items extracted from metadata JSON | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MediaEntityResponse**](MediaEntityResponse.md) | [**MediaEntityResponse**](MediaEntityResponse.md) | [**MediaEntityResponse**](MediaEntityResponse.md) |  | 

# collection

Parent collection information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Parent collection information | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TokenCollectionResponse](TokenCollectionResponse.md) | [**TokenCollectionResponse**](TokenCollectionResponse.md) | [**TokenCollectionResponse**](TokenCollectionResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

