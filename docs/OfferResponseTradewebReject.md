# OfferResponseTradewebReject

Reject a Tradeweb co-signing delegation offer. Carries no arguments — Tradeweb does not record a reject reason on the ledger, so none is accepted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer — one of the offer transaction&#39;s &#x60;cantonDetails.offerResponse.availableResponses&#x60;. That list does not change after the offer arrives; check &#x60;expiresAt&#x60; and the transaction status to see whether it is still answerable. | 

## Example

```python
from fireblocks.models.offer_response_tradeweb_reject import OfferResponseTradewebReject

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseTradewebReject from a JSON string
offer_response_tradeweb_reject_instance = OfferResponseTradewebReject.from_json(json)
# print the JSON string representation of the object
print(OfferResponseTradewebReject.to_json())

# convert the object into a dict
offer_response_tradeweb_reject_dict = offer_response_tradeweb_reject_instance.to_dict()
# create an instance of OfferResponseTradewebReject from a dict
offer_response_tradeweb_reject_from_dict = OfferResponseTradewebReject.from_dict(offer_response_tradeweb_reject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


