# TransferOperationConfigParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**source** | [**Account**](Account.md) |  | [optional] 
**destination** | [**Destination**](Destination.md) |  | 

## Example

```python
from fireblocks.models.transfer_operation_config_params import TransferOperationConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOperationConfigParams from a JSON string
transfer_operation_config_params_instance = TransferOperationConfigParams.from_json(json)
# print the JSON string representation of the object
print(TransferOperationConfigParams.to_json())

# convert the object into a dict
transfer_operation_config_params_dict = transfer_operation_config_params_instance.to_dict()
# create an instance of TransferOperationConfigParams from a dict
transfer_operation_config_params_from_dict = TransferOperationConfigParams.from_dict(transfer_operation_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


