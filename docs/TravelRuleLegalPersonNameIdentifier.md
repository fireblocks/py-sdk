# TravelRuleLegalPersonNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_person_name** | **str** | Name by which the legal person is known. The value must be encrypted. | [optional] 
**legal_person_name_identifier_type** | **str** | Specifies the type of name for a legal person. Acceptable values are: - &#39;REGISTERED&#39;: The official registered name. - &#39;TRADE&#39;: A trading name or DBA (Doing Business As) name. - &#39;OTHER&#39;: Any other type of name. The value must be encrypted. | [optional] 

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


