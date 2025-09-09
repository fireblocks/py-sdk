# ProvidersListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TradingProvider]**](TradingProvider.md) | List of available providers | 
**total** | **int** | Total number of providers matching the query. | 
**next** | **str** | A cursor for the next page of results, if available. | [optional] 

## Example

```python
from fireblocks.models.providers_list_response import ProvidersListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidersListResponse from a JSON string
providers_list_response_instance = ProvidersListResponse.from_json(json)
# print the JSON string representation of the object
print(ProvidersListResponse.to_json())

# convert the object into a dict
providers_list_response_dict = providers_list_response_instance.to_dict()
# create an instance of ProvidersListResponse from a dict
providers_list_response_from_dict = ProvidersListResponse.from_dict(providers_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


