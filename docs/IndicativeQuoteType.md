# IndicativeQuoteType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Indicates this is an indicative quote | 

## Example

```python
from fireblocks.models.indicative_quote_type import IndicativeQuoteType

# TODO update the JSON string below
json = "{}"
# create an instance of IndicativeQuoteType from a JSON string
indicative_quote_type_instance = IndicativeQuoteType.from_json(json)
# print the JSON string representation of the object
print(IndicativeQuoteType.to_json())

# convert the object into a dict
indicative_quote_type_dict = indicative_quote_type_instance.to_dict()
# create an instance of IndicativeQuoteType from a dict
indicative_quote_type_from_dict = IndicativeQuoteType.from_dict(indicative_quote_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


