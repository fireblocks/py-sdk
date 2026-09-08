# OfferResponseTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Which offer domain this response belongs to. Selects the shape of &#x60;response&#x60;. | 
**response** | [**TransferResponse**](TransferResponse.md) |  | 

## Example

```python
from fireblocks.models.offer_response_transfer import OfferResponseTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseTransfer from a JSON string
offer_response_transfer_instance = OfferResponseTransfer.from_json(json)
# print the JSON string representation of the object
print(OfferResponseTransfer.to_json())

# convert the object into a dict
offer_response_transfer_dict = offer_response_transfer_instance.to_dict()
# create an instance of OfferResponseTransfer from a dict
offer_response_transfer_from_dict = OfferResponseTransfer.from_dict(offer_response_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


