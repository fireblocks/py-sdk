# StakeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The source vault account to stake from | 
**provider_id** | [**StakingProvider**](StakingProvider.md) |  | 
**stake_amount** | **str** | Amount of tokens to stake | 
**tx_note** | **str** | The note to associate with the stake transactions. | [optional] 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 

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


