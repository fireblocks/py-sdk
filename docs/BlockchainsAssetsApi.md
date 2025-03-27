# fireblocks.BlockchainsAssetsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset**](BlockchainsAssetsApi.md#get_asset) | **GET** /assets/{id} | Get an asset
[**get_blockchain**](BlockchainsAssetsApi.md#get_blockchain) | **GET** /blockchains/{id} | Get an blockchain
[**get_supported_assets**](BlockchainsAssetsApi.md#get_supported_assets) | **GET** /supported_assets | List all asset types supported by Fireblocks - legacy endpoint
[**list_assets**](BlockchainsAssetsApi.md#list_assets) | **GET** /assets | List assets
[**list_blockchains**](BlockchainsAssetsApi.md#list_blockchains) | **GET** /blockchains | List blockchains
[**register_new_asset**](BlockchainsAssetsApi.md#register_new_asset) | **POST** /assets | Register an asset
[**set_asset_price**](BlockchainsAssetsApi.md#set_asset_price) | **POST** /assets/prices/{id} | Set asset price


# **get_asset**
> Asset get_asset(id, idempotency_key=idempotency_key)

Get an asset

Returns an asset by ID or legacyID.</br>

**Note**:

  - We will continue displaying and supporting the legacy ID (API ID). Since not all Fireblocks services fully support the new Assets UUID, please use only the legacy ID until further notice.


### Example


```python
from fireblocks.models.asset import Asset
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
    id = 'ETH' # str | The ID or legacyId of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Get an asset
        api_response = fireblocks.blockchains_assets.get_asset(id, idempotency_key=idempotency_key).result()
        print("The response of BlockchainsAssetsApi->get_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->get_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or legacyId of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset with requested identification |  * X-Request-ID -  <br>  |
**404** | - Asset with specified ID or legacy ID is not found. Error code 1504  |  -  |
**500** | Error occurred while getting an asset |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blockchain**
> BlockchainResponse get_blockchain(id)

Get an blockchain

Returns an blockchain by ID or legacyID.


### Example


```python
from fireblocks.models.blockchain_response import BlockchainResponse
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
    id = 'ETH' # str | The ID or legacyId of the blockchain

    try:
        # Get an blockchain
        api_response = fireblocks.blockchains_assets.get_blockchain(id).result()
        print("The response of BlockchainsAssetsApi->get_blockchain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->get_blockchain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or legacyId of the blockchain | 

### Return type

[**BlockchainResponse**](BlockchainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blockchain with requested identification |  * X-Request-ID -  <br>  |
**404** | - Blockchain with specified ID or legacy ID is not found. Error code 1505  |  -  |
**500** | Error occurred while getting an blockchain |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_assets**
> List[AssetTypeResponse] get_supported_assets()

List all asset types supported by Fireblocks - legacy endpoint

Legacy Endpoint – Retrieves all assets supported by Fireblocks in your workspace without extended information.</br>
**Note**:

  - This endpoint will remain available for the foreseeable future and is not deprecated.</br>
  - The `listAssets` endpoint provides more detailed asset information and improved performance.</br>
  - We recommend transitioning to the `listAssets` endpoint for better results.


### Example


```python
from fireblocks.models.asset_type_response import AssetTypeResponse
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
        # List all asset types supported by Fireblocks - legacy endpoint
        api_response = fireblocks.blockchains_assets.get_supported_assets().result()
        print("The response of BlockchainsAssetsApi->get_supported_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->get_supported_assets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AssetTypeResponse]**](AssetTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Transaction object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> ListAssetsResponse list_assets(blockchain_id=blockchain_id, asset_class=asset_class, symbol=symbol, scope=scope, deprecated=deprecated, page_cursor=page_cursor, page_size=page_size, idempotency_key=idempotency_key)

List assets

Retrieves all assets supported by Fireblocks in your workspace, providing extended information and enhanced performance compared to the legacy `supported_assets` endpoint.</br>
**Note**:

  - We will continue displaying and supporting the legacy ID (API ID). Since not all Fireblocks services fully support the new Assets UUID, please use only the legacy ID until further notice.</br>


### Example


```python
from fireblocks.models.asset_class import AssetClass
from fireblocks.models.asset_scope import AssetScope
from fireblocks.models.list_assets_response import ListAssetsResponse
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
    blockchain_id = '0f672204-a28b-464a-b318-a387abd3d3c7' # str | Blockchain id of the assets (optional)
    asset_class = fireblocks.AssetClass() # AssetClass | Assets class (optional)
    symbol = 'ETH' # str | Assets onchain symbol (optional)
    scope = fireblocks.AssetScope() # AssetScope | Scope of the assets (optional)
    deprecated = false # bool | Are assets deprecated (optional)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Next page cursor to fetch (optional)
    page_size = 500 # float | Items per page (optional) (default to 500)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # List assets
        api_response = fireblocks.blockchains_assets.list_assets(blockchain_id=blockchain_id, asset_class=asset_class, symbol=symbol, scope=scope, deprecated=deprecated, page_cursor=page_cursor, page_size=page_size, idempotency_key=idempotency_key).result()
        print("The response of BlockchainsAssetsApi->list_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->list_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_id** | **str**| Blockchain id of the assets | [optional] 
 **asset_class** | [**AssetClass**](.md)| Assets class | [optional] 
 **symbol** | **str**| Assets onchain symbol | [optional] 
 **scope** | [**AssetScope**](.md)| Scope of the assets | [optional] 
 **deprecated** | **bool**| Are assets deprecated | [optional] 
 **page_cursor** | **str**| Next page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page | [optional] [default to 500]
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of assets |  -  |
**500** | Error occurred while listing assets |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blockchains**
> ListBlockchainsResponse list_blockchains(protocol=protocol, deprecated=deprecated, test=test, page_cursor=page_cursor, page_size=page_size)

List blockchains

Returns all blockchains supported by Fireblocks.


### Example


```python
from fireblocks.models.list_blockchains_response import ListBlockchainsResponse
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
    protocol = 'SOL' # str | Blockchain protocol (optional)
    deprecated = false # bool | Is blockchain deprecated (optional)
    test = false # bool | Is test blockchain (optional)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to fetch (optional)
    page_size = 500 # float | Items per page (max 500) (optional) (default to 500)

    try:
        # List blockchains
        api_response = fireblocks.blockchains_assets.list_blockchains(protocol=protocol, deprecated=deprecated, test=test, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of BlockchainsAssetsApi->list_blockchains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->list_blockchains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | **str**| Blockchain protocol | [optional] 
 **deprecated** | **bool**| Is blockchain deprecated | [optional] 
 **test** | **bool**| Is test blockchain | [optional] 
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 500) | [optional] [default to 500]

### Return type

[**ListBlockchainsResponse**](ListBlockchainsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of supported blockchains |  -  |
**500** | Error occurred while listing blockchains |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_new_asset**
> AssetResponse register_new_asset(idempotency_key=idempotency_key, register_new_asset_request=register_new_asset_request)

Register an asset

Register a new asset to a workspace and return the newly created asset's details. Currently supported chains are:
- EVM based chains
- Stellar
- Algorand
- TRON
- NEAR
- Solana


### Example


```python
from fireblocks.models.asset_response import AssetResponse
from fireblocks.models.register_new_asset_request import RegisterNewAssetRequest
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
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    register_new_asset_request = fireblocks.RegisterNewAssetRequest() # RegisterNewAssetRequest |  (optional)

    try:
        # Register an asset
        api_response = fireblocks.blockchains_assets.register_new_asset(idempotency_key=idempotency_key, register_new_asset_request=register_new_asset_request).result()
        print("The response of BlockchainsAssetsApi->register_new_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->register_new_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **register_new_asset_request** | [**RegisterNewAssetRequest**](RegisterNewAssetRequest.md)|  | [optional] 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new asset has been created successfully |  -  |
**400** | - Listing an asset on the requested blockchain is not supported. Error code: 1000  - The asset address is invalid. Error code: 1003  - Self serve listing an asset on the requested blockchain is currently not supported, please contact support. Error code: 1004  - Blockchain is deprecated. Error code: 1006  - The asset&#39;s standard is not supported. Error code: 1007  - Unable to get expected metadata: decimals | name | symbol. Error code: 1010  |  -  |
**403** | - The asset creation quota reached. Error code: 1005  - Tenant is not allowed to create testnet assets. Error code: 1008  - Tenant is not allowed to create mainnet assets. Error code: 1009  |  -  |
**404** | - Invalid address, could not get asset information. Error code 1003  |  -  |
**409** | - The asset is already supported globally. Error code: 1001  - The asset has already been added to this workspace. Error code: 1002  |  -  |
**500** | Failed to create asset |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_asset_price**
> AssetPriceResponse set_asset_price(id, idempotency_key=idempotency_key, set_asset_price_request=set_asset_price_request)

Set asset price

Set asset price for the given asset id. Returns the asset price response.


### Example


```python
from fireblocks.models.asset_price_response import AssetPriceResponse
from fireblocks.models.set_asset_price_request import SetAssetPriceRequest
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
    id = 'ETH' # str | The ID of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    set_asset_price_request = fireblocks.SetAssetPriceRequest() # SetAssetPriceRequest |  (optional)

    try:
        # Set asset price
        api_response = fireblocks.blockchains_assets.set_asset_price(id, idempotency_key=idempotency_key, set_asset_price_request=set_asset_price_request).result()
        print("The response of BlockchainsAssetsApi->set_asset_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->set_asset_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **set_asset_price_request** | [**SetAssetPriceRequest**](SetAssetPriceRequest.md)|  | [optional] 

### Return type

[**AssetPriceResponse**](AssetPriceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset price has been set successfully. |  -  |
**403** | - Tenant is not allowed to set rate. Error code: 1002.  |  -  |
**404** | - Currency not found. Error code 1001  |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

