# fireblocks.VaultsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_asset_for_vault_account**](VaultsApi.md#activate_asset_for_vault_account) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/activate | Activate a wallet in a vault account
[**create_legacy_address**](VaultsApi.md#create_legacy_address) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/create_legacy | Convert a segwit address to legacy format
[**create_multiple_accounts**](VaultsApi.md#create_multiple_accounts) | **POST** /vault/accounts/bulk | Bulk creation of new vault accounts
[**create_vault_account**](VaultsApi.md#create_vault_account) | **POST** /vault/accounts | Create a new vault account
[**create_vault_account_asset**](VaultsApi.md#create_vault_account_asset) | **POST** /vault/accounts/{vaultAccountId}/{assetId} | Create a new wallet
[**create_vault_account_asset_address**](VaultsApi.md#create_vault_account_asset_address) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/addresses | Create new asset deposit address
[**get_asset_wallets**](VaultsApi.md#get_asset_wallets) | **GET** /vault/asset_wallets | List asset wallets (Paginated)
[**get_max_spendable_amount**](VaultsApi.md#get_max_spendable_amount) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/max_spendable_amount | Get the maximum spendable amount in a single transaction.
[**get_paged_vault_accounts**](VaultsApi.md#get_paged_vault_accounts) | **GET** /vault/accounts_paged | List vault accounts (Paginated)
[**get_public_key_info**](VaultsApi.md#get_public_key_info) | **GET** /vault/public_key_info | Get the public key information
[**get_public_key_info_for_address**](VaultsApi.md#get_public_key_info_for_address) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/{change}/{addressIndex}/public_key_info | Get the public key for a vault account
[**get_unspent_inputs**](VaultsApi.md#get_unspent_inputs) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/unspent_inputs | Get UTXO unspent inputs information
[**get_vault_account**](VaultsApi.md#get_vault_account) | **GET** /vault/accounts/{vaultAccountId} | Find a vault account by ID
[**get_vault_account_asset**](VaultsApi.md#get_vault_account_asset) | **GET** /vault/accounts/{vaultAccountId}/{assetId} | Get the asset balance for a vault account
[**get_vault_account_asset_addresses_paginated**](VaultsApi.md#get_vault_account_asset_addresses_paginated) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/addresses_paginated | List addresses (Paginated)
[**get_vault_assets**](VaultsApi.md#get_vault_assets) | **GET** /vault/assets | Get asset balance for chosen assets
[**get_vault_balance_by_asset**](VaultsApi.md#get_vault_balance_by_asset) | **GET** /vault/assets/{assetId} | Get vault balance by asset
[**hide_vault_account**](VaultsApi.md#hide_vault_account) | **POST** /vault/accounts/{vaultAccountId}/hide | Hide a vault account in the console
[**set_customer_ref_id_for_address**](VaultsApi.md#set_customer_ref_id_for_address) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/set_customer_ref_id | Assign AML customer reference ID
[**set_vault_account_auto_fuel**](VaultsApi.md#set_vault_account_auto_fuel) | **POST** /vault/accounts/{vaultAccountId}/set_auto_fuel | Turn autofueling on or off
[**set_vault_account_customer_ref_id**](VaultsApi.md#set_vault_account_customer_ref_id) | **POST** /vault/accounts/{vaultAccountId}/set_customer_ref_id | Set an AML/KYT customer reference ID for a vault account
[**unhide_vault_account**](VaultsApi.md#unhide_vault_account) | **POST** /vault/accounts/{vaultAccountId}/unhide | Unhide a vault account in the console
[**update_vault_account**](VaultsApi.md#update_vault_account) | **PUT** /vault/accounts/{vaultAccountId} | Rename a vault account
[**update_vault_account_asset_address**](VaultsApi.md#update_vault_account_asset_address) | **PUT** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId} | Update address description
[**update_vault_account_asset_balance**](VaultsApi.md#update_vault_account_asset_balance) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/balance | Refresh asset balance data


# **activate_asset_for_vault_account**
> CreateVaultAssetResponse activate_asset_for_vault_account(vault_account_id, asset_id, idempotency_key=idempotency_key)

Activate a wallet in a vault account

Initiates activation for a wallet in a vault account.

### Example


```python
from fireblocks.models.create_vault_asset_response import CreateVaultAssetResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return, or 'default' for the default vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Activate a wallet in a vault account
        api_response = fireblocks.vaults.activate_asset_for_vault_account(vault_account_id, asset_id, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->activate_asset_for_vault_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->activate_asset_for_vault_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return, or &#39;default&#39; for the default vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateVaultAssetResponse**](CreateVaultAssetResponse.md)

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

# **create_legacy_address**
> CreateAddressResponse create_legacy_address(vault_account_id, asset_id, address_id, idempotency_key=idempotency_key)

Convert a segwit address to legacy format

Converts an existing segwit address to the legacy format.

### Example


```python
from fireblocks.models.create_address_response import CreateAddressResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    address_id = 'address_id_example' # str | The segwit address to translate
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Convert a segwit address to legacy format
        api_response = fireblocks.vaults.create_legacy_address(vault_account_id, asset_id, address_id, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->create_legacy_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_legacy_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **address_id** | **str**| The segwit address to translate | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateAddressResponse**](CreateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created address |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_accounts**
> JobCreated create_multiple_accounts(create_multiple_accounts_request, idempotency_key=idempotency_key)

Bulk creation of new vault accounts

Create multiple vault accounts by running an async job. </br> **Note**: - These endpoints are currently in beta and might be subject to changes. - We limit accounts to 10k per operation and 200k per customer during beta testing. 

### Example


```python
from fireblocks.models.create_multiple_accounts_request import CreateMultipleAccountsRequest
from fireblocks.models.job_created import JobCreated
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
    create_multiple_accounts_request = fireblocks.CreateMultipleAccountsRequest() # CreateMultipleAccountsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Bulk creation of new vault accounts
        api_response = fireblocks.vaults.create_multiple_accounts(create_multiple_accounts_request, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->create_multiple_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_multiple_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_multiple_accounts_request** | [**CreateMultipleAccountsRequest**](CreateMultipleAccountsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**JobCreated**](JobCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JobCreated object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vault_account**
> VaultAccount create_vault_account(create_vault_account_request, idempotency_key=idempotency_key)

Create a new vault account

Creates a new vault account with the requested name.

### Example


```python
from fireblocks.models.create_vault_account_request import CreateVaultAccountRequest
from fireblocks.models.vault_account import VaultAccount
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
    create_vault_account_request = fireblocks.CreateVaultAccountRequest() # CreateVaultAccountRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a new vault account
        api_response = fireblocks.vaults.create_vault_account(create_vault_account_request, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->create_vault_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_vault_account_request** | [**CreateVaultAccountRequest**](CreateVaultAccountRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**VaultAccount**](VaultAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Vault Account object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vault_account_asset**
> CreateVaultAssetResponse create_vault_account_asset(vault_account_id, asset_id, idempotency_key=idempotency_key, create_assets_request=create_assets_request)

Create a new wallet

Creates a wallet for a specific asset in a vault account.

### Example


```python
from fireblocks.models.create_assets_request import CreateAssetsRequest
from fireblocks.models.create_vault_asset_response import CreateVaultAssetResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return, or 'default' for the default vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_assets_request = fireblocks.CreateAssetsRequest() # CreateAssetsRequest |  (optional)

    try:
        # Create a new wallet
        api_response = fireblocks.vaults.create_vault_account_asset(vault_account_id, asset_id, idempotency_key=idempotency_key, create_assets_request=create_assets_request).result()
        print("The response of VaultsApi->create_vault_account_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault_account_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return, or &#39;default&#39; for the default vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_assets_request** | [**CreateAssetsRequest**](CreateAssetsRequest.md)|  | [optional] 

### Return type

[**CreateVaultAssetResponse**](CreateVaultAssetResponse.md)

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

# **create_vault_account_asset_address**
> CreateAddressResponse create_vault_account_asset_address(vault_account_id, asset_id, idempotency_key=idempotency_key, create_address_request=create_address_request)

Create new asset deposit address

Creates a new deposit address for an asset of a vault account.

### Example


```python
from fireblocks.models.create_address_request import CreateAddressRequest
from fireblocks.models.create_address_response import CreateAddressResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_address_request = fireblocks.CreateAddressRequest() # CreateAddressRequest |  (optional)

    try:
        # Create new asset deposit address
        api_response = fireblocks.vaults.create_vault_account_asset_address(vault_account_id, asset_id, idempotency_key=idempotency_key, create_address_request=create_address_request).result()
        print("The response of VaultsApi->create_vault_account_asset_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault_account_asset_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return | 
 **asset_id** | **str**| The ID of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_address_request** | [**CreateAddressRequest**](CreateAddressRequest.md)|  | [optional] 

### Return type

[**CreateAddressResponse**](CreateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created address |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_wallets**
> PaginatedAssetWalletResponse get_asset_wallets(total_amount_larger_than=total_amount_larger_than, asset_id=asset_id, order_by=order_by, before=before, after=after, limit=limit)

List asset wallets (Paginated)

Gets all asset wallets at all of the vault accounts in your workspace. An asset wallet is an asset at a vault account. This method allows fast traversal of all account balances. 

### Example


```python
from fireblocks.models.paginated_asset_wallet_response import PaginatedAssetWalletResponse
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
    total_amount_larger_than = 3.4 # float | When specified, only asset wallets with total balance larger than this amount are returned. (optional)
    asset_id = 'asset_id_example' # str | When specified, only asset wallets cross vault accounts that have this asset ID are returned. (optional)
    order_by = 'DESC' # str |  (optional) (default to 'DESC')
    before = 'before_example' # str | Fetches the next paginated response before this element. This element is a cursor and is returned at the response of the previous page. (optional)
    after = 'after_example' # str | Fetches the next paginated response after this element. This element is a cursor and is returned at the response of the previous page. (optional)
    limit = 200 # float | The maximum number of asset wallets in a single response. The default is 200 and the maximum is 1000. (optional) (default to 200)

    try:
        # List asset wallets (Paginated)
        api_response = fireblocks.vaults.get_asset_wallets(total_amount_larger_than=total_amount_larger_than, asset_id=asset_id, order_by=order_by, before=before, after=after, limit=limit).result()
        print("The response of VaultsApi->get_asset_wallets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_asset_wallets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **total_amount_larger_than** | **float**| When specified, only asset wallets with total balance larger than this amount are returned. | [optional] 
 **asset_id** | **str**| When specified, only asset wallets cross vault accounts that have this asset ID are returned. | [optional] 
 **order_by** | **str**|  | [optional] [default to &#39;DESC&#39;]
 **before** | **str**| Fetches the next paginated response before this element. This element is a cursor and is returned at the response of the previous page. | [optional] 
 **after** | **str**| Fetches the next paginated response after this element. This element is a cursor and is returned at the response of the previous page. | [optional] 
 **limit** | **float**| The maximum number of asset wallets in a single response. The default is 200 and the maximum is 1000. | [optional] [default to 200]

### Return type

[**PaginatedAssetWalletResponse**](PaginatedAssetWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PaginatedAssetWalletResponse object |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_max_spendable_amount**
> GetMaxSpendableAmountResponse get_max_spendable_amount(vault_account_id, asset_id, manual_signging=manual_signging)

Get the maximum spendable amount in a single transaction.

Get the maximum amount of a particular asset that can be spent in a single transaction from a specified vault account (UTXO assets only, with a limitation on number of inputs embedded). Send several transactions if you want to spend more than the maximum spendable amount.

### Example


```python
from fireblocks.models.get_max_spendable_amount_response import GetMaxSpendableAmountResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account, or 'default' for the default vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    manual_signging = True # bool | False by default. The maximum number of inputs depends if the transaction will be signed by an automated co-signer server or on a mobile device. (optional)

    try:
        # Get the maximum spendable amount in a single transaction.
        api_response = fireblocks.vaults.get_max_spendable_amount(vault_account_id, asset_id, manual_signging=manual_signging).result()
        print("The response of VaultsApi->get_max_spendable_amount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_max_spendable_amount: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account, or &#39;default&#39; for the default vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **manual_signging** | **bool**| False by default. The maximum number of inputs depends if the transaction will be signed by an automated co-signer server or on a mobile device. | [optional] 

### Return type

[**GetMaxSpendableAmountResponse**](GetMaxSpendableAmountResponse.md)

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

# **get_paged_vault_accounts**
> VaultAccountsPagedResponse get_paged_vault_accounts(name_prefix=name_prefix, name_suffix=name_suffix, min_amount_threshold=min_amount_threshold, asset_id=asset_id, order_by=order_by, before=before, after=after, limit=limit)

List vault accounts (Paginated)

Gets all vault accounts in your workspace. This endpoint returns a limited amount of results with a quick response time.

### Example


```python
from fireblocks.models.vault_accounts_paged_response import VaultAccountsPagedResponse
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
    name_prefix = 'name_prefix_example' # str |  (optional)
    name_suffix = 'name_suffix_example' # str |  (optional)
    min_amount_threshold = 3.4 # float | Specifying minAmountThreshold will filter accounts with balances greater than this value, otherwise, it will return all accounts. (optional)
    asset_id = 'asset_id_example' # str |  (optional)
    order_by = 'DESC' # str |  (optional) (default to 'DESC')
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 200 # float |  (optional) (default to 200)

    try:
        # List vault accounts (Paginated)
        api_response = fireblocks.vaults.get_paged_vault_accounts(name_prefix=name_prefix, name_suffix=name_suffix, min_amount_threshold=min_amount_threshold, asset_id=asset_id, order_by=order_by, before=before, after=after, limit=limit).result()
        print("The response of VaultsApi->get_paged_vault_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_paged_vault_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_prefix** | **str**|  | [optional] 
 **name_suffix** | **str**|  | [optional] 
 **min_amount_threshold** | **float**| Specifying minAmountThreshold will filter accounts with balances greater than this value, otherwise, it will return all accounts. | [optional] 
 **asset_id** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] [default to &#39;DESC&#39;]
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] [default to 200]

### Return type

[**VaultAccountsPagedResponse**](VaultAccountsPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VaultAccountsPagedResponse object |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_key_info**
> PublicKeyInformation get_public_key_info(derivation_path, algorithm, compressed=compressed)

Get the public key information

Gets the public key information based on derivation path and signing algorithm.

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
    derivation_path = 'derivation_path_example' # str | 
    algorithm = 'algorithm_example' # str | 
    compressed = True # bool |  (optional)

    try:
        # Get the public key information
        api_response = fireblocks.vaults.get_public_key_info(derivation_path, algorithm, compressed=compressed).result()
        print("The response of VaultsApi->get_public_key_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_public_key_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **derivation_path** | **str**|  | 
 **algorithm** | **str**|  | 
 **compressed** | **bool**|  | [optional] 

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

# **get_public_key_info_for_address**
> PublicKeyInformation get_public_key_info_for_address(vault_account_id, asset_id, change, address_index, compressed=compressed)

Get the public key for a vault account

Gets the public key information for the vault account.

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
    vault_account_id = 'vault_account_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    change = 3.4 # float | 
    address_index = 3.4 # float | 
    compressed = True # bool |  (optional)

    try:
        # Get the public key for a vault account
        api_response = fireblocks.vaults.get_public_key_info_for_address(vault_account_id, asset_id, change, address_index, compressed=compressed).result()
        print("The response of VaultsApi->get_public_key_info_for_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_public_key_info_for_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**|  | 
 **asset_id** | **str**|  | 
 **change** | **float**|  | 
 **address_index** | **float**|  | 
 **compressed** | **bool**|  | [optional] 

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

# **get_unspent_inputs**
> List[UnspentInputsResponse] get_unspent_inputs(vault_account_id, asset_id)

Get UTXO unspent inputs information

Returns unspent inputs information of an asset in a vault account.

### Example


```python
from fireblocks.models.unspent_inputs_response import UnspentInputsResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Get UTXO unspent inputs information
        api_response = fireblocks.vaults.get_unspent_inputs(vault_account_id, asset_id).result()
        print("The response of VaultsApi->get_unspent_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_unspent_inputs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 

### Return type

[**List[UnspentInputsResponse]**](UnspentInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Unspent information per input |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_account**
> VaultAccount get_vault_account(vault_account_id)

Find a vault account by ID

Returns the requested vault account.

### Example


```python
from fireblocks.models.vault_account import VaultAccount
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return type: string

    try:
        # Find a vault account by ID
        api_response = fireblocks.vaults.get_vault_account(vault_account_id).result()
        print("The response of VaultsApi->get_vault_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return type: string | 

### Return type

[**VaultAccount**](VaultAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Vault Account object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_account_asset**
> VaultAsset get_vault_account_asset(vault_account_id, asset_id)

Get the asset balance for a vault account

Returns a wallet for a specific asset of a vault account.

### Example


```python
from fireblocks.models.vault_asset import VaultAsset
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Get the asset balance for a vault account
        api_response = fireblocks.vaults.get_vault_account_asset(vault_account_id, asset_id).result()
        print("The response of VaultsApi->get_vault_account_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_account_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return | 
 **asset_id** | **str**| The ID of the asset | 

### Return type

[**VaultAsset**](VaultAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VaultAsset object |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_account_asset_addresses_paginated**
> PaginatedAddressResponse get_vault_account_asset_addresses_paginated(vault_account_id, asset_id, limit=limit, before=before, after=after)

List addresses (Paginated)

Returns a paginated response of the addresses for a given vault account and asset.

### Example


```python
from fireblocks.models.paginated_address_response import PaginatedAddressResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset
    limit = 3.4 # float |  (optional)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)

    try:
        # List addresses (Paginated)
        api_response = fireblocks.vaults.get_vault_account_asset_addresses_paginated(vault_account_id, asset_id, limit=limit, before=before, after=after).result()
        print("The response of VaultsApi->get_vault_account_asset_addresses_paginated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_account_asset_addresses_paginated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return | 
 **asset_id** | **str**| The ID of the asset | 
 **limit** | **float**|  | [optional] 
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 

### Return type

[**PaginatedAddressResponse**](PaginatedAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of addresses, and pagination info. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_assets**
> List[VaultAsset] get_vault_assets(account_name_prefix=account_name_prefix, account_name_suffix=account_name_suffix)

Get asset balance for chosen assets

Gets the assets amount summary for all accounts or filtered accounts.

### Example


```python
from fireblocks.models.vault_asset import VaultAsset
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
    account_name_prefix = 'account_name_prefix_example' # str |  (optional)
    account_name_suffix = 'account_name_suffix_example' # str |  (optional)

    try:
        # Get asset balance for chosen assets
        api_response = fireblocks.vaults.get_vault_assets(account_name_prefix=account_name_prefix, account_name_suffix=account_name_suffix).result()
        print("The response of VaultsApi->get_vault_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name_prefix** | **str**|  | [optional] 
 **account_name_suffix** | **str**|  | [optional] 

### Return type

[**List[VaultAsset]**](VaultAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Amount by asset |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_balance_by_asset**
> VaultAsset get_vault_balance_by_asset(asset_id)

Get vault balance by asset

Gets the vault balance summary for an asset.

### Example


```python
from fireblocks.models.vault_asset import VaultAsset
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
    asset_id = 'asset_id_example' # str | 

    try:
        # Get vault balance by asset
        api_response = fireblocks.vaults.get_vault_balance_by_asset(asset_id).result()
        print("The response of VaultsApi->get_vault_balance_by_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_balance_by_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 

### Return type

[**VaultAsset**](VaultAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vault amount by asset |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_vault_account**
> VaultActionStatus hide_vault_account(vault_account_id, idempotency_key=idempotency_key)

Hide a vault account in the console

Hides the requested vault account from the web console view.

### Example


```python
from fireblocks.models.vault_action_status import VaultActionStatus
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
    vault_account_id = 'vault_account_id_example' # str | The vault account to hide
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Hide a vault account in the console
        api_response = fireblocks.vaults.hide_vault_account(vault_account_id, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->hide_vault_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->hide_vault_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account to hide | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**VaultActionStatus**](VaultActionStatus.md)

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

# **set_customer_ref_id_for_address**
> VaultActionStatus set_customer_ref_id_for_address(vault_account_id, asset_id, address_id, set_customer_ref_id_for_address_request, idempotency_key=idempotency_key)

Assign AML customer reference ID

Sets an AML/KYT customer reference ID for a specific address.

### Example


```python
from fireblocks.models.set_customer_ref_id_for_address_request import SetCustomerRefIdForAddressRequest
from fireblocks.models.vault_action_status import VaultActionStatus
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    address_id = 'address_id_example' # str | The address for which to add a description. For XRP, use <address>:<tag>, for all other assets, use only the address
    set_customer_ref_id_for_address_request = fireblocks.SetCustomerRefIdForAddressRequest() # SetCustomerRefIdForAddressRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Assign AML customer reference ID
        api_response = fireblocks.vaults.set_customer_ref_id_for_address(vault_account_id, asset_id, address_id, set_customer_ref_id_for_address_request, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->set_customer_ref_id_for_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->set_customer_ref_id_for_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **address_id** | **str**| The address for which to add a description. For XRP, use &lt;address&gt;:&lt;tag&gt;, for all other assets, use only the address | 
 **set_customer_ref_id_for_address_request** | [**SetCustomerRefIdForAddressRequest**](SetCustomerRefIdForAddressRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**VaultActionStatus**](VaultActionStatus.md)

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

# **set_vault_account_auto_fuel**
> VaultActionStatus set_vault_account_auto_fuel(vault_account_id, set_auto_fuel_request, idempotency_key=idempotency_key)

Turn autofueling on or off

Sets the autofueling property of the vault account to enabled or disabled.

### Example


```python
from fireblocks.models.set_auto_fuel_request import SetAutoFuelRequest
from fireblocks.models.vault_action_status import VaultActionStatus
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
    vault_account_id = 'vault_account_id_example' # str | The vault account ID
    set_auto_fuel_request = fireblocks.SetAutoFuelRequest() # SetAutoFuelRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Turn autofueling on or off
        api_response = fireblocks.vaults.set_vault_account_auto_fuel(vault_account_id, set_auto_fuel_request, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->set_vault_account_auto_fuel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->set_vault_account_auto_fuel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account ID | 
 **set_auto_fuel_request** | [**SetAutoFuelRequest**](SetAutoFuelRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**VaultActionStatus**](VaultActionStatus.md)

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

# **set_vault_account_customer_ref_id**
> VaultActionStatus set_vault_account_customer_ref_id(vault_account_id, set_customer_ref_id_request, idempotency_key=idempotency_key)

Set an AML/KYT customer reference ID for a vault account

Assigns an AML/KYT customer reference ID for the vault account.

### Example


```python
from fireblocks.models.set_customer_ref_id_request import SetCustomerRefIdRequest
from fireblocks.models.vault_action_status import VaultActionStatus
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
    vault_account_id = 'vault_account_id_example' # str | The vault account ID
    set_customer_ref_id_request = fireblocks.SetCustomerRefIdRequest() # SetCustomerRefIdRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set an AML/KYT customer reference ID for a vault account
        api_response = fireblocks.vaults.set_vault_account_customer_ref_id(vault_account_id, set_customer_ref_id_request, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->set_vault_account_customer_ref_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->set_vault_account_customer_ref_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account ID | 
 **set_customer_ref_id_request** | [**SetCustomerRefIdRequest**](SetCustomerRefIdRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**VaultActionStatus**](VaultActionStatus.md)

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

# **unhide_vault_account**
> VaultActionStatus unhide_vault_account(vault_account_id, idempotency_key=idempotency_key)

Unhide a vault account in the console

Makes a hidden vault account visible in web console view.

### Example


```python
from fireblocks.models.vault_action_status import VaultActionStatus
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
    vault_account_id = 'vault_account_id_example' # str | The vault account to unhide
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Unhide a vault account in the console
        api_response = fireblocks.vaults.unhide_vault_account(vault_account_id, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->unhide_vault_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->unhide_vault_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account to unhide | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**VaultActionStatus**](VaultActionStatus.md)

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

# **update_vault_account**
> RenameVaultAccountResponse update_vault_account(vault_account_id, update_vault_account_request, idempotency_key=idempotency_key)

Rename a vault account

Renames the requested vault account.

### Example


```python
from fireblocks.models.rename_vault_account_response import RenameVaultAccountResponse
from fireblocks.models.update_vault_account_request import UpdateVaultAccountRequest
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to edit
    update_vault_account_request = fireblocks.UpdateVaultAccountRequest() # UpdateVaultAccountRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Rename a vault account
        api_response = fireblocks.vaults.update_vault_account(vault_account_id, update_vault_account_request, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->update_vault_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->update_vault_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to edit | 
 **update_vault_account_request** | [**UpdateVaultAccountRequest**](UpdateVaultAccountRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**RenameVaultAccountResponse**](RenameVaultAccountResponse.md)

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

# **update_vault_account_asset_address**
> VaultActionStatus update_vault_account_asset_address(vault_account_id, asset_id, address_id, idempotency_key=idempotency_key, update_vault_account_asset_address_request=update_vault_account_asset_address_request)

Update address description

Updates the description of an existing address of an asset in a vault account.

### Example


```python
from fireblocks.models.update_vault_account_asset_address_request import UpdateVaultAccountAssetAddressRequest
from fireblocks.models.vault_action_status import VaultActionStatus
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    address_id = 'address_id_example' # str | The address for which to add a description. For XRP, use <address>:<tag>, for all other assets, use only the address
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    update_vault_account_asset_address_request = fireblocks.UpdateVaultAccountAssetAddressRequest() # UpdateVaultAccountAssetAddressRequest |  (optional)

    try:
        # Update address description
        api_response = fireblocks.vaults.update_vault_account_asset_address(vault_account_id, asset_id, address_id, idempotency_key=idempotency_key, update_vault_account_asset_address_request=update_vault_account_asset_address_request).result()
        print("The response of VaultsApi->update_vault_account_asset_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->update_vault_account_asset_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **address_id** | **str**| The address for which to add a description. For XRP, use &lt;address&gt;:&lt;tag&gt;, for all other assets, use only the address | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **update_vault_account_asset_address_request** | [**UpdateVaultAccountAssetAddressRequest**](UpdateVaultAccountAssetAddressRequest.md)|  | [optional] 

### Return type

[**VaultActionStatus**](VaultActionStatus.md)

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

# **update_vault_account_asset_balance**
> VaultAsset update_vault_account_asset_balance(vault_account_id, asset_id, idempotency_key=idempotency_key)

Refresh asset balance data

Updates the balance of a specific asset in a vault account.

### Example


```python
from fireblocks.models.vault_asset import VaultAsset
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Refresh asset balance data
        api_response = fireblocks.vaults.update_vault_account_asset_balance(vault_account_id, asset_id, idempotency_key=idempotency_key).result()
        print("The response of VaultsApi->update_vault_account_asset_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->update_vault_account_asset_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return | 
 **asset_id** | **str**| The ID of the asset | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**VaultAsset**](VaultAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VaultAsset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

