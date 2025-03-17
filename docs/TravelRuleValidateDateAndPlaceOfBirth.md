# TravelRuleValidateDateAndPlaceOfBirth

Represents the date and place of birth for a natural person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_birth** | **str** | Date of birth in ISO 8601 format (YYYY-MM-DD) | [optional] 
**place_of_birth** | **str** | Place of birth | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_date_and_place_of_birth import TravelRuleValidateDateAndPlaceOfBirth

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateDateAndPlaceOfBirth from a JSON string
travel_rule_validate_date_and_place_of_birth_instance = TravelRuleValidateDateAndPlaceOfBirth.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateDateAndPlaceOfBirth.to_json())

# convert the object into a dict
travel_rule_validate_date_and_place_of_birth_dict = travel_rule_validate_date_and_place_of_birth_instance.to_dict()
# create an instance of TravelRuleValidateDateAndPlaceOfBirth from a dict
travel_rule_validate_date_and_place_of_birth_from_dict = TravelRuleValidateDateAndPlaceOfBirth.from_dict(travel_rule_validate_date_and_place_of_birth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


