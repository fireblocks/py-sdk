# CreateConfigOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DisbursementOperationType**](DisbursementOperationType.md) |  | 
**params** | [**DisbursementOperationConfigParams**](DisbursementOperationConfigParams.md) |  | 

## Example

```python
from fireblocks.models.create_config_operation_request import CreateConfigOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfigOperationRequest from a JSON string
create_config_operation_request_instance = CreateConfigOperationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConfigOperationRequest.to_json())

# convert the object into a dict
create_config_operation_request_dict = create_config_operation_request_instance.to_dict()
# create an instance of CreateConfigOperationRequest from a dict
create_config_operation_request_from_dict = CreateConfigOperationRequest.from_dict(create_config_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


