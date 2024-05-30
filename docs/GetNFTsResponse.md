# GetNFTsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**Paging**](Paging.md) |  | [optional] 
**data** | [**List[TokenResponse]**](TokenResponse.md) |  | [optional] 

## Example

```python
from fireblocks.models.get_nfts_response import GetNFTsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNFTsResponse from a JSON string
get_nfts_response_instance = GetNFTsResponse.from_json(json)
# print the JSON string representation of the object
print(GetNFTsResponse.to_json())

# convert the object into a dict
get_nfts_response_dict = get_nfts_response_instance.to_dict()
# create an instance of GetNFTsResponse from a dict
get_nfts_response_from_dict = GetNFTsResponse.from_dict(get_nfts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


