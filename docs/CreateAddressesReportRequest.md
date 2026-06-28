# CreateAddressesReportRequest

Request body for creating a new ADDRESSES report job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** | The type of report to generate. | 
**output_format** | [**ReportOutputFormat**](ReportOutputFormat.md) |  | 
**compress** | **bool** | Gzip the output file. Defaults to true. | [optional] [default to False]
**filters** | [**AddressesFilters**](AddressesFilters.md) |  | [optional] 

## Example

```python
from fireblocks.models.create_addresses_report_request import CreateAddressesReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressesReportRequest from a JSON string
create_addresses_report_request_instance = CreateAddressesReportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAddressesReportRequest.to_json())

# convert the object into a dict
create_addresses_report_request_dict = create_addresses_report_request_instance.to_dict()
# create an instance of CreateAddressesReportRequest from a dict
create_addresses_report_request_from_dict = CreateAddressesReportRequest.from_dict(create_addresses_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


