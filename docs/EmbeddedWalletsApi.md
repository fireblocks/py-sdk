# fireblocks.EmbeddedWalletsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_embedded_wallet_asset**](EmbeddedWalletsApi.md#add_embedded_wallet_asset) | **POST** /ncw/wallets/{walletId}/accounts/{accountId}/assets/{assetId} | Add asset to account
[**create_embedded_wallet**](EmbeddedWalletsApi.md#create_embedded_wallet) | **POST** /ncw/wallets | Create a new wallet
[**create_embedded_wallet_account**](EmbeddedWalletsApi.md#create_embedded_wallet_account) | **POST** /ncw/wallets/{walletId}/accounts | Create a new account
[**get_embedded_wallet**](EmbeddedWalletsApi.md#get_embedded_wallet) | **GET** /ncw/wallets/{walletId} | Get a wallet
[**get_embedded_wallet_account**](EmbeddedWalletsApi.md#get_embedded_wallet_account) | **GET** /ncw/wallets/{walletId}/accounts/{accountId} | Get a account
[**get_embedded_wallet_addresses**](EmbeddedWalletsApi.md#get_embedded_wallet_addresses) | **GET** /ncw/wallets/{walletId}/accounts/{accountId}/assets/{assetId}/addresses | Retrieve asset addresses
[**get_embedded_wallet_asset**](EmbeddedWalletsApi.md#get_embedded_wallet_asset) | **GET** /ncw/wallets/{walletId}/accounts/{accountId}/assets/{assetId} | Retrieve asset
[**get_embedded_wallet_asset_balance**](EmbeddedWalletsApi.md#get_embedded_wallet_asset_balance) | **GET** /ncw/wallets/{walletId}/accounts/{accountId}/assets/{assetId}/balance | Retrieve asset balance
[**get_embedded_wallet_device**](EmbeddedWalletsApi.md#get_embedded_wallet_device) | **GET** /ncw/wallets/{walletId}/devices/{deviceId} | Get Embedded Wallet Device
[**get_embedded_wallet_device_setup_state**](EmbeddedWalletsApi.md#get_embedded_wallet_device_setup_state) | **GET** /ncw/wallets/{walletId}/devices/{deviceId}/setup_status | Get device key setup state
[**get_embedded_wallet_latest_backup**](EmbeddedWalletsApi.md#get_embedded_wallet_latest_backup) | **GET** /ncw/wallets/{walletId}/backup/latest | Get wallet Latest Backup details
[**get_embedded_wallet_public_key_info_for_address**](EmbeddedWalletsApi.md#get_embedded_wallet_public_key_info_for_address) | **GET** /ncw/wallets/{walletId}/accounts/{accountId}/assets/{assetId}/{change}/{addressIndex}/public_key_info | Get the public key of an asset
[**get_embedded_wallet_supported_assets**](EmbeddedWalletsApi.md#get_embedded_wallet_supported_assets) | **GET** /ncw/wallets/supported_assets | Retrieve supported assets
[**get_embedded_wallets**](EmbeddedWalletsApi.md#get_embedded_wallets) | **GET** /ncw/wallets | List wallets
[**get_public_key_info_ncw**](EmbeddedWalletsApi.md#get_public_key_info_ncw) | **GET** /ncw/wallets/{walletId}/public_key_info | Get the public key for a derivation path
[**refresh_embedded_wallet_asset_balance**](EmbeddedWalletsApi.md#refresh_embedded_wallet_asset_balance) | **PUT** /ncw/wallets/{walletId}/accounts/{accountId}/assets/{assetId}/balance | Refresh asset balance


# **add_embedded_wallet_asset**
> EmbeddedWalletAddressDetails add_embedded_wallet_asset(wallet_id, account_id, asset_id, idempotency_key=idempotency_key)

Add asset to account

Get the addresses of a specific asset, under a specific account, under a specific Non Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet_address_details import EmbeddedWalletAddressDetails
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    account_id = '0' # str | The ID of the account
    asset_id = 'BTC' # str | The ID of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add asset to account
        api_response = fireblocks.embedded_wallets.add_embedded_wallet_asset(wallet_id, account_id, asset_id, idempotency_key=idempotency_key).result()
        print("The response of EmbeddedWalletsApi->add_embedded_wallet_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->add_embedded_wallet_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **account_id** | **str**| The ID of the account | 
 **asset_id** | **str**| The ID of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**EmbeddedWalletAddressDetails**](EmbeddedWalletAddressDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedded_wallet**
> EmbeddedWallet create_embedded_wallet(idempotency_key=idempotency_key)

Create a new wallet

Create new Non Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet import EmbeddedWallet
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

    try:
        # Create a new wallet
        api_response = fireblocks.embedded_wallets.create_embedded_wallet(idempotency_key=idempotency_key).result()
        print("The response of EmbeddedWalletsApi->create_embedded_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->create_embedded_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**EmbeddedWallet**](EmbeddedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Wallet created successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_embedded_wallet_account**
> EmbeddedWalletAccount create_embedded_wallet_account(wallet_id, idempotency_key=idempotency_key)

Create a new account

Create a new account under a specific Non Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet_account import EmbeddedWalletAccount
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a new account
        api_response = fireblocks.embedded_wallets.create_embedded_wallet_account(wallet_id, idempotency_key=idempotency_key).result()
        print("The response of EmbeddedWalletsApi->create_embedded_wallet_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->create_embedded_wallet_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**EmbeddedWalletAccount**](EmbeddedWalletAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Account Created |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet**
> EmbeddedWallet get_embedded_wallet(wallet_id)

Get a wallet

Get a wallet

### Example


```python
from fireblocks.models.embedded_wallet import EmbeddedWallet
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id

    try:
        # Get a wallet
        api_response = fireblocks.embedded_wallets.get_embedded_wallet(wallet_id).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 

### Return type

[**EmbeddedWallet**](EmbeddedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_account**
> EmbeddedWalletAccount get_embedded_wallet_account(wallet_id, account_id)

Get a account

Get a specific account under a specific Non Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet_account import EmbeddedWalletAccount
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | WalletId
    account_id = '0' # str | The ID of the account

    try:
        # Get a account
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_account(wallet_id, account_id).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| WalletId | 
 **account_id** | **str**| The ID of the account | 

### Return type

[**EmbeddedWalletAccount**](EmbeddedWalletAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_addresses**
> EmbeddedWalletPaginatedAddressesResponse get_embedded_wallet_addresses(wallet_id, account_id, asset_id, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, enabled=enabled)

Retrieve asset addresses

Get the addresses of a specific asset, under a specific account, under a specific Non Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet_paginated_addresses_response import EmbeddedWalletPaginatedAddressesResponse
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    account_id = '0' # str | The ID of the account
    asset_id = 'BTC' # str | The ID of the asset
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Cursor to the next page (optional)
    page_size = 10 # float | Items per page (optional)
    sort = createdAt # str | Sort by address (optional) (default to createdAt)
    order = ASC # str | Is the order ascending or descending (optional) (default to ASC)
    enabled = true # bool | Enabled (optional)

    try:
        # Retrieve asset addresses
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_addresses(wallet_id, account_id, asset_id, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, enabled=enabled).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **account_id** | **str**| The ID of the account | 
 **asset_id** | **str**| The ID of the asset | 
 **page_cursor** | **str**| Cursor to the next page | [optional] 
 **page_size** | **float**| Items per page | [optional] 
 **sort** | **str**| Sort by address | [optional] [default to createdAt]
 **order** | **str**| Is the order ascending or descending | [optional] [default to ASC]
 **enabled** | **bool**| Enabled | [optional] 

### Return type

[**EmbeddedWalletPaginatedAddressesResponse**](EmbeddedWalletPaginatedAddressesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_asset**
> EmbeddedWalletAssetResponse get_embedded_wallet_asset(wallet_id, account_id, asset_id)

Retrieve asset

Get asset under a specific account, under a specific Non Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet_asset_response import EmbeddedWalletAssetResponse
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    account_id = '0' # str | The ID of the account
    asset_id = 'BTC' # str | The ID of the asset

    try:
        # Retrieve asset
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_asset(wallet_id, account_id, asset_id).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **account_id** | **str**| The ID of the account | 
 **asset_id** | **str**| The ID of the asset | 

### Return type

[**EmbeddedWalletAssetResponse**](EmbeddedWalletAssetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_asset_balance**
> EmbeddedWalletAssetBalance get_embedded_wallet_asset_balance(wallet_id, account_id, asset_id)

Retrieve asset balance

Get balance for specific asset, under a specific account

### Example


```python
from fireblocks.models.embedded_wallet_asset_balance import EmbeddedWalletAssetBalance
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    account_id = '0' # str | The ID of the account
    asset_id = 'BTC' # str | The ID of the asset

    try:
        # Retrieve asset balance
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_asset_balance(wallet_id, account_id, asset_id).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_asset_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_asset_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **account_id** | **str**| The ID of the account | 
 **asset_id** | **str**| The ID of the asset | 

### Return type

[**EmbeddedWalletAssetBalance**](EmbeddedWalletAssetBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_device**
> EmbeddedWalletDevice get_embedded_wallet_device(wallet_id, device_id)

Get Embedded Wallet Device

Get specific device for a specific s Wallet

### Example


```python
from fireblocks.models.embedded_wallet_device import EmbeddedWalletDevice
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    device_id = '9ee1bff0-6dba-4f0c-9b75-03fe90e66fa3' # str | Device Id

    try:
        # Get Embedded Wallet Device
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_device(wallet_id, device_id).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **device_id** | **str**| Device Id | 

### Return type

[**EmbeddedWalletDevice**](EmbeddedWalletDevice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_device_setup_state**
> EmbeddedWalletDeviceKeySetupResponse get_embedded_wallet_device_setup_state(wallet_id, device_id)

Get device key setup state

Get the state of the specific device setup key under a specific Non Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet_device_key_setup_response import EmbeddedWalletDeviceKeySetupResponse
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    device_id = '9ee1bff0-6dba-4f0c-9b75-03fe90e66fa3' # str | Device Id

    try:
        # Get device key setup state
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_device_setup_state(wallet_id, device_id).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_device_setup_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_device_setup_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **device_id** | **str**| Device Id | 

### Return type

[**EmbeddedWalletDeviceKeySetupResponse**](EmbeddedWalletDeviceKeySetupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_latest_backup**
> EmbeddedWalletLatestBackupResponse get_embedded_wallet_latest_backup(wallet_id)

Get wallet Latest Backup details

Get wallet Latest Backup details, including the deviceId, and backup time

### Example


```python
from fireblocks.models.embedded_wallet_latest_backup_response import EmbeddedWalletLatestBackupResponse
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id

    try:
        # Get wallet Latest Backup details
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_latest_backup(wallet_id).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_latest_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_latest_backup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 

### Return type

[**EmbeddedWalletLatestBackupResponse**](EmbeddedWalletLatestBackupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_public_key_info_for_address**
> PublicKeyInformation get_embedded_wallet_public_key_info_for_address(x_end_user_wallet_id, wallet_id, account_id, asset_id, change, address_index, compressed=compressed)

Get the public key of an asset

Gets the public key of an asset associated with a specific account within a Non-Custodial Wallet

### Example


```python
from fireblocks.models.public_key_information import PublicKeyInformation
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
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations.
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | The ID of the Non-Custodial wallet
    account_id = '0' # str | The ID of the account
    asset_id = 'BTC' # str | The ID of the asset
    change = 0 # float | BIP44 derivation path - change value
    address_index = 0 # float | BIP44 derivation path - index value
    compressed = true # bool | Compressed/Uncompressed public key format (optional)

    try:
        # Get the public key of an asset
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_public_key_info_for_address(x_end_user_wallet_id, wallet_id, account_id, asset_id, change, address_index, compressed=compressed).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_public_key_info_for_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_public_key_info_for_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | 
 **wallet_id** | **str**| The ID of the Non-Custodial wallet | 
 **account_id** | **str**| The ID of the account | 
 **asset_id** | **str**| The ID of the asset | 
 **change** | **float**| BIP44 derivation path - change value | 
 **address_index** | **float**| BIP44 derivation path - index value | 
 **compressed** | **bool**| Compressed/Uncompressed public key format | [optional] 

### Return type

[**PublicKeyInformation**](PublicKeyInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public Key Information |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallet_supported_assets**
> EmbeddedWalletPaginatedAssetsResponse get_embedded_wallet_supported_assets(page_cursor=page_cursor, page_size=page_size, only_base_assets=only_base_assets)

Retrieve supported assets

Get all the available supported assets for the Non-Custodial Wallet

### Example


```python
from fireblocks.models.embedded_wallet_paginated_assets_response import EmbeddedWalletPaginatedAssetsResponse
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
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Next page cursor to fetch (optional)
    page_size = 200 # float | Items per page (optional) (default to 200)
    only_base_assets = true # bool | Only base assets (optional)

    try:
        # Retrieve supported assets
        api_response = fireblocks.embedded_wallets.get_embedded_wallet_supported_assets(page_cursor=page_cursor, page_size=page_size, only_base_assets=only_base_assets).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallet_supported_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallet_supported_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Next page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page | [optional] [default to 200]
 **only_base_assets** | **bool**| Only base assets | [optional] 

### Return type

[**EmbeddedWalletPaginatedAssetsResponse**](EmbeddedWalletPaginatedAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_embedded_wallets**
> EmbeddedWalletPaginatedWalletsResponse get_embedded_wallets(page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, enabled=enabled)

List wallets

Get all Non Custodial Wallets

### Example


```python
from fireblocks.models.embedded_wallet_paginated_wallets_response import EmbeddedWalletPaginatedWalletsResponse
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
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Next page cursor to fetch (optional)
    page_size = 200 # float | Items per page (optional) (default to 200)
    sort = createdAt # str | Field(s) to use for sorting (optional) (default to createdAt)
    order = ASC # str | Is the order ascending or descending (optional) (default to ASC)
    enabled = true # bool | Enabled Wallets (optional)

    try:
        # List wallets
        api_response = fireblocks.embedded_wallets.get_embedded_wallets(page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, enabled=enabled).result()
        print("The response of EmbeddedWalletsApi->get_embedded_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_embedded_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Next page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page | [optional] [default to 200]
 **sort** | **str**| Field(s) to use for sorting | [optional] [default to createdAt]
 **order** | **str**| Is the order ascending or descending | [optional] [default to ASC]
 **enabled** | **bool**| Enabled Wallets | [optional] 

### Return type

[**EmbeddedWalletPaginatedWalletsResponse**](EmbeddedWalletPaginatedWalletsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_key_info_ncw**
> PublicKeyInformation get_public_key_info_ncw(x_end_user_wallet_id, wallet_id, derivation_path, algorithm, compressed=compressed)

Get the public key for a derivation path

Gets the public key information based on derivation path and signing algorithm within a Non-Custodial Wallet

### Example


```python
from fireblocks.models.public_key_information import PublicKeyInformation
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
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations.
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | The ID of the Non-Custodial wallet
    derivation_path = '[44,0,0,0,0]' # str | An array of integers (passed as JSON stringified array) representing the full BIP44 derivation path of the requested public key.  The first element must always be 44. 
    algorithm = 'MPC_EDDSA_ED25519' # str | Elliptic Curve
    compressed = true # bool | Compressed/Uncompressed public key format (optional)

    try:
        # Get the public key for a derivation path
        api_response = fireblocks.embedded_wallets.get_public_key_info_ncw(x_end_user_wallet_id, wallet_id, derivation_path, algorithm, compressed=compressed).result()
        print("The response of EmbeddedWalletsApi->get_public_key_info_ncw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_public_key_info_ncw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | 
 **wallet_id** | **str**| The ID of the Non-Custodial wallet | 
 **derivation_path** | **str**| An array of integers (passed as JSON stringified array) representing the full BIP44 derivation path of the requested public key.  The first element must always be 44.  | 
 **algorithm** | **str**| Elliptic Curve | 
 **compressed** | **bool**| Compressed/Uncompressed public key format | [optional] 

### Return type

[**PublicKeyInformation**](PublicKeyInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public key information |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_embedded_wallet_asset_balance**
> EmbeddedWalletAssetBalance refresh_embedded_wallet_asset_balance(wallet_id, account_id, asset_id, idempotency_key=idempotency_key)

Refresh asset balance

Refresh the balance of an asset in a specific account

### Example


```python
from fireblocks.models.embedded_wallet_asset_balance import EmbeddedWalletAssetBalance
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | Wallet Id
    account_id = '0' # str | The ID of the account
    asset_id = 'BTC' # str | The ID of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Refresh asset balance
        api_response = fireblocks.embedded_wallets.refresh_embedded_wallet_asset_balance(wallet_id, account_id, asset_id, idempotency_key=idempotency_key).result()
        print("The response of EmbeddedWalletsApi->refresh_embedded_wallet_asset_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->refresh_embedded_wallet_asset_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| Wallet Id | 
 **account_id** | **str**| The ID of the account | 
 **asset_id** | **str**| The ID of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**EmbeddedWalletAssetBalance**](EmbeddedWalletAssetBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

