# fireblocks_client.model.asset_wallet.AssetWallet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vaultId** | str,  | str,  | ID of the vault account. You can [get the vault account by this ID](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid) to retrieve vault properties such as its name, auto fueling, hidden on UI or customer reference ID. | [optional] 
**assetId** | str,  | str,  | ID of the asset. You can get more information about this asset by using the [supported assets API](https://developers.fireblocks.com/reference/get_supported-assets) | [optional] 
**available** | str,  | str,  | Available balance, available to use in a transaction. | [optional] 
**total** | str,  | str,  | Total balance at the asset wallet, as seen at the blockchain explorers. This includes balance available, and any kind of unavailable balance such as locked, frozen, or others. | [optional] 
**pending** | str,  | str,  | Pending balance. | [optional] 
**staked** | str,  | str,  | Staked balance. | [optional] 
**frozen** | str,  | str,  | Funds frozen due to the anti-money laundering policy at this workspace. | [optional] 
**lockedAmount** | str,  | str,  | Locked balance. | [optional] 
**blockHeight** | str,  | str,  | The height (number) of the block of the balance. Can by empty. | [optional] 
**blockHash** | str,  | str,  | The hash of the block of the balance. Can by empty. | [optional] 
**creationTimestamp** | str,  | str,  | Unix timestamp of the time the asset wallet was created. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

