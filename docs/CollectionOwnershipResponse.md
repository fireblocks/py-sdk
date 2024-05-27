# CollectionOwnershipResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Fireblocks collection id | 
**name** | **str** | Collection name | [optional] 
**symbol** | **str** | Collection symbol | [optional] 
**standard** | **str** | Collection contract standard | [optional] 
**blockchain_descriptor** | **str** | Collection&#39;s blockchain | 
**contract_address** | **str** | Collection contract standard | [optional] 

## Example

```python
from fireblocks_client.models.collection_ownership_response import CollectionOwnershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionOwnershipResponse from a JSON string
collection_ownership_response_instance = CollectionOwnershipResponse.from_json(json)
# print the JSON string representation of the object
print CollectionOwnershipResponse.to_json()

# convert the object into a dict
collection_ownership_response_dict = collection_ownership_response_instance.to_dict()
# create an instance of CollectionOwnershipResponse from a dict
collection_ownership_response_form_dict = collection_ownership_response.from_dict(collection_ownership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


