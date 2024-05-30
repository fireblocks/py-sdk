# RedeemFundsToLinkedDDAResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether the funds were successfully redeemed to the linked DDA | 

## Example

```python
from fireblocks.models.redeem_funds_to_linked_dda_response import RedeemFundsToLinkedDDAResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemFundsToLinkedDDAResponse from a JSON string
redeem_funds_to_linked_dda_response_instance = RedeemFundsToLinkedDDAResponse.from_json(json)
# print the JSON string representation of the object
print(RedeemFundsToLinkedDDAResponse.to_json())

# convert the object into a dict
redeem_funds_to_linked_dda_response_dict = redeem_funds_to_linked_dda_response_instance.to_dict()
# create an instance of RedeemFundsToLinkedDDAResponse from a dict
redeem_funds_to_linked_dda_response_from_dict = RedeemFundsToLinkedDDAResponse.from_dict(redeem_funds_to_linked_dda_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


