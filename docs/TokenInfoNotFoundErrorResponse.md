# TokenInfoNotFoundErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Not found error code | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.token_info_not_found_error_response import TokenInfoNotFoundErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInfoNotFoundErrorResponse from a JSON string
token_info_not_found_error_response_instance = TokenInfoNotFoundErrorResponse.from_json(json)
# print the JSON string representation of the object
print(TokenInfoNotFoundErrorResponse.to_json())

# convert the object into a dict
token_info_not_found_error_response_dict = token_info_not_found_error_response_instance.to_dict()
# create an instance of TokenInfoNotFoundErrorResponse from a dict
token_info_not_found_error_response_from_dict = TokenInfoNotFoundErrorResponse.from_dict(token_info_not_found_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


