# GetOwnershipTokens200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**Paging**](Paging.md) |  | [optional] 
**data** | [**List[TokenOwnershipResponse]**](TokenOwnershipResponse.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.get_ownership_tokens200_response import GetOwnershipTokens200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOwnershipTokens200Response from a JSON string
get_ownership_tokens200_response_instance = GetOwnershipTokens200Response.from_json(json)
# print the JSON string representation of the object
print GetOwnershipTokens200Response.to_json()

# convert the object into a dict
get_ownership_tokens200_response_dict = get_ownership_tokens200_response_instance.to_dict()
# create an instance of GetOwnershipTokens200Response from a dict
get_ownership_tokens200_response_form_dict = get_ownership_tokens200_response.from_dict(get_ownership_tokens200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


