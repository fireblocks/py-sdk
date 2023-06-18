# TokenOwnershipResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Fireblocks NFT asset id | 
**token_id** | **str** | Token id within the contract/collection | 
**standard** | **str** | ERC721 / ERC1155 | 
**metadata_uri** | **str** | URL of the original token JSON metadata | [optional] 
**cached_metadata_uri** | **str** | URL of the cached token JSON metadata | [optional] 
**media** | [**List[MediaEntityResponse]**](MediaEntityResponse.md) | Media items extracted from metadata JSON | 
**collection** | [**TokenResponseCollection**](TokenResponseCollection.md) |  | [optional] 
**balance** | **str** |  | 
**vault_account_id** | **str** |  | 
**ownership_start_time** | **float** |  | 
**ownership_last_update_time** | **float** |  | 
**blockchain_descriptor** | **str** |  | 
**description** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from fireblocks_client.models.token_ownership_response import TokenOwnershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenOwnershipResponse from a JSON string
token_ownership_response_instance = TokenOwnershipResponse.from_json(json)
# print the JSON string representation of the object
print TokenOwnershipResponse.to_json()

# convert the object into a dict
token_ownership_response_dict = token_ownership_response_instance.to_dict()
# create an instance of TokenOwnershipResponse from a dict
token_ownership_response_form_dict = token_ownership_response.from_dict(token_ownership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


