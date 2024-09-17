# CollectionBurnResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | Transaction Id for the burn operation | 

## Example

```python
from fireblocks.models.collection_burn_response_dto import CollectionBurnResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionBurnResponseDto from a JSON string
collection_burn_response_dto_instance = CollectionBurnResponseDto.from_json(json)
# print the JSON string representation of the object
print(CollectionBurnResponseDto.to_json())

# convert the object into a dict
collection_burn_response_dto_dict = collection_burn_response_dto_instance.to_dict()
# create an instance of CollectionBurnResponseDto from a dict
collection_burn_response_dto_from_dict = CollectionBurnResponseDto.from_dict(collection_burn_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


