# fireblocks_client.model.vault_asset.VaultAsset

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**total** | str,  | str,  | The total wallet balance. In EOS this value includes the network balance, self staking and pending refund. For all other coins it is the balance as it appears on the blockchain. | [optional] 
**balance** | str,  | str,  | Deprecated - replaced by \&quot;total\&quot; | [optional] 
**available** | str,  | str,  | Funds available for transfer. Equals the blockchain balance minus any locked amounts | [optional] 
**pending** | str,  | str,  | The cumulative balance of all transactions pending to be cleared | [optional] 
**frozen** | str,  | str,  | The cumulative frozen balance | [optional] 
**lockedAmount** | str,  | str,  | Funds in outgoing transactions that are not yet published to the network | [optional] 
**staked** | str,  | str,  | Staked balance | [optional] 
**totalStakedCPU** | decimal.Decimal, int, float,  | decimal.Decimal,  | Deprecated | [optional] 
**totalStakedNetwork** | str,  | str,  | Deprecated | [optional] 
**selfStakedCPU** | str,  | str,  | Deprecated | [optional] 
**selfStakedNetwork** | str,  | str,  | Deprecated | [optional] 
**pendingRefundCPU** | str,  | str,  | Deprecated | [optional] 
**pendingRefundNetwork** | str,  | str,  | Deprecated | [optional] 
**blockHeight** | str,  | str,  |  | [optional] 
**blockHash** | str,  | str,  |  | [optional] 
**rewardsInfo** | [**RewardsInfo**](RewardsInfo.md) | [**RewardsInfo**](RewardsInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

