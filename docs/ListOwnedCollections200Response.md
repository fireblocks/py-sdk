# ListOwnedCollections200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paging** | [**Paging**](Paging.md) |  | [optional] 
**data** | [**List[CollectionOwnershipResponse]**](CollectionOwnershipResponse.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.list_owned_collections200_response import ListOwnedCollections200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListOwnedCollections200Response from a JSON string
list_owned_collections200_response_instance = ListOwnedCollections200Response.from_json(json)
# print the JSON string representation of the object
print ListOwnedCollections200Response.to_json()

# convert the object into a dict
list_owned_collections200_response_dict = list_owned_collections200_response_instance.to_dict()
# create an instance of ListOwnedCollections200Response from a dict
list_owned_collections200_response_form_dict = list_owned_collections200_response.from_dict(list_owned_collections200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


