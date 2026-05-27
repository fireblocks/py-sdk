# fireblocks.AuditLogsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](AuditLogsApi.md#get_audit_logs) | **GET** /management/audit_logs | Get audit logs


# **get_audit_logs**
> GetAuditLogsResponse get_audit_logs(start_time=start_time, end_time=end_time, time_period=time_period, category=category, subject=subject, event=event, user=user, user_id=user_id, order=order, page_size=page_size, page_cursor=page_cursor, cursor=cursor)

Get audit logs

Retrieve audit log events for the workspace with optional filtering, date range, sorting, and cursor-based pagination.

Filters within the same field are combined as OR (e.g. category=Administration&category=Security returns events in either category). Filters across different fields are combined as AND.

**Deprecated parameters:** `timePeriod` and `cursor` remain functional for backward compatibility but new integrations should use `startTime`/`endTime` and `pageCursor` instead.

Endpoint Permission: Admin, Non-Signing Admin, Auditor, Security Admin, Security Auditor.

### Example


```python
from fireblocks.models.get_audit_logs_response import GetAuditLogsResponse
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
    start_time = 56 # int | Start of date range as epoch time in milliseconds. Takes precedence over timePeriod when provided. Must be no more than 1 year before the current time. (optional)
    end_time = 56 # int | End of date range as epoch time in milliseconds. Must be after startTime. Defaults to now when omitted. (optional)
    time_period = 'time_period_example' # str | Deprecated. Use startTime/endTime instead. Ignored when startTime is provided. Defaults to DAY when neither timePeriod nor startTime is supplied. (optional)
    category = ['category_example'] # List[str] | Filter by event category. Repeat the parameter for multiple values (OR logic within field). (optional)
    subject = ['subject_example'] # List[str] | Filter by event subject. Repeat the parameter for multiple values. (optional)
    event = ['event_example'] # List[str] | Filter by event type. Repeat the parameter for multiple values. (optional)
    user = ['user_example'] # List[str] | Filter by user name. Repeat the parameter for multiple values. (optional)
    user_id = ['user_id_example'] # List[str] | Filter by user ID. Repeat the parameter for multiple values. (optional)
    order = DESC # str | Sort direction. Defaults to DESC. (optional) (default to DESC)
    page_size = 200 # int | Number of results per page. Maximum 500. Defaults to 200. (optional) (default to 200)
    page_cursor = 'page_cursor_example' # str | Cursor returned from the previous response to fetch the next page. (optional)
    cursor = 'cursor_example' # str | Deprecated. Use pageCursor instead. (optional)

    try:
        # Get audit logs
        api_response = fireblocks.audit_logs.get_audit_logs(start_time=start_time, end_time=end_time, time_period=time_period, category=category, subject=subject, event=event, user=user, user_id=user_id, order=order, page_size=page_size, page_cursor=page_cursor, cursor=cursor).result()
        print("The response of AuditLogsApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Start of date range as epoch time in milliseconds. Takes precedence over timePeriod when provided. Must be no more than 1 year before the current time. | [optional] 
 **end_time** | **int**| End of date range as epoch time in milliseconds. Must be after startTime. Defaults to now when omitted. | [optional] 
 **time_period** | **str**| Deprecated. Use startTime/endTime instead. Ignored when startTime is provided. Defaults to DAY when neither timePeriod nor startTime is supplied. | [optional] 
 **category** | [**List[str]**](str.md)| Filter by event category. Repeat the parameter for multiple values (OR logic within field). | [optional] 
 **subject** | [**List[str]**](str.md)| Filter by event subject. Repeat the parameter for multiple values. | [optional] 
 **event** | [**List[str]**](str.md)| Filter by event type. Repeat the parameter for multiple values. | [optional] 
 **user** | [**List[str]**](str.md)| Filter by user name. Repeat the parameter for multiple values. | [optional] 
 **user_id** | [**List[str]**](str.md)| Filter by user ID. Repeat the parameter for multiple values. | [optional] 
 **order** | **str**| Sort direction. Defaults to DESC. | [optional] [default to DESC]
 **page_size** | **int**| Number of results per page. Maximum 500. Defaults to 200. | [optional] [default to 200]
 **page_cursor** | **str**| Cursor returned from the previous response to fetch the next page. | [optional] 
 **cursor** | **str**| Deprecated. Use pageCursor instead. | [optional] 

### Return type

[**GetAuditLogsResponse**](GetAuditLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit log events matching the requested filters and date range |  * X-Request-ID -  <br>  |
**400** | Error Response |  * X-Request-ID -  <br>  |
**403** | Error Response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

