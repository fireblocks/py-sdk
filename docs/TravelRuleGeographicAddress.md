# TravelRuleGeographicAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** |  | [optional] 
**town_name** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**building_number** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**address_type** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**sub_department** | **str** |  | [optional] 
**building_name** | **str** |  | [optional] 
**floor** | **str** |  | [optional] 
**post_box** | **str** |  | [optional] 
**room** | **str** |  | [optional] 
**town_location_name** | **str** |  | [optional] 
**district_name** | **str** |  | [optional] 
**country_sub_division** | **str** |  | [optional] 
**address_line** | **List[str]** |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_geographic_address import TravelRuleGeographicAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleGeographicAddress from a JSON string
travel_rule_geographic_address_instance = TravelRuleGeographicAddress.from_json(json)
# print the JSON string representation of the object
print(TravelRuleGeographicAddress.to_json())

# convert the object into a dict
travel_rule_geographic_address_dict = travel_rule_geographic_address_instance.to_dict()
# create an instance of TravelRuleGeographicAddress from a dict
travel_rule_geographic_address_from_dict = TravelRuleGeographicAddress.from_dict(travel_rule_geographic_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


