# CantonCallEndInvestorInviteCancel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**payload** | [**EndInvestorPayload**](EndInvestorPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call_end_investor_invite_cancel import CantonCallEndInvestorInviteCancel

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallEndInvestorInviteCancel from a JSON string
canton_call_end_investor_invite_cancel_instance = CantonCallEndInvestorInviteCancel.from_json(json)
# print the JSON string representation of the object
print(CantonCallEndInvestorInviteCancel.to_json())

# convert the object into a dict
canton_call_end_investor_invite_cancel_dict = canton_call_end_investor_invite_cancel_instance.to_dict()
# create an instance of CantonCallEndInvestorInviteCancel from a dict
canton_call_end_investor_invite_cancel_from_dict = CantonCallEndInvestorInviteCancel.from_dict(canton_call_end_investor_invite_cancel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


