# TravelRuleValidateNationalIdentification

Represents a national identifier for a person or entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_of_issue** | **str** | Country that issued the national identifier (ISO-3166 Alpha-2 country code) | [optional] 
**national_identifier** | **str** | National identifier (max 35 characters) | [optional] 
**national_identifier_type** | **str** | Type of national identifier. Acceptable values include: - &#39;PASSPORT&#39;: Passport number - &#39;NATIONAL_ID&#39;: National identification number - &#39;TAX_ID&#39;: Tax identification number - &#39;SOCIAL_SECURITY&#39;: Social security number | [optional] 
**registration_authority** | **str** | Registration authority (format -&gt; RA followed by 6 digits) | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_national_identification import TravelRuleValidateNationalIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateNationalIdentification from a JSON string
travel_rule_validate_national_identification_instance = TravelRuleValidateNationalIdentification.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateNationalIdentification.to_json())

# convert the object into a dict
travel_rule_validate_national_identification_dict = travel_rule_validate_national_identification_instance.to_dict()
# create an instance of TravelRuleValidateNationalIdentification from a dict
travel_rule_validate_national_identification_from_dict = TravelRuleValidateNationalIdentification.from_dict(travel_rule_validate_national_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


