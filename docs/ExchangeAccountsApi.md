# fireblocks_client.ExchangeAccountsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_assets**](ExchangeAccountsApi.md#convert_assets) | **POST** /exchange_accounts/{exchangeAccountId}/convert | Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.
[**get_exchange_account_asset**](ExchangeAccountsApi.md#get_exchange_account_asset) | **GET** /exchange_accounts/{exchangeAccountId}/{assetId} | Find an asset for an exchange account
[**get_exchange_account_by_id**](ExchangeAccountsApi.md#get_exchange_account_by_id) | **GET** /exchange_accounts/{exchangeAccountId} | Find a specific exchange account
[**get_exchange_accounts**](ExchangeAccountsApi.md#get_exchange_accounts) | **GET** /exchange_accounts | List exchange accounts
[**internal_transfer**](ExchangeAccountsApi.md#internal_transfer) | **POST** /exchange_accounts/{exchangeAccountId}/internal_transfer | Internal tranfer for exchange accounts


# **convert_assets**
> convert_assets(exchange_account_id, convert_assets_request=convert_assets_request)

Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.

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
    api_instance = fireblocks_client.ExchangeAccountsApi(api_client)
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account. Please make sure the exchange supports conversions. To find the ID of your exchange account, use GET/exchange_accounts.
    convert_assets_request = fireblocks_client.ConvertAssetsRequest() # ConvertAssetsRequest |  (optional)

    try:
        # Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.
        api_instance.convert_assets(exchange_account_id, convert_assets_request=convert_assets_request)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->convert_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_account_id** | **str**| The ID of the exchange account. Please make sure the exchange supports conversions. To find the ID of your exchange account, use GET/exchange_accounts. | 
 **convert_assets_request** | [**ConvertAssetsRequest**](ConvertAssetsRequest.md)|  | [optional] 

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
**200** | Conversion successful |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_account_asset**
> ExchangeAsset get_exchange_account_asset(exchange_account_id, asset_id)

Find an asset for an exchange account

Returns an asset for an exchange account.

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
    api_instance = fireblocks_client.ExchangeAccountsApi(api_client)
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account to return
    asset_id = 'asset_id_example' # str | The ID of the asset to return

    try:
        # Find an asset for an exchange account
        api_response = api_instance.get_exchange_account_asset(exchange_account_id, asset_id)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExchangeAccountAsset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_account_by_id**
> ExchangeAccount get_exchange_account_by_id(exchange_account_id)

Find a specific exchange account

Returns an exchange account by ID.

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
    api_instance = fireblocks_client.ExchangeAccountsApi(api_client)
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account to return

    try:
        # Find a specific exchange account
        api_response = api_instance.get_exchange_account_by_id(exchange_account_id)
        print("The response of ExchangeAccountsApi->get_exchange_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_account_by_id: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExchangeAccount object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_accounts**
> List[ExchangeAccount] get_exchange_accounts()

List exchange accounts

Returns all exchange accounts.

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
    api_instance = fireblocks_client.ExchangeAccountsApi(api_client)

    try:
        # List exchange accounts
        api_response = api_instance.get_exchange_accounts()
        print("The response of ExchangeAccountsApi->get_exchange_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ExchangeAccount]**](ExchangeAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExchangeAccount object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_transfer**
> internal_transfer(exchange_account_id, create_internal_transfer_request=create_internal_transfer_request)

Internal tranfer for exchange accounts

Transfers funds between trading accounts under the same exchange account.

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
    api_instance = fireblocks_client.ExchangeAccountsApi(api_client)
    exchange_account_id = 'exchange_account_id_example' # str | The ID of the exchange account to return
    create_internal_transfer_request = fireblocks_client.CreateInternalTransferRequest() # CreateInternalTransferRequest |  (optional)

    try:
        # Internal tranfer for exchange accounts
        api_instance.internal_transfer(exchange_account_id, create_internal_transfer_request=create_internal_transfer_request)
    except Exception as e:
        print("Exception when calling ExchangeAccountsApi->internal_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_account_id** | **str**| The ID of the exchange account to return | 
 **create_internal_transfer_request** | [**CreateInternalTransferRequest**](CreateInternalTransferRequest.md)|  | [optional] 

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
**201** | Transfer succeeded |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

