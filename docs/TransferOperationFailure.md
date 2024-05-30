# TransferOperationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | [**TransferOperationFailureData**](TransferOperationFailureData.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_operation_failure import TransferOperationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationFailure from a JSON string
transfer_operation_failure_instance = TransferOperationFailure.from_json(json)
# print the JSON string representation of the object
print(TransferOperationFailure.to_json())

# convert the object into a dict
transfer_operation_failure_dict = transfer_operation_failure_instance.to_dict()
# create an instance of TransferOperationFailure from a dict
transfer_operation_failure_from_dict = TransferOperationFailure.from_dict(transfer_operation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


