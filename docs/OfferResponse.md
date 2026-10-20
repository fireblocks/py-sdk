# OfferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer — one of the offer transaction&#39;s &#x60;cantonDetails.offerResponse.availableResponses&#x60;. That list does not change after the offer arrives; check &#x60;expiresAt&#x60; and the transaction status to see whether it is still answerable. | 
**payload** | [**DtccOnboardingRejectPayload**](DtccOnboardingRejectPayload.md) |  | 

## Example

```python
from fireblocks.models.offer_response import OfferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponse from a JSON string
offer_response_instance = OfferResponse.from_json(json)
# print the JSON string representation of the object
print(OfferResponse.to_json())

# convert the object into a dict
offer_response_dict = offer_response_instance.to_dict()
# create an instance of OfferResponse from a dict
offer_response_from_dict = OfferResponse.from_dict(offer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


