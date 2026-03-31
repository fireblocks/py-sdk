# Position


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the staking position | 
**vault_account_id** | **str** | The source vault account to stake from | 
**validator_name** | **str** | The destination validator address name | 
**provider_name** | **str** | The destination validator provider name | 
**chain_descriptor** | **str** | The protocol identifier (e.g. \&quot;ETH\&quot;/ \&quot;SOL\&quot;) to use | 
**amount** | **str** | Total value of the staking position. For Solana, Lido and Ethereum (compounding validator): includes the original stake plus accumulated rewards. For MATIC, Cosmos and Ethereum (legacy validator): refers to the amount currently staked. | 
**rewards_amount** | **str** | The amount staked in the position, measured in the staked asset unit. | 
**date_created** | **datetime** | When was the request made (ISO Date). | 
**date_updated** | **datetime** | When has the position last changed (ISO Date). | 
**status** | **str** | The current status. | 
**validator_address** | **str** | The destination address of the staking transaction. | 
**provider_id** | [**StakingProvider**](StakingProvider.md) |  | 
**available_actions** | **List[str]** | An array of available actions that can be performed. for example, actions like \&quot;UNSTAKE\&quot; or \&quot;WITHDRAW\&quot;. | 
**in_progress** | **bool** | Indicates whether there is an ongoing action for this position related to this request | 
**in_progress_tx_id** | **str** | The transaction ID of the initial stake position request only. Only present when there is an active initial stake transaction. | [optional] 
**blockchain_position_info** | [**DelegationBlockchainPositionInfo**](DelegationBlockchainPositionInfo.md) |  | 

## Example

```python
from fireblocks.models.position import Position

# TODO update the JSON string below
json = "{}"
# create an instance of Position from a JSON string
position_instance = Position.from_json(json)
# print the JSON string representation of the object
print(Position.to_json())

# convert the object into a dict
position_dict = position_instance.to_dict()
# create an instance of Position from a dict
position_from_dict = Position.from_dict(position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


