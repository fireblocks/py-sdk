# fireblocks.SwapBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_terms_of_service**](SwapBetaApi.md#approve_terms_of_service) | **POST** /swap/providers/{providerId}/approve_terms | Approve terms of service
[**create_quote**](SwapBetaApi.md#create_quote) | **POST** /swap/providers/{providerId}/quote | Create a quote
[**create_swap_operation**](SwapBetaApi.md#create_swap_operation) | **POST** /swap/operations | Create swap operation
[**get_swap_operation_by_id**](SwapBetaApi.md#get_swap_operation_by_id) | **GET** /swap/operations/{operationId} | Get operation details
[**get_swap_operations**](SwapBetaApi.md#get_swap_operations) | **GET** /swap/operations | Get Operations list
[**get_swap_providers**](SwapBetaApi.md#get_swap_providers) | **GET** /swap/providers | Get Providers List


# **approve_terms_of_service**
> SwapProvider approve_terms_of_service(provider_id, idempotency_key=idempotency_key)

Approve terms of service

Approve the terms of service for a swap provider.
Some providers require this approval before performing a swap action for the first time.

Note: These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Swap, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Editor.

### Example


```python
from fireblocks.models.swap_provider import SwapProvider
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
    provider_id = 'provider_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Approve terms of service
        api_response = fireblocks.swap_beta.approve_terms_of_service(provider_id, idempotency_key=idempotency_key).result()
        print("The response of SwapBetaApi->approve_terms_of_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapBetaApi->approve_terms_of_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SwapProvider**](SwapProvider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully approve terms of service |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quote**
> QuoteResponse create_quote(provider_id, quote_request, idempotency_key=idempotency_key)

Create a quote

Create a quote from specific swap provider.

Note: These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Swap, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.quote_request import QuoteRequest
from fireblocks.models.quote_response import QuoteResponse
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
    provider_id = 'provider_id_example' # str | 
    quote_request = fireblocks.QuoteRequest() # QuoteRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a quote
        api_response = fireblocks.swap_beta.create_quote(provider_id, quote_request, idempotency_key=idempotency_key).result()
        print("The response of SwapBetaApi->create_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapBetaApi->create_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**|  | 
 **quote_request** | [**QuoteRequest**](QuoteRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The response can be one of two possible DTOs, depending if the request contains the accountId property. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_swap_operation**
> SwapOperation create_swap_operation(swap_operation_request, idempotency_key=idempotency_key)

Create swap operation

Create swap operation based on a provided quote Id

Note: These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Swap, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Editor.

### Example


```python
from fireblocks.models.swap_operation import SwapOperation
from fireblocks.models.swap_operation_request import SwapOperationRequest
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
    swap_operation_request = fireblocks.SwapOperationRequest() # SwapOperationRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create swap operation
        api_response = fireblocks.swap_beta.create_swap_operation(swap_operation_request, idempotency_key=idempotency_key).result()
        print("The response of SwapBetaApi->create_swap_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapBetaApi->create_swap_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swap_operation_request** | [**SwapOperationRequest**](SwapOperationRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SwapOperation**](SwapOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swap_operation_by_id**
> SwapOperation get_swap_operation_by_id(operation_id)

Get operation details

Get swap operation Details by ID.

Note:These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Swap, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.swap_operation import SwapOperation
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
    operation_id = 'operation_id_example' # str | 

    try:
        # Get operation details
        api_response = fireblocks.swap_beta.get_swap_operation_by_id(operation_id).result()
        print("The response of SwapBetaApi->get_swap_operation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapBetaApi->get_swap_operation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**|  | 

### Return type

[**SwapOperation**](SwapOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swap_operations**
> SwapOperationsPaginatedResponse get_swap_operations(page_cursor=page_cursor, page_size=page_size)

Get Operations list

Return a list of swap operations for the specific workspace
The operations are sorted by creation date in descending order, meaning the most recent operation appears first.

Note:These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.swap_operations_paginated_response import SwapOperationsPaginatedResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 10 # float | Number of items in a page, Acceptable values are 1-100. Maximum value is 100 (optional) (default to 10)

    try:
        # Get Operations list
        api_response = fireblocks.swap_beta.get_swap_operations(page_cursor=page_cursor, page_size=page_size).result()
        print("The response of SwapBetaApi->get_swap_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapBetaApi->get_swap_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Number of items in a page, Acceptable values are 1-100. Maximum value is 100 | [optional] [default to 10]

### Return type

[**SwapOperationsPaginatedResponse**](SwapOperationsPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated response containing OperationDto objects |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swap_providers**
> SwapProvidersPaginatedResponse get_swap_providers(page_cursor=page_cursor, page_size=page_size)

Get Providers List

Return a list of all supported swap providers.

Note: These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Swap, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.swap_providers_paginated_response import SwapProvidersPaginatedResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 10 # float | Number of items in a page, Acceptable values are 1-100. Maximum value is 100 (optional) (default to 10)

    try:
        # Get Providers List
        api_response = fireblocks.swap_beta.get_swap_providers(page_cursor=page_cursor, page_size=page_size).result()
        print("The response of SwapBetaApi->get_swap_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwapBetaApi->get_swap_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Number of items in a page, Acceptable values are 1-100. Maximum value is 100 | [optional] [default to 10]

### Return type

[**SwapProvidersPaginatedResponse**](SwapProvidersPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated response containing ProviderDto objects |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

