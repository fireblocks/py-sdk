# OfferResponseAllocationWithdraw

Withdraw the allocation you made by accepting this offer, unlocking the holding. Carries no arguments — the allocation is resolved from the offer. Answers `409` until the accept has settled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer — one of the offer transaction&#39;s &#x60;cantonDetails.offerResponse.availableResponses&#x60;. That list does not change after the offer arrives; check &#x60;expiresAt&#x60; and the transaction status to see whether it is still answerable. | 

## Example

```python
from fireblocks.models.offer_response_allocation_withdraw import OfferResponseAllocationWithdraw

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseAllocationWithdraw from a JSON string
offer_response_allocation_withdraw_instance = OfferResponseAllocationWithdraw.from_json(json)
# print the JSON string representation of the object
print(OfferResponseAllocationWithdraw.to_json())

# convert the object into a dict
offer_response_allocation_withdraw_dict = offer_response_allocation_withdraw_instance.to_dict()
# create an instance of OfferResponseAllocationWithdraw from a dict
offer_response_allocation_withdraw_from_dict = OfferResponseAllocationWithdraw.from_dict(offer_response_allocation_withdraw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


