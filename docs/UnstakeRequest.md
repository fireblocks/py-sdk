# UnstakeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of position to unstake | 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 
**amount** | **str** | Amount of tokens to unstake. Only supported for liquid staking (Lido) to enable partial unstaking. For other chains, this field is ignored and the entire position will be unstaked. If not provided, the entire position will be unstaked. | [optional] 

## Example

```python
from fireblocks.models.unstake_request import UnstakeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnstakeRequest from a JSON string
unstake_request_instance = UnstakeRequest.from_json(json)
# print the JSON string representation of the object
print(UnstakeRequest.to_json())

# convert the object into a dict
unstake_request_dict = unstake_request_instance.to_dict()
# create an instance of UnstakeRequest from a dict
unstake_request_from_dict = UnstakeRequest.from_dict(unstake_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


