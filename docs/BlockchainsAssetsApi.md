# fireblocks_client.BlockchainsAssetsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_assets**](BlockchainsAssetsApi.md#get_supported_assets) | **GET** /supported_assets | List all asset types supported by Fireblocks
[**register_new_asset**](BlockchainsAssetsApi.md#register_new_asset) | **POST** /assets | Register an asset


# **get_supported_assets**
> List[AssetTypeResponse] get_supported_assets()

List all asset types supported by Fireblocks

Returns all asset types supported by Fireblocks.

### Example


```python
import fireblocks_client
from fireblocks_client.models.asset_type_response import AssetTypeResponse
from fireblocks_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fireblocks.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fireblocks_client.Configuration(
    host = "https://api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with fireblocks_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireblocks_client.BlockchainsAssetsApi(api_client)

    try:
        # List all asset types supported by Fireblocks
        api_response = api_instance.get_supported_assets()
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

# **register_new_asset**
> AssetResponse register_new_asset(idempotency_key=idempotency_key, register_new_asset_request=register_new_asset_request)

Register an asset

Register a new asset to a workspace and return the newly created asset's details. Currently supported for EVM based chains only.

### Example


```python
import fireblocks_client
from fireblocks_client.models.asset_response import AssetResponse
from fireblocks_client.models.register_new_asset_request import RegisterNewAssetRequest
from fireblocks_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fireblocks.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fireblocks_client.Configuration(
    host = "https://api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with fireblocks_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireblocks_client.BlockchainsAssetsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    register_new_asset_request = fireblocks_client.RegisterNewAssetRequest() # RegisterNewAssetRequest |  (optional)

    try:
        # Register an asset
        api_response = api_instance.register_new_asset(idempotency_key=idempotency_key, register_new_asset_request=register_new_asset_request)
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
**400** | - Listing an asset on the requested blockchain is not supported. Error code: 1000  - The asset address is invalid. Error code: 1003  - Self serve listing an asset on the requested blockchain is currently not supported, please contact support. Error code: 1004  |  -  |
**403** | - The asset creation quota reached. Error code: 1005  |  -  |
**404** | - Invalid address, could not get asset information. Error code 1003  |  -  |
**409** | - The asset is already supported globally. Error code: 1001  - The asset has already been added to this workspace. Error code: 1002  |  -  |
**500** | Failed to create asset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

