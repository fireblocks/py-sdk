# TokenOwnershipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Fireblocks NFT asset id | 
**token_id** | **str** | Token id within the contract/collection | 
**standard** | **str** | ERC721 / ERC1155 | 
**metadata_uri** | **str** | URL of the original token JSON metadata | [optional] 
**cached_metadata_uri** | **str** | URL of the cached token JSON metadata | [optional] 
**media** | [**List[MediaEntityResponse]**](MediaEntityResponse.md) | Media items extracted from metadata JSON | [optional] 
**spam** | [**SpamOwnershipResponse**](SpamOwnershipResponse.md) | Owned Token&#39;s Spam status | [optional] 
**collection** | [**TokenCollectionResponse**](TokenCollectionResponse.md) | Parent collection information | [optional] 
**balance** | **str** |  | 
**vault_account_id** | **str** |  | [optional] 
**ownership_start_time** | **float** |  | 
**ownership_last_update_time** | **float** |  | 
**blockchain_descriptor** | **str** |  | 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**ncw_id** | **str** | Ownership Non-Custodial Wallet ID | [optional] 
**ncw_account_id** | **str** | Ownership Non-Custodial Wallet&#39;s account ID | [optional] 
**status** | **str** | Owned Token&#39;s status | 

## Example

```python
from fireblocks.models.token_ownership_response import TokenOwnershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenOwnershipResponse from a JSON string
token_ownership_response_instance = TokenOwnershipResponse.from_json(json)
# print the JSON string representation of the object
print(TokenOwnershipResponse.to_json())

# convert the object into a dict
token_ownership_response_dict = token_ownership_response_instance.to_dict()
# create an instance of TokenOwnershipResponse from a dict
token_ownership_response_from_dict = TokenOwnershipResponse.from_dict(token_ownership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


