# SolanaRewardsBreakdown

A breakdown of the staking rewards earned by the position.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuance** | **str** | The issuance reward amount earned by the position, measured in the staked asset unit. | 
**mev** | **str** | The MEV reward amount earned by the position, measured in the staked asset unit. | 
**last_reward_synced_at** | **datetime** | The last time the rewards were synced (ISO Date). | 

## Example

```python
from fireblocks.models.solana_rewards_breakdown import SolanaRewardsBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaRewardsBreakdown from a JSON string
solana_rewards_breakdown_instance = SolanaRewardsBreakdown.from_json(json)
# print the JSON string representation of the object
print(SolanaRewardsBreakdown.to_json())

# convert the object into a dict
solana_rewards_breakdown_dict = solana_rewards_breakdown_instance.to_dict()
# create an instance of SolanaRewardsBreakdown from a dict
solana_rewards_breakdown_from_dict = SolanaRewardsBreakdown.from_dict(solana_rewards_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


