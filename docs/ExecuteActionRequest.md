# ExecuteActionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The source vault account to stake from | 
**provider_id** | **str** | The ID of the provider | 
**stake_amount** | **str** | Amount of tokens to stake | 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | **str** | Represents the fee level for a transaction, which can be set as slow, medium, or fast. Only one of fee/feeLevel is required. | [optional] 
**id** | **str** | id of position to withdraw | 
**amount** | **str** | The number of tokens to unstake.  This optional field is applicable only for liquid staking and allows for a partial unstake of the position.  If not provided, the entire position will be unstaked by default. | [optional] 

## Example

```python
from fireblocks.models.execute_action_request import ExecuteActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteActionRequest from a JSON string
execute_action_request_instance = ExecuteActionRequest.from_json(json)
# print the JSON string representation of the object
print(ExecuteActionRequest.to_json())

# convert the object into a dict
execute_action_request_dict = execute_action_request_instance.to_dict()
# create an instance of ExecuteActionRequest from a dict
execute_action_request_from_dict = ExecuteActionRequest.from_dict(execute_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


