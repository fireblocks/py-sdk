# ReportConflictResponse

Returned when a report with the same type and filters is already being processed for your workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** | Fireblocks error code for this conflict | 
**name** | **str** | Error name | 
**id** | **str** | The ID of the report currently being processed. Use this ID to poll for status. | 

## Example

```python
from fireblocks.models.report_conflict_response import ReportConflictResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportConflictResponse from a JSON string
report_conflict_response_instance = ReportConflictResponse.from_json(json)
# print the JSON string representation of the object
print(ReportConflictResponse.to_json())

# convert the object into a dict
report_conflict_response_dict = report_conflict_response_instance.to_dict()
# create an instance of ReportConflictResponse from a dict
report_conflict_response_from_dict = ReportConflictResponse.from_dict(report_conflict_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


