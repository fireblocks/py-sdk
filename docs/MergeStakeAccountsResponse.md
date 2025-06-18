# MergeStakeAccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the merge position (the id of the destination position) | 

## Example

```python
from fireblocks.models.merge_stake_accounts_response import MergeStakeAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MergeStakeAccountsResponse from a JSON string
merge_stake_accounts_response_instance = MergeStakeAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(MergeStakeAccountsResponse.to_json())

# convert the object into a dict
merge_stake_accounts_response_dict = merge_stake_accounts_response_instance.to_dict()
# create an instance of MergeStakeAccountsResponse from a dict
merge_stake_accounts_response_from_dict = MergeStakeAccountsResponse.from_dict(merge_stake_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


