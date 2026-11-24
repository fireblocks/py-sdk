# SolanaRewardsBreakdown

A breakdown of the staking rewards earned by the position.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflation** | **str** | The inflation reward amount earned by the position, measured in the staked asset unit. | 
**mev** | **str** | The MEV reward amount earned by the position, measured in the staked asset unit. | 
**last_reward_synced_at** | **datetime** | The time (UTC) of the last sync that fetched this position&#39;s rewards from the rewards provider. It is updated on every sync, including when nothing new was found, so it is not the date of the newest reward (see latestInflationRewardDate and latestMevRewardDate). | 
**latest_inflation_reward_date** | **date** | The date (UTC, YYYY-MM-DD) of the newest inflation reward the rewards provider has returned for this stake account. Null until the provider returns one. | [optional] 
**latest_mev_reward_date** | **date** | The date (UTC, YYYY-MM-DD) of the newest MEV reward the rewards provider has returned for this stake account. Null until the provider returns one, and for validators without MEV rewards. | [optional] 

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


