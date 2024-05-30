# ScreeningVerdictMatchedRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**category** | **List[str]** |  | [optional] 

## Example

```python
from fireblocks_client.models.screening_verdict_matched_rule import ScreeningVerdictMatchedRule

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningVerdictMatchedRule from a JSON string
screening_verdict_matched_rule_instance = ScreeningVerdictMatchedRule.from_json(json)
# print the JSON string representation of the object
print(ScreeningVerdictMatchedRule.to_json())

# convert the object into a dict
screening_verdict_matched_rule_dict = screening_verdict_matched_rule_instance.to_dict()
# create an instance of ScreeningVerdictMatchedRule from a dict
screening_verdict_matched_rule_from_dict = ScreeningVerdictMatchedRule.from_dict(screening_verdict_matched_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


