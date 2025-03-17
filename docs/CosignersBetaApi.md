# fireblocks.CosignersBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cosigner**](CosignersBetaApi.md#add_cosigner) | **POST** /cosigners | Add cosigner
[**get_api_key**](CosignersBetaApi.md#get_api_key) | **GET** /cosigners/{cosignerId}/api_keys/{apiKeyId} | Get API key
[**get_api_keys**](CosignersBetaApi.md#get_api_keys) | **GET** /cosigners/{cosignerId}/api_keys | Get all API keys
[**get_cosigner**](CosignersBetaApi.md#get_cosigner) | **GET** /cosigners/{cosignerId} | Get cosigner
[**get_cosigners**](CosignersBetaApi.md#get_cosigners) | **GET** /cosigners | Get all cosigners
[**get_request_status**](CosignersBetaApi.md#get_request_status) | **GET** /cosigners/{cosignerId}/api_keys/{apiKeyId}/{requestId} | Get request status
[**pair_api_key**](CosignersBetaApi.md#pair_api_key) | **PUT** /cosigners/{cosignerId}/api_keys/{apiKeyId} | Pair API key
[**rename_cosigner**](CosignersBetaApi.md#rename_cosigner) | **PATCH** /cosigners/{cosignerId} | Rename cosigner
[**unpair_api_key**](CosignersBetaApi.md#unpair_api_key) | **DELETE** /cosigners/{cosignerId}/api_keys/{apiKeyId} | Unpair API key
[**update_callback_handler**](CosignersBetaApi.md#update_callback_handler) | **PATCH** /cosigners/{cosignerId}/api_keys/{apiKeyId} | Update API key callback handler


# **add_cosigner**
> AddCosignerResponse add_cosigner(add_cosigner_request, idempotency_key=idempotency_key)

Add cosigner

Add a new cosigner. The cosigner will be pending pairing until the API key is manually paired

### Example


```python
from fireblocks.models.add_cosigner_request import AddCosignerRequest
from fireblocks.models.add_cosigner_response import AddCosignerResponse
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
    add_cosigner_request = fireblocks.AddCosignerRequest() # AddCosignerRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add cosigner
        api_response = fireblocks.cosigners_beta.add_cosigner(add_cosigner_request, idempotency_key=idempotency_key).result()
        print("The response of CosignersBetaApi->add_cosigner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->add_cosigner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_cosigner_request** | [**AddCosignerRequest**](AddCosignerRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AddCosignerResponse**](AddCosignerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Pending cosigner added |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key**
> ApiKey get_api_key(cosigner_id, api_key_id)

Get API key

Get an API key by ID
**Note:** These endpoints are currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.api_key import ApiKey
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    api_key_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API key

    try:
        # Get API key
        api_response = fireblocks.cosigners_beta.get_api_key(cosigner_id, api_key_id).result()
        print("The response of CosignersBetaApi->get_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->get_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_key_id** | **str**| The unique identifier of the API key | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ApiKey object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys**
> ApiKeysPaginatedResponse get_api_keys(cosigner_id, order=order, page_cursor=page_cursor, page_size=page_size)

Get all API keys

Get all cosigner paired API keys (paginated)

### Example


```python
from fireblocks.models.api_keys_paginated_response import ApiKeysPaginatedResponse
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 10 # float | Maximum number of items in the page (optional) (default to 10)

    try:
        # Get all API keys
        api_response = fireblocks.cosigners_beta.get_api_keys(cosigner_id, order=order, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of CosignersBetaApi->get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->get_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 10]

### Return type

[**ApiKeysPaginatedResponse**](ApiKeysPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated response containing ApiKey objects |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cosigner**
> Cosigner get_cosigner(cosigner_id)

Get cosigner

Get a cosigner by ID
**Note:** These endpoints are currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.cosigner import Cosigner
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner

    try:
        # Get cosigner
        api_response = fireblocks.cosigners_beta.get_cosigner(cosigner_id).result()
        print("The response of CosignersBetaApi->get_cosigner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->get_cosigner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 

### Return type

[**Cosigner**](Cosigner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A cosigner object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cosigners**
> CosignersPaginatedResponse get_cosigners(order=order, page_cursor=page_cursor, page_size=page_size)

Get all cosigners

Get all workspace cosigners (paginated)
**Note:** These endpoints are currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.cosigners_paginated_response import CosignersPaginatedResponse
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
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 10 # float | Maximum number of items in the page (optional) (default to 10)

    try:
        # Get all cosigners
        api_response = fireblocks.cosigners_beta.get_cosigners(order=order, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of CosignersBetaApi->get_cosigners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->get_cosigners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 10]

### Return type

[**CosignersPaginatedResponse**](CosignersPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated response containing Cosigner objects |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_status**
> Status get_request_status(cosigner_id, api_key_id, request_id)

Get request status

Get the status of an asynchronous request

### Example


```python
from fireblocks.models.status import Status
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    api_key_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API key
    request_id = 'request_id_example' # str | 

    try:
        # Get request status
        api_response = fireblocks.cosigners_beta.get_request_status(cosigner_id, api_key_id, request_id).result()
        print("The response of CosignersBetaApi->get_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->get_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_key_id** | **str**| The unique identifier of the API key | 
 **request_id** | **str**|  | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of the request |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pair_api_key**
> PairApiKeyResponse pair_api_key(cosigner_id, api_key_id, pair_api_key_request, idempotency_key=idempotency_key)

Pair API key

Pair an API key to a cosigner

### Example


```python
from fireblocks.models.pair_api_key_request import PairApiKeyRequest
from fireblocks.models.pair_api_key_response import PairApiKeyResponse
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    api_key_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API key
    pair_api_key_request = fireblocks.PairApiKeyRequest() # PairApiKeyRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Pair API key
        api_response = fireblocks.cosigners_beta.pair_api_key(cosigner_id, api_key_id, pair_api_key_request, idempotency_key=idempotency_key).result()
        print("The response of CosignersBetaApi->pair_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->pair_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_key_id** | **str**| The unique identifier of the API key | 
 **pair_api_key_request** | [**PairApiKeyRequest**](PairApiKeyRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**PairApiKeyResponse**](PairApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The API key object to be paired |  * X-Request-ID -  <br>  * Location -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_cosigner**
> Cosigner rename_cosigner(cosigner_id, rename_cosigner)

Rename cosigner

Rename a cosigner by ID
**Note:** These endpoints are currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.cosigner import Cosigner
from fireblocks.models.rename_cosigner import RenameCosigner
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    rename_cosigner = fireblocks.RenameCosigner() # RenameCosigner | 

    try:
        # Rename cosigner
        api_response = fireblocks.cosigners_beta.rename_cosigner(cosigner_id, rename_cosigner).result()
        print("The response of CosignersBetaApi->rename_cosigner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->rename_cosigner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **rename_cosigner** | [**RenameCosigner**](RenameCosigner.md)|  | 

### Return type

[**Cosigner**](Cosigner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A cosigner object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpair_api_key**
> ApiKey unpair_api_key(cosigner_id, api_key_id)

Unpair API key

Unpair an API key from a cosigner

### Example


```python
from fireblocks.models.api_key import ApiKey
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    api_key_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API key

    try:
        # Unpair API key
        api_response = fireblocks.cosigners_beta.unpair_api_key(cosigner_id, api_key_id).result()
        print("The response of CosignersBetaApi->unpair_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->unpair_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_key_id** | **str**| The unique identifier of the API key | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The API key object to be unpaired |  * X-Request-ID -  <br>  * Location -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_callback_handler**
> UpdateCallbackHandlerResponse update_callback_handler(cosigner_id, api_key_id, update_callback_handler_request)

Update API key callback handler

Update the callback handler of an API key

### Example


```python
from fireblocks.models.update_callback_handler_request import UpdateCallbackHandlerRequest
from fireblocks.models.update_callback_handler_response import UpdateCallbackHandlerResponse
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    api_key_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API key
    update_callback_handler_request = fireblocks.UpdateCallbackHandlerRequest() # UpdateCallbackHandlerRequest | 

    try:
        # Update API key callback handler
        api_response = fireblocks.cosigners_beta.update_callback_handler(cosigner_id, api_key_id, update_callback_handler_request).result()
        print("The response of CosignersBetaApi->update_callback_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersBetaApi->update_callback_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_key_id** | **str**| The unique identifier of the API key | 
 **update_callback_handler_request** | [**UpdateCallbackHandlerRequest**](UpdateCallbackHandlerRequest.md)|  | 

### Return type

[**UpdateCallbackHandlerResponse**](UpdateCallbackHandlerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The API key object with the new callback handler |  * X-Request-ID -  <br>  * Location -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

