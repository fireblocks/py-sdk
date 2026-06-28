# CreateReportRequest

Request body for creating a new asynchronous report job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** | The type of report to generate. | 
**output_format** | [**ReportOutputFormat**](ReportOutputFormat.md) |  | 
**compress** | **bool** | Gzip the output file. Defaults to true. | [optional] [default to False]
**filters** | [**AddressesFilters**](AddressesFilters.md) |  | [optional] 

## Example

```python
from fireblocks.models.create_report_request import CreateReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReportRequest from a JSON string
create_report_request_instance = CreateReportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReportRequest.to_json())

# convert the object into a dict
create_report_request_dict = create_report_request_instance.to_dict()
# create an instance of CreateReportRequest from a dict
create_report_request_from_dict = CreateReportRequest.from_dict(create_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


