# VaultAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**total** | **str** | The total wallet balance. In EOS this value includes the network balance, self staking and pending refund. For all other coins it is the balance as it appears on the blockchain. | [optional] 
**balance** | **str** | Deprecated - replaced by \&quot;total\&quot; | [optional] 
**available** | **str** | Funds available for transfer. Equals the blockchain balance minus any locked amounts | [optional] 
**pending** | **str** | The cumulative balance of all transactions pending to be cleared | [optional] 
**frozen** | **str** | The cumulative frozen balance | [optional] 
**locked_amount** | **str** | Funds in outgoing transactions that are not yet published to the network | [optional] 
**staked** | **str** | Staked balance | [optional] 
**total_staked_cpu** | **float** | Deprecated | [optional] 
**total_staked_network** | **str** | Deprecated | [optional] 
**self_staked_cpu** | **str** | Deprecated | [optional] 
**self_staked_network** | **str** | Deprecated | [optional] 
**pending_refund_cpu** | **str** | Deprecated | [optional] 
**pending_refund_network** | **str** | Deprecated | [optional] 
**block_height** | **str** |  | [optional] 
**block_hash** | **str** |  | [optional] 
**rewards_info** | [**RewardsInfo**](RewardsInfo.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.vault_asset import VaultAsset

# TODO update the JSON string below
json = "{}"
# create an instance of VaultAsset from a JSON string
vault_asset_instance = VaultAsset.from_json(json)
# print the JSON string representation of the object
print VaultAsset.to_json()

# convert the object into a dict
vault_asset_dict = vault_asset_instance.to_dict()
# create an instance of VaultAsset from a dict
vault_asset_form_dict = vault_asset.from_dict(vault_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


