# CollectionLinkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The collection id | 
**status** | **str** | The collection status | 
**type** | [**CollectionType**](CollectionType.md) |  | 
**display_name** | **str** | The display name of the collection. If was not provided, would be taken from the contract template | [optional] 
**collection_metadata** | [**CollectionMetadataDto**](CollectionMetadataDto.md) | The collection&#39;s metadata | [optional] 

## Example

```python
from fireblocks.models.collection_link_dto import CollectionLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionLinkDto from a JSON string
collection_link_dto_instance = CollectionLinkDto.from_json(json)
# print the JSON string representation of the object
print(CollectionLinkDto.to_json())

# convert the object into a dict
collection_link_dto_dict = collection_link_dto_instance.to_dict()
# create an instance of CollectionLinkDto from a dict
collection_link_dto_from_dict = CollectionLinkDto.from_dict(collection_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


