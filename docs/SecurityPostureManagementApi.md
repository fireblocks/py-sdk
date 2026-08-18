# fireblocks.SecurityPostureManagementApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_findings**](SecurityPostureManagementApi.md#get_security_findings) | **GET** /security/fspm/findings | Get FSPM security findings


# **get_security_findings**
> GetFindingsExternalResponse get_security_findings(page_cursor=page_cursor, page_size=page_size, severity=severity, category=category, status=status)

Get FSPM security findings

Returns a paginated list of FSPM security findings for the workspace.
Endpoint Permissions: Security Admin, Security Auditor.


### Example


```python
from fireblocks.models.get_findings_external_response import GetFindingsExternalResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor indicating the page position. Omit to fetch the first page. (optional)
    page_size = 10 # int | Number of results per page (optional) (default to 10)
    severity = 'HIGH' # str | Filter by severity level (optional)
    category = 'USER_MANAGEMENT' # str | Filter by finding category (optional)
    status = 'OPEN' # str | Filter by finding status (optional)

    try:
        # Get FSPM security findings
        api_response = fireblocks.security_posture_management.get_security_findings(page_cursor=page_cursor, page_size=page_size, severity=severity, category=category, status=status).result()
        print("The response of SecurityPostureManagementApi->get_security_findings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPostureManagementApi->get_security_findings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor indicating the page position. Omit to fetch the first page. | [optional] 
 **page_size** | **int**| Number of results per page | [optional] [default to 10]
 **severity** | **str**| Filter by severity level | [optional] 
 **category** | **str**| Filter by finding category | [optional] 
 **status** | **str**| Filter by finding status | [optional] 

### Return type

[**GetFindingsExternalResponse**](GetFindingsExternalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of FSPM findings |  * X-Request-ID -  <br>  |
**400** | Bad request — invalid or malformed query parameters. |  * X-Request-ID -  <br>  |
**401** | Unauthorized — missing or invalid authentication token. |  * X-Request-ID -  <br>  |
**403** | Forbidden — insufficient permissions or feature is disabled. |  * X-Request-ID -  <br>  |
**429** | Too many requests — rate limit exceeded, slow down and retry later. |  * X-Request-ID -  <br>  |
**5XX** | Internal error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

