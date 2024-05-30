# fireblocks_client.ExternalWalletsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_to_external_wallet**](ExternalWalletsApi.md#add_asset_to_external_wallet) | **POST** /external_wallets/{walletId}/{assetId} | Add an asset to an external wallet.
[**create_external_wallet**](ExternalWalletsApi.md#create_external_wallet) | **POST** /external_wallets | Create an external wallet
[**delete_external_wallet**](ExternalWalletsApi.md#delete_external_wallet) | **DELETE** /external_wallets/{walletId} | Delete an external wallet
[**get_external_wallet**](ExternalWalletsApi.md#get_external_wallet) | **GET** /external_wallets/{walletId} | Find an external wallet
[**get_external_wallet_asset**](ExternalWalletsApi.md#get_external_wallet_asset) | **GET** /external_wallets/{walletId}/{assetId} | Get an asset from an external wallet
[**get_external_wallets**](ExternalWalletsApi.md#get_external_wallets) | **GET** /external_wallets | List external wallets
[**remove_asset_from_external_wallet**](ExternalWalletsApi.md#remove_asset_from_external_wallet) | **DELETE** /external_wallets/{walletId}/{assetId} | Delete an asset from an external wallet
[**set_external_wallet_customer_ref_id**](ExternalWalletsApi.md#set_external_wallet_customer_ref_id) | **POST** /external_wallets/{walletId}/set_customer_ref_id | Set an AML customer reference ID for an external wallet


# **add_asset_to_external_wallet**
> ExternalWalletAsset add_asset_to_external_wallet(wallet_id, asset_id, idempotency_key=idempotency_key, add_asset_to_external_wallet_request=add_asset_to_external_wallet_request)

Add an asset to an external wallet.

Adds an asset to an existing external wallet.

### Example


```python
from fireblocks_client.models.add_asset_to_external_wallet_request import AddAssetToExternalWalletRequest
from fireblocks_client.models.external_wallet_asset import ExternalWalletAsset
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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to add
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    add_asset_to_external_wallet_request = fireblocks_client.AddAssetToExternalWalletRequest() # AddAssetToExternalWalletRequest |  (optional)

    try:
        # Add an asset to an external wallet.
        api_response = fireblocks.external_wallets.add_asset_to_external_wallet(wallet_id, asset_id, idempotency_key=idempotency_key, add_asset_to_external_wallet_request=add_asset_to_external_wallet_request).result()
        print("The response of ExternalWalletsApi->add_asset_to_external_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->add_asset_to_external_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the wallet | 
 **asset_id** | **str**| The ID of the asset to add | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **add_asset_to_external_wallet_request** | [**AddAssetToExternalWalletRequest**](AddAssetToExternalWalletRequest.md)|  | [optional] 

### Return type

[**ExternalWalletAsset**](ExternalWalletAsset.md)

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

# **create_external_wallet**
> UnmanagedWallet create_external_wallet(idempotency_key=idempotency_key, create_wallet_request=create_wallet_request)

Create an external wallet

Creates a new external wallet with the requested name.

### Example


```python
from fireblocks_client.models.create_wallet_request import CreateWalletRequest
from fireblocks_client.models.unmanaged_wallet import UnmanagedWallet
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
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_wallet_request = fireblocks_client.CreateWalletRequest() # CreateWalletRequest |  (optional)

    try:
        # Create an external wallet
        api_response = fireblocks.external_wallets.create_external_wallet(idempotency_key=idempotency_key, create_wallet_request=create_wallet_request).result()
        print("The response of ExternalWalletsApi->create_external_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->create_external_wallet: %s\n" % e)
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
**200** | A Wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_wallet**
> delete_external_wallet(wallet_id)

Delete an external wallet

Deletes an external wallet by ID.

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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet to delete

    try:
        # Delete an external wallet
        fireblocks.external_wallets.delete_external_wallet(wallet_id).result()
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->delete_external_wallet: %s\n" % e)
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

# **get_external_wallet**
> UnmanagedWallet get_external_wallet(wallet_id)

Find an external wallet

Returns an external wallet by ID.

### Example


```python
from fireblocks_client.models.unmanaged_wallet import UnmanagedWallet
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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet to return

    try:
        # Find an external wallet
        api_response = fireblocks.external_wallets.get_external_wallet(wallet_id).result()
        print("The response of ExternalWalletsApi->get_external_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->get_external_wallet: %s\n" % e)
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

# **get_external_wallet_asset**
> ExternalWalletAsset get_external_wallet_asset(wallet_id, asset_id)

Get an asset from an external wallet

Returns an external wallet by wallet ID and asset ID.

### Example


```python
from fireblocks_client.models.external_wallet_asset import ExternalWalletAsset
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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to return

    try:
        # Get an asset from an external wallet
        api_response = fireblocks.external_wallets.get_external_wallet_asset(wallet_id, asset_id).result()
        print("The response of ExternalWalletsApi->get_external_wallet_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->get_external_wallet_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the wallet | 
 **asset_id** | **str**| The ID of the asset to return | 

### Return type

[**ExternalWalletAsset**](ExternalWalletAsset.md)

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

# **get_external_wallets**
> List[UnmanagedWallet] get_external_wallets()

List external wallets

Gets a list of external wallets under the workspace.

### Example


```python
from fireblocks_client.models.unmanaged_wallet import UnmanagedWallet
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

    try:
        # List external wallets
        api_response = fireblocks.external_wallets.get_external_wallets().result()
        print("The response of ExternalWalletsApi->get_external_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->get_external_wallets: %s\n" % e)
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
**200** | A list of external wallets |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_from_external_wallet**
> remove_asset_from_external_wallet(wallet_id, asset_id)

Delete an asset from an external wallet

Deletes an external wallet asset by ID.

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
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to delete

    try:
        # Delete an asset from an external wallet
        fireblocks.external_wallets.remove_asset_from_external_wallet(wallet_id, asset_id).result()
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->remove_asset_from_external_wallet: %s\n" % e)
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

# **set_external_wallet_customer_ref_id**
> set_external_wallet_customer_ref_id(wallet_id, set_customer_ref_id_request, idempotency_key=idempotency_key)

Set an AML customer reference ID for an external wallet

Sets an AML/KYT customer reference ID for the specific external wallet.

### Example


```python
from fireblocks_client.models.set_customer_ref_id_request import SetCustomerRefIdRequest
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
    wallet_id = 'wallet_id_example' # str | The wallet ID
    set_customer_ref_id_request = fireblocks_client.SetCustomerRefIdRequest() # SetCustomerRefIdRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set an AML customer reference ID for an external wallet
        fireblocks.external_wallets.set_external_wallet_customer_ref_id(wallet_id, set_customer_ref_id_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->set_external_wallet_customer_ref_id: %s\n" % e)
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

