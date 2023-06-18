# TokenResponseCollection

Parent collection information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**symbol** | **str** |  | 

## Example

```python
from fireblocks_client.models.token_response_collection import TokenResponseCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponseCollection from a JSON string
token_response_collection_instance = TokenResponseCollection.from_json(json)
# print the JSON string representation of the object
print TokenResponseCollection.to_json()

# convert the object into a dict
token_response_collection_dict = token_response_collection_instance.to_dict()
# create an instance of TokenResponseCollection from a dict
token_response_collection_form_dict = token_response_collection.from_dict(token_response_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


