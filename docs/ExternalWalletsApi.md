# fireblocks_client.ExternalWalletsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_to_external_wallet**](ExternalWalletsApi.md#add_asset_to_external_wallet) | **POST** /external_wallets/{walletId}/{assetId} | Add an asset to an external wallet.
[**create_external_wallet**](ExternalWalletsApi.md#create_external_wallet) | **POST** /external_wallets | Create an external wallet
[**delete_external_wallet**](ExternalWalletsApi.md#delete_external_wallet) | **DELETE** /external_wallets/{walletId} | Delete an external wallet
[**get_asset_in_external_wallet**](ExternalWalletsApi.md#get_asset_in_external_wallet) | **GET** /external_wallets/{walletId}/{assetId} | Get an asset from an external wallet
[**get_external_wallet_by_id**](ExternalWalletsApi.md#get_external_wallet_by_id) | **GET** /external_wallets/{walletId} | Find an external wallet
[**get_external_wallets**](ExternalWalletsApi.md#get_external_wallets) | **GET** /external_wallets | List external wallets
[**remove_asset_from_external_wallet**](ExternalWalletsApi.md#remove_asset_from_external_wallet) | **DELETE** /external_wallets/{walletId}/{assetId} | Delete an asset from an external wallet
[**set_customer_ref_id_for_external_wallet**](ExternalWalletsApi.md#set_customer_ref_id_for_external_wallet) | **POST** /external_wallets/{walletId}/set_customer_ref_id | Set an AML customer reference ID for an external wallet


# **add_asset_to_external_wallet**
> ExternalWalletAsset add_asset_to_external_wallet(wallet_id, asset_id, add_asset_to_external_wallet_request=add_asset_to_external_wallet_request)

Add an asset to an external wallet.

Adds an asset to an existing external wallet.

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to add
    add_asset_to_external_wallet_request = fireblocks_client.AddAssetToExternalWalletRequest() # AddAssetToExternalWalletRequest |  (optional)

    try:
        # Add an asset to an external wallet.
        api_response = api_instance.add_asset_to_external_wallet(wallet_id, asset_id, add_asset_to_external_wallet_request=add_asset_to_external_wallet_request)
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
 **add_asset_to_external_wallet_request** | [**AddAssetToExternalWalletRequest**](AddAssetToExternalWalletRequest.md)|  | [optional] 

### Return type

[**ExternalWalletAsset**](ExternalWalletAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_external_wallet**
> UnmanagedWallet create_external_wallet(create_internal_wallet_request=create_internal_wallet_request)

Create an external wallet

Creates a new external wallet with the requested name.

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)
    create_internal_wallet_request = fireblocks_client.CreateInternalWalletRequest() # CreateInternalWalletRequest |  (optional)

    try:
        # Create an external wallet
        api_response = api_instance.create_external_wallet(create_internal_wallet_request=create_internal_wallet_request)
        print("The response of ExternalWalletsApi->create_external_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->create_external_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_internal_wallet_request** | [**CreateInternalWalletRequest**](CreateInternalWalletRequest.md)|  | [optional] 

### Return type

[**UnmanagedWallet**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | The ID of the wallet to delete

    try:
        # Delete an external wallet
        api_instance.delete_external_wallet(wallet_id)
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

# **get_asset_in_external_wallet**
> ExternalWalletAsset get_asset_in_external_wallet(wallet_id, asset_id)

Get an asset from an external wallet

Returns an external wallet by wallet ID and asset ID.

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to return

    try:
        # Get an asset from an external wallet
        api_response = api_instance.get_asset_in_external_wallet(wallet_id, asset_id)
        print("The response of ExternalWalletsApi->get_asset_in_external_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->get_asset_in_external_wallet: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_wallet_by_id**
> UnmanagedWallet get_external_wallet_by_id(wallet_id)

Find an external wallet

Returns an external wallet by ID.

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | The ID of the wallet to return

    try:
        # Find an external wallet
        api_response = api_instance.get_external_wallet_by_id(wallet_id)
        print("The response of ExternalWalletsApi->get_external_wallet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->get_external_wallet_by_id: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_wallets**
> List[UnmanagedWallet] get_external_wallets()

List external wallets

Gets a list of external wallets under the workspace.

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)

    try:
        # List external wallets
        api_response = api_instance.get_external_wallets()
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
 - **Accept**: */*, application/json

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | The ID of the wallet
    asset_id = 'asset_id_example' # str | The ID of the asset to delete

    try:
        # Delete an asset from an external wallet
        api_instance.remove_asset_from_external_wallet(wallet_id, asset_id)
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

# **set_customer_ref_id_for_external_wallet**
> set_customer_ref_id_for_external_wallet(wallet_id, set_customer_ref_id_for_vault_account_request)

Set an AML customer reference ID for an external wallet

Sets an AML/KYT customer reference ID for the specific external wallet.

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
    api_instance = fireblocks_client.ExternalWalletsApi(api_client)
    wallet_id = 'wallet_id_example' # str | The wallet ID
    set_customer_ref_id_for_vault_account_request = fireblocks_client.SetCustomerRefIdForVaultAccountRequest() # SetCustomerRefIdForVaultAccountRequest | 

    try:
        # Set an AML customer reference ID for an external wallet
        api_instance.set_customer_ref_id_for_external_wallet(wallet_id, set_customer_ref_id_for_vault_account_request)
    except Exception as e:
        print("Exception when calling ExternalWalletsApi->set_customer_ref_id_for_external_wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The wallet ID | 
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

