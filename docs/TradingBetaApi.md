# fireblocks.TradingBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order**](TradingBetaApi.md#create_order) | **POST** /trading/orders | Create an order
[**create_quote**](TradingBetaApi.md#create_quote) | **POST** /trading/quotes | Create a quote
[**get_order**](TradingBetaApi.md#get_order) | **GET** /trading/orders/{orderId} | Get order details
[**get_orders**](TradingBetaApi.md#get_orders) | **GET** /trading/orders | Get orders
[**get_trading_providers**](TradingBetaApi.md#get_trading_providers) | **GET** /trading/providers | Get providers


# **create_order**
> OrderDetails create_order(create_order_request, idempotency_key=idempotency_key)

Create an order

Create an order to buy or sell an asset. If no source is given, an external source will be use.

Note: These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Trading, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Editor.

### Example


```python
from fireblocks.models.create_order_request import CreateOrderRequest
from fireblocks.models.order_details import OrderDetails
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
    create_order_request = fireblocks.CreateOrderRequest() # CreateOrderRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create an order
        api_response = fireblocks.trading_beta.create_order(create_order_request, idempotency_key=idempotency_key).result()
        print("The response of TradingBetaApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingBetaApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_request** | [**CreateOrderRequest**](CreateOrderRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**OrderDetails**](OrderDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Order creation response |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | Not found |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quote**
> QuotesResponse create_quote(create_quote, idempotency_key=idempotency_key)

Create a quote

Generate a time-limited quote for asset conversion, providing exchange rate and amount calculations.

Note: These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Trading, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Editor.

### Example


```python
from fireblocks.models.create_quote import CreateQuote
from fireblocks.models.quotes_response import QuotesResponse
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
    create_quote = fireblocks.CreateQuote() # CreateQuote | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a quote
        api_response = fireblocks.trading_beta.create_quote(create_quote, idempotency_key=idempotency_key).result()
        print("The response of TradingBetaApi->create_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingBetaApi->create_quote: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_quote** | [**CreateQuote**](CreateQuote.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**QuotesResponse**](QuotesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Quote created |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | Not found |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OrderDetails get_order(order_id)

Get order details

Retrieve detailed information about a specific order by its ID.

Note:These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Trading, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.order_details import OrderDetails
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
    order_id = 'order_id_example' # str | The ID of the order to fetch.

    try:
        # Get order details
        api_response = fireblocks.trading_beta.get_order(order_id).result()
        print("The response of TradingBetaApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingBetaApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The ID of the order to fetch. | 

### Return type

[**OrderDetails**](OrderDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order response |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | Not found |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> GetOrdersResponse get_orders(page_size, page_cursor=page_cursor, order=order, account_id=account_id, provider_id=provider_id, statuses=statuses, start_time=start_time, end_time=end_time, asset_conversion_type=asset_conversion_type)

Get orders

Retrieve a paginated list of orders with optional filtering by account, provider, status, and time range.

Note:These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Trading, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.get_orders_response import GetOrdersResponse
from fireblocks.models.order_status import OrderStatus
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
    page_size = 56 # int | pageSize for pagination.
    page_cursor = 'page_cursor_example' # str |  (optional)
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)
    account_id = ['account_id_example'] # List[str] | Filter by accountId. (optional)
    provider_id = ['provider_id_example'] # List[str] | Filter by providerId. (optional)
    statuses = [fireblocks.OrderStatus()] # List[OrderStatus] | Filter by order status. (optional)
    start_time = 56 # int |  (optional)
    end_time = 56 # int |  (optional)
    asset_conversion_type = 'asset_conversion_type_example' # str |  (optional)

    try:
        # Get orders
        api_response = fireblocks.trading_beta.get_orders(page_size, page_cursor=page_cursor, order=order, account_id=account_id, provider_id=provider_id, statuses=statuses, start_time=start_time, end_time=end_time, asset_conversion_type=asset_conversion_type).result()
        print("The response of TradingBetaApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingBetaApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| pageSize for pagination. | 
 **page_cursor** | **str**|  | [optional] 
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]
 **account_id** | [**List[str]**](str.md)| Filter by accountId. | [optional] 
 **provider_id** | [**List[str]**](str.md)| Filter by providerId. | [optional] 
 **statuses** | [**List[OrderStatus]**](OrderStatus.md)| Filter by order status. | [optional] 
 **start_time** | **int**|  | [optional] 
 **end_time** | **int**|  | [optional] 
 **asset_conversion_type** | **str**|  | [optional] 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders response |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | Not found |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trading_providers**
> ProvidersListResponse get_trading_providers(page_size=page_size, page_cursor=page_cursor)

Get providers

Retrieve a list of all available external providers supporting trading activities through the platform.

Note: These endpoints are currently in beta and might be subject to changes.

If you want to participate and learn more about the Fireblocks Trading, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.providers_list_response import ProvidersListResponse
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
    page_size = 20 # int | Page size for pagination. (optional) (default to 20)
    page_cursor = 'page_cursor_example' # str | Page cursor for pagination. (optional)

    try:
        # Get providers
        api_response = fireblocks.trading_beta.get_trading_providers(page_size=page_size, page_cursor=page_cursor).result()
        print("The response of TradingBetaApi->get_trading_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingBetaApi->get_trading_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size for pagination. | [optional] [default to 20]
 **page_cursor** | **str**| Page cursor for pagination. | [optional] 

### Return type

[**ProvidersListResponse**](ProvidersListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Providers response |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

