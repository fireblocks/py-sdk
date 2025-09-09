# MarketExecutionRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | Side of the order | [default to 'BUY']
**base_amount** | **str** | Amount to convert | 
**base_asset_id** | **str** | Source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**type** | **str** | Order type for market orders | 

## Example

```python
from fireblocks.models.market_execution_request_details import MarketExecutionRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MarketExecutionRequestDetails from a JSON string
market_execution_request_details_instance = MarketExecutionRequestDetails.from_json(json)
# print the JSON string representation of the object
print(MarketExecutionRequestDetails.to_json())

# convert the object into a dict
market_execution_request_details_dict = market_execution_request_details_instance.to_dict()
# create an instance of MarketExecutionRequestDetails from a dict
market_execution_request_details_from_dict = MarketExecutionRequestDetails.from_dict(market_execution_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


