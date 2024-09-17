# TravelRuleNationalIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_of_issue** | **str** |  | [optional] 
**national_identifier** | **str** |  | [optional] 
**national_identifier_type** | **str** |  | [optional] 
**registration_authority** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_national_identification import TravelRuleNationalIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleNationalIdentification from a JSON string
travel_rule_national_identification_instance = TravelRuleNationalIdentification.from_json(json)
# print the JSON string representation of the object
print(TravelRuleNationalIdentification.to_json())

# convert the object into a dict
travel_rule_national_identification_dict = travel_rule_national_identification_instance.to_dict()
# create an instance of TravelRuleNationalIdentification from a dict
travel_rule_national_identification_from_dict = TravelRuleNationalIdentification.from_dict(travel_rule_national_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


