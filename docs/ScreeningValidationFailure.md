# ScreeningValidationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fireblocks.models.screening_validation_failure import ScreeningValidationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningValidationFailure from a JSON string
screening_validation_failure_instance = ScreeningValidationFailure.from_json(json)
# print the JSON string representation of the object
print(ScreeningValidationFailure.to_json())

# convert the object into a dict
screening_validation_failure_dict = screening_validation_failure_instance.to_dict()
# create an instance of ScreeningValidationFailure from a dict
screening_validation_failure_from_dict = ScreeningValidationFailure.from_dict(screening_validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


