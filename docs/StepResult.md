# StepResult

The result of one workflow step's execution during a screening.  Carries the step's outcome next to the two rule evaluations that produced it — which trigger rule decided the connector should run, and which outcome rule read the response — plus the provider's own verdict and risk level.  A step that did not screen carries a `bypassReason` instead of a risk level. Only `PASSED_BY_POLICY` means the policy deliberately let it through; every other reason means the check could not be performed, and the step is rejected rather than passed. A bypass is not an approval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** | Identifier of this step within the workflow. | 
**connector_id** | **str** | Identifier of the connector that executed this step. | 
**operation** | [**ScreeningOperationEnum**](ScreeningOperationEnum.md) |  | 
**trigger_rule_outcome** | [**TriggerRuleOutcomeEnum**](TriggerRuleOutcomeEnum.md) |  | 
**matched_trigger_rule** | [**Rule**](Rule.md) |  | [optional] 
**outcome_rule_outcome** | [**ScreeningOutcomeEnum**](ScreeningOutcomeEnum.md) |  | 
**matched_outcome_rule** | [**Rule**](Rule.md) |  | [optional] 
**outcome** | [**ScreeningOutcomeEnum**](ScreeningOutcomeEnum.md) |  | 
**metadata** | **Dict[str, object]** | Connector-specific data, keyed by the connector&#39;s configured outcomeMetaParameters for this operation. | [optional] 
**ticket_id** | **str** | The connector-side screening ticket identifier. | [optional] 
**verdict** | [**ConnectorVerdictEnum**](ConnectorVerdictEnum.md) |  | [optional] 
**connector_status** | [**ConnectorStatusEnum**](ConnectorStatusEnum.md) |  | [optional] 
**bypass_reason** | [**BypassReasonEnum**](BypassReasonEnum.md) |  | [optional] 
**risk** | [**RiskLevelEnum**](RiskLevelEnum.md) |  | [optional] 

## Example

```python
from fireblocks.models.step_result import StepResult

# TODO update the JSON string below
json = "{}"
# create an instance of StepResult from a JSON string
step_result_instance = StepResult.from_json(json)
# print the JSON string representation of the object
print(StepResult.to_json())

# convert the object into a dict
step_result_dict = step_result_instance.to_dict()
# create an instance of StepResult from a dict
step_result_from_dict = StepResult.from_dict(step_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


