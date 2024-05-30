# fireblocks.OTABetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ota_status**](OTABetaApi.md#get_ota_status) | **GET** /management/ota | Returns current OTA status
[**set_ota_status**](OTABetaApi.md#set_ota_status) | **PUT** /management/ota | Enable or disable transactions to OTA


# **get_ota_status**
> GetOtaStatusResponse get_ota_status()

Returns current OTA status

Returns current OTA status

### Example


```python
from fireblocks.models.get_ota_status_response import GetOtaStatusResponse
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

    try:
        # Returns current OTA status
        api_response = fireblocks.ota_beta.get_ota_status().result()
        print("The response of OTABetaApi->get_ota_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OTABetaApi->get_ota_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOtaStatusResponse**](GetOtaStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current OTA status |  -  |
**404** | Configuration not found for tenant |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ota_status**
> SetOtaStatusResponse set_ota_status(set_ota_status_request, idempotency_key=idempotency_key)

Enable or disable transactions to OTA

Enable or disable transactions to OTA

### Example


```python
from fireblocks.models.set_ota_status_request import SetOtaStatusRequest
from fireblocks.models.set_ota_status_response import SetOtaStatusResponse
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
    set_ota_status_request = fireblocks.SetOtaStatusRequest() # SetOtaStatusRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Enable or disable transactions to OTA
        api_response = fireblocks.ota_beta.set_ota_status(set_ota_status_request, idempotency_key=idempotency_key).result()
        print("The response of OTABetaApi->set_ota_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OTABetaApi->set_ota_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_ota_status_request** | [**SetOtaStatusRequest**](SetOtaStatusRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SetOtaStatusResponse**](SetOtaStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successfully updated OTA status |  * X-Request-ID -  <br>  |
**400** | Bad request |  -  |
**409** | Similar request already pending |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

