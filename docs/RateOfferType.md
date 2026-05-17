# RateOfferType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_type** | **str** | The type of offer — RATE for indicative pricing. | 

## Example

```python
from fireblocks.models.rate_offer_type import RateOfferType

# TODO update the JSON string below
json = "{}"
# create an instance of RateOfferType from a JSON string
rate_offer_type_instance = RateOfferType.from_json(json)
# print the JSON string representation of the object
print(RateOfferType.to_json())

# convert the object into a dict
rate_offer_type_dict = rate_offer_type_instance.to_dict()
# create an instance of RateOfferType from a dict
rate_offer_type_from_dict = RateOfferType.from_dict(rate_offer_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


