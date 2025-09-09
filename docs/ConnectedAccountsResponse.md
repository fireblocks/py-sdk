# ConnectedAccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConnectedAccount]**](ConnectedAccount.md) | List of connected accounts matching the query. | 
**total** | **int** | Total number of accounts by query. | [optional] 
**next** | **str** | A cursor for the next page of results, if available. | [optional] 

## Example

```python
from fireblocks.models.connected_accounts_response import ConnectedAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountsResponse from a JSON string
connected_accounts_response_instance = ConnectedAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountsResponse.to_json())

# convert the object into a dict
connected_accounts_response_dict = connected_accounts_response_instance.to_dict()
# create an instance of ConnectedAccountsResponse from a dict
connected_accounts_response_from_dict = ConnectedAccountsResponse.from_dict(connected_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


