# StepOperationConfig

Configuration for one operation the step's connector handles. The operation arrives on the screening request; the connector decides how to handle it.  Two rule sets govern the step, and both are configured here rather than sent per request, so the same call behaves differently across workflows. Trigger rules decide whether the connector runs at all; outcome rules turn the provider's response into the step's verdict. With neither configured the step runs under the connector's own defaults, which for `kyt_trmlabs` are permissive: the screening completes without consulting the provider.  The four parameter lists are the contract for writing those rules: a rule naming a field outside `triggerRuleParameters` or `outcomeEvaluationParameters` is rejected. They are derived from the connector registry rather than stored, so a connector gaining a field is reflected here without a migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**ScreeningOperationEnum**](ScreeningOperationEnum.md) |  | [optional] 
**required_parameters** | **List[str]** | Resolved server-side on every &#x60;GetWorkflow&#x60; call from the step&#39;s connector definition for this operation. Read-only: ignored on write. | [optional] 
**optional_parameters** | **List[str]** | Like &#x60;requiredParameters&#x60;, but optional inputs to the operation. | [optional] 
**trigger_rule_parameters** | **List[str]** | Fields a condition in &#x60;triggerRuleSetStruct&#x60; may reference. | [optional] 
**outcome_evaluation_parameters** | **List[str]** | Provider response fields a condition in &#x60;outcomeRuleSetStruct&#x60; may reference. | [optional] 
**outcome_meta_parameters** | **List[str]** | Additional provider response fields returned with the result; not usable in &#x60;outcomeRuleSetStruct&#x60; conditions. | [optional] 
**trigger_rule_set_struct** | [**RuleSet**](RuleSet.md) |  | [optional] 
**trigger_rule_set_json** | **str** | The tenant&#39;s trigger rules, as a JSON-encoded string. Set for steps whose rules are still defined as a legacy screening policy rather than natively in Compliance Orchestrator, and refreshed on every read. Mutually exclusive with &#x60;triggerRuleSetStruct&#x60;. | [optional] 
**outcome_rule_set_struct** | [**RuleSet**](RuleSet.md) |  | [optional] 
**outcome_rule_set_json** | **str** | The tenant&#39;s outcome rules, as a JSON-encoded string. Set for steps whose rules are still defined as a legacy screening policy rather than natively in Compliance Orchestrator, and refreshed on every read. Mutually exclusive with &#x60;outcomeRuleSetStruct&#x60;. | [optional] 

## Example

```python
from fireblocks.models.step_operation_config import StepOperationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StepOperationConfig from a JSON string
step_operation_config_instance = StepOperationConfig.from_json(json)
# print the JSON string representation of the object
print(StepOperationConfig.to_json())

# convert the object into a dict
step_operation_config_dict = step_operation_config_instance.to_dict()
# create an instance of StepOperationConfig from a dict
step_operation_config_from_dict = StepOperationConfig.from_dict(step_operation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


