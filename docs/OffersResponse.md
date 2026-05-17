# OffersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**List[Offer]**](Offer.md) | List of offers returned for the requested asset pair. | 
**errors** | [**List[ScopeItemFailure]**](ScopeItemFailure.md) | Partial failures encountered while requesting offers. Empty when all offer requests succeed. | 

## Example

```python
from fireblocks.models.offers_response import OffersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OffersResponse from a JSON string
offers_response_instance = OffersResponse.from_json(json)
# print the JSON string representation of the object
print(OffersResponse.to_json())

# convert the object into a dict
offers_response_dict = offers_response_instance.to_dict()
# create an instance of OffersResponse from a dict
offers_response_from_dict = OffersResponse.from_dict(offers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


