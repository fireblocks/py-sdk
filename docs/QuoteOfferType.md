# QuoteOfferType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_type** | **str** | The type of offer — QUOTE for executable committed quotes. | 

## Example

```python
from fireblocks.models.quote_offer_type import QuoteOfferType

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteOfferType from a JSON string
quote_offer_type_instance = QuoteOfferType.from_json(json)
# print the JSON string representation of the object
print(QuoteOfferType.to_json())

# convert the object into a dict
quote_offer_type_dict = quote_offer_type_instance.to_dict()
# create an instance of QuoteOfferType from a dict
quote_offer_type_from_dict = QuoteOfferType.from_dict(quote_offer_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


