# EmbeddedWalletAssetRewardInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_rewards** | **str** | Amount that is pending for rewards | 

## Example

```python
from fireblocks.models.embedded_wallet_asset_reward_info import EmbeddedWalletAssetRewardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletAssetRewardInfo from a JSON string
embedded_wallet_asset_reward_info_instance = EmbeddedWalletAssetRewardInfo.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletAssetRewardInfo.to_json())

# convert the object into a dict
embedded_wallet_asset_reward_info_dict = embedded_wallet_asset_reward_info_instance.to_dict()
# create an instance of EmbeddedWalletAssetRewardInfo from a dict
embedded_wallet_asset_reward_info_from_dict = EmbeddedWalletAssetRewardInfo.from_dict(embedded_wallet_asset_reward_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


