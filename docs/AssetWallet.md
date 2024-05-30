# AssetWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_id** | **str** | ID of the vault account. You can [get the vault account by this ID](https://developers.fireblocks.com/reference/get_vault-accounts-vaultaccountid) to retrieve vault properties such as its name, auto fueling, hidden on UI or customer reference ID. | [optional] 
**asset_id** | **str** | ID of the asset. You can get more information about this asset by using the [supported assets API](https://developers.fireblocks.com/reference/get_supported-assets) | [optional] 
**available** | **str** | Available balance, available to use in a transaction. | [optional] 
**total** | **str** | Total balance at the asset wallet, as seen at the blockchain explorers. This includes balance available, and any kind of unavailable balance such as locked, frozen, or others. | [optional] 
**pending** | **str** | Pending balance. | [optional] 
**staked** | **str** | Staked balance. | [optional] 
**frozen** | **str** | Funds frozen due to the anti-money laundering policy at this workspace. | [optional] 
**locked_amount** | **str** | Locked balance. | [optional] 
**block_height** | **str** | The height (number) of the block of the balance. Can by empty. | [optional] 
**block_hash** | **str** | The hash of the block of the balance. Can by empty. | [optional] 
**creation_timestamp** | **str** | Unix timestamp of the time the asset wallet was created. | [optional] 

## Example

```python
from fireblocks.models.asset_wallet import AssetWallet

# TODO update the JSON string below
json = "{}"
# create an instance of AssetWallet from a JSON string
asset_wallet_instance = AssetWallet.from_json(json)
# print the JSON string representation of the object
print(AssetWallet.to_json())

# convert the object into a dict
asset_wallet_dict = asset_wallet_instance.to_dict()
# create an instance of AssetWallet from a dict
asset_wallet_from_dict = AssetWallet.from_dict(asset_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


