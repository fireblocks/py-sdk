# fireblocks_client.VaultsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_asset_for_vault_account**](VaultsApi.md#activate_asset_for_vault_account) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/activate | Activate a wallet in a vault account
[**create_legacy_address_for_vault_account_asset**](VaultsApi.md#create_legacy_address_for_vault_account_asset) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/create_legacy | Convert a segwit address to legacy format
[**create_vault_account**](VaultsApi.md#create_vault_account) | **POST** /vault/accounts | Create a new vault account
[**create_vault_account_asset**](VaultsApi.md#create_vault_account_asset) | **POST** /vault/accounts/{vaultAccountId}/{assetId} | Create a new wallet
[**create_vault_account_asset_address**](VaultsApi.md#create_vault_account_asset_address) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/addresses | Create new asset deposit address
[**get_asset_wallets**](VaultsApi.md#get_asset_wallets) | **GET** /vault/asset_wallets | List asset wallets (Paginated)
[**get_max_spendable_amount**](VaultsApi.md#get_max_spendable_amount) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/max_spendable_amount | Get the maximum spendable amount in a single transaction.
[**get_paged_vault_accounts**](VaultsApi.md#get_paged_vault_accounts) | **GET** /vault/accounts_paged | List vault acounts (Paginated)
[**get_public_key_info**](VaultsApi.md#get_public_key_info) | **GET** /vault/public_key_info/ | Get the public key information
[**get_public_key_info_for_address**](VaultsApi.md#get_public_key_info_for_address) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/{change}/{addressIndex}/public_key_info | Get the public key for a vault account
[**get_vault_account_asset**](VaultsApi.md#get_vault_account_asset) | **GET** /vault/accounts/{vaultAccountId}/{assetId} | Get the asset balance for a vault account
[**get_vault_account_asset_addresses**](VaultsApi.md#get_vault_account_asset_addresses) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/addresses | Get asset addresses
[**get_vault_account_asset_unspent_inputs**](VaultsApi.md#get_vault_account_asset_unspent_inputs) | **GET** /vault/accounts/{vaultAccountId}/{assetId}/unspent_inputs | Get UTXO unspent inputs information
[**get_vault_account_by_id**](VaultsApi.md#get_vault_account_by_id) | **GET** /vault/accounts/{vaultAccountId} | Find a vault account by ID
[**get_vault_accounts**](VaultsApi.md#get_vault_accounts) | **GET** /vault/accounts | List vault accounts
[**get_vault_asset_by_id**](VaultsApi.md#get_vault_asset_by_id) | **GET** /vault/assets/{assetId} | Get vault balance by asset
[**get_vault_assets**](VaultsApi.md#get_vault_assets) | **GET** /vault/assets | Get asset balance for chosen assets
[**hide_vault_account**](VaultsApi.md#hide_vault_account) | **POST** /vault/accounts/{vaultAccountId}/hide | Hide a vault account in the console
[**set_auto_fuel_for_vault_account**](VaultsApi.md#set_auto_fuel_for_vault_account) | **POST** /vault/accounts/{vaultAccountId}/set_auto_fuel | Turn autofueling on or off
[**set_customer_ref_id_for_vault_account**](VaultsApi.md#set_customer_ref_id_for_vault_account) | **POST** /vault/accounts/{vaultAccountId}/set_customer_ref_id | Set an AML/KYT customer reference ID for a vault account
[**set_customer_ref_id_for_vault_account_asset_address**](VaultsApi.md#set_customer_ref_id_for_vault_account_asset_address) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/set_customer_ref_id | Assign AML customer reference ID
[**unhide_vault_account**](VaultsApi.md#unhide_vault_account) | **POST** /vault/accounts/{vaultAccountId}/unhide | Unhide a vault account in the console
[**update_vault_account**](VaultsApi.md#update_vault_account) | **PUT** /vault/accounts/{vaultAccountId} | Rename a vault account
[**update_vault_account_asset_address**](VaultsApi.md#update_vault_account_asset_address) | **PUT** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId} | Update address description
[**update_vault_account_asset_balance**](VaultsApi.md#update_vault_account_asset_balance) | **POST** /vault/accounts/{vaultAccountId}/{assetId}/balance | Refresh asset balance data


# **activate_asset_for_vault_account**
> CreateVaultAssetResponse activate_asset_for_vault_account(vault_account_id, asset_id)

Activate a wallet in a vault account

Initiates activation for a wallet in a vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return, or 'default' for the default vault account
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Activate a wallet in a vault account
        api_response = api_instance.activate_asset_for_vault_account(vault_account_id, asset_id)
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

### Return type

[**CreateVaultAssetResponse**](CreateVaultAssetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_legacy_address_for_vault_account_asset**
> CreateAddressResponse create_legacy_address_for_vault_account_asset(vault_account_id, asset_id, address_id)

Convert a segwit address to legacy format

Converts an existing segwit address to the legacy format.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    address_id = 'address_id_example' # str | The segwit address to translate

    try:
        # Convert a segwit address to legacy format
        api_response = api_instance.create_legacy_address_for_vault_account_asset(vault_account_id, asset_id, address_id)
        print("The response of VaultsApi->create_legacy_address_for_vault_account_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_legacy_address_for_vault_account_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **address_id** | **str**| The segwit address to translate | 

### Return type

[**CreateAddressResponse**](CreateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created address |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vault_account**
> VaultAccount create_vault_account(create_vault_account_request)

Create a new vault account

Creates a new vault account with the requested name.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    create_vault_account_request = fireblocks_client.CreateVaultAccountRequest() # CreateVaultAccountRequest | 

    try:
        # Create a new vault account
        api_response = api_instance.create_vault_account(create_vault_account_request)
        print("The response of VaultsApi->create_vault_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_vault_account_request** | [**CreateVaultAccountRequest**](CreateVaultAccountRequest.md)|  | 

### Return type

[**VaultAccount**](VaultAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Vault Account object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vault_account_asset**
> CreateVaultAssetResponse create_vault_account_asset(vault_account_id, asset_id, create_vault_account_asset_request=create_vault_account_asset_request)

Create a new wallet

Creates a wallet for a specific asset in a vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return, or 'default' for the default vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    create_vault_account_asset_request = fireblocks_client.CreateVaultAccountAssetRequest() # CreateVaultAccountAssetRequest |  (optional)

    try:
        # Create a new wallet
        api_response = api_instance.create_vault_account_asset(vault_account_id, asset_id, create_vault_account_asset_request=create_vault_account_asset_request)
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
 **create_vault_account_asset_request** | [**CreateVaultAccountAssetRequest**](CreateVaultAccountAssetRequest.md)|  | [optional] 

### Return type

[**CreateVaultAssetResponse**](CreateVaultAssetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vault_account_asset_address**
> CreateAddressResponse create_vault_account_asset_address(vault_account_id, asset_id, create_vault_account_asset_address_request=create_vault_account_asset_address_request)

Create new asset deposit address

Creates a new deposit address for an asset of a vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset
    create_vault_account_asset_address_request = fireblocks_client.CreateVaultAccountAssetAddressRequest() # CreateVaultAccountAssetAddressRequest |  (optional)

    try:
        # Create new asset deposit address
        api_response = api_instance.create_vault_account_asset_address(vault_account_id, asset_id, create_vault_account_asset_address_request=create_vault_account_asset_address_request)
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
 **create_vault_account_asset_address_request** | [**CreateVaultAccountAssetAddressRequest**](CreateVaultAccountAssetAddressRequest.md)|  | [optional] 

### Return type

[**CreateAddressResponse**](CreateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created address |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_wallets**
> PaginatedAssetWalletResponse get_asset_wallets(total_amount_larger_than=total_amount_larger_than, asset_id=asset_id, before=before, after=after, limit=limit)

List asset wallets (Paginated)

Gets all asset wallets at all of the vault accounts in your workspace. An asset wallet is an asset at a vault account. This method allows fast traversal of all account balances. **Note:**   - This API endpoint is in limited availability and available for selected customers. If you would like to get early access to this endpoint, please reach out to [Fireblocks Support](https://support.fireblocks.io/hc/en-us/requests/new?ticket_form_id=36000337220)   - This API call is subject to [rate limits](https://developers.fireblocks.com/reference/rate-limiting). 

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    total_amount_larger_than = 3.4 # float | When specified, only asset wallets with total balance larger than this amount are returned. (optional)
    asset_id = 'asset_id_example' # str | When specified, only asset wallets cross vault accounts that have this asset ID are returned. (optional)
    before = 'before_example' # str | Fetches the next paginated response before this element. This element is a cursor and is returned at the response of the previous page. (optional)
    after = 'after_example' # str | Fetches the next paginated response after this element. This element is a cursor and is returned at the response of the previous page. (optional)
    limit = 200 # float | The maximum number of asset wallets in a single response. The default is 200 and the maximum is 1000. (optional) (default to 200)

    try:
        # List asset wallets (Paginated)
        api_response = api_instance.get_asset_wallets(total_amount_larger_than=total_amount_larger_than, asset_id=asset_id, before=before, after=after, limit=limit)
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
 **before** | **str**| Fetches the next paginated response before this element. This element is a cursor and is returned at the response of the previous page. | [optional] 
 **after** | **str**| Fetches the next paginated response after this element. This element is a cursor and is returned at the response of the previous page. | [optional] 
 **limit** | **float**| The maximum number of asset wallets in a single response. The default is 200 and the maximum is 1000. | [optional] [default to 200]

### Return type

[**PaginatedAssetWalletResponse**](PaginatedAssetWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PaginatedAssetWalletResponse object |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_max_spendable_amount**
> get_max_spendable_amount(vault_account_id, asset_id, manual_signging=manual_signging)

Get the maximum spendable amount in a single transaction.

Get the maximum amount of a particular asset that can be spent in a single transaction from a specified vault account (UTXO assets only, with a limitation on number of inputs embedded). Send several transactions if you want to spend more than the maximum spendable amount.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account, or 'default' for the default vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    manual_signging = True # bool | False by default. The maximum number of inputs depends if the transaction will be signed by an automated co-signer server or on a mobile device. (optional)

    try:
        # Get the maximum spendable amount in a single transaction.
        api_instance.get_max_spendable_amount(vault_account_id, asset_id, manual_signging=manual_signging)
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

void (empty response body)

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
> VaultAccountsPagedResponse get_paged_vault_accounts(name_prefix=name_prefix, name_suffix=name_suffix, min_amount_threshold=min_amount_threshold, asset_id=asset_id, max_bip44_address_index_used=max_bip44_address_index_used, max_bip44_change_address_index_used=max_bip44_change_address_index_used, order_by=order_by, before=before, after=after, limit=limit)

List vault acounts (Paginated)

Gets all vault accounts in your workspace. This endpoint returns a limited amount of results with a quick response time.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    name_prefix = 'name_prefix_example' # str |  (optional)
    name_suffix = 'name_suffix_example' # str |  (optional)
    min_amount_threshold = 3.4 # float |  (optional)
    asset_id = 'asset_id_example' # str |  (optional)
    max_bip44_address_index_used = 3.4 # float |  (optional)
    max_bip44_change_address_index_used = 3.4 # float |  (optional)
    order_by = 'DESC' # str |  (optional) (default to 'DESC')
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)
    limit = 200 # float |  (optional) (default to 200)

    try:
        # List vault acounts (Paginated)
        api_response = api_instance.get_paged_vault_accounts(name_prefix=name_prefix, name_suffix=name_suffix, min_amount_threshold=min_amount_threshold, asset_id=asset_id, max_bip44_address_index_used=max_bip44_address_index_used, max_bip44_change_address_index_used=max_bip44_change_address_index_used, order_by=order_by, before=before, after=after, limit=limit)
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
 **min_amount_threshold** | **float**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **max_bip44_address_index_used** | **float**|  | [optional] 
 **max_bip44_change_address_index_used** | **float**|  | [optional] 
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
 - **Accept**: */*

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
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    derivation_path = 'derivation_path_example' # str | 
    algorithm = 'algorithm_example' # str | 
    compressed = True # bool |  (optional)

    try:
        # Get the public key information
        api_response = api_instance.get_public_key_info(derivation_path, algorithm, compressed=compressed)
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
 - **Accept**: */*, application/json

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
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | 
    asset_id = 'asset_id_example' # str | 
    change = 3.4 # float | 
    address_index = 3.4 # float | 
    compressed = True # bool |  (optional)

    try:
        # Get the public key for a vault account
        api_response = api_instance.get_public_key_info_for_address(vault_account_id, asset_id, change, address_index, compressed=compressed)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public Key Information |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_account_asset**
> VaultAsset get_vault_account_asset(vault_account_id, asset_id)

Get the asset balance for a vault account

Returns a wallet for a specific asset of a vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Get the asset balance for a vault account
        api_response = api_instance.get_vault_account_asset(vault_account_id, asset_id)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VaultAsset object |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_account_asset_addresses**
> List[VaultWalletAddress] get_vault_account_asset_addresses(vault_account_id, asset_id)

Get asset addresses

Lists all addresses for specific asset of vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Get asset addresses
        api_response = api_instance.get_vault_account_asset_addresses(vault_account_id, asset_id)
        print("The response of VaultsApi->get_vault_account_asset_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_account_asset_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to return | 
 **asset_id** | **str**| The ID of the asset | 

### Return type

[**List[VaultWalletAddress]**](VaultWalletAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of deposit addresses |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_account_asset_unspent_inputs**
> List[UnspentInputsResponse] get_vault_account_asset_unspent_inputs(vault_account_id, asset_id)

Get UTXO unspent inputs information

Returns unspent inputs information of an asset in a vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Get UTXO unspent inputs information
        api_response = api_instance.get_vault_account_asset_unspent_inputs(vault_account_id, asset_id)
        print("The response of VaultsApi->get_vault_account_asset_unspent_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_account_asset_unspent_inputs: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Unspent information per input |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_account_by_id**
> VaultAccount get_vault_account_by_id(vault_account_id)

Find a vault account by ID

Returns the requested vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return type: string

    try:
        # Find a vault account by ID
        api_response = api_instance.get_vault_account_by_id(vault_account_id)
        print("The response of VaultsApi->get_vault_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_account_by_id: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Vault Account object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_accounts**
> List[VaultAccount] get_vault_accounts(name_prefix=name_prefix, name_suffix=name_suffix, min_amount_threshold=min_amount_threshold, asset_id=asset_id, max_bip44_address_index_used=max_bip44_address_index_used, max_bip44_change_address_index_used=max_bip44_change_address_index_used)

List vault accounts

Gets all vault accounts in your workspace.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    name_prefix = 'name_prefix_example' # str |  (optional)
    name_suffix = 'name_suffix_example' # str |  (optional)
    min_amount_threshold = 3.4 # float |  (optional)
    asset_id = 'asset_id_example' # str |  (optional)
    max_bip44_address_index_used = 3.4 # float |  (optional)
    max_bip44_change_address_index_used = 3.4 # float |  (optional)

    try:
        # List vault accounts
        api_response = api_instance.get_vault_accounts(name_prefix=name_prefix, name_suffix=name_suffix, min_amount_threshold=min_amount_threshold, asset_id=asset_id, max_bip44_address_index_used=max_bip44_address_index_used, max_bip44_change_address_index_used=max_bip44_change_address_index_used)
        print("The response of VaultsApi->get_vault_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_prefix** | **str**|  | [optional] 
 **name_suffix** | **str**|  | [optional] 
 **min_amount_threshold** | **float**|  | [optional] 
 **asset_id** | **str**|  | [optional] 
 **max_bip44_address_index_used** | **float**|  | [optional] 
 **max_bip44_change_address_index_used** | **float**|  | [optional] 

### Return type

[**List[VaultAccount]**](VaultAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of vault accounts |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_asset_by_id**
> VaultAsset get_vault_asset_by_id(asset_id)

Get vault balance by asset

Gets the vault balance summary for an asset.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    asset_id = 'asset_id_example' # str | 

    try:
        # Get vault balance by asset
        api_response = api_instance.get_vault_asset_by_id(asset_id)
        print("The response of VaultsApi->get_vault_asset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault_asset_by_id: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vault amount by asset |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault_assets**
> List[VaultAsset] get_vault_assets(account_name_prefix=account_name_prefix, account_name_suffix=account_name_suffix)

Get asset balance for chosen assets

Gets the assets amount summary for all accounts or filtered accounts.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    account_name_prefix = 'account_name_prefix_example' # str |  (optional)
    account_name_suffix = 'account_name_suffix_example' # str |  (optional)

    try:
        # Get asset balance for chosen assets
        api_response = api_instance.get_vault_assets(account_name_prefix=account_name_prefix, account_name_suffix=account_name_suffix)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Amount by asset |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_vault_account**
> hide_vault_account(vault_account_id)

Hide a vault account in the console

Hides the requested vault account from the web console view.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The vault account to hide

    try:
        # Hide a vault account in the console
        api_instance.hide_vault_account(vault_account_id)
    except Exception as e:
        print("Exception when calling VaultsApi->hide_vault_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account to hide | 

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

# **set_auto_fuel_for_vault_account**
> set_auto_fuel_for_vault_account(vault_account_id, set_auto_fuel_for_vault_account_request)

Turn autofueling on or off

Sets the autofueling property of the vault account to enabled or disabled.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The vault account ID
    set_auto_fuel_for_vault_account_request = fireblocks_client.SetAutoFuelForVaultAccountRequest() # SetAutoFuelForVaultAccountRequest | 

    try:
        # Turn autofueling on or off
        api_instance.set_auto_fuel_for_vault_account(vault_account_id, set_auto_fuel_for_vault_account_request)
    except Exception as e:
        print("Exception when calling VaultsApi->set_auto_fuel_for_vault_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account ID | 
 **set_auto_fuel_for_vault_account_request** | [**SetAutoFuelForVaultAccountRequest**](SetAutoFuelForVaultAccountRequest.md)|  | 

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

# **set_customer_ref_id_for_vault_account**
> set_customer_ref_id_for_vault_account(vault_account_id, set_customer_ref_id_for_vault_account_request)

Set an AML/KYT customer reference ID for a vault account

Assigns an AML/KYT customer reference ID for the vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The vault account ID
    set_customer_ref_id_for_vault_account_request = fireblocks_client.SetCustomerRefIdForVaultAccountRequest() # SetCustomerRefIdForVaultAccountRequest | 

    try:
        # Set an AML/KYT customer reference ID for a vault account
        api_instance.set_customer_ref_id_for_vault_account(vault_account_id, set_customer_ref_id_for_vault_account_request)
    except Exception as e:
        print("Exception when calling VaultsApi->set_customer_ref_id_for_vault_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account ID | 
 **set_customer_ref_id_for_vault_account_request** | [**SetCustomerRefIdForVaultAccountRequest**](SetCustomerRefIdForVaultAccountRequest.md)|  | 

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

# **set_customer_ref_id_for_vault_account_asset_address**
> set_customer_ref_id_for_vault_account_asset_address(vault_account_id, asset_id, address_id, set_customer_ref_id_for_vault_account_request)

Assign AML customer reference ID

Sets an AML/KYT customer reference ID for a specific address.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    address_id = 'address_id_example' # str | The address for which to add a description. For XRP, use <address>:<tag>, for all other assets, use only the address
    set_customer_ref_id_for_vault_account_request = fireblocks_client.SetCustomerRefIdForVaultAccountRequest() # SetCustomerRefIdForVaultAccountRequest | 

    try:
        # Assign AML customer reference ID
        api_instance.set_customer_ref_id_for_vault_account_asset_address(vault_account_id, asset_id, address_id, set_customer_ref_id_for_vault_account_request)
    except Exception as e:
        print("Exception when calling VaultsApi->set_customer_ref_id_for_vault_account_asset_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **address_id** | **str**| The address for which to add a description. For XRP, use &lt;address&gt;:&lt;tag&gt;, for all other assets, use only the address | 
 **set_customer_ref_id_for_vault_account_request** | [**SetCustomerRefIdForVaultAccountRequest**](SetCustomerRefIdForVaultAccountRequest.md)|  | 

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

# **unhide_vault_account**
> unhide_vault_account(vault_account_id)

Unhide a vault account in the console

Makes a hidden vault account visible in web console view.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The vault account to unhide

    try:
        # Unhide a vault account in the console
        api_instance.unhide_vault_account(vault_account_id)
    except Exception as e:
        print("Exception when calling VaultsApi->unhide_vault_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The vault account to unhide | 

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

# **update_vault_account**
> update_vault_account(vault_account_id, update_vault_account_request)

Rename a vault account

Renames the requested vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to edit
    update_vault_account_request = fireblocks_client.UpdateVaultAccountRequest() # UpdateVaultAccountRequest | 

    try:
        # Rename a vault account
        api_instance.update_vault_account(vault_account_id, update_vault_account_request)
    except Exception as e:
        print("Exception when calling VaultsApi->update_vault_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account to edit | 
 **update_vault_account_request** | [**UpdateVaultAccountRequest**](UpdateVaultAccountRequest.md)|  | 

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

# **update_vault_account_asset_address**
> update_vault_account_asset_address(vault_account_id, asset_id, address_id, update_vault_account_asset_address_request=update_vault_account_asset_address_request)

Update address description

Updates the description of an existing address of an asset in a vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    address_id = 'address_id_example' # str | The address for which to add a description. For XRP, use <address>:<tag>, for all other assets, use only the address
    update_vault_account_asset_address_request = fireblocks_client.UpdateVaultAccountAssetAddressRequest() # UpdateVaultAccountAssetAddressRequest |  (optional)

    try:
        # Update address description
        api_instance.update_vault_account_asset_address(vault_account_id, asset_id, address_id, update_vault_account_asset_address_request=update_vault_account_asset_address_request)
    except Exception as e:
        print("Exception when calling VaultsApi->update_vault_account_asset_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **address_id** | **str**| The address for which to add a description. For XRP, use &lt;address&gt;:&lt;tag&gt;, for all other assets, use only the address | 
 **update_vault_account_asset_address_request** | [**UpdateVaultAccountAssetAddressRequest**](UpdateVaultAccountAssetAddressRequest.md)|  | [optional] 

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

# **update_vault_account_asset_balance**
> VaultAsset update_vault_account_asset_balance(vault_account_id, asset_id, body=body)

Refresh asset balance data

Updates the balance of a specific asset in a vault account.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.VaultsApi(api_client)
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account to return
    asset_id = 'asset_id_example' # str | The ID of the asset
    body = None # object |  (optional)

    try:
        # Refresh asset balance data
        api_response = api_instance.update_vault_account_asset_balance(vault_account_id, asset_id, body=body)
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
 **body** | **object**|  | [optional] 

### Return type

[**VaultAsset**](VaultAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A VaultAsset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

