# GetPositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Position2]**](Position2.md) | Page of user lending positions for this query. | 
**next** | **str** | Opaque cursor for the next page; empty when there is no next page. | [optional] 
**prev** | **str** | Opaque cursor for the previous page; empty when there is no previous page. | [optional] 
**total** | **int** | Total number of items matching the query. | 

## Example

```python
from fireblocks.models.get_positions_response import GetPositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPositionsResponse from a JSON string
get_positions_response_instance = GetPositionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetPositionsResponse.to_json())

# convert the object into a dict
get_positions_response_dict = get_positions_response_instance.to_dict()
# create an instance of GetPositionsResponse from a dict
get_positions_response_from_dict = GetPositionsResponse.from_dict(get_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


