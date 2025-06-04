# EmbeddedWalletAssetBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the asset balance entry | 
**total** | **str** | Total balance amount for the asset in the account (including pending, locked, and available) | 
**available** | **str** | The balance available for use or withdrawal | 
**pending** | **str** | Amount pending confirmation from blockchain (e.g., unconfirmed deposits) | 
**frozen** | **str** | Balance that is frozen due to policy or regulatory lock | 
**locked_amount** | **str** | Funds locked for operations such as staking or delegation | 
**block_height** | **str** | Latest known blockchain height when balance was fetched | [optional] 
**block_hash** | **str** | Hash of the blockchain block associated with the current balance state | [optional] 
**reward_info** | [**EmbeddedWalletAssetRewardInfo**](EmbeddedWalletAssetRewardInfo.md) |  | [optional] 

## Example

```python
from fireblocks.models.embedded_wallet_asset_balance import EmbeddedWalletAssetBalance

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletAssetBalance from a JSON string
embedded_wallet_asset_balance_instance = EmbeddedWalletAssetBalance.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletAssetBalance.to_json())

# convert the object into a dict
embedded_wallet_asset_balance_dict = embedded_wallet_asset_balance_instance.to_dict()
# create an instance of EmbeddedWalletAssetBalance from a dict
embedded_wallet_asset_balance_from_dict = EmbeddedWalletAssetBalance.from_dict(embedded_wallet_asset_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


