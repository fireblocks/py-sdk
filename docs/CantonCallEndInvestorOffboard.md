# CantonCallEndInvestorOffboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Which call to make. Selects the shape of &#x60;payload&#x60;. | 
**payload** | [**EndInvestorPayload**](EndInvestorPayload.md) |  | 

## Example

```python
from fireblocks.models.canton_call_end_investor_offboard import CantonCallEndInvestorOffboard

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallEndInvestorOffboard from a JSON string
canton_call_end_investor_offboard_instance = CantonCallEndInvestorOffboard.from_json(json)
# print the JSON string representation of the object
print(CantonCallEndInvestorOffboard.to_json())

# convert the object into a dict
canton_call_end_investor_offboard_dict = canton_call_end_investor_offboard_instance.to_dict()
# create an instance of CantonCallEndInvestorOffboard from a dict
canton_call_end_investor_offboard_from_dict = CantonCallEndInvestorOffboard.from_dict(canton_call_end_investor_offboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


