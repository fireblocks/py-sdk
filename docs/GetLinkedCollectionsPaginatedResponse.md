# GetLinkedCollectionsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CollectionLinkDto]**](CollectionLinkDto.md) | The data of the current page | [optional] 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.get_linked_collections_paginated_response import GetLinkedCollectionsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLinkedCollectionsPaginatedResponse from a JSON string
get_linked_collections_paginated_response_instance = GetLinkedCollectionsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetLinkedCollectionsPaginatedResponse.to_json())

# convert the object into a dict
get_linked_collections_paginated_response_dict = get_linked_collections_paginated_response_instance.to_dict()
# create an instance of GetLinkedCollectionsPaginatedResponse from a dict
get_linked_collections_paginated_response_from_dict = GetLinkedCollectionsPaginatedResponse.from_dict(get_linked_collections_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


