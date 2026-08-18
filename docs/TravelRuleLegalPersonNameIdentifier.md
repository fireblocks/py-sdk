# TravelRuleLegalPersonNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_identifier** | [**List[TravelRuleLegalNameIdentifier]**](TravelRuleLegalNameIdentifier.md) | An array of name identifiers of the legal person. | [optional] 
**local_name_identifier** | [**List[TravelRuleLegalNameIdentifier]**](TravelRuleLegalNameIdentifier.md) | An array of local name identifiers of the legal person. | [optional] 
**phonetic_name_identifier** | [**List[TravelRuleLegalNameIdentifier]**](TravelRuleLegalNameIdentifier.md) | An array of phonetic name identifiers of the legal person. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_legal_person_name_identifier import TravelRuleLegalPersonNameIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleLegalPersonNameIdentifier from a JSON string
travel_rule_legal_person_name_identifier_instance = TravelRuleLegalPersonNameIdentifier.from_json(json)
# print the JSON string representation of the object
print(TravelRuleLegalPersonNameIdentifier.to_json())

# convert the object into a dict
travel_rule_legal_person_name_identifier_dict = travel_rule_legal_person_name_identifier_instance.to_dict()
# create an instance of TravelRuleLegalPersonNameIdentifier from a dict
travel_rule_legal_person_name_identifier_from_dict = TravelRuleLegalPersonNameIdentifier.from_dict(travel_rule_legal_person_name_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


