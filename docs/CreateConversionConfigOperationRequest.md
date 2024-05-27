# CreateConversionConfigOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ConversionOperationType**](ConversionOperationType.md) |  | 
**params** | [**ConversionOperationConfigParams**](ConversionOperationConfigParams.md) |  | 

## Example

```python
from fireblocks_client.models.create_conversion_config_operation_request import CreateConversionConfigOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConversionConfigOperationRequest from a JSON string
create_conversion_config_operation_request_instance = CreateConversionConfigOperationRequest.from_json(json)
# print the JSON string representation of the object
print CreateConversionConfigOperationRequest.to_json()

# convert the object into a dict
create_conversion_config_operation_request_dict = create_conversion_config_operation_request_instance.to_dict()
# create an instance of CreateConversionConfigOperationRequest from a dict
create_conversion_config_operation_request_form_dict = create_conversion_config_operation_request.from_dict(create_conversion_config_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


