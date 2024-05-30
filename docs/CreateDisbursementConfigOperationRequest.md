# CreateDisbursementConfigOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DisbursementOperationType**](DisbursementOperationType.md) |  | 
**params** | [**DisbursementOperationConfigParams**](DisbursementOperationConfigParams.md) |  | 

## Example

```python
from fireblocks_client.models.create_disbursement_config_operation_request import CreateDisbursementConfigOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDisbursementConfigOperationRequest from a JSON string
create_disbursement_config_operation_request_instance = CreateDisbursementConfigOperationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDisbursementConfigOperationRequest.to_json())

# convert the object into a dict
create_disbursement_config_operation_request_dict = create_disbursement_config_operation_request_instance.to_dict()
# create an instance of CreateDisbursementConfigOperationRequest from a dict
create_disbursement_config_operation_request_from_dict = CreateDisbursementConfigOperationRequest.from_dict(create_disbursement_config_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


