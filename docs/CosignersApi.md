# fireblocks.CosignersApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cosigner**](CosignersApi.md#add_cosigner) | **POST** /cosigners | Add cosigner
[**get_cosigner**](CosignersApi.md#get_cosigner) | **GET** /cosigners/{cosignerId} | Get cosigner
[**get_cosigner_api_user**](CosignersApi.md#get_cosigner_api_user) | **GET** /cosigners/{cosignerId}/api_users/{apiUserId} | Get API user
[**get_cosigner_api_user_request_status**](CosignersApi.md#get_cosigner_api_user_request_status) | **GET** /cosigners/{cosignerId}/api_users/{apiUserId}/{requestId} | Get API user request status
[**get_cosigner_api_users**](CosignersApi.md#get_cosigner_api_users) | **GET** /cosigners/{cosignerId}/api_users | Get all API users
[**get_cosigners**](CosignersApi.md#get_cosigners) | **GET** /cosigners | Get all cosigners
[**pair_cosigner_api_user**](CosignersApi.md#pair_cosigner_api_user) | **PUT** /cosigners/{cosignerId}/api_users/{apiUserId} | Pair API user
[**rename_cosigner**](CosignersApi.md#rename_cosigner) | **PATCH** /cosigners/{cosignerId} | Rename cosigner
[**unpair_cosigner_api_user**](CosignersApi.md#unpair_cosigner_api_user) | **DELETE** /cosigners/{cosignerId}/api_users/{apiUserId} | Unpair API user
[**update_cosigner_api_user_callback_handler**](CosignersApi.md#update_cosigner_api_user_callback_handler) | **PATCH** /cosigners/{cosignerId}/api_users/{apiUserId} | Update API user callback handler


# **add_cosigner**
> AddCosignerResponse add_cosigner(add_cosigner_request, idempotency_key=idempotency_key)

Add cosigner

Add a new cosigner. The cosigner will be pending pairing until the API user is manually paired (see `pairCosignerApiUser`).
Endpoint Permission: Admin and Non-Signing Admin.

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
        api_response = fireblocks.cosigners.add_cosigner(add_cosigner_request, idempotency_key=idempotency_key).result()
        print("The response of CosignersApi->add_cosigner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->add_cosigner: %s\n" % e)
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

# **get_cosigner**
> Cosigner get_cosigner(cosigner_id)

Get cosigner

Get a cosigner by ID.
Endpoint Permission: Admin and Non-Signing Admin.

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
        api_response = fireblocks.cosigners.get_cosigner(cosigner_id).result()
        print("The response of CosignersApi->get_cosigner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->get_cosigner: %s\n" % e)
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

# **get_cosigner_api_user**
> CosignerApiUser get_cosigner_api_user(cosigner_id, api_user_id)

Get API user

Get an API user by ID.
Endpoint Permission: Admin and Non-Signing Admin.

### Example


```python
from fireblocks.models.cosigner_api_user import CosignerApiUser
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
    api_user_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API user

    try:
        # Get API user
        api_response = fireblocks.cosigners.get_cosigner_api_user(cosigner_id, api_user_id).result()
        print("The response of CosignersApi->get_cosigner_api_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->get_cosigner_api_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_user_id** | **str**| The unique identifier of the API user | 

### Return type

[**CosignerApiUser**](CosignerApiUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A CosignerApiUser object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cosigner_api_user_request_status**
> Status get_cosigner_api_user_request_status(cosigner_id, api_user_id, request_id)

Get API user request status

Get the status of an asynchronous request
Endpoint Permission: Admin and Non-Signing Admin.

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
    api_user_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API user
    request_id = 'request_id_example' # str | 

    try:
        # Get API user request status
        api_response = fireblocks.cosigners.get_cosigner_api_user_request_status(cosigner_id, api_user_id, request_id).result()
        print("The response of CosignersApi->get_cosigner_api_user_request_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->get_cosigner_api_user_request_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_user_id** | **str**| The unique identifier of the API user | 
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

# **get_cosigner_api_users**
> ApiUsersPaginatedResponse get_cosigner_api_users(cosigner_id, order=order, page_cursor=page_cursor, page_size=page_size)

Get all API users

Get all cosigner paired API users (paginated).
Endpoint Permission: Admin and Non-Signing Admin.

### Example


```python
from fireblocks.models.api_users_paginated_response import ApiUsersPaginatedResponse
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
        # Get all API users
        api_response = fireblocks.cosigners.get_cosigner_api_users(cosigner_id, order=order, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of CosignersApi->get_cosigner_api_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->get_cosigner_api_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 10]

### Return type

[**ApiUsersPaginatedResponse**](ApiUsersPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated response containing CosignerApiUser objects |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cosigners**
> CosignersPaginatedResponse get_cosigners(order=order, page_cursor=page_cursor, page_size=page_size)

Get all cosigners

Get all workspace cosigners (paginated).
Endpoint Permission: Admin and Non-Signing Admin.

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
        api_response = fireblocks.cosigners.get_cosigners(order=order, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of CosignersApi->get_cosigners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->get_cosigners: %s\n" % e)
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

# **pair_cosigner_api_user**
> PairApiUserResponse pair_cosigner_api_user(cosigner_id, api_user_id, pair_api_user_request, idempotency_key=idempotency_key)

Pair API user

Pair an API user to a cosigner
Endpoint Permission: Admin and Non-Signing Admin.

### Example


```python
from fireblocks.models.pair_api_user_request import PairApiUserRequest
from fireblocks.models.pair_api_user_response import PairApiUserResponse
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
    api_user_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API user
    pair_api_user_request = fireblocks.PairApiUserRequest() # PairApiUserRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Pair API user
        api_response = fireblocks.cosigners.pair_cosigner_api_user(cosigner_id, api_user_id, pair_api_user_request, idempotency_key=idempotency_key).result()
        print("The response of CosignersApi->pair_cosigner_api_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->pair_cosigner_api_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_user_id** | **str**| The unique identifier of the API user | 
 **pair_api_user_request** | [**PairApiUserRequest**](PairApiUserRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**PairApiUserResponse**](PairApiUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The API user object to be paired |  * X-Request-ID -  <br>  * Location -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_cosigner**
> Cosigner rename_cosigner(cosigner_id, rename_cosigner)

Rename cosigner

Rename a cosigner by ID.
Endpoint Permission: Admin and Non-Signing Admin.

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
        api_response = fireblocks.cosigners.rename_cosigner(cosigner_id, rename_cosigner).result()
        print("The response of CosignersApi->rename_cosigner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->rename_cosigner: %s\n" % e)
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

# **unpair_cosigner_api_user**
> CosignerApiUser unpair_cosigner_api_user(cosigner_id, api_user_id)

Unpair API user

Unpair an API user from a cosigner
Endpoint Permission: Admin and Non-Signing Admin.

### Example


```python
from fireblocks.models.cosigner_api_user import CosignerApiUser
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
    api_user_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API user

    try:
        # Unpair API user
        api_response = fireblocks.cosigners.unpair_cosigner_api_user(cosigner_id, api_user_id).result()
        print("The response of CosignersApi->unpair_cosigner_api_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->unpair_cosigner_api_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_user_id** | **str**| The unique identifier of the API user | 

### Return type

[**CosignerApiUser**](CosignerApiUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The API user object to be unpaired |  * X-Request-ID -  <br>  * Location -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cosigner_api_user_callback_handler**
> UpdateCallbackHandlerResponse update_cosigner_api_user_callback_handler(cosigner_id, api_user_id, update_callback_handler_request)

Update API user callback handler

Update the callback handler of an API user
Endpoint Permission: Admin and Non-Signing Admin.

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
    api_user_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the API user
    update_callback_handler_request = fireblocks.UpdateCallbackHandlerRequest() # UpdateCallbackHandlerRequest | 

    try:
        # Update API user callback handler
        api_response = fireblocks.cosigners.update_cosigner_api_user_callback_handler(cosigner_id, api_user_id, update_callback_handler_request).result()
        print("The response of CosignersApi->update_cosigner_api_user_callback_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CosignersApi->update_cosigner_api_user_callback_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosigner_id** | **str**| The unique identifier of the cosigner | 
 **api_user_id** | **str**| The unique identifier of the API user | 
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
**202** | The API user object with the new callback handler |  * X-Request-ID -  <br>  * Location -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

