# MergeStakeAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Id of the source position to merge from | 
**destination_id** | **str** | Id of the destination position to merge into | 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 

## Example

```python
from fireblocks.models.merge_stake_accounts_request import MergeStakeAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeStakeAccountsRequest from a JSON string
merge_stake_accounts_request_instance = MergeStakeAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(MergeStakeAccountsRequest.to_json())

# convert the object into a dict
merge_stake_accounts_request_dict = merge_stake_accounts_request_instance.to_dict()
# create an instance of MergeStakeAccountsRequest from a dict
merge_stake_accounts_request_from_dict = MergeStakeAccountsRequest.from_dict(merge_stake_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


