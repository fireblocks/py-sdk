# ReQuoteDetailsReQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**RetryRequoteTypeEnum**](RetryRequoteTypeEnum.md) |  | 
**count** | **int** | If quote is expired, how many times to re-generate new quotes to try having the order executed as in the original quote. | 
**slippage_bps** | **int** | Slippage tolerance in basis points (bps) for quote orders - 1 is 0.01% and 10000 is 100% | [optional] 

## Example

```python
from fireblocks.models.re_quote_details_re_quote import ReQuoteDetailsReQuote

# TODO update the JSON string below
json = "{}"
# create an instance of ReQuoteDetailsReQuote from a JSON string
re_quote_details_re_quote_instance = ReQuoteDetailsReQuote.from_json(json)
# print the JSON string representation of the object
print(ReQuoteDetailsReQuote.to_json())

# convert the object into a dict
re_quote_details_re_quote_dict = re_quote_details_re_quote_instance.to_dict()
# create an instance of ReQuoteDetailsReQuote from a dict
re_quote_details_re_quote_from_dict = ReQuoteDetailsReQuote.from_dict(re_quote_details_re_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


