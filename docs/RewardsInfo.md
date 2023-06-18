# RewardsInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_rewards** | **str** | Amount that is pending for rewards | [optional] 

## Example

```python
from fireblocks_client.models.rewards_info import RewardsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RewardsInfo from a JSON string
rewards_info_instance = RewardsInfo.from_json(json)
# print the JSON string representation of the object
print RewardsInfo.to_json()

# convert the object into a dict
rewards_info_dict = rewards_info_instance.to_dict()
# create an instance of RewardsInfo from a dict
rewards_info_form_dict = rewards_info.from_dict(rewards_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


