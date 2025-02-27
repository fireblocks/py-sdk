# TravelRuleLegalPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**TravelRuleLegalPersonNameIdentifier**](TravelRuleLegalPersonNameIdentifier.md) |  | [optional] 
**geographic_address** | [**List[TravelRuleGeographicAddress]**](TravelRuleGeographicAddress.md) | The array of geographic addresses associated with the legal person. | [optional] 
**national_identification** | [**TravelRuleNationalIdentification**](TravelRuleNationalIdentification.md) |  | [optional] 
**customer_identification** | **str** | A unique identifier that identifies the customer in the organization&#39;s context. The value must be encrypted. | [optional] 
**customer_number** | **str** | A distinct identifier that uniquely identifies the customer within the organization. The value must be encrypted. | [optional] 
**country_of_registration** | **str** | The ISO-3166 Alpha-2 country code where the legal person is registered. The value must be encrypted. | [optional] 

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


