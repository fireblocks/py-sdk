# fireblocks.ExchangeAccountsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_exchange_account**](ExchangeAccountsApi.md#add_exchange_account) | **POST** /exchange_accounts | Add an exchange account
[**convert_assets**](ExchangeAccountsApi.md#convert_assets) | **POST** /exchange_accounts/{exchangeAccountId}/convert | Convert exchange account funds from the source asset to the destination asset.
[**get_exchange_account**](ExchangeAccountsApi.md#get_exchange_account) | **GET** /exchange_accounts/{exchangeAccountId} | Find a specific exchange account
[**get_exchange_account_asset**](ExchangeAccountsApi.md#get_exchange_account_asset) | **GET** /exchange_accounts/{exchangeAccountId}/{assetId} | Find an asset for an exchange account
[**get_exchange_accounts_credentials_public_key**](ExchangeAccountsApi.md#get_exchange_accounts_credentials_public_key) | **GET** /exchange_accounts/credentials_public_key | Get public key to encrypt exchange credentials
[**get_paged_exchange_accounts**](ExchangeAccountsApi.md#get_paged_exchange_accounts) | **GET** /exchange_accounts/paged | Pagination list exchange accounts
[**internal_transfer**](ExchangeAccountsApi.md#internal_transfer) | **POST** /exchange_accounts/{exchangeAccountId}/internal_transfer | Internal transfer for exchange accounts


# **add_exchange_account**
> AddExchangeAccountResponse add_exchange_account(add_exchange_account_request, idempotency_key=idempotency_key)

Add an exchange account

Add an exchange account to exchanges.

### Example


```python
from fireblocks.models.add_exchange_account_request import AddExchangeAccountRequest
from fireblocks.models.add_exchange_account_response import AddExchangeAccountResponse
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
    add_exchange_account_request = fireblocks.AddExchangeAccountRequest() # AddExchangeAccountRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add an exchange account
        api_response = fireblocks.exchange_accounts.add_exchange_account(add_exchange_account_request, idempotency_key=idempotency_key).result()
        print("The response of ExchangeAccountsApi->add_exchange_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->add_exchange_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_exchange_account_request** | [**AddExchangeAccountRequest**](AddExchangeAccountRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AddExchangeAccountResponse**](AddExchangeAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An Exchange Account identifier object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_assets**
> ConvertAssetsResponse convert_assets(exchange_account_id, idempotency_key=idempotency_key, convert_assets_request=convert_assets_request)

Convert exchange account funds from the source asset to the destination asset.

Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.

### Example


```python
from fireblocks.models.convert_assets_request import ConvertAssetsRequest
from fireblocks.models.convert_assets_response import ConvertAssetsResponse
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
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account. Please make sure the exchange supports conversions. To find the ID of your exchange account, use GET/exchange_accounts.
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    convert_assets_request = fireblocks.ConvertAssetsRequest() # ConvertAssetsRequest |  (optional)

    try:
        # Convert exchange account funds from the source asset to the destination asset.
        api_response = fireblocks.exchange_accounts.convert_assets(exchange_account_id, idempotency_key=idempotency_key, convert_assets_request=convert_assets_request).result()
        print("The response of ExchangeAccountsApi->convert_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->convert_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_account_id** | **str**| The ID of the exchange account. Please make sure the exchange supports conversions. To find the ID of your exchange account, use GET/exchange_accounts. | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **convert_assets_request** | [**ConvertAssetsRequest**](ConvertAssetsRequest.md)|  | [optional] 

### Return type

[**ConvertAssetsResponse**](ConvertAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion successful |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_account**
> ExchangeAccount get_exchange_account(exchange_account_id)

Find a specific exchange account

Returns an exchange account by ID.

### Example


```python
from fireblocks.models.exchange_account import ExchangeAccount
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
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account to return

    try:
        # Find a specific exchange account
        api_response = fireblocks.exchange_accounts.get_exchange_account(exchange_account_id).result()
        print("The response of ExchangeAccountsApi->get_exchange_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_account_id** | **str**| The ID of the exchange account to return | 

### Return type

[**ExchangeAccount**](ExchangeAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExchangeAccount object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_account_asset**
> ExchangeAsset get_exchange_account_asset(exchange_account_id, asset_id)

Find an asset for an exchange account

Returns an asset for an exchange account.

### Example


```python
from fireblocks.models.exchange_asset import ExchangeAsset
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
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account to return
    asset_id = 'asset_id_example' # str | The ID of the asset to return

    try:
        # Find an asset for an exchange account
        api_response = fireblocks.exchange_accounts.get_exchange_account_asset(exchange_account_id, asset_id).result()
        print("The response of ExchangeAccountsApi->get_exchange_account_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_account_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_account_id** | **str**| The ID of the exchange account to return | 
 **asset_id** | **str**| The ID of the asset to return | 

### Return type

[**ExchangeAsset**](ExchangeAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExchangeAccountAsset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_accounts_credentials_public_key**
> GetExchangeAccountsCredentialsPublicKeyResponse get_exchange_accounts_credentials_public_key()

Get public key to encrypt exchange credentials

Return public key

### Example


```python
from fireblocks.models.get_exchange_accounts_credentials_public_key_response import GetExchangeAccountsCredentialsPublicKeyResponse
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
        # Get public key to encrypt exchange credentials
        api_response = fireblocks.exchange_accounts.get_exchange_accounts_credentials_public_key().result()
        print("The response of ExchangeAccountsApi->get_exchange_accounts_credentials_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_accounts_credentials_public_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetExchangeAccountsCredentialsPublicKeyResponse**](GetExchangeAccountsCredentialsPublicKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | public key as string |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paged_exchange_accounts**
> GetPagedExchangeAccountsResponse get_paged_exchange_accounts(limit, before=before, after=after)

Pagination list exchange accounts

Returns a page include exchange accounts.

### Example


```python
from fireblocks.models.get_paged_exchange_accounts_response import GetPagedExchangeAccountsResponse
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
    limit = 3 # float | number of exchanges per page (default to 3)
    before = 'before_example' # str |  (optional)
    after = 'after_example' # str |  (optional)

    try:
        # Pagination list exchange accounts
        api_response = fireblocks.exchange_accounts.get_paged_exchange_accounts(limit, before=before, after=after).result()
        print("The response of ExchangeAccountsApi->get_paged_exchange_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->get_paged_exchange_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| number of exchanges per page | [default to 3]
 **before** | **str**|  | [optional] 
 **after** | **str**|  | [optional] 

### Return type

[**GetPagedExchangeAccountsResponse**](GetPagedExchangeAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExchangeAccount object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_transfer**
> InternalTransferResponse internal_transfer(exchange_account_id, idempotency_key=idempotency_key, create_internal_transfer_request=create_internal_transfer_request)

Internal transfer for exchange accounts

Transfers funds between trading accounts under the same exchange account.

### Example


```python
from fireblocks.models.create_internal_transfer_request import CreateInternalTransferRequest
from fireblocks.models.internal_transfer_response import InternalTransferResponse
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
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account to return
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_internal_transfer_request = fireblocks.CreateInternalTransferRequest() # CreateInternalTransferRequest |  (optional)

    try:
        # Internal transfer for exchange accounts
        api_response = fireblocks.exchange_accounts.internal_transfer(exchange_account_id, idempotency_key=idempotency_key, create_internal_transfer_request=create_internal_transfer_request).result()
        print("The response of ExchangeAccountsApi->internal_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->internal_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_account_id** | **str**| The ID of the exchange account to return | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_internal_transfer_request** | [**CreateInternalTransferRequest**](CreateInternalTransferRequest.md)|  | [optional] 

### Return type

[**InternalTransferResponse**](InternalTransferResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer succeeded |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

