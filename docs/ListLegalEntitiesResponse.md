# ListLegalEntitiesResponse

Paginated response containing a list of legal entity registrations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of legal entity registrations (optional) | [optional] 
**data** | [**List[LegalEntityRegistration]**](LegalEntityRegistration.md) | Legal entity registrations for the current page | 
**next** | **str** | Cursor to pass as &#x60;pageCursor&#x60; to retrieve the next page | [optional] 
**prev** | **str** | Cursor to pass as &#x60;pageCursor&#x60; to retrieve the previous page | [optional] 

## Example

```python
from fireblocks.models.list_legal_entities_response import ListLegalEntitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListLegalEntitiesResponse from a JSON string
list_legal_entities_response_instance = ListLegalEntitiesResponse.from_json(json)
# print the JSON string representation of the object
print(ListLegalEntitiesResponse.to_json())

# convert the object into a dict
list_legal_entities_response_dict = list_legal_entities_response_instance.to_dict()
# create an instance of ListLegalEntitiesResponse from a dict
list_legal_entities_response_from_dict = ListLegalEntitiesResponse.from_dict(list_legal_entities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


