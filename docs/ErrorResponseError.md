# ErrorResponseError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from fireblocks_client.models.error_response_error import ErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseError from a JSON string
error_response_error_instance = ErrorResponseError.from_json(json)
# print the JSON string representation of the object
print ErrorResponseError.to_json()

# convert the object into a dict
error_response_error_dict = error_response_error_instance.to_dict()
# create an instance of ErrorResponseError from a dict
error_response_error_form_dict = error_response_error.from_dict(error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


