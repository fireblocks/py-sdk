# TravelRuleGetAllVASPsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TravelRuleVASP]**](TravelRuleVASP.md) | An array of VASP objects, referencing the TravelRuleVASP schema. | 
**total** | **int** | The total number of VASPs. | [optional] 
**next** | **str** | The URL for the next page of results. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_get_all_vasps_response import TravelRuleGetAllVASPsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleGetAllVASPsResponse from a JSON string
travel_rule_get_all_vasps_response_instance = TravelRuleGetAllVASPsResponse.from_json(json)
# print the JSON string representation of the object
print(TravelRuleGetAllVASPsResponse.to_json())

# convert the object into a dict
travel_rule_get_all_vasps_response_dict = travel_rule_get_all_vasps_response_instance.to_dict()
# create an instance of TravelRuleGetAllVASPsResponse from a dict
travel_rule_get_all_vasps_response_from_dict = TravelRuleGetAllVASPsResponse.from_dict(travel_rule_get_all_vasps_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


