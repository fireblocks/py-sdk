# fireblocks.BlockchainsAssetsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_by_id**](BlockchainsAssetsBetaApi.md#get_asset_by_id) | **GET** /assets/{id} | Get an asset
[**get_blockchain_by_id**](BlockchainsAssetsBetaApi.md#get_blockchain_by_id) | **GET** /blockchains/{id} | Get an blockchain
[**list_assets**](BlockchainsAssetsBetaApi.md#list_assets) | **GET** /assets | List assets
[**list_blockchains**](BlockchainsAssetsBetaApi.md#list_blockchains) | **GET** /blockchains | List blockchains


# **get_asset_by_id**
> AssetResponseBeta get_asset_by_id(id, idempotency_key=idempotency_key)

Get an asset

Returns an asset by ID or legacyID.</br>

**Note**:
- This endpoint is now in Beta, disabled for general availability at this time.


### Example


```python
from fireblocks.models.asset_response_beta import AssetResponseBeta
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
        api_response = fireblocks.blockchains_assets_beta.get_asset_by_id(id, idempotency_key=idempotency_key).result()
        print("The response of BlockchainsAssetsBetaApi->get_asset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsBetaApi->get_asset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or legacyId of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AssetResponseBeta**](AssetResponseBeta.md)

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

# **get_blockchain_by_id**
> BlockchainResponse get_blockchain_by_id(id)

Get an blockchain

Returns an blockchain by ID or legacyID.</br>

**Note**:
- This endpoint is now in Beta, disabled for general availability at this time.


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
        api_response = fireblocks.blockchains_assets_beta.get_blockchain_by_id(id).result()
        print("The response of BlockchainsAssetsBetaApi->get_blockchain_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsBetaApi->get_blockchain_by_id: %s\n" % e)
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

# **list_assets**
> ListAssetsResponse list_assets(blockchain_id=blockchain_id, asset_class=asset_class, symbol=symbol, scope=scope, deprecated=deprecated, page_cursor=page_cursor, page_size=page_size, idempotency_key=idempotency_key)

List assets

Returns all asset type supported by Fireblocks.</br>

**Note**:
- This endpoint is now in Beta, disabled for general availability at this time.


### Example


```python
from fireblocks.models.asset_class_beta import AssetClassBeta
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
    asset_class = fireblocks.AssetClassBeta() # AssetClassBeta | Assets class (optional)
    symbol = 'ETH' # str | Assets onchain symbol (optional)
    scope = 'Global' # str | Scope of the assets (optional)
    deprecated = false # bool | Are assets deprecated (optional)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Next page cursor to fetch (optional)
    page_size = 500 # float | Items per page (optional) (default to 500)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # List assets
        api_response = fireblocks.blockchains_assets_beta.list_assets(blockchain_id=blockchain_id, asset_class=asset_class, symbol=symbol, scope=scope, deprecated=deprecated, page_cursor=page_cursor, page_size=page_size, idempotency_key=idempotency_key).result()
        print("The response of BlockchainsAssetsBetaApi->list_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsBetaApi->list_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_id** | **str**| Blockchain id of the assets | [optional] 
 **asset_class** | [**AssetClassBeta**](.md)| Assets class | [optional] 
 **symbol** | **str**| Assets onchain symbol | [optional] 
 **scope** | **str**| Scope of the assets | [optional] 
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

Returns all blockchains supported by Fireblocks.</br>

**Note**:
- This endpoint is now in Beta, disabled for general availability at this time.


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
        api_response = fireblocks.blockchains_assets_beta.list_blockchains(protocol=protocol, deprecated=deprecated, test=test, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of BlockchainsAssetsBetaApi->list_blockchains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsBetaApi->list_blockchains: %s\n" % e)
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

