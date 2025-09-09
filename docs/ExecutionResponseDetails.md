# ExecutionResponseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Order type for limit orders | 
**time_in_force** | [**TimeInForce**](TimeInForce.md) |  | 
**limit_price** | **str** | Price for limit orders | 
**side** | **str** | Side of the order | [default to 'BUY']
**base_amount** | **str** | Amount to convert | 
**base_asset_id** | **str** | Source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_id** | **str** | Quote ID for quote orders | 
**quote_amount** | **str** | Quote amount for quote orders | 
**re_quote** | [**QuoteExecutionWithRequoteResponseDetailsAllOfReQuote**](QuoteExecutionWithRequoteResponseDetailsAllOfReQuote.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_response_details import ExecutionResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionResponseDetails from a JSON string
execution_response_details_instance = ExecutionResponseDetails.from_json(json)
# print the JSON string representation of the object
print(ExecutionResponseDetails.to_json())

# convert the object into a dict
execution_response_details_dict = execution_response_details_instance.to_dict()
# create an instance of ExecutionResponseDetails from a dict
execution_response_details_from_dict = ExecutionResponseDetails.from_dict(execution_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


