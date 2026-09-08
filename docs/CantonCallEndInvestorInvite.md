# CantonCallEndInvestorInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**payload** | [**EndInvestorPayload**](EndInvestorPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call_end_investor_invite import CantonCallEndInvestorInvite

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallEndInvestorInvite from a JSON string
canton_call_end_investor_invite_instance = CantonCallEndInvestorInvite.from_json(json)
# print the JSON string representation of the object
print(CantonCallEndInvestorInvite.to_json())

# convert the object into a dict
canton_call_end_investor_invite_dict = canton_call_end_investor_invite_instance.to_dict()
# create an instance of CantonCallEndInvestorInvite from a dict
canton_call_end_investor_invite_from_dict = CantonCallEndInvestorInvite.from_dict(canton_call_end_investor_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


