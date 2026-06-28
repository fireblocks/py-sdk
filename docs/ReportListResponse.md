# ReportListResponse

Paginated list of report jobs. Download URLs are not included in list items — call `GET /v1/reports/{reportId}` to retrieve the download URL for a specific completed report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ReportJob]**](ReportJob.md) | Page of report jobs | 
**next** | **str** | Opaque cursor for the next page. Null on the last page. | 
**prev** | **str** | Opaque cursor for the previous page. Null on the first page. | 

## Example

```python
from fireblocks.models.report_list_response import ReportListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportListResponse from a JSON string
report_list_response_instance = ReportListResponse.from_json(json)
# print the JSON string representation of the object
print(ReportListResponse.to_json())

# convert the object into a dict
report_list_response_dict = report_list_response_instance.to_dict()
# create an instance of ReportListResponse from a dict
report_list_response_from_dict = ReportListResponse.from_dict(report_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


