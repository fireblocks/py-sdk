# ConnectedAccountBalancesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConnectedAccountBalances]**](ConnectedAccountBalances.md) | Flat balance row for a single asset within an account and wallet type. One row per (assetId, balanceType). | 
**total** | **int** | Total number of balance rows by query. | [optional] 
**next** | **str** | A cursor for the next page of results, if available. | [optional] 

## Example

```python
from fireblocks.models.connected_account_balances_response import ConnectedAccountBalancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountBalancesResponse from a JSON string
connected_account_balances_response_instance = ConnectedAccountBalancesResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountBalancesResponse.to_json())

# convert the object into a dict
connected_account_balances_response_dict = connected_account_balances_response_instance.to_dict()
# create an instance of ConnectedAccountBalancesResponse from a dict
connected_account_balances_response_from_dict = ConnectedAccountBalancesResponse.from_dict(connected_account_balances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


