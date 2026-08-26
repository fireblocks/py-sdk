# fireblocks.SecurityPostureManagementApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_finding_by_id**](SecurityPostureManagementApi.md#get_security_finding_by_id) | **GET** /security/fspm/findings/{id} | Get a FSPM security finding by ID
[**get_security_findings**](SecurityPostureManagementApi.md#get_security_findings) | **GET** /security/fspm/findings | Get FSPM security findings
[**update_security_finding_by_id**](SecurityPostureManagementApi.md#update_security_finding_by_id) | **PATCH** /security/fspm/findings/{id} | Update a FSPM security finding by ID


# **get_security_finding_by_id**
> SecurityFindingDetailed get_security_finding_by_id(id)

Get a FSPM security finding by ID

Returns a single FSPM security finding for the workspace, redacted to the public field set.
Endpoint Roles: Security Admin, Security Auditor.


### Example


```python
from fireblocks.models.security_finding_detailed import SecurityFindingDetailed
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
    id = 'd7ca6101-a65e-4a9c-b6c1-b8bd697e0cd2' # str | Unique identifier of the finding

    try:
        # Get a FSPM security finding by ID
        api_response = fireblocks.security_posture_management.get_security_finding_by_id(id).result()
        print("The response of SecurityPostureManagementApi->get_security_finding_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPostureManagementApi->get_security_finding_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the finding | 

### Return type

[**SecurityFindingDetailed**](SecurityFindingDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single FSPM finding |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_findings**
> GetFindingsExternalResponse get_security_findings(page_cursor=page_cursor, page_size=page_size, severity=severity, category=category, status=status)

Get FSPM security findings

Returns a paginated list of FSPM security findings for the workspace.
Endpoint Roles: Security Admin, Security Auditor.


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

# **update_security_finding_by_id**
> SecurityFindingDetailed update_security_finding_by_id(id, update_finding_external_request, idempotency_key=idempotency_key)

Update a FSPM security finding by ID

Accepts or reopens a finding for the workspace. When accepting a finding
(`status: "ACCEPTED"`), `statusUpdatedReason` is required.
Endpoint Roles: Security Admin.


### Example


```python
from fireblocks.models.security_finding_detailed import SecurityFindingDetailed
from fireblocks.models.update_finding_external_request import UpdateFindingExternalRequest
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
    id = 'd7ca6101-a65e-4a9c-b6c1-b8bd697e0cd2' # str | Unique identifier of the finding
    update_finding_external_request = fireblocks.UpdateFindingExternalRequest() # UpdateFindingExternalRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update a FSPM security finding by ID
        api_response = fireblocks.security_posture_management.update_security_finding_by_id(id, update_finding_external_request, idempotency_key=idempotency_key).result()
        print("The response of SecurityPostureManagementApi->update_security_finding_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPostureManagementApi->update_security_finding_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the finding | 
 **update_finding_external_request** | [**UpdateFindingExternalRequest**](UpdateFindingExternalRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SecurityFindingDetailed**](SecurityFindingDetailed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated FSPM finding |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

