# TravelRuleValidateLegalNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_person_name** | **str** | Name by which the legal person is known. | 
**legal_person_name_identifier_type** | **str** | Specifies the type of name for a legal person (IVMS101 LegalPersonNameTypeCode). Acceptable values are: - &#39;LEGL&#39;: Legal name - official name under which the organisation is registered. - &#39;SHRT&#39;: Short name of the organisation. - &#39;TRAD&#39;: Trading name - name used by the business for commercial purposes. | 

## Example

```python
from fireblocks.models.travel_rule_validate_legal_name_identifier import TravelRuleValidateLegalNameIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateLegalNameIdentifier from a JSON string
travel_rule_validate_legal_name_identifier_instance = TravelRuleValidateLegalNameIdentifier.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateLegalNameIdentifier.to_json())

# convert the object into a dict
travel_rule_validate_legal_name_identifier_dict = travel_rule_validate_legal_name_identifier_instance.to_dict()
# create an instance of TravelRuleValidateLegalNameIdentifier from a dict
travel_rule_validate_legal_name_identifier_from_dict = TravelRuleValidateLegalNameIdentifier.from_dict(travel_rule_validate_legal_name_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


