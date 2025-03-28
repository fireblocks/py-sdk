# InvalidParamaterValueError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Bad request error message | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.invalid_paramater_value_error import InvalidParamaterValueError

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParamaterValueError from a JSON string
invalid_paramater_value_error_instance = InvalidParamaterValueError.from_json(json)
# print the JSON string representation of the object
print(InvalidParamaterValueError.to_json())

# convert the object into a dict
invalid_paramater_value_error_dict = invalid_paramater_value_error_instance.to_dict()
# create an instance of InvalidParamaterValueError from a dict
invalid_paramater_value_error_from_dict = InvalidParamaterValueError.from_dict(invalid_paramater_value_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


