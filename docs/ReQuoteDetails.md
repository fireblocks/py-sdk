# ReQuoteDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**re_quote** | [**ReQuoteDetailsReQuote**](ReQuoteDetailsReQuote.md) |  | [optional] 

## Example

```python
from fireblocks.models.re_quote_details import ReQuoteDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReQuoteDetails from a JSON string
re_quote_details_instance = ReQuoteDetails.from_json(json)
# print the JSON string representation of the object
print(ReQuoteDetails.to_json())

# convert the object into a dict
re_quote_details_dict = re_quote_details_instance.to_dict()
# create an instance of ReQuoteDetails from a dict
re_quote_details_from_dict = ReQuoteDetails.from_dict(re_quote_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


