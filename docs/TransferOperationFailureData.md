# TransferOperationFailureData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** |  | 
**tx_status** | **str** |  | 
**tx_sub_status** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.transfer_operation_failure_data import TransferOperationFailureData

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationFailureData from a JSON string
transfer_operation_failure_data_instance = TransferOperationFailureData.from_json(json)
# print the JSON string representation of the object
print(TransferOperationFailureData.to_json())

# convert the object into a dict
transfer_operation_failure_data_dict = transfer_operation_failure_data_instance.to_dict()
# create an instance of TransferOperationFailureData from a dict
transfer_operation_failure_data_from_dict = TransferOperationFailureData.from_dict(transfer_operation_failure_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


