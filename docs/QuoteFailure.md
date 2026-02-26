# QuoteFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Identifier of the provider for which the quote request failed. | 
**account_id** | **str** | Identifier of the account for which the quote request failed (optional). | [optional] 
**error** | [**TradingErrorSchema**](TradingErrorSchema.md) |  | 

## Example

```python
from fireblocks.models.quote_failure import QuoteFailure

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteFailure from a JSON string
quote_failure_instance = QuoteFailure.from_json(json)
# print the JSON string representation of the object
print(QuoteFailure.to_json())

# convert the object into a dict
quote_failure_dict = quote_failure_instance.to_dict()
# create an instance of QuoteFailure from a dict
quote_failure_from_dict = QuoteFailure.from_dict(quote_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


