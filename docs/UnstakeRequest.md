# UnstakeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of position to unstake | 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 
**amount** | **str** | The number of tokens to unstake.  This optional field is applicable only for liquid staking and allows for a partial unstake of the position.  If not provided, the entire position will be unstaked by default. | [optional] 

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


