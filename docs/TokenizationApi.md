# fireblocks_client.TokenizationApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_linked_token**](TokenizationApi.md#get_linked_token) | **GET** /tokenization/tokens/{id} | Return a linked token
[**get_linked_tokens**](TokenizationApi.md#get_linked_tokens) | **GET** /tokenization/tokens | List all linked tokens
[**issue_new_token**](TokenizationApi.md#issue_new_token) | **POST** /tokenization/tokens | Issue a new token
[**link**](TokenizationApi.md#link) | **POST** /tokenization/tokens/link | Link a token
[**unlink**](TokenizationApi.md#unlink) | **DELETE** /tokenization/tokens/{id} | Unlink a token


# **get_linked_token**
> TokenLinkDto get_linked_token(id)

Return a linked token

Return a linked token, with its status and metadata.

### Example


```python
from fireblocks_client.models.token_link_dto import TokenLinkDto
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
    id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb' # str | The token link id

    try:
        # Return a linked token
        api_response = fireblocks.tokenization.get_linked_token(id).result()
        print("The response of TokenizationApi->get_linked_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_linked_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The token link id | 

### Return type

[**TokenLinkDto**](TokenLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token fetched successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_tokens**
> TokensPaginatedResponse get_linked_tokens(page_cursor=page_cursor, page_size=page_size, status=status)

List all linked tokens

Return all linked tokens (paginated)

### Example


```python
from fireblocks_client.models.tokens_paginated_response import TokensPaginatedResponse
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
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page (optional)
    page_size = 10 # float | Number of items per page, requesting more then max will return max items (optional)
    status = COMPLETED # object | A comma separated list of statuses to filter. Default is \"COMPLETED\" (optional)

    try:
        # List all linked tokens
        api_response = fireblocks.tokenization.get_linked_tokens(page_cursor=page_cursor, page_size=page_size, status=status).result()
        print("The response of TokenizationApi->get_linked_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_linked_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Page cursor to get the next page | [optional] 
 **page_size** | **float**| Number of items per page, requesting more then max will return max items | [optional] 
 **status** | [**object**](.md)| A comma separated list of statuses to filter. Default is \&quot;COMPLETED\&quot; | [optional] 

### Return type

[**TokensPaginatedResponse**](TokensPaginatedResponse.md)

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

# **issue_new_token**
> TokenLinkDto issue_new_token(create_token_request_dto, idempotency_key=idempotency_key)

Issue a new token

Facilitates the creation of a new token, supporting both EVM-based and Stellar/Ripple platforms. For EVM, it deploys the corresponding contract template to the blockchain and links the token to the workspace. For Stellar/Ripple, it links a newly created token directly to the workspace without deploying a contract. Returns the token link with status \"PENDING\" until the token is deployed or \"SUCCESS\" if no deployment is needed.

### Example


```python
from fireblocks_client.models.create_token_request_dto import CreateTokenRequestDto
from fireblocks_client.models.token_link_dto import TokenLinkDto
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
    create_token_request_dto = fireblocks_client.CreateTokenRequestDto() # CreateTokenRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Issue a new token
        api_response = fireblocks.tokenization.issue_new_token(create_token_request_dto, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->issue_new_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->issue_new_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_token_request_dto** | [**CreateTokenRequestDto**](CreateTokenRequestDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TokenLinkDto**](TokenLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Token was created successfully |  -  |
**409** | Asset already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link**
> TokenLinkDto link(token_link_request_dto, idempotency_key=idempotency_key)

Link a token

Link an already existing token (by assetId, collectionId or contractId as refId) to a workspace across EVM, Stellar, or Ripple platforms. The token will be linked to the workspace if it does not already exist.

### Example


```python
from fireblocks_client.models.token_link_dto import TokenLinkDto
from fireblocks_client.models.token_link_request_dto import TokenLinkRequestDto
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
    token_link_request_dto = fireblocks_client.TokenLinkRequestDto() # TokenLinkRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Link a token
        api_response = fireblocks.tokenization.link(token_link_request_dto, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_link_request_dto** | [**TokenLinkRequestDto**](TokenLinkRequestDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TokenLinkDto**](TokenLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token linked successfully |  -  |
**201** |  |  -  |
**404** | Could not find the underlying token identifier (refId) to link the token to |  -  |
**409** | Token link for {refId} already exists |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink**
> unlink(id)

Unlink a token

Unlink a token. The token will be unlinked from the workspace. The token will not be deleted on chain nor the refId, only the link to the workspace will be removed.

### Example


```python
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath

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
    id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb' # str | The token link id

    try:
        # Unlink a token
        fireblocks.tokenization.unlink(id).result()
    except Exception as e:
        print("Exception when calling TokenizationApi->unlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The token link id | 

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
**200** | Token unlinked successfully |  -  |
**204** |  |  -  |
**404** | Link did not exist |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

