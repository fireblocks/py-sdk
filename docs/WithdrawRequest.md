# WithdrawRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of position to withdraw | 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 

## Example

```python
from fireblocks.models.withdraw_request import WithdrawRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawRequest from a JSON string
withdraw_request_instance = WithdrawRequest.from_json(json)
# print the JSON string representation of the object
print(WithdrawRequest.to_json())

# convert the object into a dict
withdraw_request_dict = withdraw_request_instance.to_dict()
# create an instance of WithdrawRequest from a dict
withdraw_request_from_dict = WithdrawRequest.from_dict(withdraw_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


