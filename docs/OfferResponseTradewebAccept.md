# OfferResponseTradewebAccept

Accept a Tradeweb co-signing delegation offer. Carries no arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer — one of the offer transaction&#39;s &#x60;cantonDetails.offerResponse.availableResponses&#x60;. That list does not change after the offer arrives; check &#x60;expiresAt&#x60; and the transaction status to see whether it is still answerable. | 

## Example

```python
from fireblocks.models.offer_response_tradeweb_accept import OfferResponseTradewebAccept

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseTradewebAccept from a JSON string
offer_response_tradeweb_accept_instance = OfferResponseTradewebAccept.from_json(json)
# print the JSON string representation of the object
print(OfferResponseTradewebAccept.to_json())

# convert the object into a dict
offer_response_tradeweb_accept_dict = offer_response_tradeweb_accept_instance.to_dict()
# create an instance of OfferResponseTradewebAccept from a dict
offer_response_tradeweb_accept_from_dict = OfferResponseTradewebAccept.from_dict(offer_response_tradeweb_accept_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


