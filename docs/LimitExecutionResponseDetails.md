# LimitExecutionResponseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | Side of the order | [default to 'BUY']
**base_amount** | **str** | Amount to convert | 
**base_asset_id** | **str** | Source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**type** | **str** | Order type for limit orders | 
**time_in_force** | [**TimeInForce**](TimeInForce.md) |  | 
**limit_price** | **str** | Price for limit orders | 

## Example

```python
from fireblocks.models.limit_execution_response_details import LimitExecutionResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LimitExecutionResponseDetails from a JSON string
limit_execution_response_details_instance = LimitExecutionResponseDetails.from_json(json)
# print the JSON string representation of the object
print(LimitExecutionResponseDetails.to_json())

# convert the object into a dict
limit_execution_response_details_dict = limit_execution_response_details_instance.to_dict()
# create an instance of LimitExecutionResponseDetails from a dict
limit_execution_response_details_from_dict = LimitExecutionResponseDetails.from_dict(limit_execution_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


