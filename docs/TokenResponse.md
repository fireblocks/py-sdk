# TokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Fireblocks NFT asset id | 
**token_id** | **str** | Token id within the contract/collection | 
**standard** | **str** | ERC721 / ERC1155 | 
**metadata_uri** | **str** | URL of the original token JSON metadata | [optional] 
**cached_metadata_uri** | **str** | URL of the cached token JSON metadata | [optional] 
**media** | [**List[MediaEntityResponse]**](MediaEntityResponse.md) | Media items extracted from metadata JSON | [optional] 
**spam** | [**SpamTokenResponse**](SpamTokenResponse.md) | Token spam status | [optional] 
**collection** | [**TokenCollectionResponse**](TokenCollectionResponse.md) | Parent collection information | [optional] 
**blockchain_descriptor** | **str** |  | 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print TokenResponse.to_json()

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_form_dict = token_response.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


