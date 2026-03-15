# MarketExecutionRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MarketTypeEnum**](MarketTypeEnum.md) |  | 
**side** | [**Side**](Side.md) |  | 
**base_amount** | **str** | Amount in baseAssetId. BUY &#x3D; base amount to receive; SELL &#x3D; base amount to sell. | 
**base_asset_id** | **str** | The asset you receive on BUY / give on SELL. | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Counter asset used to pay/receive | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 

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


