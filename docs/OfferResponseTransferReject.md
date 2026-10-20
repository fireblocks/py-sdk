# OfferResponseTransferReject

Reject an inbound 2-step transfer offer. Carries no arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer — one of the offer transaction&#39;s &#x60;cantonDetails.offerResponse.availableResponses&#x60;. That list does not change after the offer arrives; check &#x60;expiresAt&#x60; and the transaction status to see whether it is still answerable. | 

## Example

```python
from fireblocks.models.offer_response_transfer_reject import OfferResponseTransferReject

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseTransferReject from a JSON string
offer_response_transfer_reject_instance = OfferResponseTransferReject.from_json(json)
# print the JSON string representation of the object
print(OfferResponseTransferReject.to_json())

# convert the object into a dict
offer_response_transfer_reject_dict = offer_response_transfer_reject_instance.to_dict()
# create an instance of OfferResponseTransferReject from a dict
offer_response_transfer_reject_from_dict = OfferResponseTransferReject.from_dict(offer_response_transfer_reject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


