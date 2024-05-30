# ListOwnedTokensResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**Paging**](Paging.md) |  | [optional] 
**data** | [**List[TokenResponse]**](TokenResponse.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.list_owned_tokens_response import ListOwnedTokensResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOwnedTokensResponse from a JSON string
list_owned_tokens_response_instance = ListOwnedTokensResponse.from_json(json)
# print the JSON string representation of the object
print(ListOwnedTokensResponse.to_json())

# convert the object into a dict
list_owned_tokens_response_dict = list_owned_tokens_response_instance.to_dict()
# create an instance of ListOwnedTokensResponse from a dict
list_owned_tokens_response_from_dict = ListOwnedTokensResponse.from_dict(list_owned_tokens_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


