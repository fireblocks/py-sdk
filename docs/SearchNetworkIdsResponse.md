# SearchNetworkIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NetworkIdResponse]**](NetworkIdResponse.md) |  | [optional] 
**next** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.search_network_ids_response import SearchNetworkIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchNetworkIdsResponse from a JSON string
search_network_ids_response_instance = SearchNetworkIdsResponse.from_json(json)
# print the JSON string representation of the object
print(SearchNetworkIdsResponse.to_json())

# convert the object into a dict
search_network_ids_response_dict = search_network_ids_response_instance.to_dict()
# create an instance of SearchNetworkIdsResponse from a dict
search_network_ids_response_from_dict = SearchNetworkIdsResponse.from_dict(search_network_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


