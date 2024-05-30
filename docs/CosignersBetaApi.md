# fireblocks_client.CosignersBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_key**](CosignersBetaApi.md#get_api_key) | **GET** /cosigners/{cosignerId}/api_keys/{apiKeyId} | Get API key
[**get_api_keys**](CosignersBetaApi.md#get_api_keys) | **GET** /cosigners/{cosignerId}/api_keys | Get all API keys
[**get_cosigner**](CosignersBetaApi.md#get_cosigner) | **GET** /cosigners/{cosignerId} | Get cosigner
[**get_cosigners**](CosignersBetaApi.md#get_cosigners) | **GET** /cosigners | Get all cosigners
[**rename_cosigner**](CosignersBetaApi.md#rename_cosigner) | **PATCH** /cosigners/{cosignerId} | Rename cosigner


# **get_api_key**
> ApiKey get_api_key(cosigner_id, api_key_id)

Get API key

Get an API key by ID **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks_client.models.api_key import ApiKey
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

Get all cosigner paired API keys (paginated) **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks_client.models.api_keys_paginated_response import ApiKeysPaginatedResponse
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    order = 'DESC' # str | ASC / DESC ordering (default DESC) (optional) (default to 'DESC')
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
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to &#39;DESC&#39;]
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

Get a cosigner by ID **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks_client.models.cosigner import Cosigner
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

Get all workspace cosigners (paginated) **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks_client.models.cosigners_paginated_response import CosignersPaginatedResponse
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
    order = 'DESC' # str | ASC / DESC ordering (default DESC) (optional) (default to 'DESC')
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
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to &#39;DESC&#39;]
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

# **rename_cosigner**
> Cosigner rename_cosigner(cosigner_id, rename_cosigner)

Rename cosigner

Rename a cosigner by ID **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks_client.models.cosigner import Cosigner
from fireblocks_client.models.rename_cosigner import RenameCosigner
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
    cosigner_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the cosigner
    rename_cosigner = fireblocks_client.RenameCosigner() # RenameCosigner | 

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

