# QuoteExecutionWithRequoteResponseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Order type for quote orders | 
**quote_id** | **str** | Quote ID for quote orders | 
**quote_amount** | **str** | Quote amount for quote orders | 
**side** | **str** | Side of the order | [default to 'BUY']
**base_amount** | **str** | Amount to convert | 
**base_asset_id** | **str** | Source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**re_quote** | [**QuoteExecutionWithRequoteResponseDetailsAllOfReQuote**](QuoteExecutionWithRequoteResponseDetailsAllOfReQuote.md) |  | [optional] 

## Example

```python
from fireblocks.models.quote_execution_with_requote_response_details import QuoteExecutionWithRequoteResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteExecutionWithRequoteResponseDetails from a JSON string
quote_execution_with_requote_response_details_instance = QuoteExecutionWithRequoteResponseDetails.from_json(json)
# print the JSON string representation of the object
print(QuoteExecutionWithRequoteResponseDetails.to_json())

# convert the object into a dict
quote_execution_with_requote_response_details_dict = quote_execution_with_requote_response_details_instance.to_dict()
# create an instance of QuoteExecutionWithRequoteResponseDetails from a dict
quote_execution_with_requote_response_details_from_dict = QuoteExecutionWithRequoteResponseDetails.from_dict(quote_execution_with_requote_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


