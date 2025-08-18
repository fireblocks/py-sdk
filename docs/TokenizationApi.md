# fireblocks.TokenizationApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**burn_collection_token**](TokenizationApi.md#burn_collection_token) | **POST** /tokenization/collections/{id}/tokens/burn | Burn tokens
[**create_new_collection**](TokenizationApi.md#create_new_collection) | **POST** /tokenization/collections | Create a new collection
[**deactivate_and_unlink_adapters**](TokenizationApi.md#deactivate_and_unlink_adapters) | **DELETE** /tokenization/multichain/bridge/layerzero | Remove LayerZero adapters
[**deploy_and_link_adapters**](TokenizationApi.md#deploy_and_link_adapters) | **POST** /tokenization/multichain/bridge/layerzero | Deploy LayerZero adapters
[**fetch_collection_token_details**](TokenizationApi.md#fetch_collection_token_details) | **GET** /tokenization/collections/{id}/tokens/{tokenId} | Get collection token details
[**get_collection_by_id**](TokenizationApi.md#get_collection_by_id) | **GET** /tokenization/collections/{id} | Get a collection by id
[**get_deployable_address**](TokenizationApi.md#get_deployable_address) | **POST** /tokenization/multichain/deterministic_address | Get deterministic address for contract deployment
[**get_layer_zero_dvn_config**](TokenizationApi.md#get_layer_zero_dvn_config) | **GET** /tokenization/multichain/bridge/layerzero/config/{adapterTokenLinkId}/dvns | Get LayerZero DVN configuration
[**get_layer_zero_peers**](TokenizationApi.md#get_layer_zero_peers) | **GET** /tokenization/multichain/bridge/layerzero/config/{adapterTokenLinkId}/peers | Get LayerZero peers
[**get_linked_collections**](TokenizationApi.md#get_linked_collections) | **GET** /tokenization/collections | Get collections
[**get_linked_token**](TokenizationApi.md#get_linked_token) | **GET** /tokenization/tokens/{id} | Return a linked token
[**get_linked_tokens**](TokenizationApi.md#get_linked_tokens) | **GET** /tokenization/tokens | List all linked tokens
[**issue_new_token**](TokenizationApi.md#issue_new_token) | **POST** /tokenization/tokens | Issue a new token
[**issue_token_multi_chain**](TokenizationApi.md#issue_token_multi_chain) | **POST** /tokenization/multichain/tokens | Issue a token on one or more blockchains
[**link**](TokenizationApi.md#link) | **POST** /tokenization/tokens/link | Link a contract
[**mint_collection_token**](TokenizationApi.md#mint_collection_token) | **POST** /tokenization/collections/{id}/tokens/mint | Mint tokens
[**re_issue_token_multi_chain**](TokenizationApi.md#re_issue_token_multi_chain) | **POST** /tokenization/multichain/reissue/token/{tokenLinkId} | Reissue a multichain token
[**remove_layer_zero_peers**](TokenizationApi.md#remove_layer_zero_peers) | **DELETE** /tokenization/multichain/bridge/layerzero/config/peers | Remove LayerZero peers
[**set_layer_zero_dvn_config**](TokenizationApi.md#set_layer_zero_dvn_config) | **POST** /tokenization/multichain/bridge/layerzero/config/dvns | Set LayerZero DVN configuration
[**set_layer_zero_peers**](TokenizationApi.md#set_layer_zero_peers) | **POST** /tokenization/multichain/bridge/layerzero/config/peers | Set LayerZero peers
[**unlink**](TokenizationApi.md#unlink) | **DELETE** /tokenization/tokens/{id} | Unlink a token
[**unlink_collection**](TokenizationApi.md#unlink_collection) | **DELETE** /tokenization/collections/{id} | Delete a collection link
[**validate_layer_zero_channel_config**](TokenizationApi.md#validate_layer_zero_channel_config) | **GET** /tokenization/multichain/bridge/layerzero/validate | Validate LayerZero channel configuration


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

# **deactivate_and_unlink_adapters**
> RemoveLayerZeroAdaptersResponse deactivate_and_unlink_adapters(remove_layer_zero_adapters_request, idempotency_key=idempotency_key)

Remove LayerZero adapters

Remove LayerZero adapters by deactivating and unlinking them. This endpoint revokes roles and deactivates the specified adapter contracts.

### Example


```python
from fireblocks.models.remove_layer_zero_adapters_request import RemoveLayerZeroAdaptersRequest
from fireblocks.models.remove_layer_zero_adapters_response import RemoveLayerZeroAdaptersResponse
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
    remove_layer_zero_adapters_request = fireblocks.RemoveLayerZeroAdaptersRequest() # RemoveLayerZeroAdaptersRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Remove LayerZero adapters
        api_response = fireblocks.tokenization.deactivate_and_unlink_adapters(remove_layer_zero_adapters_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->deactivate_and_unlink_adapters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->deactivate_and_unlink_adapters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_layer_zero_adapters_request** | [**RemoveLayerZeroAdaptersRequest**](RemoveLayerZeroAdaptersRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**RemoveLayerZeroAdaptersResponse**](RemoveLayerZeroAdaptersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero adapters removal process completed |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**409** | Token link processing error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_and_link_adapters**
> List[AdapterProcessingResult] deploy_and_link_adapters(deploy_layer_zero_adapters_request, idempotency_key=idempotency_key)

Deploy LayerZero adapters

Deploy LayerZero adapters for multichain token bridging functionality. This endpoint creates adapter contracts that enable cross-chain token transfers.

### Example


```python
from fireblocks.models.adapter_processing_result import AdapterProcessingResult
from fireblocks.models.deploy_layer_zero_adapters_request import DeployLayerZeroAdaptersRequest
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
    deploy_layer_zero_adapters_request = fireblocks.DeployLayerZeroAdaptersRequest() # DeployLayerZeroAdaptersRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Deploy LayerZero adapters
        api_response = fireblocks.tokenization.deploy_and_link_adapters(deploy_layer_zero_adapters_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->deploy_and_link_adapters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->deploy_and_link_adapters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy_layer_zero_adapters_request** | [**DeployLayerZeroAdaptersRequest**](DeployLayerZeroAdaptersRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**List[AdapterProcessingResult]**](AdapterProcessingResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero adapters deployed successfully |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**409** | Token link preparation error |  -  |
**422** | Token link is not fungible |  -  |
**500** | Internal server error |  -  |

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

# **get_deployable_address**
> DeployableAddressResponse get_deployable_address(get_deployable_address_request, idempotency_key=idempotency_key)

Get deterministic address for contract deployment

Get a deterministic address for contract deployment. The address is derived from the contract's bytecode and  provided salt. This endpoint is used to get the address of a contract that will be deployed in the future.

### Example


```python
from fireblocks.models.deployable_address_response import DeployableAddressResponse
from fireblocks.models.get_deployable_address_request import GetDeployableAddressRequest
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
    get_deployable_address_request = fireblocks.GetDeployableAddressRequest() # GetDeployableAddressRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Get deterministic address for contract deployment
        api_response = fireblocks.tokenization.get_deployable_address(get_deployable_address_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->get_deployable_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_deployable_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_deployable_address_request** | [**GetDeployableAddressRequest**](GetDeployableAddressRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**DeployableAddressResponse**](DeployableAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deterministic address for contract deployment |  -  |
**400** | Invalid parameters or template has no bytecode |  -  |
**409** | Address is already taken |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layer_zero_dvn_config**
> GetLayerZeroDvnConfigResponse get_layer_zero_dvn_config(adapter_token_link_id, peer_adapter_token_link_id=peer_adapter_token_link_id)

Get LayerZero DVN configuration

Retrieve the DVN (Data Verification Network) configuration for a specific adapter. Returns DVN configurations for channels between the source adapter and its peers.

### Example


```python
from fireblocks.models.get_layer_zero_dvn_config_response import GetLayerZeroDvnConfigResponse
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
    adapter_token_link_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The token link id of the adapter token link
    peer_adapter_token_link_id = '6add4f2a-b206-4114-8f94-2882618ffbb4' # str | Optional peer adapter token link ID to filter results (optional)

    try:
        # Get LayerZero DVN configuration
        api_response = fireblocks.tokenization.get_layer_zero_dvn_config(adapter_token_link_id, peer_adapter_token_link_id=peer_adapter_token_link_id).result()
        print("The response of TokenizationApi->get_layer_zero_dvn_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_layer_zero_dvn_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adapter_token_link_id** | **str**| The token link id of the adapter token link | 
 **peer_adapter_token_link_id** | **str**| Optional peer adapter token link ID to filter results | [optional] 

### Return type

[**GetLayerZeroDvnConfigResponse**](GetLayerZeroDvnConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero DVN configuration retrieved successfully |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layer_zero_peers**
> GetLayerZeroPeersResponse get_layer_zero_peers(adapter_token_link_id)

Get LayerZero peers

Retrieve the LayerZero peers configured for a specific adapter. Returns information about peer relationships for cross-chain communication.

### Example


```python
from fireblocks.models.get_layer_zero_peers_response import GetLayerZeroPeersResponse
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
    adapter_token_link_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The token link id of the adapter token link

    try:
        # Get LayerZero peers
        api_response = fireblocks.tokenization.get_layer_zero_peers(adapter_token_link_id).result()
        print("The response of TokenizationApi->get_layer_zero_peers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->get_layer_zero_peers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adapter_token_link_id** | **str**| The token link id of the adapter token link | 

### Return type

[**GetLayerZeroPeersResponse**](GetLayerZeroPeersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero peers retrieved successfully |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**500** | Internal server error |  -  |

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

# **issue_token_multi_chain**
> List[TokenLinkDto] issue_token_multi_chain(create_multichain_token_request, idempotency_key=idempotency_key)

Issue a token on one or more blockchains

Facilitates the creation of a new token on one or more blockchains.

### Example


```python
from fireblocks.models.create_multichain_token_request import CreateMultichainTokenRequest
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
    create_multichain_token_request = fireblocks.CreateMultichainTokenRequest() # CreateMultichainTokenRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Issue a token on one or more blockchains
        api_response = fireblocks.tokenization.issue_token_multi_chain(create_multichain_token_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->issue_token_multi_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->issue_token_multi_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_multichain_token_request** | [**CreateMultichainTokenRequest**](CreateMultichainTokenRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**List[TokenLinkDto]**](TokenLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tokens were created successfully |  -  |
**400** | Invalid input. |  -  |
**409** | Address is already taken. |  -  |

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

# **re_issue_token_multi_chain**
> List[TokenLinkDto] re_issue_token_multi_chain(token_link_id, reissue_multichain_token_request, idempotency_key=idempotency_key)

Reissue a multichain token

Reissue a multichain token. This endpoint allows you to reissue a token on one or more blockchains. The token must be initially issued using the issueTokenMultiChain endpoint.

### Example


```python
from fireblocks.models.reissue_multichain_token_request import ReissueMultichainTokenRequest
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
    token_link_id = 'token_link_id_example' # str | The ID of the token link
    reissue_multichain_token_request = fireblocks.ReissueMultichainTokenRequest() # ReissueMultichainTokenRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Reissue a multichain token
        api_response = fireblocks.tokenization.re_issue_token_multi_chain(token_link_id, reissue_multichain_token_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->re_issue_token_multi_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->re_issue_token_multi_chain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_link_id** | **str**| The ID of the token link | 
 **reissue_multichain_token_request** | [**ReissueMultichainTokenRequest**](ReissueMultichainTokenRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**List[TokenLinkDto]**](TokenLinkDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully reissued multichain token |  -  |
**400** | Invalid input |  -  |
**404** | Deployed contract not found |  -  |
**409** | Address is already taken |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_layer_zero_peers**
> RemoveLayerZeroPeersResponse remove_layer_zero_peers(remove_layer_zero_peers_request, idempotency_key=idempotency_key)

Remove LayerZero peers

Remove LayerZero peers to disconnect adapter contracts. This endpoint removes peer relationships between LayerZero adapters.

### Example


```python
from fireblocks.models.remove_layer_zero_peers_request import RemoveLayerZeroPeersRequest
from fireblocks.models.remove_layer_zero_peers_response import RemoveLayerZeroPeersResponse
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
    remove_layer_zero_peers_request = fireblocks.RemoveLayerZeroPeersRequest() # RemoveLayerZeroPeersRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Remove LayerZero peers
        api_response = fireblocks.tokenization.remove_layer_zero_peers(remove_layer_zero_peers_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->remove_layer_zero_peers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->remove_layer_zero_peers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_layer_zero_peers_request** | [**RemoveLayerZeroPeersRequest**](RemoveLayerZeroPeersRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**RemoveLayerZeroPeersResponse**](RemoveLayerZeroPeersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero peers removal process completed |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**409** | Token link processing error |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_layer_zero_dvn_config**
> SetLayerZeroDvnConfigResponse set_layer_zero_dvn_config(set_layer_zero_dvn_config_request, idempotency_key=idempotency_key)

Set LayerZero DVN configuration

Configure DVN settings for LayerZero adapters. This endpoint sets up the DVN configuration for message verification between source and destination adapters.

### Example


```python
from fireblocks.models.set_layer_zero_dvn_config_request import SetLayerZeroDvnConfigRequest
from fireblocks.models.set_layer_zero_dvn_config_response import SetLayerZeroDvnConfigResponse
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
    set_layer_zero_dvn_config_request = fireblocks.SetLayerZeroDvnConfigRequest() # SetLayerZeroDvnConfigRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set LayerZero DVN configuration
        api_response = fireblocks.tokenization.set_layer_zero_dvn_config(set_layer_zero_dvn_config_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->set_layer_zero_dvn_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->set_layer_zero_dvn_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_layer_zero_dvn_config_request** | [**SetLayerZeroDvnConfigRequest**](SetLayerZeroDvnConfigRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SetLayerZeroDvnConfigResponse**](SetLayerZeroDvnConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero DVN configuration set successfully |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**409** | Token link preparation error |  -  |
**422** | Bridging protocol blockchain metadata not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_layer_zero_peers**
> SetLayerZeroPeersResponse set_layer_zero_peers(set_layer_zero_peers_request, idempotency_key=idempotency_key)

Set LayerZero peers

Set LayerZero peers to establish connections between adapter contracts. This endpoint creates peer relationships that enable cross-chain communication. It sets the destination adapter as a peer of the source adapter. If `bidirectional` is true, it also sets the source adapter as a peer of the destination adapter(s).

### Example


```python
from fireblocks.models.set_layer_zero_peers_request import SetLayerZeroPeersRequest
from fireblocks.models.set_layer_zero_peers_response import SetLayerZeroPeersResponse
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
    set_layer_zero_peers_request = fireblocks.SetLayerZeroPeersRequest() # SetLayerZeroPeersRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set LayerZero peers
        api_response = fireblocks.tokenization.set_layer_zero_peers(set_layer_zero_peers_request, idempotency_key=idempotency_key).result()
        print("The response of TokenizationApi->set_layer_zero_peers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->set_layer_zero_peers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_layer_zero_peers_request** | [**SetLayerZeroPeersRequest**](SetLayerZeroPeersRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SetLayerZeroPeersResponse**](SetLayerZeroPeersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero peers set successfully |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**409** | Token link preparation error |  -  |
**422** | Token link is not fungible |  -  |
**500** | Internal server error |  -  |

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

# **validate_layer_zero_channel_config**
> ValidateLayerZeroChannelResponse validate_layer_zero_channel_config(adapter_token_link_id, peer_adapter_token_link_id)

Validate LayerZero channel configuration

Validate the LayerZero channel configuration between adapters. This endpoint checks if the channel configuration is correct and returns any validation errors.

### Example


```python
from fireblocks.models.validate_layer_zero_channel_response import ValidateLayerZeroChannelResponse
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
    adapter_token_link_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The token link ID of the adapter
    peer_adapter_token_link_id = '6add4f2a-b206-4114-8f94-2882618ffbb4' # str | Peer adapter token link ID to validate against

    try:
        # Validate LayerZero channel configuration
        api_response = fireblocks.tokenization.validate_layer_zero_channel_config(adapter_token_link_id, peer_adapter_token_link_id).result()
        print("The response of TokenizationApi->validate_layer_zero_channel_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenizationApi->validate_layer_zero_channel_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adapter_token_link_id** | **str**| The token link ID of the adapter | 
 **peer_adapter_token_link_id** | **str**| Peer adapter token link ID to validate against | 

### Return type

[**ValidateLayerZeroChannelResponse**](ValidateLayerZeroChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerZero channel configuration validation completed |  -  |
**400** | Bad request, invalid input data or parameters |  -  |
**404** | Token link not found |  -  |
**422** | Bridging protocol blockchain metadata not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

