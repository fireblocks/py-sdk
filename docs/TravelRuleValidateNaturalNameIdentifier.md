# TravelRuleValidateNaturalNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_identifier** | **str** | The primary identifier of the name | [optional] 
**secondary_identifier** | **str** | The secondary identifier of the name | [optional] 
**name_identifier_type** | **str** | Specifies the type of name for a natural person. Acceptable values are: - &#39;ALIA&#39;: Alias name, a name other than the legal name by which a natural person is also known. - &#39;BIRT&#39;: Name at birth, the name given to a natural person at birth. - &#39;MAID&#39;: Maiden name, the original name of a natural person who has changed their name after marriage. - &#39;LEGL&#39;: Legal name, the name that identifies a natural person for legal, official, or administrative purposes. - &#39;MISC&#39;: Unspecified, a name by which a natural person may be known but cannot otherwise be categorized. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_natural_name_identifier import TravelRuleValidateNaturalNameIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateNaturalNameIdentifier from a JSON string
travel_rule_validate_natural_name_identifier_instance = TravelRuleValidateNaturalNameIdentifier.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateNaturalNameIdentifier.to_json())

# convert the object into a dict
travel_rule_validate_natural_name_identifier_dict = travel_rule_validate_natural_name_identifier_instance.to_dict()
# create an instance of TravelRuleValidateNaturalNameIdentifier from a dict
travel_rule_validate_natural_name_identifier_from_dict = TravelRuleValidateNaturalNameIdentifier.from_dict(travel_rule_validate_natural_name_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


