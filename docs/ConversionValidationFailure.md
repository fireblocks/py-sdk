# ConversionValidationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fireblocks.models.conversion_validation_failure import ConversionValidationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionValidationFailure from a JSON string
conversion_validation_failure_instance = ConversionValidationFailure.from_json(json)
# print the JSON string representation of the object
print(ConversionValidationFailure.to_json())

# convert the object into a dict
conversion_validation_failure_dict = conversion_validation_failure_instance.to_dict()
# create an instance of ConversionValidationFailure from a dict
conversion_validation_failure_from_dict = ConversionValidationFailure.from_dict(conversion_validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


