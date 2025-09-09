# QuoteExecutionResponseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | Side of the order | [default to 'BUY']
**base_amount** | **str** | Amount to convert | 
**base_asset_id** | **str** | Source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**type** | **str** | Order type for quote orders | 
**quote_id** | **str** | Quote ID for quote orders | 
**quote_amount** | **str** | Quote amount for quote orders | 

## Example

```python
from fireblocks.models.quote_execution_response_details import QuoteExecutionResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteExecutionResponseDetails from a JSON string
quote_execution_response_details_instance = QuoteExecutionResponseDetails.from_json(json)
# print the JSON string representation of the object
print(QuoteExecutionResponseDetails.to_json())

# convert the object into a dict
quote_execution_response_details_dict = quote_execution_response_details_instance.to_dict()
# create an instance of QuoteExecutionResponseDetails from a dict
quote_execution_response_details_from_dict = QuoteExecutionResponseDetails.from_dict(quote_execution_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


