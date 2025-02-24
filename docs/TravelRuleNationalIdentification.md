# TravelRuleNationalIdentification

Represents a national identifier for a person or entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_of_issue** | **str** | Country that issued the national identifier (ISO-3166 Alpha-2 country code). The value must be encrypted. | [optional] 
**national_identifier** | **str** | National identifier (max 35 characters). The value must be encrypted. | [optional] 
**national_identifier_type** | **str** | Type of national identifier. Acceptable values include: - &#39;PASSPORT&#39;: Passport number - &#39;NATIONAL_ID&#39;: National identification number - &#39;TAX_ID&#39;: Tax identification number - &#39;SOCIAL_SECURITY&#39;: Social security number The value must be encrypted. | [optional] 
**registration_authority** | **str** | Registration authority (format -&gt; RA followed by 6 digits). The value must be encrypted. | [optional] 

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


