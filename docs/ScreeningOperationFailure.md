# ScreeningOperationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | [**ScreeningOperationExecutionOutput**](ScreeningOperationExecutionOutput.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.screening_operation_failure import ScreeningOperationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningOperationFailure from a JSON string
screening_operation_failure_instance = ScreeningOperationFailure.from_json(json)
# print the JSON string representation of the object
print ScreeningOperationFailure.to_json()

# convert the object into a dict
screening_operation_failure_dict = screening_operation_failure_instance.to_dict()
# create an instance of ScreeningOperationFailure from a dict
screening_operation_failure_form_dict = screening_operation_failure.from_dict(screening_operation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


