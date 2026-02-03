# ExecutionRequestDetails

Order execution details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**QuoteTypeEnum**](QuoteTypeEnum.md) |  | 
**side** | [**Side**](Side.md) |  | 
**base_amount** | **str** | Amount to convert | 
**base_asset_id** | **str** | Source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_id** | **str** | Quote ID for quote orders | 
**re_quote** | [**ReQuoteDetailsReQuote**](ReQuoteDetailsReQuote.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_request_details import ExecutionRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionRequestDetails from a JSON string
execution_request_details_instance = ExecutionRequestDetails.from_json(json)
# print the JSON string representation of the object
print(ExecutionRequestDetails.to_json())

# convert the object into a dict
execution_request_details_dict = execution_request_details_instance.to_dict()
# create an instance of ExecutionRequestDetails from a dict
execution_request_details_from_dict = ExecutionRequestDetails.from_dict(execution_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


