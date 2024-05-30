# fireblocks.ResetDeviceApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_device**](ResetDeviceApi.md#reset_device) | **POST** /management/users/{id}/reset_device | Resets device


# **reset_device**
> reset_device(id, idempotency_key=idempotency_key)

Resets device

Resets mobile device for given console user, that user will need to do mobile onboarding again.

### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    id = 'id_example' # str | The ID of the console user
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Resets device
        fireblocks.reset_device.reset_device(id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling ResetDeviceApi->reset_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the console user | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset device approval request has been sent |  * X-Request-ID -  <br>  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  * X-Request-ID -  <br>  |
**403** | Lacking permissions. |  * X-Request-ID -  <br>  |
**5XX** | Internal error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

