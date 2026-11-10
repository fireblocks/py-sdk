# TradingPairsListPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TradingPair]**](TradingPair.md) | List of trading pairs. | 
**total** | **int** | Total number of trading pairs matching the query. Best-effort count; may be absent when results are aggregated across multiple providers. | [optional] 
**next** | **str** | A cursor for the next page of results, if available. | [optional] 

## Example

```python
from fireblocks.models.trading_pairs_list_page import TradingPairsListPage

# TODO update the JSON string below
json = "{}"
# create an instance of TradingPairsListPage from a JSON string
trading_pairs_list_page_instance = TradingPairsListPage.from_json(json)
# print the JSON string representation of the object
print(TradingPairsListPage.to_json())

# convert the object into a dict
trading_pairs_list_page_dict = trading_pairs_list_page_instance.to_dict()
# create an instance of TradingPairsListPage from a dict
trading_pairs_list_page_from_dict = TradingPairsListPage.from_dict(trading_pairs_list_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


