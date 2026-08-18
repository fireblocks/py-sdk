# TravelRuleLegalNameIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_person_name** | **str** | Name by which the legal person is known. The value must be encrypted. | 
**legal_person_name_identifier_type** | **str** | Specifies the type of name for a legal person (IVMS101 LegalPersonNameTypeCode). Acceptable values are: - &#39;LEGL&#39;: Legal name - official name under which the organisation is registered. - &#39;SHRT&#39;: Short name of the organisation. - &#39;TRAD&#39;: Trading name - name used by the business for commercial purposes. The value must be encrypted. | 

## Example

```python
from fireblocks.models.travel_rule_legal_name_identifier import TravelRuleLegalNameIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleLegalNameIdentifier from a JSON string
travel_rule_legal_name_identifier_instance = TravelRuleLegalNameIdentifier.from_json(json)
# print the JSON string representation of the object
print(TravelRuleLegalNameIdentifier.to_json())

# convert the object into a dict
travel_rule_legal_name_identifier_dict = travel_rule_legal_name_identifier_instance.to_dict()
# create an instance of TravelRuleLegalNameIdentifier from a dict
travel_rule_legal_name_identifier_from_dict = TravelRuleLegalNameIdentifier.from_dict(travel_rule_legal_name_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


