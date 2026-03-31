# TravelRuleResult

Deprecated: This field is not currently returned in the API response. Detailed Travel Rule screening result containing provider-specific data. Contains Travel Rule specific information like verified status, rule type, and actions. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**TravelRuleDirectionEnum**](TravelRuleDirectionEnum.md) |  | [optional] 
**is_verified** | **bool** | Whether the travel rule information was verified | [optional] 
**action** | [**TravelRuleVerdictEnum**](TravelRuleVerdictEnum.md) |  | [optional] 
**provider_response** | **Dict[str, object]** | Complete response from the travel rule provider. This is a dynamic object that varies significantly between different travel rule providers (NOTABENE etc.). Each provider has their own proprietary response format and schema.  Examples of provider-specific structures: - NOTABENE: Contains VASP information, PII data, protocol-specific fields  The structure is provider-dependent and cannot be standardized as each vendor implements their own proprietary data models and response formats.  | [optional] 
**matched_rule** | [**TravelRuleMatchedRule**](TravelRuleMatchedRule.md) |  | [optional] 

## Example

```python
from fireblocks.models.travel_rule_result import TravelRuleResult

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleResult from a JSON string
travel_rule_result_instance = TravelRuleResult.from_json(json)
# print the JSON string representation of the object
print(TravelRuleResult.to_json())

# convert the object into a dict
travel_rule_result_dict = travel_rule_result_instance.to_dict()
# create an instance of TravelRuleResult from a dict
travel_rule_result_from_dict = TravelRuleResult.from_dict(travel_rule_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


