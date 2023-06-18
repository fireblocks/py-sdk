# RewardInfo

This field is relevant only for Algorand transactions. Both `srcRewards` and `destRewards` will appear only for Vault to Vault transactions, otherwise you will receive only the Fireblocks’ side of the transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_rewards** | **str** |  | [optional] 
**dest_rewards** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.reward_info import RewardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RewardInfo from a JSON string
reward_info_instance = RewardInfo.from_json(json)
# print the JSON string representation of the object
print RewardInfo.to_json()

# convert the object into a dict
reward_info_dict = reward_info_instance.to_dict()
# create an instance of RewardInfo from a dict
reward_info_form_dict = reward_info.from_dict(reward_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


