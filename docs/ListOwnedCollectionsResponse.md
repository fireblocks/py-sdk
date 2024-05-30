# ListOwnedCollectionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**Paging**](Paging.md) |  | [optional] 
**data** | [**List[CollectionOwnershipResponse]**](CollectionOwnershipResponse.md) |  | [optional] 

## Example

```python
from fireblocks.models.list_owned_collections_response import ListOwnedCollectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListOwnedCollectionsResponse from a JSON string
list_owned_collections_response_instance = ListOwnedCollectionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListOwnedCollectionsResponse.to_json())

# convert the object into a dict
list_owned_collections_response_dict = list_owned_collections_response_instance.to_dict()
# create an instance of ListOwnedCollectionsResponse from a dict
list_owned_collections_response_from_dict = ListOwnedCollectionsResponse.from_dict(list_owned_collections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


