# TravelRuleLegalPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**TravelRuleLegalPersonNameIdentifier**](TravelRuleLegalPersonNameIdentifier.md) |  | [optional] 
**geographic_address** | [**List[TravelRuleGeographicAddress]**](TravelRuleGeographicAddress.md) |  | [optional] 
**national_identification** | [**List[TravelRuleNationalIdentification]**](TravelRuleNationalIdentification.md) |  | [optional] 
**customer_identification** | **str** |  | [optional] 
**customer_number** | **str** |  | [optional] 
**country_of_registration** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_legal_person import TravelRuleLegalPerson

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleLegalPerson from a JSON string
travel_rule_legal_person_instance = TravelRuleLegalPerson.from_json(json)
# print the JSON string representation of the object
print(TravelRuleLegalPerson.to_json())

# convert the object into a dict
travel_rule_legal_person_dict = travel_rule_legal_person_instance.to_dict()
# create an instance of TravelRuleLegalPerson from a dict
travel_rule_legal_person_from_dict = TravelRuleLegalPerson.from_dict(travel_rule_legal_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


