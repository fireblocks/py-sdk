# CreateReportResponse

Returned when a report job is successfully created. Use the `id` to poll for status via `GET /v1/reports/{reportId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the report job | 

## Example

```python
from fireblocks.models.create_report_response import CreateReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReportResponse from a JSON string
create_report_response_instance = CreateReportResponse.from_json(json)
# print the JSON string representation of the object
print(CreateReportResponse.to_json())

# convert the object into a dict
create_report_response_dict = create_report_response_instance.to_dict()
# create an instance of CreateReportResponse from a dict
create_report_response_from_dict = CreateReportResponse.from_dict(create_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


