# OfferResponseTransferWithdraw

Withdraw your own OUTGOING transfer offer. Carries no arguments — `offerId` in the path is the offer, so the vault account and blockchain are resolved from it rather than restated. Was `CantonCallType.TRANSFER_WITHDRAW` with a 3-field payload until FA-10624.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | How you are answering the offer. Must be one of the values listed in the transaction&#39;s &#x60;cantonDetails.offerResponse.availableResponses&#x60; — TOP-LEVEL on the transaction, not nested under an &#x60;additionalInfo&#x60; envelope, which does not exist on &#x60;TransactionResponse&#x60;. &#x60;availableResponses&#x60; states what this offer TYPE accepts. It is set when the offer arrives and does not change, so it does NOT tell you whether the offer is still answerable — check &#x60;expiresAt&#x60; and the transaction&#39;s status for that, and expect this endpoint to be the authority: it re-checks state and expiry on every call and answers 409 when either has moved. | 

## Example

```python
from fireblocks.models.offer_response_transfer_withdraw import OfferResponseTransferWithdraw

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseTransferWithdraw from a JSON string
offer_response_transfer_withdraw_instance = OfferResponseTransferWithdraw.from_json(json)
# print the JSON string representation of the object
print(OfferResponseTransferWithdraw.to_json())

# convert the object into a dict
offer_response_transfer_withdraw_dict = offer_response_transfer_withdraw_instance.to_dict()
# create an instance of OfferResponseTransferWithdraw from a dict
offer_response_transfer_withdraw_from_dict = OfferResponseTransferWithdraw.from_dict(offer_response_transfer_withdraw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


