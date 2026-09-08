# OfferResponseAccepted

The outgoing transaction that carries the response. Its on-chain outcome arrives by webhook as a status update on this transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The outgoing response transaction. | 
**status** | **str** | The transaction&#39;s status at the time of this response — &#x60;SUBMITTED&#x60;. | 
**response_type** | **str** | The response type you sent, echoed back so you can correlate without re-reading. | 

## Example

```python
from fireblocks.models.offer_response_accepted import OfferResponseAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseAccepted from a JSON string
offer_response_accepted_instance = OfferResponseAccepted.from_json(json)
# print the JSON string representation of the object
print(OfferResponseAccepted.to_json())

# convert the object into a dict
offer_response_accepted_dict = offer_response_accepted_instance.to_dict()
# create an instance of OfferResponseAccepted from a dict
offer_response_accepted_from_dict = OfferResponseAccepted.from_dict(offer_response_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


