# GetOwnershipTokensResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**Paging**](Paging.md) |  | [optional] 
**data** | [**List[TokenOwnershipResponse]**](TokenOwnershipResponse.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.get_ownership_tokens_response import GetOwnershipTokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOwnershipTokensResponse from a JSON string
get_ownership_tokens_response_instance = GetOwnershipTokensResponse.from_json(json)
# print the JSON string representation of the object
print GetOwnershipTokensResponse.to_json()

# convert the object into a dict
get_ownership_tokens_response_dict = get_ownership_tokens_response_instance.to_dict()
# create an instance of GetOwnershipTokensResponse from a dict
get_ownership_tokens_response_form_dict = get_ownership_tokens_response.from_dict(get_ownership_tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


