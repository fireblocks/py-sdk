# LimitExecutionRequestDetails


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
from fireblocks.models.limit_execution_request_details import LimitExecutionRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LimitExecutionRequestDetails from a JSON string
limit_execution_request_details_instance = LimitExecutionRequestDetails.from_json(json)
# print the JSON string representation of the object
print(LimitExecutionRequestDetails.to_json())

# convert the object into a dict
limit_execution_request_details_dict = limit_execution_request_details_instance.to_dict()
# create an instance of LimitExecutionRequestDetails from a dict
limit_execution_request_details_from_dict = LimitExecutionRequestDetails.from_dict(limit_execution_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


