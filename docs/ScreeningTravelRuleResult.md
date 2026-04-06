# ScreeningTravelRuleResult

Deprecated: This field is not currently returned in the API response. Detailed Travel Rule screening result containing provider-specific data. Contains Travel Rule specific information like verified status, rule type, and actions. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**TravelRuleDirectionEnum**](TravelRuleDirectionEnum.md) |  | [optional] 
**is_verified** | **bool** | Whether the travel rule information was verified | [optional] 
**action** | [**TravelRuleVerdictEnum**](TravelRuleVerdictEnum.md) |  | [optional] 
**provider_response** | **Dict[str, object]** | Complete response from the travel rule provider. This is a dynamic object that varies significantly between different travel rule providers (NOTABENE etc.). Each provider has their own proprietary response format and schema.  Examples of provider-specific structures: - NOTABENE: Contains VASP information, PII data, protocol-specific fields  The structure is provider-dependent and cannot be standardized as each vendor implements their own proprietary data models and response formats.  | [optional] 
**matched_rule** | [**ScreeningTravelRuleMatchedRule**](ScreeningTravelRuleMatchedRule.md) |  | [optional] 

## Example

```python
from fireblocks.models.screening_travel_rule_result import ScreeningTravelRuleResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningTravelRuleResult from a JSON string
screening_travel_rule_result_instance = ScreeningTravelRuleResult.from_json(json)
# print the JSON string representation of the object
print(ScreeningTravelRuleResult.to_json())

# convert the object into a dict
screening_travel_rule_result_dict = screening_travel_rule_result_instance.to_dict()
# create an instance of ScreeningTravelRuleResult from a dict
screening_travel_rule_result_from_dict = ScreeningTravelRuleResult.from_dict(screening_travel_rule_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


