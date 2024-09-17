# CollectionTokenMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Token&#39;s name | 
**description** | **str** | Token&#39;s description | 
**image** | **str** | Token&#39;s image URL | [optional] 
**animation_url** | **str** | Token&#39;s animation URL | [optional] 
**external_url** | **str** | Token&#39;s external URL | [optional] 
**attributes** | [**List[CollectionTokenMetadataAttributeDto]**](CollectionTokenMetadataAttributeDto.md) | Token&#39;s metadata attributes | [optional] 

## Example

```python
from fireblocks.models.collection_token_metadata_dto import CollectionTokenMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionTokenMetadataDto from a JSON string
collection_token_metadata_dto_instance = CollectionTokenMetadataDto.from_json(json)
# print the JSON string representation of the object
print(CollectionTokenMetadataDto.to_json())

# convert the object into a dict
collection_token_metadata_dto_dict = collection_token_metadata_dto_instance.to_dict()
# create an instance of CollectionTokenMetadataDto from a dict
collection_token_metadata_dto_from_dict = CollectionTokenMetadataDto.from_dict(collection_token_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


