# GetOpportunitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Opportunity]**](Opportunity.md) | Page of lending opportunities for this query. | 
**next** | **str** | Opaque cursor for the next page; empty when there is no next page. | [optional] 
**prev** | **str** | Opaque cursor for the previous page; empty when there is no previous page. | [optional] 
**total** | **int** | Total number of items matching the query. | 

## Example

```python
from fireblocks.models.get_opportunities_response import GetOpportunitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpportunitiesResponse from a JSON string
get_opportunities_response_instance = GetOpportunitiesResponse.from_json(json)
# print the JSON string representation of the object
print(GetOpportunitiesResponse.to_json())

# convert the object into a dict
get_opportunities_response_dict = get_opportunities_response_instance.to_dict()
# create an instance of GetOpportunitiesResponse from a dict
get_opportunities_response_from_dict = GetOpportunitiesResponse.from_dict(get_opportunities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


