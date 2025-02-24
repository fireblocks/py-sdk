# TravelRuleValidateNaturalPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**List[TravelRuleValidateNaturalPersonNameIdentifier]**](TravelRuleValidateNaturalPersonNameIdentifier.md) | An array of structured name identifiers for the natural person, referencing the TravelRuleNaturalPersonNameIdentifier schema. | [optional] 
**geographic_address** | [**List[TravelRuleValidateGeographicAddress]**](TravelRuleValidateGeographicAddress.md) | An array of geographic addresses associated with the natural person, referencing the TravelRuleGeographicAddress schema. | [optional] 
**national_identification** | [**TravelRuleValidateNationalIdentification**](TravelRuleValidateNationalIdentification.md) |  | [optional] 
**date_and_place_of_birth** | [**TravelRuleValidateDateAndPlaceOfBirth**](TravelRuleValidateDateAndPlaceOfBirth.md) |  | [optional] 
**customer_identification** | **str** | A unique identifier for the customer within the organization&#39;s context. | [optional] 
**country_of_residence** | **str** | The ISO-3166 Alpha-2 country code of the natural person&#39;s residence. | [optional] 
**customer_number** | **str** | A distinct identifier that uniquely identifies the customer within the organization. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_natural_person import TravelRuleValidateNaturalPerson

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateNaturalPerson from a JSON string
travel_rule_validate_natural_person_instance = TravelRuleValidateNaturalPerson.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateNaturalPerson.to_json())

# convert the object into a dict
travel_rule_validate_natural_person_dict = travel_rule_validate_natural_person_instance.to_dict()
# create an instance of TravelRuleValidateNaturalPerson from a dict
travel_rule_validate_natural_person_from_dict = TravelRuleValidateNaturalPerson.from_dict(travel_rule_validate_natural_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


