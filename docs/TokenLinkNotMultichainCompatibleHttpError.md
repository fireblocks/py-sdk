# TokenLinkNotMultichainCompatibleHttpError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Bad request error message | 
**code** | **float** | Error code | 

## Example

```python
from fireblocks.models.token_link_not_multichain_compatible_http_error import TokenLinkNotMultichainCompatibleHttpError

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkNotMultichainCompatibleHttpError from a JSON string
token_link_not_multichain_compatible_http_error_instance = TokenLinkNotMultichainCompatibleHttpError.from_json(json)
# print the JSON string representation of the object
print(TokenLinkNotMultichainCompatibleHttpError.to_json())

# convert the object into a dict
token_link_not_multichain_compatible_http_error_dict = token_link_not_multichain_compatible_http_error_instance.to_dict()
# create an instance of TokenLinkNotMultichainCompatibleHttpError from a dict
token_link_not_multichain_compatible_http_error_from_dict = TokenLinkNotMultichainCompatibleHttpError.from_dict(token_link_not_multichain_compatible_http_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


