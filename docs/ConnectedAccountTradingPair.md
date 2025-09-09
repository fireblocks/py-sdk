# ConnectedAccountTradingPair


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the trading pair. | 
**base_asset_id** | **str** | The Symbol of the base asset. | 
**quote_asset_id** | **str** | The symbol of the quote asset. | 
**supported_types** | [**List[ConnectedAccountTradingPairSupportedType]**](ConnectedAccountTradingPairSupportedType.md) |  | 

## Example

```python
from fireblocks.models.connected_account_trading_pair import ConnectedAccountTradingPair

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountTradingPair from a JSON string
connected_account_trading_pair_instance = ConnectedAccountTradingPair.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountTradingPair.to_json())

# convert the object into a dict
connected_account_trading_pair_dict = connected_account_trading_pair_instance.to_dict()
# create an instance of ConnectedAccountTradingPair from a dict
connected_account_trading_pair_from_dict = ConnectedAccountTradingPair.from_dict(connected_account_trading_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


