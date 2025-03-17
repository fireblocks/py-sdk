# fireblocks.TokenizationApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**burn_collection_token**](TokenizationApi.md#burn_collection_token) | **POST** /tokenization/collections/{id}/tokens/burn | Burn tokens
[**create_new_collection**](TokenizationApi.md#create_new_collection) | **POST** /tokenization/collections | Create a new collection
[**fetch_collection_token_details**](TokenizationApi.md#fetch_collection_token_details) | **GET** /tokenization/collections/{id}/tokens/{tokenId} | Get collection token details
[**get_collection_by_id**](TokenizationApi.md#get_collection_by_id) | **GET** /tokenization/collections/{id} | Get a collection by id
[**get_linked_collections**](TokenizationApi.md#get_linked_collections) | **GET** /tokenization/collections | Get collections
[**get_linked_token**](TokenizationApi.md#get_linked_token) | **GET** /tokenization/tokens/{id} | Return a linked token
[**get_linked_tokens**](TokenizationApi.md#get_linked_tokens) | **GET** /tokenization/tokens | List all linked tokens
[**issue_new_token**](TokenizationApi.md#issue_new_token) | **POST** /tokenization/tokens | Issue a new token
[**link**](TokenizationApi.md#link) | **POST** /tokenization/tokens/link | Link a contract
[**mint_collection_token**](TokenizationApi.md#mint_collection_token) | **POST** /tokenization/collections/{id}/tokens/mint | Mint tokens
[**unlink**](TokenizationApi.md#unlink) | **DELETE** /tokenization/tokens/{id} | Unlink a token
[**unlink_collection**](TokenizationApi.md#unlink_collection) | **DELETE** /tokenization/collections/{id} | Delete a collection link


# **burn_collection_token**
> CollectionBurnResponseDto burn_collection_token(id, collection_burn_request_dto, idempotency_key=idempotency_key)

Burn tokens

Burn tokens in a collection

### Example


```python
from fireblocks.models.collection_burn_request_dto import CollectionBurnRequestDto
from fireblocks.models.collection_burn_response_dto import CollectionBurnResponseDto
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
    id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb' # str | The collection link id
    collection_burn_request_dto = fireblocks.CollectionBurnRequestDto() # CollectionBurnRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Burn tokens
        api_response = fireblocks.tokenization.burn_collection_token(id, collection_burn_request_dto, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->burn_collection_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->burn_collection_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The collection link id | 
 **collection_burn_request_dto** | [**CollectionBurnRequestDto**](CollectionBurnRequestDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CollectionBurnResponseDto**](CollectionBurnResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Tokens burned successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_collection**
> CollectionLinkDto create_new_collection(collection_deploy_request_dto, idempotency_key=idempotency_key)

Create a new collection

Create a new collection and link it as a token

### Example


```python
from fireblocks.models.collection_deploy_request_dto import CollectionDeployRequestDto
from fireblocks.models.collection_link_dto import CollectionLinkDto
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
    collection_deploy_request_dto = fireblocks.CollectionDeployRequestDto() # CollectionDeployRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a new collection
        api_response = fireblocks.tokenization.create_new_collection(collection_deploy_request_dto, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->create_new_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->create_new_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_deploy_request_dto** | [**CollectionDeployRequestDto**](CollectionDeployRequestDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CollectionLinkDto**](CollectionLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Collection was created successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_collection_token_details**
> CollectionLinkDto fetch_collection_token_details(id, token_id)

Get collection token details

Get collection token details by id

### Example


```python
from fireblocks.models.collection_link_dto import CollectionLinkDto
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
    id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb' # str | The collection link id
    token_id = '1' # str | The tokenId as it appears on the blockchain

    try:
        # Get collection token details
        api_response = fireblocks.tokenization.fetch_collection_token_details(id, token_id).result()
        print("The response of TokenizationApi->fetch_collection_token_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->fetch_collection_token_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The collection link id | 
 **token_id** | **str**| The tokenId as it appears on the blockchain | 

### Return type

[**CollectionLinkDto**](CollectionLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection token details were fetched successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_by_id**
> CollectionLinkDto get_collection_by_id(id)

Get a collection by id

Get a collection by id

### Example


```python
from fireblocks.models.collection_link_dto import CollectionLinkDto
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
    id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb' # str | The token link id

    try:
        # Get a collection by id
        api_response = fireblocks.tokenization.get_collection_by_id(id).result()
        print("The response of TokenizationApi->get_collection_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_collection_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The token link id | 

### Return type

[**CollectionLinkDto**](CollectionLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection fetched successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_collections**
> GetLinkedCollectionsPaginatedResponse get_linked_collections(page_cursor=page_cursor, page_size=page_size, status=status)

Get collections

Get collections (paginated)

### Example


```python
from fireblocks.models.get_linked_collections_paginated_response import GetLinkedCollectionsPaginatedResponse
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
    page_cursor = 'page_cursor_example' # str | Page cursor to get the next page, for example - \"MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==\" (optional)
    page_size = 100 # float | Number of items per page (max 100), requesting more then 100 will return 100 items (optional) (default to 100)
    status = COMPLETED # object | A comma separated list of statuses to filter. Default is \"COMPLETED\" (optional)

    try:
        # Get collections
        api_response = fireblocks.tokenization.get_linked_collections(page_cursor=page_cursor, page_size=page_size, status=status).result()
        print("The response of TokenizationApi->get_linked_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_linked_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Page cursor to get the next page, for example - \&quot;MjAyMy0xMi0xMyAyMDozNjowOC4zMDI&#x3D;:MTEwMA&#x3D;&#x3D;\&quot; | [optional] 
 **page_size** | **float**| Number of items per page (max 100), requesting more then 100 will return 100 items | [optional] [default to 100]
 **status** | [**object**](.md)| A comma separated list of statuses to filter. Default is \&quot;COMPLETED\&quot; | [optional] 

### Return type

[**GetLinkedCollectionsPaginatedResponse**](GetLinkedCollectionsPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection fetched successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_token**
> TokenLinkDto get_linked_token(id)

Return a linked token

Return a linked token, with its status and metadata.

### Example


```python
from fireblocks.models.token_link_dto import TokenLinkDto
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
from fireblocks.models.tokens_paginated_response import TokensPaginatedResponse
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

Facilitates the creation of a new token, supporting both EVM-based and Stellar/Ripple platforms. For EVM, it deploys the corresponding contract template to the blockchain and links the token to the workspace. For Stellar/Ripple, it links a newly created token directly to the workspace without deploying a contract. Returns the token link with status "PENDING" until the token is deployed or "SUCCESS" if no deployment is needed.

### Example


```python
from fireblocks.models.create_token_request_dto import CreateTokenRequestDto
from fireblocks.models.token_link_dto import TokenLinkDto
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
    create_token_request_dto = fireblocks.CreateTokenRequestDto() # CreateTokenRequestDto | 
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

Link a contract

Link an a contract

### Example


```python
from fireblocks.models.token_link_dto import TokenLinkDto
from fireblocks.models.token_link_request_dto import TokenLinkRequestDto
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
    token_link_request_dto = fireblocks.TokenLinkRequestDto() # TokenLinkRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Link a contract
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
**404** | Could not find the underlying contract to link to |  -  |
**409** | Token link for {refId} already exists |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mint_collection_token**
> CollectionMintResponseDto mint_collection_token(id, collection_mint_request_dto, idempotency_key=idempotency_key)

Mint tokens

Mint tokens and upload metadata

### Example


```python
from fireblocks.models.collection_mint_request_dto import CollectionMintRequestDto
from fireblocks.models.collection_mint_response_dto import CollectionMintResponseDto
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
    id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb' # str | The collection link id
    collection_mint_request_dto = fireblocks.CollectionMintRequestDto() # CollectionMintRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Mint tokens
        api_response = fireblocks.tokenization.mint_collection_token(id, collection_mint_request_dto, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->mint_collection_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->mint_collection_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The collection link id | 
 **collection_mint_request_dto** | [**CollectionMintRequestDto**](CollectionMintRequestDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CollectionMintResponseDto**](CollectionMintResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Tokens minted successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink**
> unlink(id)

Unlink a token

Unlink a token. The token will be unlinked from the workspace. The token will not be deleted on chain nor the refId, only the link to the workspace will be removed.

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

# **unlink_collection**
> unlink_collection(id)

Delete a collection link

Delete a collection link

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
    id = 'fbfbfbfb-fbfb-fbfb-fbfb-fbfbfbfbfbfb' # str | The token link id

    try:
        # Delete a collection link
        fireblocks.tokenization.unlink_collection(id).result()
    except Exception as e:
        print("Exception when calling TokenizationApi->unlink_collection: %s\n" % e)
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
**204** | Collection unlinked successfully |  -  |
**404** | Link for collection does not exist |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

