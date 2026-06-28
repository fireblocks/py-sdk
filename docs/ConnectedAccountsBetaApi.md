# fireblocks.ConnectedAccountsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connected_account**](ConnectedAccountsBetaApi.md#create_connected_account) | **POST** /connected_accounts | Create a connected account
[**disconnect_connected_account**](ConnectedAccountsBetaApi.md#disconnect_connected_account) | **DELETE** /connected_accounts/{accountId} | Disconnect connected account
[**get_connected_account**](ConnectedAccountsBetaApi.md#get_connected_account) | **GET** /connected_accounts/{accountId} | Get connected account
[**get_connected_account_allowlist**](ConnectedAccountsBetaApi.md#get_connected_account_allowlist) | **GET** /connected_accounts/{accountId}/allowlist | Get allowlist for connected account
[**get_connected_account_allowlist_entry**](ConnectedAccountsBetaApi.md#get_connected_account_allowlist_entry) | **GET** /connected_accounts/{accountId}/allowlist/{allowlistId} | Get a single allowlist entry for a connected account
[**get_connected_account_balances**](ConnectedAccountsBetaApi.md#get_connected_account_balances) | **GET** /connected_accounts/{accountId}/balances | Get balances for an account
[**get_connected_account_rates**](ConnectedAccountsBetaApi.md#get_connected_account_rates) | **GET** /connected_accounts/{accountId}/rates | Get exchange rates for an account
[**get_connected_account_trading_pairs**](ConnectedAccountsBetaApi.md#get_connected_account_trading_pairs) | **GET** /connected_accounts/{accountId}/manifest/capabilities/trading/pairs | Get supported trading pairs for an account
[**get_connected_accounts**](ConnectedAccountsBetaApi.md#get_connected_accounts) | **GET** /connected_accounts | Get connected accounts
[**rename_connected_account**](ConnectedAccountsBetaApi.md#rename_connected_account) | **POST** /connected_accounts/{accountId}/rename | Rename Connected Account
[**sync_connected_account_allowlist**](ConnectedAccountsBetaApi.md#sync_connected_account_allowlist) | **POST** /connected_accounts/{accountId}/allowlist/sync | Sync allowlist for connected account


# **create_connected_account**
> CreateConnectedAccountResponse create_connected_account(create_connected_account_request, idempotency_key=idempotency_key)

Create a connected account

Creates a new connected account for the authenticated tenant.

The `creds` field must be a Base64-encoded RSA-encrypted credential blob.
Use `GET /exchange_accounts/credentials_public_key` to retrieve the public key for encryption.

The `providerType` is derived server-side from the `providerId` — callers do not supply it.

Endpoint Permission: Editor, Admin, Non-Signing Admin.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.create_connected_account_request import CreateConnectedAccountRequest
from fireblocks.models.create_connected_account_response import CreateConnectedAccountResponse
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
    create_connected_account_request = fireblocks.CreateConnectedAccountRequest() # CreateConnectedAccountRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a connected account
        api_response = fireblocks.connected_accounts_beta.create_connected_account(create_connected_account_request, idempotency_key=idempotency_key).result()
        print("The response of ConnectedAccountsBetaApi->create_connected_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->create_connected_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connected_account_request** | [**CreateConnectedAccountRequest**](CreateConnectedAccountRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateConnectedAccountResponse**](CreateConnectedAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Account created (or pending approval). |  * X-Request-ID -  <br>  |
**400** | Bad request — invalid field or provider constraints violated. |  * X-Request-ID -  <br>  |
**401** | Unauthorized. Missing / invalid JWT token, or insufficient role (Editor or higher required). |  * X-Request-ID -  <br>  |
**403** | Feature not enabled for this tenant. |  * X-Request-ID -  <br>  |
**404** | mainAccountId not found. |  * X-Request-ID -  <br>  |
**422** | Invalid credentials. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_connected_account**
> disconnect_connected_account(account_id)

Disconnect connected account

Disconnect a connected account by ID.

**Note**:
- This endpoint is currently in beta and might be subject to changes.


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
    account_id = 'account_id_example' # str | The ID of the account to disconnect.

    try:
        # Disconnect connected account
        fireblocks.connected_accounts_beta.disconnect_connected_account(account_id).result()
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->disconnect_connected_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to disconnect. | 

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
**204** | Account disconnected successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_account**
> ConnectedSingleAccountResponse get_connected_account(account_id)

Get connected account

Retrieve detailed information about a specific connected account by ID.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.connected_single_account_response import ConnectedSingleAccountResponse
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
    account_id = 'account_id_example' # str | The ID of the account to fetch.

    try:
        # Get connected account
        api_response = fireblocks.connected_accounts_beta.get_connected_account(account_id).result()
        print("The response of ConnectedAccountsBetaApi->get_connected_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->get_connected_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to fetch. | 

### Return type

[**ConnectedSingleAccountResponse**](ConnectedSingleAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_account_allowlist**
> AllowlistResponse get_connected_account_allowlist(account_id, status=status, asset_id=asset_id, network_id=network_id, address=address, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get allowlist for connected account

Retrieves the address allowlist for a specified connected account.

**Note:** This endpoint is currently in beta and might be subject to changes. Currently supports CoinbaseExchange/Binance accounts only.


### Example


```python
from fireblocks.models.allowlist_entry_status import AllowlistEntryStatus
from fireblocks.models.allowlist_response import AllowlistResponse
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
    account_id = 'account_id_example' # str | The connected account identifier
    status = fireblocks.AllowlistEntryStatus() # AllowlistEntryStatus | Filter by allowlist entry status (optional)
    asset_id = 'asset_id_example' # str | Filter by Fireblocks asset ID.  See [List assets](https://developers.fireblocks.com/reference/listassets) for the canonical list of Fireblocks asset IDs.  (optional)
    network_id = 'network_id_example' # str | Filter by Fireblocks network ID.  See [List blockchains](https://developers.fireblocks.com/reference/listblockchains) for the canonical list of Fireblocks blockchain identifiers.  (optional)
    address = 'address_example' # str | Filter by specific address (optional)
    page_cursor = 'page_cursor_example' # str | Pagination cursor for next page (optional)
    page_size = 56 # int | Maximum number of entries to return (optional)
    sort_by = addedAt # str | Field to sort results by. (optional) (default to addedAt)
    order = DESC # str | Sort order (ASC or DESC). (optional) (default to DESC)

    try:
        # Get allowlist for connected account
        api_response = fireblocks.connected_accounts_beta.get_connected_account_allowlist(account_id, status=status, asset_id=asset_id, network_id=network_id, address=address, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of ConnectedAccountsBetaApi->get_connected_account_allowlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->get_connected_account_allowlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The connected account identifier | 
 **status** | [**AllowlistEntryStatus**](.md)| Filter by allowlist entry status | [optional] 
 **asset_id** | **str**| Filter by Fireblocks asset ID.  See [List assets](https://developers.fireblocks.com/reference/listassets) for the canonical list of Fireblocks asset IDs.  | [optional] 
 **network_id** | **str**| Filter by Fireblocks network ID.  See [List blockchains](https://developers.fireblocks.com/reference/listblockchains) for the canonical list of Fireblocks blockchain identifiers.  | [optional] 
 **address** | **str**| Filter by specific address | [optional] 
 **page_cursor** | **str**| Pagination cursor for next page | [optional] 
 **page_size** | **int**| Maximum number of entries to return | [optional] 
 **sort_by** | **str**| Field to sort results by. | [optional] [default to addedAt]
 **order** | **str**| Sort order (ASC or DESC). | [optional] [default to DESC]

### Return type

[**AllowlistResponse**](AllowlistResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Allowlist entries response |  * X-Request-ID -  <br>  |
**404** | Connected account not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_account_allowlist_entry**
> AllowlistEntryResponse get_connected_account_allowlist_entry(account_id, allowlist_id)

Get a single allowlist entry for a connected account

Retrieves a single allowlist entry by its Fireblocks identifier for a specified connected account.

**Note:** This endpoint is currently in beta and might be subject to changes. Currently supports CoinbaseExchange/Binance accounts only.


### Example


```python
from fireblocks.models.allowlist_entry_response import AllowlistEntryResponse
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
    account_id = 'account_id_example' # str | The connected account identifier
    allowlist_id = 'allowlist_id_example' # str | The Fireblocks allowlist entry identifier

    try:
        # Get a single allowlist entry for a connected account
        api_response = fireblocks.connected_accounts_beta.get_connected_account_allowlist_entry(account_id, allowlist_id).result()
        print("The response of ConnectedAccountsBetaApi->get_connected_account_allowlist_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->get_connected_account_allowlist_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The connected account identifier | 
 **allowlist_id** | **str**| The Fireblocks allowlist entry identifier | 

### Return type

[**AllowlistEntryResponse**](AllowlistEntryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Allowlist entry response |  * X-Request-ID -  <br>  |
**404** | Connected account or allowlist entry not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_account_balances**
> ConnectedAccountBalancesResponse get_connected_account_balances(account_id, page_size=page_size, page_cursor=page_cursor)

Get balances for an account

Retrieve current asset balances for a specific connected account as a flat list (one row per `assetId`, `balanceType`).

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.connected_account_balances_response import ConnectedAccountBalancesResponse
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
    account_id = 'account_id_example' # str | The ID of the account to fetch balances for.
    page_size = 56 # int | Page size for pagination. (optional)
    page_cursor = 'page_cursor_example' # str | Page cursor for pagination. (optional)

    try:
        # Get balances for an account
        api_response = fireblocks.connected_accounts_beta.get_connected_account_balances(account_id, page_size=page_size, page_cursor=page_cursor).result()
        print("The response of ConnectedAccountsBetaApi->get_connected_account_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->get_connected_account_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to fetch balances for. | 
 **page_size** | **int**| Page size for pagination. | [optional] 
 **page_cursor** | **str**| Page cursor for pagination. | [optional] 

### Return type

[**ConnectedAccountBalancesResponse**](ConnectedAccountBalancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account balances response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_account_rates**
> ConnectedAccountRateResponse get_connected_account_rates(account_id, base_asset_id, quote_asset_id)

Get exchange rates for an account

Retrieve current exchange rates for converting between specific assets in a connected account.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.connected_account_rate_response import ConnectedAccountRateResponse
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
    account_id = 'account_id_example' # str | The ID of the account to fetch rates for.
    base_asset_id = 'base_asset_id_example' # str | The ID of the asset to fetch rates for.
    quote_asset_id = 'quote_asset_id_example' # str | The ID of the asset to get the rates nominally.

    try:
        # Get exchange rates for an account
        api_response = fireblocks.connected_accounts_beta.get_connected_account_rates(account_id, base_asset_id, quote_asset_id).result()
        print("The response of ConnectedAccountsBetaApi->get_connected_account_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->get_connected_account_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to fetch rates for. | 
 **base_asset_id** | **str**| The ID of the asset to fetch rates for. | 
 **quote_asset_id** | **str**| The ID of the asset to get the rates nominally. | 

### Return type

[**ConnectedAccountRateResponse**](ConnectedAccountRateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rates response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_account_trading_pairs**
> ConnectedAccountTradingPairsResponse get_connected_account_trading_pairs(account_id, page_size=page_size, page_cursor=page_cursor)

Get supported trading pairs for an account

Retrieve all asset trading pairs supported by a specific connected account, including the pair type (`quote`, `market`, `onOffRamp`).

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.connected_account_trading_pairs_response import ConnectedAccountTradingPairsResponse
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
    account_id = 'account_id_example' # str | The ID of the account to fetch supported pairs for.
    page_size = 100 # int | Page size for pagination. (optional) (default to 100)
    page_cursor = 'page_cursor_example' # str | Page cursor for pagination. (optional)

    try:
        # Get supported trading pairs for an account
        api_response = fireblocks.connected_accounts_beta.get_connected_account_trading_pairs(account_id, page_size=page_size, page_cursor=page_cursor).result()
        print("The response of ConnectedAccountsBetaApi->get_connected_account_trading_pairs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->get_connected_account_trading_pairs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the account to fetch supported pairs for. | 
 **page_size** | **int**| Page size for pagination. | [optional] [default to 100]
 **page_cursor** | **str**| Page cursor for pagination. | [optional] 

### Return type

[**ConnectedAccountTradingPairsResponse**](ConnectedAccountTradingPairsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported pairs response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connected_accounts**
> ConnectedAccountsResponse get_connected_accounts(main_accounts=main_accounts, page_size=page_size, page_cursor=page_cursor)

Get connected accounts

Returns all connected accounts.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.connected_accounts_response import ConnectedAccountsResponse
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
    main_accounts = False # bool | Whether to include only main accounts in the response. (optional) (default to False)
    page_size = 56 # int | Page size for pagination. (optional)
    page_cursor = 'page_cursor_example' # str | Page cursor for pagination. (optional)

    try:
        # Get connected accounts
        api_response = fireblocks.connected_accounts_beta.get_connected_accounts(main_accounts=main_accounts, page_size=page_size, page_cursor=page_cursor).result()
        print("The response of ConnectedAccountsBetaApi->get_connected_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->get_connected_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_accounts** | **bool**| Whether to include only main accounts in the response. | [optional] [default to False]
 **page_size** | **int**| Page size for pagination. | [optional] 
 **page_cursor** | **str**| Page cursor for pagination. | [optional] 

### Return type

[**ConnectedAccountsResponse**](ConnectedAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get accounts response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_connected_account**
> RenameConnectedAccountResponse rename_connected_account(account_id, rename_connected_account_request, idempotency_key=idempotency_key)

Rename Connected Account

Rename a connected account by account ID.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.rename_connected_account_request import RenameConnectedAccountRequest
from fireblocks.models.rename_connected_account_response import RenameConnectedAccountResponse
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
    account_id = 'account_id_example' # str | The unique identifier of the connected account
    rename_connected_account_request = fireblocks.RenameConnectedAccountRequest() # RenameConnectedAccountRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Rename Connected Account
        api_response = fireblocks.connected_accounts_beta.rename_connected_account(account_id, rename_connected_account_request, idempotency_key=idempotency_key).result()
        print("The response of ConnectedAccountsBetaApi->rename_connected_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->rename_connected_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The unique identifier of the connected account | 
 **rename_connected_account_request** | [**RenameConnectedAccountRequest**](RenameConnectedAccountRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**RenameConnectedAccountResponse**](RenameConnectedAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully renamed connected account. |  * X-Request-ID -  <br>  |
**400** | Bad request. Missing tenantId, accountId, or accountName. |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**403** | Failed to rename connected account. |  -  |
**404** | Connected account not found |  -  |
**409** | Conflict. Account name is already in use by another account. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_connected_account_allowlist**
> sync_connected_account_allowlist(account_id, idempotency_key=idempotency_key)

Sync allowlist for connected account

Triggers an on-demand sync from the exchange, bypassing the cache and fetching live data immediately.

**Rate limit:** 1 request per minute per connected account.

**Note:** This endpoint is currently in beta and might be subject to changes. Currently supports CoinbaseExchange/Binance accounts only.


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
    account_id = 'account_id_example' # str | The connected account identifier
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Sync allowlist for connected account
        fireblocks.connected_accounts_beta.sync_connected_account_allowlist(account_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling ConnectedAccountsBetaApi->sync_connected_account_allowlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The connected account identifier | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**202** | Sync request accepted and processing |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

