# Delegation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the staking position | 
**vault_account_id** | **str** | The source vault account to stake from | 
**validator_name** | **str** | The destination validator address name | 
**provider_name** | **str** | The destination validator provider name | 
**chain_descriptor** | **str** | The protocol identifier (e.g. \&quot;ETH\&quot;/ \&quot;SOL\&quot;) to use | 
**amount** | **str** | Amount of tokens to stake, measured in the staked asset unit. | 
**rewards_amount** | **str** | The amount staked in the position, measured in the staked asset unit. | 
**date_created** | **datetime** | When was the request made (ISO Date). | 
**date_updated** | **datetime** | When has the position last changed (ISO Date). | 
**status** | **str** | The current status. | 
**related_transactions** | [**List[RelatedTransaction]**](RelatedTransaction.md) | An array of transaction objects related to this position. Each object includes a &#39;txId&#39; representing the transaction ID and a &#39;completed&#39; boolean indicating if the transaction was completed. | 
**validator_address** | **str** | The destination address of the staking transaction. | 
**provider_id** | [**StakingProvider**](StakingProvider.md) |  | 
**available_actions** | **List[str]** | An array of available actions that can be performed. for example, actions like \&quot;unstake\&quot; or \&quot;withdraw\&quot;. | 
**in_progress** | **bool** | Indicates whether there is an ongoing action for this position (true if ongoing, false if not). | 
**in_progress_tx_id** | **str** | The transaction ID of the ongoing request | [optional] 
**blockchain_position_info** | [**SolanaBlockchainData**](SolanaBlockchainData.md) |  | 
**related_requests** | [**List[RelatedRequest]**](RelatedRequest.md) | An array of partial unstake requests for this position, relevant only for the Lido provider. Each object includes the status of the unstake request, a boolean indicating whether the action is in progress, the amount of tokens to unstake, and the transaction ID of the request. With Lido, a position may have multiple partial unstake requests in different states. This field is optional and not applicable for other providers. | [optional] 

## Example

```python
from fireblocks.models.delegation import Delegation

# TODO update the JSON string below
json = "{}"
# create an instance of Delegation from a JSON string
delegation_instance = Delegation.from_json(json)
# print the JSON string representation of the object
print(Delegation.to_json())

# convert the object into a dict
delegation_dict = delegation_instance.to_dict()
# create an instance of Delegation from a dict
delegation_from_dict = Delegation.from_dict(delegation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


