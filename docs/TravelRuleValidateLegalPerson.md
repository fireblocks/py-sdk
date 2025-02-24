# TravelRuleValidateLegalPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**TravelRuleValidateLegalPersonNameIdentifier**](TravelRuleValidateLegalPersonNameIdentifier.md) |  | [optional] 
**geographic_address** | [**List[TravelRuleValidateGeographicAddress]**](TravelRuleValidateGeographicAddress.md) | The array of geographic addresses associated with the legal person. | [optional] 
**national_identification** | [**TravelRuleValidateNationalIdentification**](TravelRuleValidateNationalIdentification.md) |  | [optional] 
**customer_identification** | **str** | A unique identifier that identifies the customer in the organization&#39;s context. | [optional] 
**customer_number** | **str** | A distinct identifier that uniquely identifies the customer within the organization. | [optional] 
**country_of_registration** | **str** | The ISO-3166 Alpha-2 country code where the legal person is registered. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_legal_person import TravelRuleValidateLegalPerson

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateLegalPerson from a JSON string
travel_rule_validate_legal_person_instance = TravelRuleValidateLegalPerson.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateLegalPerson.to_json())

# convert the object into a dict
travel_rule_validate_legal_person_dict = travel_rule_validate_legal_person_instance.to_dict()
# create an instance of TravelRuleValidateLegalPerson from a dict
travel_rule_validate_legal_person_from_dict = TravelRuleValidateLegalPerson.from_dict(travel_rule_validate_legal_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


