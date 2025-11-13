# ScreeningAmlMatchedRule

AML matched rule information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Identifier of the matched rule | [optional] 
**rule_name** | **str** | Name of the matched rule | [optional] 
**action** | [**PolicyVerdictActionEnum2**](PolicyVerdictActionEnum2.md) |  | [optional] 

## Example

```python
from fireblocks.models.screening_aml_matched_rule import ScreeningAmlMatchedRule

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningAmlMatchedRule from a JSON string
screening_aml_matched_rule_instance = ScreeningAmlMatchedRule.from_json(json)
# print the JSON string representation of the object
print(ScreeningAmlMatchedRule.to_json())

# convert the object into a dict
screening_aml_matched_rule_dict = screening_aml_matched_rule_instance.to_dict()
# create an instance of ScreeningAmlMatchedRule from a dict
screening_aml_matched_rule_from_dict = ScreeningAmlMatchedRule.from_dict(screening_aml_matched_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


