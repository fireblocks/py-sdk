# fireblocks.ReportsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsBetaApi.md#create_report) | **POST** /reports | Create a report
[**get_report**](ReportsBetaApi.md#get_report) | **GET** /reports/{reportId} | Get report status
[**list_reports**](ReportsBetaApi.md#list_reports) | **GET** /reports | List reports


# **create_report**
> CreateReportResponse create_report(create_report_request, idempotency_key=idempotency_key)

Create a report

Creates a new asynchronous report job and returns a receipt containing the report ID.
Poll `GET /v1/reports/{reportId}` to check status. When `status` is `COMPLETED`, the poll
response includes a fresh pre-signed download URL in `links.downloadUrl`.

**Note:** These endpoints are currently in beta and might be subject to changes.

Endpoint Permission: Viewer and above.


### Example


```python
from fireblocks.models.create_report_request import CreateReportRequest
from fireblocks.models.create_report_response import CreateReportResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    create_report_request = fireblocks.CreateReportRequest() # CreateReportRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a report
        api_response = fireblocks.reports_beta.create_report(create_report_request, idempotency_key=idempotency_key).result()
        print("The response of ReportsBetaApi->create_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsBetaApi->create_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_report_request** | [**CreateReportRequest**](CreateReportRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateReportResponse**](CreateReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Report job accepted and queued for processing |  * X-Request-ID -  <br>  |
**409** | A report with the same type and filters is already being processed |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report**
> ReportJobResponse get_report(report_id)

Get report status

Returns the current status of a report job. Check the `status` field to determine the outcome.

When `status` is `COMPLETED`, the response includes a fresh pre-signed download URL in
`links.downloadUrl` (TTL ~1 hour). Re-poll this endpoint to obtain a new URL after expiry.

When `status` is `FAILED`, the `failedAt` timestamp indicates when the failure occurred.

**Note:** These endpoints are currently in beta and might be subject to changes.

Endpoint Permission: Viewer and above.


### Example


```python
from fireblocks.models.report_job_response import ReportJobResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    report_id = '0190b3c2-7e4a-7c31-9f2a-1b6d8e5a0c11' # str | The unique identifier of the report job

    try:
        # Get report status
        api_response = fireblocks.reports_beta.get_report(report_id).result()
        print("The response of ReportsBetaApi->get_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsBetaApi->get_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique identifier of the report job | 

### Return type

[**ReportJobResponse**](ReportJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Report job details |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reports**
> ReportListResponse list_reports(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order, status=status, report_type=report_type)

List reports

Returns a paginated list of report jobs scoped to the calling tenant.

**Note:** Download URLs are not included in list responses. Call `GET /v1/reports/{reportId}` to
obtain a fresh signed download URL for a specific completed report.

**Note:** These endpoints are currently in beta and might be subject to changes.

Endpoint Permission: Viewer and above.


### Example


```python
from fireblocks.models.report_list_response import ReportListResponse
from fireblocks.models.report_status import ReportStatus
from fireblocks.models.report_type import ReportType
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    page_cursor = 'page_cursor_example' # str | Opaque cursor returned from a previous list call (optional)
    page_size = 20 # int | Maximum number of items per page (optional) (default to 20)
    sort_by = createdAt # str | Field to sort by (optional) (default to createdAt)
    order = DESC # str | Sort direction (optional) (default to DESC)
    status = [fireblocks.ReportStatus()] # List[ReportStatus] | Filter by lifecycle status. Repeat the parameter to filter on multiple statuses (e.g., ?status=QUEUED&status=PROCESSING). (optional)
    report_type = [fireblocks.ReportType()] # List[ReportType] | Filter by report type. Repeat the parameter to filter on multiple types. (optional)

    try:
        # List reports
        api_response = fireblocks.reports_beta.list_reports(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order, status=status, report_type=report_type).result()
        print("The response of ReportsBetaApi->list_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsBetaApi->list_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Opaque cursor returned from a previous list call | [optional] 
 **page_size** | **int**| Maximum number of items per page | [optional] [default to 20]
 **sort_by** | **str**| Field to sort by | [optional] [default to createdAt]
 **order** | **str**| Sort direction | [optional] [default to DESC]
 **status** | [**List[ReportStatus]**](ReportStatus.md)| Filter by lifecycle status. Repeat the parameter to filter on multiple statuses (e.g., ?status&#x3D;QUEUED&amp;status&#x3D;PROCESSING). | [optional] 
 **report_type** | [**List[ReportType]**](ReportType.md)| Filter by report type. Repeat the parameter to filter on multiple types. | [optional] 

### Return type

[**ReportListResponse**](ReportListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of report jobs |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

