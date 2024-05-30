# GetConnectionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SessionDTO]**](SessionDTO.md) | Array with the requested Web3 connection&#39;s data | 
**paging** | [**Paging**](Paging.md) |  | [optional] 

## Example

```python
from fireblocks.models.get_connections_response import GetConnectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConnectionsResponse from a JSON string
get_connections_response_instance = GetConnectionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetConnectionsResponse.to_json())

# convert the object into a dict
get_connections_response_dict = get_connections_response_instance.to_dict()
# create an instance of GetConnectionsResponse from a dict
get_connections_response_from_dict = GetConnectionsResponse.from_dict(get_connections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


