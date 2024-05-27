# ConversionOperationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fireblocks_client.models.conversion_operation_failure import ConversionOperationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionOperationFailure from a JSON string
conversion_operation_failure_instance = ConversionOperationFailure.from_json(json)
# print the JSON string representation of the object
print ConversionOperationFailure.to_json()

# convert the object into a dict
conversion_operation_failure_dict = conversion_operation_failure_instance.to_dict()
# create an instance of ConversionOperationFailure from a dict
conversion_operation_failure_form_dict = conversion_operation_failure.from_dict(conversion_operation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


