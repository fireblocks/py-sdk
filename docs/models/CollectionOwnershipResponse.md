# fireblocks_client.model.collection_ownership_response.CollectionOwnershipResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**symbol** | str,  | str,  | Collection symbol | 
**blockchainDescriptor** | str,  | str,  | Collection&#x27;s blockchain | must be one of ["ETH", "ETH_TEST3", "POLYGON", "POLYGON_TEST_MUMBAI", ] 
**name** | str,  | str,  | Collection name | 
**id** | str,  | str,  | Fireblocks collection id | 
**standard** | str,  | str,  | Collection contract standard | [optional] 
**contractAddress** | str,  | str,  | Collection contract standard | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

