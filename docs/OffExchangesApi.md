# fireblocks_client.OffExchangesApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_off_exchange**](OffExchangesApi.md#add_off_exchange) | **POST** /off_exchange/add | add collateral
[**get_off_exchange_collateral_accounts**](OffExchangesApi.md#get_off_exchange_collateral_accounts) | **GET** /off_exchange/collateral_accounts/{mainExchangeAccountId} | Find a specific collateral exchange account
[**get_off_exchange_settlement_transactions**](OffExchangesApi.md#get_off_exchange_settlement_transactions) | **GET** /off_exchange/settlements/transactions | get settlements transactions from exchange
[**remove_off_exchange**](OffExchangesApi.md#remove_off_exchange) | **POST** /off_exchange/remove | remove collateral
[**settle_off_exchange_trades**](OffExchangesApi.md#settle_off_exchange_trades) | **POST** /off_exchange/settlements/trader | create settlement for a trader


# **add_off_exchange**
> CreateTransactionResponse add_off_exchange(add_collateral_request_body=add_collateral_request_body)

add collateral

add collateral, create deposit request

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
    api_instance = fireblocks_client.OffExchangesApi(api_client)
    add_collateral_request_body = fireblocks_client.AddCollateralRequestBody() # AddCollateralRequestBody |  (optional)

    try:
        # add collateral
        api_response = api_instance.add_off_exchange(add_collateral_request_body=add_collateral_request_body)
        print("The response of OffExchangesApi->add_off_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->add_off_exchange: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_collateral_request_body** | [**AddCollateralRequestBody**](AddCollateralRequestBody.md)|  | [optional] 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A transaction object |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_off_exchange_collateral_accounts**
> ExchangeAccount get_off_exchange_collateral_accounts(main_exchange_account_id)

Find a specific collateral exchange account

Returns a collateral account by mainExchangeAccountId.

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
    api_instance = fireblocks_client.OffExchangesApi(api_client)
    main_exchange_account_id = 'main_exchange_account_id_example' # str | The id of the main exchange account for which the requested collateral account is associated with

    try:
        # Find a specific collateral exchange account
        api_response = api_instance.get_off_exchange_collateral_accounts(main_exchange_account_id)
        print("The response of OffExchangesApi->get_off_exchange_collateral_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->get_off_exchange_collateral_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_exchange_account_id** | **str**| The id of the main exchange account for which the requested collateral account is associated with | 

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

# **get_off_exchange_settlement_transactions**
> SettlementResponse get_off_exchange_settlement_transactions(main_exchange_account_id)

get settlements transactions from exchange

get settlements transactions from exchange

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
    api_instance = fireblocks_client.OffExchangesApi(api_client)
    main_exchange_account_id = 'main_exchange_account_id_example' # str | 

    try:
        # get settlements transactions from exchange
        api_response = api_instance.get_off_exchange_settlement_transactions(main_exchange_account_id)
        print("The response of OffExchangesApi->get_off_exchange_settlement_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->get_off_exchange_settlement_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **main_exchange_account_id** | **str**|  | 

### Return type

[**SettlementResponse**](SettlementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A settlement transactions |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_off_exchange**
> CreateTransactionResponse remove_off_exchange(remove_collateral_request_body=remove_collateral_request_body)

remove collateral

remove collateral, create withdraw request

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
    api_instance = fireblocks_client.OffExchangesApi(api_client)
    remove_collateral_request_body = fireblocks_client.RemoveCollateralRequestBody() # RemoveCollateralRequestBody |  (optional)

    try:
        # remove collateral
        api_response = api_instance.remove_off_exchange(remove_collateral_request_body=remove_collateral_request_body)
        print("The response of OffExchangesApi->remove_off_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->remove_off_exchange: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remove_collateral_request_body** | [**RemoveCollateralRequestBody**](RemoveCollateralRequestBody.md)|  | [optional] 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A transaction object |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_off_exchange_trades**
> SettlementResponse settle_off_exchange_trades(settlement_request_body=settlement_request_body)

create settlement for a trader

create settlement for a trader

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
    api_instance = fireblocks_client.OffExchangesApi(api_client)
    settlement_request_body = fireblocks_client.SettlementRequestBody() # SettlementRequestBody |  (optional)

    try:
        # create settlement for a trader
        api_response = api_instance.settle_off_exchange_trades(settlement_request_body=settlement_request_body)
        print("The response of OffExchangesApi->settle_off_exchange_trades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->settle_off_exchange_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_request_body** | [**SettlementRequestBody**](SettlementRequestBody.md)|  | [optional] 

### Return type

[**SettlementResponse**](SettlementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A settlement object |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

