# GetProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EarnProvider]**](EarnProvider.md) | Page of integrated lending providers. | 
**next** | **str** | Opaque cursor for the next page; empty when there is no next page. | [optional] 
**prev** | **str** | Opaque cursor for the previous page; empty when there is no previous page. | [optional] 
**total** | **int** | Total number of items matching the query. | 

## Example

```python
from fireblocks.models.get_providers_response import GetProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProvidersResponse from a JSON string
get_providers_response_instance = GetProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(GetProvidersResponse.to_json())

# convert the object into a dict
get_providers_response_dict = get_providers_response_instance.to_dict()
# create an instance of GetProvidersResponse from a dict
get_providers_response_from_dict = GetProvidersResponse.from_dict(get_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


