# ReportJobLinks

Download URL for the report. Present only when `status` is `COMPLETED`, and only on `GET /v1/reports/{reportId}` — not included in list responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** | URL to download the report file. A new URL is generated on each request to &#x60;GET /v1/reports/{reportId}&#x60; while &#x60;status&#x60; is &#x60;COMPLETED&#x60;. Re-poll to obtain a fresh URL after the previous one expires (approximately 1 hour). | 
**download_url_expires_at** | **int** | Epoch milliseconds (UTC) when the download URL expires | 

## Example

```python
from fireblocks.models.report_job_links import ReportJobLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ReportJobLinks from a JSON string
report_job_links_instance = ReportJobLinks.from_json(json)
# print the JSON string representation of the object
print(ReportJobLinks.to_json())

# convert the object into a dict
report_job_links_dict = report_job_links_instance.to_dict()
# create an instance of ReportJobLinks from a dict
report_job_links_from_dict = ReportJobLinks.from_dict(report_job_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


