# TRLinkAssessTravelRuleResponse

Response indicating whether Travel Rule compliance is required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | [**TRLinkAssessmentDecision**](TRLinkAssessmentDecision.md) |  | 
**reason** | **str** | Explanation of the decision | 
**required_fields** | **List[str]** | List of required fields if Travel Rule is required | [optional] 
**missing_info** | **List[str]** | List of missing fields if more information is needed | [optional] 
**thresholds** | [**TRLinkThresholds**](TRLinkThresholds.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_assess_travel_rule_response import TRLinkAssessTravelRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAssessTravelRuleResponse from a JSON string
tr_link_assess_travel_rule_response_instance = TRLinkAssessTravelRuleResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkAssessTravelRuleResponse.to_json())

# convert the object into a dict
tr_link_assess_travel_rule_response_dict = tr_link_assess_travel_rule_response_instance.to_dict()
# create an instance of TRLinkAssessTravelRuleResponse from a dict
tr_link_assess_travel_rule_response_from_dict = TRLinkAssessTravelRuleResponse.from_dict(tr_link_assess_travel_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


