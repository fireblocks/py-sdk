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
from fireblocks_client.models.get_audit_logs_response import GetAuditLogsResponse
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
    time_period = 'time_period_example' # str | The last time period to fetch audit logs (optional)
    cursor = 'cursor_example' # str | The next id to start fetch audit logs from (optional)

    try:
        # Get audit logs
        api_response = fireblocks.audit_logs.get_audit_logs(time_period=time_period, cursor=cursor).result()
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
from fireblocks_client.models.get_audit_logs_response_dto import GetAuditLogsResponseDTO
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
    time_period = 'time_period_example' # str | The last time period to fetch audit logs (optional)

    try:
        # Get audit logs
        api_response = fireblocks.audit_logs.get_audits(time_period=time_period).result()
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

