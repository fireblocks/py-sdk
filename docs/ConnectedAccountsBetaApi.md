# fireblocks.ConnectedAccountsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connected_account**](ConnectedAccountsBetaApi.md#get_connected_account) | **GET** /connected_accounts/{accountId} | Get connected account
[**get_connected_account_balances**](ConnectedAccountsBetaApi.md#get_connected_account_balances) | **GET** /connected_accounts/{accountId}/balances | Get balances for an account
[**get_connected_account_rates**](ConnectedAccountsBetaApi.md#get_connected_account_rates) | **GET** /connected_accounts/{accountId}/rates | Get exchange rates for an account
[**get_connected_account_trading_pairs**](ConnectedAccountsBetaApi.md#get_connected_account_trading_pairs) | **GET** /connected_accounts/{accountId}/manifest/capabilities/trading/pairs | Get supported trading pairs for an account
[**get_connected_accounts**](ConnectedAccountsBetaApi.md#get_connected_accounts) | **GET** /connected_accounts | Get connected accounts


# **get_connected_account**
> ConnectedSingleAccountResponse get_connected_account(account_id)

Get connected account

Retrieve detailed information about a specific connected account by ID. </br>
**Note**:
- This endpoint is currently in beta and might be subject to changes.


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

# **get_connected_account_balances**
> ConnectedAccountBalancesResponse get_connected_account_balances(account_id, page_size=page_size, page_cursor=page_cursor)

Get balances for an account

Retrieve current asset balances for a specific connected account as a flat list (one row per assetId, balanceType)
 </br>
 **Note**:
 - This endpoint is currently in beta and might be subject to changes.


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

Retrieve all asset trading pairs supported by a specific connected account, including the pair type (quote, market, onOffRamp).

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

Returns all connected accounts </br>
**Note**:
- This endpoint is currently in beta and might be subject to changes.


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

