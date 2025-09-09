# QuoteExecutionWithRequoteRequestDetailsAllOfReQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates that the order should be re-quoted if the original quote is expired. This will lead to a market order. | 
**count** | **float** | If quote is expired, how many times to re-generate new quotes to try having the order executed as in the original quote. | 
**slippage_bps** | **float** | Slippage tolerance in basis points (bps) for quote orders - 1 is 0.01% and 10000 is 100% | [optional] [default to 1]

## Example

```python
from fireblocks.models.quote_execution_with_requote_request_details_all_of_re_quote import QuoteExecutionWithRequoteRequestDetailsAllOfReQuote

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteExecutionWithRequoteRequestDetailsAllOfReQuote from a JSON string
quote_execution_with_requote_request_details_all_of_re_quote_instance = QuoteExecutionWithRequoteRequestDetailsAllOfReQuote.from_json(json)
# print the JSON string representation of the object
print(QuoteExecutionWithRequoteRequestDetailsAllOfReQuote.to_json())

# convert the object into a dict
quote_execution_with_requote_request_details_all_of_re_quote_dict = quote_execution_with_requote_request_details_all_of_re_quote_instance.to_dict()
# create an instance of QuoteExecutionWithRequoteRequestDetailsAllOfReQuote from a dict
quote_execution_with_requote_request_details_all_of_re_quote_from_dict = QuoteExecutionWithRequoteRequestDetailsAllOfReQuote.from_dict(quote_execution_with_requote_request_details_all_of_re_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


