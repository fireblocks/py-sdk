# CollectionMintResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | Transaction Id for the mint operation | 

## Example

```python
from fireblocks.models.collection_mint_response_dto import CollectionMintResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionMintResponseDto from a JSON string
collection_mint_response_dto_instance = CollectionMintResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionMintResponseDto.to_json())

# convert the object into a dict
collection_mint_response_dto_dict = collection_mint_response_dto_instance.to_dict()
# create an instance of CollectionMintResponseDto from a dict
collection_mint_response_dto_from_dict = CollectionMintResponseDto.from_dict(collection_mint_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


