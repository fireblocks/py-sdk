# ClaimRewardsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of position to withdraw rewards from | 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 

## Example

```python
from fireblocks.models.claim_rewards_request import ClaimRewardsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimRewardsRequest from a JSON string
claim_rewards_request_instance = ClaimRewardsRequest.from_json(json)
# print the JSON string representation of the object
print(ClaimRewardsRequest.to_json())

# convert the object into a dict
claim_rewards_request_dict = claim_rewards_request_instance.to_dict()
# create an instance of ClaimRewardsRequest from a dict
claim_rewards_request_from_dict = ClaimRewardsRequest.from_dict(claim_rewards_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


