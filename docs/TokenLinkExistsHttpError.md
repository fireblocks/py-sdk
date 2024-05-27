# TokenLinkExistsHttpError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **int** | HTTP status code | [optional] 
**message** | **str** | Error message | [optional] 
**error** | **str** | Short description of the HTTP error | [optional] 

## Example

```python
from fireblocks_client.models.token_link_exists_http_error import TokenLinkExistsHttpError

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkExistsHttpError from a JSON string
token_link_exists_http_error_instance = TokenLinkExistsHttpError.from_json(json)
# print the JSON string representation of the object
print TokenLinkExistsHttpError.to_json()

# convert the object into a dict
token_link_exists_http_error_dict = token_link_exists_http_error_instance.to_dict()
# create an instance of TokenLinkExistsHttpError from a dict
token_link_exists_http_error_form_dict = token_link_exists_http_error.from_dict(token_link_exists_http_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


