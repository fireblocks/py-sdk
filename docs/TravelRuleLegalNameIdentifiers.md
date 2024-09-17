# TravelRuleLegalNameIdentifiers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_person_name_identifier_type** | **str** |  | [optional] 
**legal_person_name** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_legal_name_identifiers import TravelRuleLegalNameIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleLegalNameIdentifiers from a JSON string
travel_rule_legal_name_identifiers_instance = TravelRuleLegalNameIdentifiers.from_json(json)
# print the JSON string representation of the object
print(TravelRuleLegalNameIdentifiers.to_json())

# convert the object into a dict
travel_rule_legal_name_identifiers_dict = travel_rule_legal_name_identifiers_instance.to_dict()
# create an instance of TravelRuleLegalNameIdentifiers from a dict
travel_rule_legal_name_identifiers_from_dict = TravelRuleLegalNameIdentifiers.from_dict(travel_rule_legal_name_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


