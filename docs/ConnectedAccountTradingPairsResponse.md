# ConnectedAccountTradingPairsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConnectedAccountTradingPair]**](ConnectedAccountTradingPair.md) |  | 
**total** | **int** | Total number of asset pairs matching the query. | [optional] 
**next** | **str** | A cursor for the next page of results, if available. | [optional] 

## Example

```python
from fireblocks.models.connected_account_trading_pairs_response import ConnectedAccountTradingPairsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountTradingPairsResponse from a JSON string
connected_account_trading_pairs_response_instance = ConnectedAccountTradingPairsResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountTradingPairsResponse.to_json())

# convert the object into a dict
connected_account_trading_pairs_response_dict = connected_account_trading_pairs_response_instance.to_dict()
# create an instance of ConnectedAccountTradingPairsResponse from a dict
connected_account_trading_pairs_response_from_dict = ConnectedAccountTradingPairsResponse.from_dict(connected_account_trading_pairs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


