# GetScreeningResultResponse

The current status, outcome, per-step results, and audit log for a screening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_id** | **str** | Identifier of the screening being queried. | 
**workflow_id** | **str** | Identifier of the workflow that produced this screening. | 
**screening_status** | [**ComplianceScreeningStatusEnum**](ComplianceScreeningStatusEnum.md) |  | 
**outcome** | [**ScreeningOutcomeEnum**](ScreeningOutcomeEnum.md) |  | [optional] 
**steps** | [**List[StepResult]**](StepResult.md) | Flat step list. | 
**audit_log** | [**List[AuditLogEntry]**](AuditLogEntry.md) | Append-only audit trail for this screening. | 

## Example

```python
from fireblocks.models.get_screening_result_response import GetScreeningResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetScreeningResultResponse from a JSON string
get_screening_result_response_instance = GetScreeningResultResponse.from_json(json)
# print the JSON string representation of the object
print(GetScreeningResultResponse.to_json())

# convert the object into a dict
get_screening_result_response_dict = get_screening_result_response_instance.to_dict()
# create an instance of GetScreeningResultResponse from a dict
get_screening_result_response_from_dict = GetScreeningResultResponse.from_dict(get_screening_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


