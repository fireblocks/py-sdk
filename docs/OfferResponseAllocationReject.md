# OfferResponseAllocationReject

Reject a CIP-56 allocation request. Carries no arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer. Must be one of the values listed in the transaction&#39;s &#x60;cantonDetails.offerResponse.availableResponses&#x60; — TOP-LEVEL on the transaction, not nested under an &#x60;additionalInfo&#x60; envelope, which does not exist on &#x60;TransactionResponse&#x60;. &#x60;availableResponses&#x60; states what this offer TYPE accepts. It is set when the offer arrives and does not change, so it does NOT tell you whether the offer is still answerable — check &#x60;expiresAt&#x60; and the transaction&#39;s status for that, and expect this endpoint to be the authority: it re-checks state and expiry on every call and answers 409 when either has moved. | 

## Example

```python
from fireblocks.models.offer_response_allocation_reject import OfferResponseAllocationReject

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseAllocationReject from a JSON string
offer_response_allocation_reject_instance = OfferResponseAllocationReject.from_json(json)
# print the JSON string representation of the object
print(OfferResponseAllocationReject.to_json())

# convert the object into a dict
offer_response_allocation_reject_dict = offer_response_allocation_reject_instance.to_dict()
# create an instance of OfferResponseAllocationReject from a dict
offer_response_allocation_reject_from_dict = OfferResponseAllocationReject.from_dict(offer_response_allocation_reject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


