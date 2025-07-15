# TagsPagedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Tag]**](Tag.md) |  | 
**next** | **str** | Cursor to the next page | 

## Example

```python
from fireblocks.models.tags_paged_response import TagsPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagsPagedResponse from a JSON string
tags_paged_response_instance = TagsPagedResponse.from_json(json)
# print the JSON string representation of the object
print(TagsPagedResponse.to_json())

# convert the object into a dict
tags_paged_response_dict = tags_paged_response_instance.to_dict()
# create an instance of TagsPagedResponse from a dict
tags_paged_response_from_dict = TagsPagedResponse.from_dict(tags_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


