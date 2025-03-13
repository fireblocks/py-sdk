# fireblocks.InternalWalletsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_internal_wallet**](InternalWalletsApi.md#create_internal_wallet) | **POST** /internal_wallets | Create an internal wallet
[**create_internal_wallet_asset**](InternalWalletsApi.md#create_internal_wallet_asset) | **POST** /internal_wallets/{walletId}/{assetId} | Add an asset to an internal wallet
[**delete_internal_wallet**](InternalWalletsApi.md#delete_internal_wallet) | **DELETE** /internal_wallets/{walletId} | Delete an internal wallet
[**delete_internal_wallet_asset**](InternalWalletsApi.md#delete_internal_wallet_asset) | **DELETE** /internal_wallets/{walletId}/{assetId} | Delete a whitelisted address from an internal wallet
[**get_internal_wallet**](InternalWalletsApi.md#get_internal_wallet) | **GET** /internal_wallets/{walletId} | Get assets for internal wallet
[**get_internal_wallet_asset**](InternalWalletsApi.md#get_internal_wallet_asset) | **GET** /internal_wallets/{walletId}/{assetId} | Get an asset from an internal wallet
[**get_internal_wallets**](InternalWalletsApi.md#get_internal_wallets) | **GET** /internal_wallets | List internal wallets
[**set_customer_ref_id_for_internal_wallet**](InternalWalletsApi.md#set_customer_ref_id_for_internal_wallet) | **POST** /internal_wallets/{walletId}/set_customer_ref_id | Set an AML/KYT customer reference ID for an internal wallet


# **create_internal_wallet**
> UnmanagedWallet create_internal_wallet(idempotency_key=idempotency_key, create_wallet_request=create_wallet_request)

Create an internal wallet

Creates a new internal wallet with the requested name.

### Example


```python
from fireblocks.models.create_wallet_request import CreateWalletRequest
from fireblocks.models.unmanaged_wallet import UnmanagedWallet
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
    create_wallet_request = fireblocks.CreateWalletRequest() # CreateWalletRequest |  (optional)

    try:
        # Create an internal wallet
        api_response = fireblocks.internal_wallets.create_internal_wallet(idempotency_key=idempotency_key, create_wallet_request=create_wallet_request).result()
        print("The response of InternalWalletsApi->create_internal_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalWalletsApi->create_internal_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_wallet_request** | [**CreateWalletRequest**](CreateWalletRequest.md)|  | [optional] 

### Return type

[**UnmanagedWallet**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A new wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_internal_wallet_asset**
> WalletAsset create_internal_wallet_asset(wallet_id, asset_id, idempotency_key=idempotency_key, create_internal_wallet_asset_request=create_internal_wallet_asset_request)

Add an asset to an internal wallet

Adds an asset to an existing internal wallet.

### Example


```python
from fireblocks.models.create_internal_wallet_asset_request import CreateInternalWalletAssetRequest
from fireblocks.models.wallet_asset import WalletAsset
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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to add
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_internal_wallet_asset_request = fireblocks.CreateInternalWalletAssetRequest() # CreateInternalWalletAssetRequest |  (optional)

    try:
        # Add an asset to an internal wallet
        api_response = fireblocks.internal_wallets.create_internal_wallet_asset(wallet_id, asset_id, idempotency_key=idempotency_key, create_internal_wallet_asset_request=create_internal_wallet_asset_request).result()
        print("The response of InternalWalletsApi->create_internal_wallet_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalWalletsApi->create_internal_wallet_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the wallet | 
 **asset_id** | **str**| The ID of the asset to add | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_internal_wallet_asset_request** | [**CreateInternalWalletAssetRequest**](CreateInternalWalletAssetRequest.md)|  | [optional] 

### Return type

[**WalletAsset**](WalletAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_internal_wallet**
> delete_internal_wallet(wallet_id)

Delete an internal wallet

Deletes an internal wallet by ID.

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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet to delete

    try:
        # Delete an internal wallet
        fireblocks.internal_wallets.delete_internal_wallet(wallet_id).result()
    except Exception as e:
        print("Exception when calling InternalWalletsApi->delete_internal_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the wallet to delete | 

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
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_internal_wallet_asset**
> delete_internal_wallet_asset(wallet_id, asset_id)

Delete a whitelisted address from an internal wallet

Deletes a whitelisted address (for an asset) from an internal wallet.

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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to delete

    try:
        # Delete a whitelisted address from an internal wallet
        fireblocks.internal_wallets.delete_internal_wallet_asset(wallet_id, asset_id).result()
    except Exception as e:
        print("Exception when calling InternalWalletsApi->delete_internal_wallet_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the wallet | 
 **asset_id** | **str**| The ID of the asset to delete | 

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
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_internal_wallet**
> UnmanagedWallet get_internal_wallet(wallet_id)

Get assets for internal wallet

Returns all assets in an internal wallet by ID.

### Example


```python
from fireblocks.models.unmanaged_wallet import UnmanagedWallet
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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet to return

    try:
        # Get assets for internal wallet
        api_response = fireblocks.internal_wallets.get_internal_wallet(wallet_id).result()
        print("The response of InternalWalletsApi->get_internal_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalWalletsApi->get_internal_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the wallet to return | 

### Return type

[**UnmanagedWallet**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_internal_wallet_asset**
> WalletAsset get_internal_wallet_asset(wallet_id, asset_id)

Get an asset from an internal wallet

Returns information for an asset in an internal wallet.

### Example


```python
from fireblocks.models.wallet_asset import WalletAsset
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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to return

    try:
        # Get an asset from an internal wallet
        api_response = fireblocks.internal_wallets.get_internal_wallet_asset(wallet_id, asset_id).result()
        print("The response of InternalWalletsApi->get_internal_wallet_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalWalletsApi->get_internal_wallet_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the wallet | 
 **asset_id** | **str**| The ID of the asset to return | 

### Return type

[**WalletAsset**](WalletAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_internal_wallets**
> List[UnmanagedWallet] get_internal_wallets()

List internal wallets

Gets a list of internal wallets.

**Note**: BTC-based assets belonging to whitelisted addresses cannot be retrieved between 00:00 UTC and 00:01 UTC daily due to third-party provider, Blockchair, being unavailable for this 60 second period. Please wait until the next minute to retrieve BTC-based assets.


### Example


```python
from fireblocks.models.unmanaged_wallet import UnmanagedWallet
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
        # List internal wallets
        api_response = fireblocks.internal_wallets.get_internal_wallets().result()
        print("The response of InternalWalletsApi->get_internal_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalWalletsApi->get_internal_wallets: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UnmanagedWallet]**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of internal wallets |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_customer_ref_id_for_internal_wallet**
> set_customer_ref_id_for_internal_wallet(wallet_id, set_customer_ref_id_request, idempotency_key=idempotency_key)

Set an AML/KYT customer reference ID for an internal wallet

Sets an AML/KYT customer reference ID for the specific internal wallet.

### Example


```python
from fireblocks.models.set_customer_ref_id_request import SetCustomerRefIdRequest
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
    wallet_id = 'wallet_id_example' # str | The wallet ID
    set_customer_ref_id_request = fireblocks.SetCustomerRefIdRequest() # SetCustomerRefIdRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set an AML/KYT customer reference ID for an internal wallet
        fireblocks.internal_wallets.set_customer_ref_id_for_internal_wallet(wallet_id, set_customer_ref_id_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling InternalWalletsApi->set_customer_ref_id_for_internal_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID | 
 **set_customer_ref_id_request** | [**SetCustomerRefIdRequest**](SetCustomerRefIdRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

