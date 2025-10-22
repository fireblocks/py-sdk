# CollectionMintRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The id of the vault account that initiates the mint function. | 
**to** | **str** | The EVM address to mint to  | 
**token_id** | **str** | The token id, recommended to have numerical format and in sequential order | 
**amount** | **str** | For ERC721, amount is optional or should always be 1 and for ERC1155, amount should be 1 or greater | [optional] 
**metadata_uri** | **str** | URL of metadata uploaded, skip uploading to IPFS if this field is provided with any value | [optional] 
**metadata** | [**CollectionTokenMetadataDto**](CollectionTokenMetadataDto.md) | Metadata to upload | [optional] 
**external_id** | **str** | External id that can be used to identify the transaction in your system. The unique identifier of the transaction outside of Fireblocks with max length of 255 characters | [optional] 

## Example

```python
from fireblocks.models.collection_mint_request_dto import CollectionMintRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionMintRequestDto from a JSON string
collection_mint_request_dto_instance = CollectionMintRequestDto.from_json(json)
# print the JSON string representation of the object
print(CollectionMintRequestDto.to_json())

# convert the object into a dict
collection_mint_request_dto_dict = collection_mint_request_dto_instance.to_dict()
# create an instance of CollectionMintRequestDto from a dict
collection_mint_request_dto_from_dict = CollectionMintRequestDto.from_dict(collection_mint_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


