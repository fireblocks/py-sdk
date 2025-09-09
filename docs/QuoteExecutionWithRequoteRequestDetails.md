# QuoteExecutionWithRequoteRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Order type for quote orders | 
**quote_id** | **str** | Quote ID for quote orders | 
**re_quote** | [**QuoteExecutionWithRequoteRequestDetailsAllOfReQuote**](QuoteExecutionWithRequoteRequestDetailsAllOfReQuote.md) |  | [optional] 

## Example

```python
from fireblocks.models.quote_execution_with_requote_request_details import QuoteExecutionWithRequoteRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteExecutionWithRequoteRequestDetails from a JSON string
quote_execution_with_requote_request_details_instance = QuoteExecutionWithRequoteRequestDetails.from_json(json)
# print the JSON string representation of the object
print(QuoteExecutionWithRequoteRequestDetails.to_json())

# convert the object into a dict
quote_execution_with_requote_request_details_dict = quote_execution_with_requote_request_details_instance.to_dict()
# create an instance of QuoteExecutionWithRequoteRequestDetails from a dict
quote_execution_with_requote_request_details_from_dict = QuoteExecutionWithRequoteRequestDetails.from_dict(quote_execution_with_requote_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


