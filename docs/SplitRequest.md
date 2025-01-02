# SplitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of position to split | 
**amount** | **str** | Amount of tokens to be transferred to the new stake account. | 
**fee** | **str** | Represents the fee for a transaction, which can be specified as a percentage value. Only one of fee/feeLevel is required. | [optional] 
**fee_level** | [**FeeLevel**](FeeLevel.md) |  | [optional] 
**tx_note** | **str** | The note to associate with the transactions. | [optional] 

## Example

```python
from fireblocks.models.split_request import SplitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SplitRequest from a JSON string
split_request_instance = SplitRequest.from_json(json)
# print the JSON string representation of the object
print(SplitRequest.to_json())

# convert the object into a dict
split_request_dict = split_request_instance.to_dict()
# create an instance of SplitRequest from a dict
split_request_from_dict = SplitRequest.from_dict(split_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


