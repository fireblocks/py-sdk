# fireblocks.BlockchainLinkBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_blockchain_link_chain**](BlockchainLinkBetaApi.md#activate_blockchain_link_chain) | **POST** /blockchain_link/blockchains/{blockchainId}/activate | Activate a blockchain (triggers activation workflow)
[**create_blockchain_link_chain**](BlockchainLinkBetaApi.md#create_blockchain_link_chain) | **POST** /blockchain_link/blockchains | Create a new blockchain
[**delete_blockchain_link_chain**](BlockchainLinkBetaApi.md#delete_blockchain_link_chain) | **DELETE** /blockchain_link/blockchains/{blockchainId} | Delete a blockchain
[**get_blockchain_link_billing_info**](BlockchainLinkBetaApi.md#get_blockchain_link_billing_info) | **GET** /blockchain_link/blockchains/billing_info | Get tenant billing info
[**get_blockchain_link_chain**](BlockchainLinkBetaApi.md#get_blockchain_link_chain) | **GET** /blockchain_link/blockchains/{blockchainId} | Get a blockchain by ID
[**get_blockchain_link_test_wallet_address**](BlockchainLinkBetaApi.md#get_blockchain_link_test_wallet_address) | **GET** /blockchain_link/blockchains/test_wallet_address | Get the test wallet address
[**list_blockchain_link_chains**](BlockchainLinkBetaApi.md#list_blockchain_link_chains) | **GET** /blockchain_link/blockchains | List blockchains with pagination and filtering
[**trigger_blockchain_link_validation**](BlockchainLinkBetaApi.md#trigger_blockchain_link_validation) | **POST** /blockchain_link/blockchains/{blockchainId}/validate | Trigger validation workflow
[**update_blockchain_link_chain**](BlockchainLinkBetaApi.md#update_blockchain_link_chain) | **PUT** /blockchain_link/blockchains/{blockchainId} | Update a blockchain


# **activate_blockchain_link_chain**
> ActivateBlockchainResponse activate_blockchain_link_chain(blockchain_id, idempotency_key=idempotency_key)

Activate a blockchain (triggers activation workflow)

Starts the asynchronous activation workflow for the blockchain identified by its ID, transitioning it towards the ACTIVATED state.

### Example


```python
from fireblocks.models.activate_blockchain_response import ActivateBlockchainResponse
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
    blockchain_id = 'blockchain_id_example' # str | Required blockchain ID to activate
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Activate a blockchain (triggers activation workflow)
        api_response = fireblocks.blockchain_link_beta.activate_blockchain_link_chain(blockchain_id, idempotency_key=idempotency_key).result()
        print("The response of BlockchainLinkBetaApi->activate_blockchain_link_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->activate_blockchain_link_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_id** | **str**| Required blockchain ID to activate | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ActivateBlockchainResponse**](ActivateBlockchainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blockchain_link_chain**
> CreateBlockchainResponse create_blockchain_link_chain(create_blockchain_request, idempotency_key=idempotency_key)

Create a new blockchain

Registers a new tenant-managed blockchain from the supplied declared properties. The blockchain starts in the CREATED state and must be activated separately before it can be used.

### Example


```python
from fireblocks.models.create_blockchain_request import CreateBlockchainRequest
from fireblocks.models.create_blockchain_response import CreateBlockchainResponse
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
    create_blockchain_request = fireblocks.CreateBlockchainRequest() # CreateBlockchainRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a new blockchain
        api_response = fireblocks.blockchain_link_beta.create_blockchain_link_chain(create_blockchain_request, idempotency_key=idempotency_key).result()
        print("The response of BlockchainLinkBetaApi->create_blockchain_link_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->create_blockchain_link_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_blockchain_request** | [**CreateBlockchainRequest**](CreateBlockchainRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateBlockchainResponse**](CreateBlockchainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blockchain_link_chain**
> delete_blockchain_link_chain(blockchain_id)

Delete a blockchain

Permanently removes a blockchain identified by its ID. The blockchain must not be in an active lifecycle state.

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
    blockchain_id = 'blockchain_id_example' # str | tenant_id is extracted from JWT token context

    try:
        # Delete a blockchain
        fireblocks.blockchain_link_beta.delete_blockchain_link_chain(blockchain_id).result()
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->delete_blockchain_link_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_id** | **str**| tenant_id is extracted from JWT token context | 

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
**204** | No Content |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_link_billing_info**
> GetBillingInfoResponse get_blockchain_link_billing_info()

Get tenant billing info

Returns the tenant's blockchain activation limit and current usage. tenant_id is derived from the JWT token context.

### Example


```python
from fireblocks.models.get_billing_info_response import GetBillingInfoResponse
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
        # Get tenant billing info
        api_response = fireblocks.blockchain_link_beta.get_blockchain_link_billing_info().result()
        print("The response of BlockchainLinkBetaApi->get_blockchain_link_billing_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->get_blockchain_link_billing_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBillingInfoResponse**](GetBillingInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_link_chain**
> GetBlockchainByIdResponse get_blockchain_link_chain(blockchain_id)

Get a blockchain by ID

Returns a single blockchain owned by the tenant, identified by its ID.

### Example


```python
from fireblocks.models.get_blockchain_by_id_response import GetBlockchainByIdResponse
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
    blockchain_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | ID of the blockchain to retrieve (supplied as a path parameter).

    try:
        # Get a blockchain by ID
        api_response = fireblocks.blockchain_link_beta.get_blockchain_link_chain(blockchain_id).result()
        print("The response of BlockchainLinkBetaApi->get_blockchain_link_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->get_blockchain_link_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_id** | **str**| ID of the blockchain to retrieve (supplied as a path parameter). | 

### Return type

[**GetBlockchainByIdResponse**](GetBlockchainByIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain_link_test_wallet_address**
> GetTestWalletAddressResponse get_blockchain_link_test_wallet_address()

Get the test wallet address

Returns the Ethereum address derived from the configured external wallet private key, used by the UI for test transfers. tenant_id is derived from the JWT token context.

### Example


```python
from fireblocks.models.get_test_wallet_address_response import GetTestWalletAddressResponse
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
        # Get the test wallet address
        api_response = fireblocks.blockchain_link_beta.get_blockchain_link_test_wallet_address().result()
        print("The response of BlockchainLinkBetaApi->get_blockchain_link_test_wallet_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->get_blockchain_link_test_wallet_address: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTestWalletAddressResponse**](GetTestWalletAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blockchain_link_chains**
> ListBlockchainsResponse2 list_blockchain_link_chains(page_cursor=page_cursor, page_size=page_size, search=search, status=status, blockchain_env=blockchain_env, sort_by=sort_by, order=order, status_exclude=status_exclude)

List blockchains with pagination and filtering

Returns the tenant's blockchains, paginated and filterable by state, network environment, and free-text search, with configurable sorting.

### Example


```python
from fireblocks.models.blockchain_environment import BlockchainEnvironment
from fireblocks.models.blockchain_sort_field import BlockchainSortField
from fireblocks.models.blockchain_state_filter import BlockchainStateFilter
from fireblocks.models.list_blockchains_response2 import ListBlockchainsResponse2
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
    page_cursor = '1' # str | tenant_id is extracted from JWT token context. Opaque cursor for the requested page. Currently encodes the 1-based page number as a decimal string (\"1\", \"2\", ...); treat as opaque on the client. Absent = first page. (optional)
    page_size = 20 # float | Maximum number of items per page. Default 20, clamped to [1, 1000]. (optional) (default to 20)
    search = 'eth' # str | Free-text search across chain and symbol name. (optional)
    status = [fireblocks.BlockchainStateFilter()] # List[BlockchainStateFilter] | Include filter (repeated query params). (optional)
    blockchain_env = fireblocks.BlockchainEnvironment() # BlockchainEnvironment | Filter by network. (optional)
    sort_by = fireblocks.BlockchainSortField() # BlockchainSortField | Sort field. Default: createdAt. (optional)
    order = DESC # str | Sort order. Default: DESC. (optional) (default to DESC)
    status_exclude = [fireblocks.BlockchainStateFilter()] # List[BlockchainStateFilter] | Exclude filter (repeated query params). (optional)

    try:
        # List blockchains with pagination and filtering
        api_response = fireblocks.blockchain_link_beta.list_blockchain_link_chains(page_cursor=page_cursor, page_size=page_size, search=search, status=status, blockchain_env=blockchain_env, sort_by=sort_by, order=order, status_exclude=status_exclude).result()
        print("The response of BlockchainLinkBetaApi->list_blockchain_link_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->list_blockchain_link_chains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| tenant_id is extracted from JWT token context. Opaque cursor for the requested page. Currently encodes the 1-based page number as a decimal string (\&quot;1\&quot;, \&quot;2\&quot;, ...); treat as opaque on the client. Absent &#x3D; first page. | [optional] 
 **page_size** | **float**| Maximum number of items per page. Default 20, clamped to [1, 1000]. | [optional] [default to 20]
 **search** | **str**| Free-text search across chain and symbol name. | [optional] 
 **status** | [**List[BlockchainStateFilter]**](BlockchainStateFilter.md)| Include filter (repeated query params). | [optional] 
 **blockchain_env** | [**BlockchainEnvironment**](.md)| Filter by network. | [optional] 
 **sort_by** | [**BlockchainSortField**](.md)| Sort field. Default: createdAt. | [optional] 
 **order** | **str**| Sort order. Default: DESC. | [optional] [default to DESC]
 **status_exclude** | [**List[BlockchainStateFilter]**](BlockchainStateFilter.md)| Exclude filter (repeated query params). | [optional] 

### Return type

[**ListBlockchainsResponse2**](ListBlockchainsResponse2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_blockchain_link_validation**
> TriggerValidationFlowResponse trigger_blockchain_link_validation(blockchain_id, idempotency_key=idempotency_key)

Trigger validation workflow

Starts the asynchronous validation workflow for a blockchain and its associated validation session.

### Example


```python
from fireblocks.models.trigger_validation_flow_response import TriggerValidationFlowResponse
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
    blockchain_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | ID of the blockchain to validate.
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Trigger validation workflow
        api_response = fireblocks.blockchain_link_beta.trigger_blockchain_link_validation(blockchain_id, idempotency_key=idempotency_key).result()
        print("The response of BlockchainLinkBetaApi->trigger_blockchain_link_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->trigger_blockchain_link_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_id** | **str**| ID of the blockchain to validate. | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TriggerValidationFlowResponse**](TriggerValidationFlowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_blockchain_link_chain**
> UpdateBlockchainResponse update_blockchain_link_chain(blockchain_id, blockchain_declared_properties, idempotency_key=idempotency_key)

Update a blockchain

Updates the declared properties of an existing blockchain identified by its ID. Only the fields supplied in the request are modified.

### Example


```python
from fireblocks.models.blockchain_declared_properties import BlockchainDeclaredProperties
from fireblocks.models.update_blockchain_response import UpdateBlockchainResponse
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
    blockchain_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | ID of the blockchain to update (supplied as a path parameter).
    blockchain_declared_properties = fireblocks.BlockchainDeclaredProperties() # BlockchainDeclaredProperties | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update a blockchain
        api_response = fireblocks.blockchain_link_beta.update_blockchain_link_chain(blockchain_id, blockchain_declared_properties, idempotency_key=idempotency_key).result()
        print("The response of BlockchainLinkBetaApi->update_blockchain_link_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainLinkBetaApi->update_blockchain_link_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_id** | **str**| ID of the blockchain to update (supplied as a path parameter). | 
 **blockchain_declared_properties** | [**BlockchainDeclaredProperties**](BlockchainDeclaredProperties.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**UpdateBlockchainResponse**](UpdateBlockchainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

