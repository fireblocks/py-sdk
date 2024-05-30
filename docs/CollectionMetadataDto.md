# CollectionMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fb_collection_id** | **str** | Fireblocks collection id | 
**name** | **str** | Collection name | [optional] 
**symbol** | **str** | Collection symbol | [optional] 
**standard** | **str** | Collection contract standard | [optional] 
**blockchain_descriptor** | **str** | Collection&#39;s blockchain | 
**contract_address** | **str** | Collection contract address | [optional] 

## Example

```python
from fireblocks_client.models.collection_metadata_dto import CollectionMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionMetadataDto from a JSON string
collection_metadata_dto_instance = CollectionMetadataDto.from_json(json)
# print the JSON string representation of the object
print(CollectionMetadataDto.to_json())

# convert the object into a dict
collection_metadata_dto_dict = collection_metadata_dto_instance.to_dict()
# create an instance of CollectionMetadataDto from a dict
collection_metadata_dto_from_dict = CollectionMetadataDto.from_dict(collection_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


