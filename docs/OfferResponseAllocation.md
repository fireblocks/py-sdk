# OfferResponseAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Which offer domain this response belongs to. Selects the shape of &#x60;response&#x60;. | 
**response** | [**AllocationResponse**](AllocationResponse.md) |  | 

## Example

```python
from fireblocks.models.offer_response_allocation import OfferResponseAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of OfferResponseAllocation from a JSON string
offer_response_allocation_instance = OfferResponseAllocation.from_json(json)
# print the JSON string representation of the object
print(OfferResponseAllocation.to_json())

# convert the object into a dict
offer_response_allocation_dict = offer_response_allocation_instance.to_dict()
# create an instance of OfferResponseAllocation from a dict
offer_response_allocation_from_dict = OfferResponseAllocation.from_dict(offer_response_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


