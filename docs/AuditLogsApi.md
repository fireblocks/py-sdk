# fireblocks_client.AuditLogsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](AuditLogsApi.md#get_audit_logs) | **GET** /management/audit_logs | Get audit logs
[**get_audits**](AuditLogsApi.md#get_audits) | **GET** /audits | Get audit logs


# **get_audit_logs**
> GetAuditLogsResponse get_audit_logs(time_period=time_period, cursor=cursor)

Get audit logs

Get all audits

### Example


```python
import fireblocks_client
from fireblocks_client.models.get_audit_logs_response import GetAuditLogsResponse
from fireblocks_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fireblocks.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fireblocks_client.Configuration(
    host = "https://api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with fireblocks_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireblocks_client.AuditLogsApi(api_client)
    time_period = 'time_period_example' # str | The last time period to fetch audit logs (optional)
    cursor = 'cursor_example' # str | The next id to start fetch audit logs from (optional)

    try:
        # Get audit logs
        api_response = api_instance.get_audit_logs(time_period=time_period, cursor=cursor)
        print("The response of AuditLogsApi->get_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->get_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_period** | **str**| The last time period to fetch audit logs | [optional] 
 **cursor** | **str**| The next id to start fetch audit logs from | [optional] 

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
**200** | Audit logs from requested time period |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audits**
> GetAuditLogsResponseDTO get_audits(time_period=time_period)

Get audit logs

Get all audits

### Example


```python
import fireblocks_client
from fireblocks_client.models.get_audit_logs_response_dto import GetAuditLogsResponseDTO
from fireblocks_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fireblocks.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fireblocks_client.Configuration(
    host = "https://api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with fireblocks_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireblocks_client.AuditLogsApi(api_client)
    time_period = 'time_period_example' # str | The last time period to fetch audit logs (optional)

    try:
        # Get audit logs
        api_response = api_instance.get_audits(time_period=time_period)
        print("The response of AuditLogsApi->get_audits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->get_audits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_period** | **str**| The last time period to fetch audit logs | [optional] 

### Return type

[**GetAuditLogsResponseDTO**](GetAuditLogsResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audit logs from requested time period |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

