# TokenCollectionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**symbol** | **str** |  | 

## Example

```python
from fireblocks_client.models.token_collection_response import TokenCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCollectionResponse from a JSON string
token_collection_response_instance = TokenCollectionResponse.from_json(json)
# print the JSON string representation of the object
print TokenCollectionResponse.to_json()

# convert the object into a dict
token_collection_response_dict = token_collection_response_instance.to_dict()
# create an instance of TokenCollectionResponse from a dict
token_collection_response_form_dict = token_collection_response.from_dict(token_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


