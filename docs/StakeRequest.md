# StakeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The Fireblocks vault account ID that will source the funds for staking. | 
**provider_id** | [**StakingProvider**](StakingProvider.md) |  | 
**stake_amount** | **str** | The amount of tokens to stake. The amount may be truncated to match the chain&#39;s decimal precision requirements. | 
**tx_note** | **str** | Optional note or comment to associate with the stake transaction. This note will be included in transaction records and can be used for tracking or audit purposes. | [optional] 
**fee** | **str** | Optional transaction fee. Controls the priority and cost of the blockchain transaction. Only one of &#39;fee&#39; or &#39;feeLevel&#39; should be provided; if both are specified, &#39;feeLevel&#39; takes precedence. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 
**chain_descriptor** | **str** | Protocol identifier for the staking operation | [optional] 
**id** | **str** | Applies only to Ethereum compounding validator staking (Pectra/EIP-7251). The ID of an existing staking position to add additional stake to. When provided, adds stake to the specified position instead of creating a new one. Requires &#39;isCompoundingValidator&#39; to be true. | [optional] 
**is_compounding_validator** | **bool** | Applies only to Ethereum staking. Indicates whether to use a compounding validator (see Pectra/EIP-7251). When true, creates a position that supports adding additional stake via the &#39;id&#39; parameter. If not provided, defaults to false and a legacy (non-compounding) validator will be used. | [optional] 

## Example

```python
from fireblocks.models.stake_request import StakeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StakeRequest from a JSON string
stake_request_instance = StakeRequest.from_json(json)
# print the JSON string representation of the object
print(StakeRequest.to_json())

# convert the object into a dict
stake_request_dict = stake_request_instance.to_dict()
# create an instance of StakeRequest from a dict
stake_request_from_dict = StakeRequest.from_dict(stake_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


