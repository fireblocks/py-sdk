# AmlMatchedRule

AML matched rule information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **str** | Identifier of the matched rule | [optional] 
**rule_name** | **str** | Name of the matched rule | [optional] 
**action** | [**PolicyVerdictActionEnum**](PolicyVerdictActionEnum.md) |  | [optional] 

## Example

```python
from fireblocks.models.aml_matched_rule import AmlMatchedRule

# TODO update the JSON string below
json = "{}"
# create an instance of AmlMatchedRule from a JSON string
aml_matched_rule_instance = AmlMatchedRule.from_json(json)
# print the JSON string representation of the object
print(AmlMatchedRule.to_json())

# convert the object into a dict
aml_matched_rule_dict = aml_matched_rule_instance.to_dict()
# create an instance of AmlMatchedRule from a dict
aml_matched_rule_from_dict = AmlMatchedRule.from_dict(aml_matched_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


