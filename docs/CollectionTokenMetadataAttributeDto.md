# CollectionTokenMetadataAttributeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trait_type** | **str** | Name of the trait | 
**value** | **str** | Value of the trait | 
**display_type** | **str** | A field indicating how you would like trait to be displayed | [optional] 

## Example

```python
from fireblocks.models.collection_token_metadata_attribute_dto import CollectionTokenMetadataAttributeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionTokenMetadataAttributeDto from a JSON string
collection_token_metadata_attribute_dto_instance = CollectionTokenMetadataAttributeDto.from_json(json)
# print the JSON string representation of the object
print(CollectionTokenMetadataAttributeDto.to_json())

# convert the object into a dict
collection_token_metadata_attribute_dto_dict = collection_token_metadata_attribute_dto_instance.to_dict()
# create an instance of CollectionTokenMetadataAttributeDto from a dict
collection_token_metadata_attribute_dto_from_dict = CollectionTokenMetadataAttributeDto.from_dict(collection_token_metadata_attribute_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


