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
> CreateTransactionResponse add_off_exchange(idempotency_key=idempotency_key, add_collateral_request_body=add_collateral_request_body)

add collateral

add collateral, create deposit request

### Example


```python
from fireblocks_client.models.add_collateral_request_body import AddCollateralRequestBody
from fireblocks_client.models.create_transaction_response import CreateTransactionResponse
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
    add_collateral_request_body = fireblocks_client.AddCollateralRequestBody() # AddCollateralRequestBody |  (optional)

    try:
        # add collateral
        api_response = fireblocks.off_exchanges.add_off_exchange(idempotency_key=idempotency_key, add_collateral_request_body=add_collateral_request_body).result()
        print("The response of OffExchangesApi->add_off_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->add_off_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **add_collateral_request_body** | [**AddCollateralRequestBody**](AddCollateralRequestBody.md)|  | [optional] 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

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
from fireblocks_client.models.exchange_account import ExchangeAccount
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
    main_exchange_account_id = 'main_exchange_account_id_example' # str | The id of the main exchange account for which the requested collateral account is associated with

    try:
        # Find a specific collateral exchange account
        api_response = fireblocks.off_exchanges.get_off_exchange_collateral_accounts(main_exchange_account_id).result()
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An ExchangeAccount object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_off_exchange_settlement_transactions**
> ExchangeSettlementTransactionsResponse get_off_exchange_settlement_transactions(main_exchange_account_id)

get settlements transactions from exchange

get settlements transactions from exchange

### Example


```python
from fireblocks_client.models.exchange_settlement_transactions_response import ExchangeSettlementTransactionsResponse
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
    main_exchange_account_id = 'main_exchange_account_id_example' # str | 

    try:
        # get settlements transactions from exchange
        api_response = fireblocks.off_exchanges.get_off_exchange_settlement_transactions(main_exchange_account_id).result()
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

[**ExchangeSettlementTransactionsResponse**](ExchangeSettlementTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A settlement transactions |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_off_exchange**
> CreateTransactionResponse remove_off_exchange(idempotency_key=idempotency_key, remove_collateral_request_body=remove_collateral_request_body)

remove collateral

remove collateral, create withdraw request

### Example


```python
from fireblocks_client.models.create_transaction_response import CreateTransactionResponse
from fireblocks_client.models.remove_collateral_request_body import RemoveCollateralRequestBody
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
    remove_collateral_request_body = fireblocks_client.RemoveCollateralRequestBody() # RemoveCollateralRequestBody |  (optional)

    try:
        # remove collateral
        api_response = fireblocks.off_exchanges.remove_off_exchange(idempotency_key=idempotency_key, remove_collateral_request_body=remove_collateral_request_body).result()
        print("The response of OffExchangesApi->remove_off_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->remove_off_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **remove_collateral_request_body** | [**RemoveCollateralRequestBody**](RemoveCollateralRequestBody.md)|  | [optional] 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A transaction object |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settle_off_exchange_trades**
> SettlementResponse settle_off_exchange_trades(idempotency_key=idempotency_key, settlement_request_body=settlement_request_body)

create settlement for a trader

create settlement for a trader

### Example


```python
from fireblocks_client.models.settlement_request_body import SettlementRequestBody
from fireblocks_client.models.settlement_response import SettlementResponse
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
    settlement_request_body = fireblocks_client.SettlementRequestBody() # SettlementRequestBody |  (optional)

    try:
        # create settlement for a trader
        api_response = fireblocks.off_exchanges.settle_off_exchange_trades(idempotency_key=idempotency_key, settlement_request_body=settlement_request_body).result()
        print("The response of OffExchangesApi->settle_off_exchange_trades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffExchangesApi->settle_off_exchange_trades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **settlement_request_body** | [**SettlementRequestBody**](SettlementRequestBody.md)|  | [optional] 

### Return type

[**SettlementResponse**](SettlementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A settlement object |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

