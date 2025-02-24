# TravelRuleValidateLegalPersonNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_person_name** | **str** | Name by which the legal person is known. | [optional] 
**legal_person_name_identifier_type** | **str** | Specifies the type of name for a legal person. Acceptable values are: - &#39;REGISTERED&#39;: The official registered name. - &#39;TRADE&#39;: A trading name or DBA (Doing Business As) name. - &#39;OTHER&#39;: Any other type of name. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_legal_person_name_identifier import TravelRuleValidateLegalPersonNameIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateLegalPersonNameIdentifier from a JSON string
travel_rule_validate_legal_person_name_identifier_instance = TravelRuleValidateLegalPersonNameIdentifier.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateLegalPersonNameIdentifier.to_json())

# convert the object into a dict
travel_rule_validate_legal_person_name_identifier_dict = travel_rule_validate_legal_person_name_identifier_instance.to_dict()
# create an instance of TravelRuleValidateLegalPersonNameIdentifier from a dict
travel_rule_validate_legal_person_name_identifier_from_dict = TravelRuleValidateLegalPersonNameIdentifier.from_dict(travel_rule_validate_legal_person_name_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


