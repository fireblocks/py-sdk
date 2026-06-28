# ReportJob

A report job. Optional fields are status-dependent: `completedAt`, `rowCount`, and `fileSizeBytes` are present only when `status` is `COMPLETED`; `failedAt` is present only when `status` is `FAILED`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the report job | 
**status** | [**ReportStatus**](ReportStatus.md) |  | 
**report_type** | [**ReportType**](ReportType.md) |  | 
**output_format** | [**ReportOutputFormat**](ReportOutputFormat.md) |  | 
**compress** | **bool** | Whether the output file is gzip-compressed | 
**requested_by_user_id** | **str** | ID of the user who requested the report | 
**created_at** | **int** | Epoch milliseconds (UTC) when the job was created | 
**completed_at** | **int** | Epoch milliseconds (UTC) when the report completed. Only present when &#x60;status&#x60; is &#x60;COMPLETED&#x60;. | [optional] 
**failed_at** | **int** | Epoch milliseconds (UTC) when the report failed. Only present when &#x60;status&#x60; is &#x60;FAILED&#x60;. | [optional] 
**row_count** | **int** | Number of rows in the report file. Only present when &#x60;status&#x60; is &#x60;COMPLETED&#x60;. | [optional] 
**file_size_bytes** | **int** | Size of the report file in bytes (includes compression when &#x60;compress&#x60; is &#x60;true&#x60;). Only present when &#x60;status&#x60; is &#x60;COMPLETED&#x60;. | [optional] 

## Example

```python
from fireblocks.models.report_job import ReportJob

# TODO update the JSON string below
json = "{}"
# create an instance of ReportJob from a JSON string
report_job_instance = ReportJob.from_json(json)
# print the JSON string representation of the object
print(ReportJob.to_json())

# convert the object into a dict
report_job_dict = report_job_instance.to_dict()
# create an instance of ReportJob from a dict
report_job_from_dict = ReportJob.from_dict(report_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


