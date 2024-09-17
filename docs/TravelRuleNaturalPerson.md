# TravelRuleNaturalPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**List[TravelRuleNaturalPersonNameIdentifier]**](TravelRuleNaturalPersonNameIdentifier.md) |  | [optional] 
**geographic_address** | [**List[TravelRuleGeographicAddress]**](TravelRuleGeographicAddress.md) |  | [optional] 
**national_identification** | [**List[TravelRuleNationalIdentification]**](TravelRuleNationalIdentification.md) |  | [optional] 
**date_and_place_of_birth** | [**List[TravelRuleDateAndPlaceOfBirth]**](TravelRuleDateAndPlaceOfBirth.md) |  | [optional] 
**customer_identification** | **str** |  | [optional] 
**country_of_residence** | **str** |  | [optional] 
**customer_number** | **str** |  | [optional] 
**country_of_registration** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_natural_person import TravelRuleNaturalPerson

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleNaturalPerson from a JSON string
travel_rule_natural_person_instance = TravelRuleNaturalPerson.from_json(json)
# print the JSON string representation of the object
print(TravelRuleNaturalPerson.to_json())

# convert the object into a dict
travel_rule_natural_person_dict = travel_rule_natural_person_instance.to_dict()
# create an instance of TravelRuleNaturalPerson from a dict
travel_rule_natural_person_from_dict = TravelRuleNaturalPerson.from_dict(travel_rule_natural_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


