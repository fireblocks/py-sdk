# GetNFTs200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**Paging**](Paging.md) |  | [optional] 
**data** | [**List[TokenResponse]**](TokenResponse.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.get_nfts200_response import GetNFTs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNFTs200Response from a JSON string
get_nfts200_response_instance = GetNFTs200Response.from_json(json)
# print the JSON string representation of the object
print GetNFTs200Response.to_json()

# convert the object into a dict
get_nfts200_response_dict = get_nfts200_response_instance.to_dict()
# create an instance of GetNFTs200Response from a dict
get_nfts200_response_form_dict = get_nfts200_response.from_dict(get_nfts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


