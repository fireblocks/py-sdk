# OfferResponseOnboarding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Which offer domain this response belongs to. Selects the shape of &#x60;response&#x60;. | 
**response** | [**OnboardingResponse**](OnboardingResponse.md) |  | 

## Example

```python
from fireblocks.models.offer_response_onboarding import OfferResponseOnboarding

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseOnboarding from a JSON string
offer_response_onboarding_instance = OfferResponseOnboarding.from_json(json)
# print the JSON string representation of the object
print(OfferResponseOnboarding.to_json())

# convert the object into a dict
offer_response_onboarding_dict = offer_response_onboarding_instance.to_dict()
# create an instance of OfferResponseOnboarding from a dict
offer_response_onboarding_from_dict = OfferResponseOnboarding.from_dict(offer_response_onboarding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


