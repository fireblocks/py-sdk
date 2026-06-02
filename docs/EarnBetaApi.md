# fireblocks.EarnBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_terms_of_service**](EarnBetaApi.md#approve_terms_of_service) | **POST** /earn/providers/approve_terms_of_service | Approve earn provider terms of service
[**create_earn_action**](EarnBetaApi.md#create_earn_action) | **POST** /earn/actions | Create and execute a lending action (deposit or withdraw)
[**get_earn_action**](EarnBetaApi.md#get_earn_action) | **GET** /earn/actions/{id} | Get a single earn lending action
[**get_earn_actions**](EarnBetaApi.md#get_earn_actions) | **GET** /earn/actions | List earn lending actions
[**get_earn_opportunities**](EarnBetaApi.md#get_earn_opportunities) | **GET** /earn/opportunities | Get list of earn opportunities
[**get_earn_positions**](EarnBetaApi.md#get_earn_positions) | **GET** /earn/positions | Get list of earn positions
[**get_earn_providers**](EarnBetaApi.md#get_earn_providers) | **GET** /earn/providers | Get list of earn providers


# **approve_terms_of_service**
> approve_terms_of_service(idempotency_key=idempotency_key)

Approve earn provider terms of service

Approves earn provider terms of service for this workspace (one-time per tenant).
When `isTermsApprovalRequired` is true on a provider (see list providers),
call this once before creating or executing earn actions with providers that require it.
After success, `GET /earn/providers` reflects `isTermsOfServiceApproved`.

**Note:** This endpoint is currently in beta and might be subject to changes.


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
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Approve earn provider terms of service
        fireblocks.earn_beta.approve_terms_of_service(idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling EarnBetaApi->approve_terms_of_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | Terms of service accepted. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_earn_action**
> CreateEarnActionResponse create_earn_action(create_earn_action_request, idempotency_key=idempotency_key)

Create and execute a lending action (deposit or withdraw)

Creates and runs a sequence of on-chain steps for either a deposit into or a withdrawal from an earn
vault/market. Specify the operation with `action` in the request body (`DEPOSIT` or `WITHDRAW`).

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.create_earn_action_request import CreateEarnActionRequest
from fireblocks.models.create_earn_action_response import CreateEarnActionResponse
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
    create_earn_action_request = fireblocks.CreateEarnActionRequest() # CreateEarnActionRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create and execute a lending action (deposit or withdraw)
        api_response = fireblocks.earn_beta.create_earn_action(create_earn_action_request, idempotency_key=idempotency_key).result()
        print("The response of EarnBetaApi->create_earn_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EarnBetaApi->create_earn_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_earn_action_request** | [**CreateEarnActionRequest**](CreateEarnActionRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateEarnActionResponse**](CreateEarnActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., opportunity, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earn_action**
> GetActionResponse get_earn_action(id)

Get a single earn lending action

Returns one lending action by its action sequence id (tenant-scoped).

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.get_action_response import GetActionResponse
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
    id = 'id_example' # str | Action sequence id (UUID).

    try:
        # Get a single earn lending action
        api_response = fireblocks.earn_beta.get_earn_action(id).result()
        print("The response of EarnBetaApi->get_earn_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EarnBetaApi->get_earn_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Action sequence id (UUID). | 

### Return type

[**GetActionResponse**](GetActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted access. |  * X-Request-ID -  <br>  |
**404** | Not found: action does not exist or is not visible for this tenant. |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earn_actions**
> GetActionsResponse get_earn_actions(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

List earn lending actions

Returns a paginated list of lending actions (deposits and withdrawals) for the authenticated tenant.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.get_actions_response import GetActionsResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor for the next or previous page of results. (optional)
    page_size = 100 # int | Number of items per page (default 100, max 100). (optional) (default to 100)
    sort_by = 'sort_by_example' # str | Field to sort results by. (optional)
    order = DESC # str | Sort order (ASC or DESC). (optional) (default to DESC)

    try:
        # List earn lending actions
        api_response = fireblocks.earn_beta.get_earn_actions(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of EarnBetaApi->get_earn_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EarnBetaApi->get_earn_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor for the next or previous page of results. | [optional] 
 **page_size** | **int**| Number of items per page (default 100, max 100). | [optional] [default to 100]
 **sort_by** | **str**| Field to sort results by. | [optional] 
 **order** | **str**| Sort order (ASC or DESC). | [optional] [default to DESC]

### Return type

[**GetActionsResponse**](GetActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted access. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist. |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earn_opportunities**
> GetOpportunitiesResponse get_earn_opportunities(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get list of earn opportunities

Get list of earn opportunities (vaults).

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.get_opportunities_response import GetOpportunitiesResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor for the next or previous page of results. (optional)
    page_size = 100 # int | Number of items per page. (optional) (default to 100)
    sort_by = 'sort_by_example' # str | Field to sort results by. (optional)
    order = DESC # str | Sort order (ASC or DESC). (optional) (default to DESC)

    try:
        # Get list of earn opportunities
        api_response = fireblocks.earn_beta.get_earn_opportunities(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of EarnBetaApi->get_earn_opportunities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EarnBetaApi->get_earn_opportunities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor for the next or previous page of results. | [optional] 
 **page_size** | **int**| Number of items per page. | [optional] [default to 100]
 **sort_by** | **str**| Field to sort results by. | [optional] 
 **order** | **str**| Sort order (ASC or DESC). | [optional] [default to DESC]

### Return type

[**GetOpportunitiesResponse**](GetOpportunitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted access. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist. |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earn_positions**
> GetPositionsResponse get_earn_positions(chain_id=chain_id, provider_id=provider_id, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get list of earn positions

Get list of earn positions for accounts tracked for this workspace. 
Optional query parameters filter by chain, provider, and pagination.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.get_positions_response import GetPositionsResponse
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
    chain_id = 56 # int |  (optional)
    provider_id = 'provider_id_example' # str |  (optional)
    page_cursor = 'page_cursor_example' # str | Cursor for the next or previous page of results. (optional)
    page_size = 100 # int | Number of items per page. (optional) (default to 100)
    sort_by = 'sort_by_example' # str | Field to sort results by. (optional)
    order = DESC # str | Sort order (ASC or DESC). (optional) (default to DESC)

    try:
        # Get list of earn positions
        api_response = fireblocks.earn_beta.get_earn_positions(chain_id=chain_id, provider_id=provider_id, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of EarnBetaApi->get_earn_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EarnBetaApi->get_earn_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **int**|  | [optional] 
 **provider_id** | **str**|  | [optional] 
 **page_cursor** | **str**| Cursor for the next or previous page of results. | [optional] 
 **page_size** | **int**| Number of items per page. | [optional] [default to 100]
 **sort_by** | **str**| Field to sort results by. | [optional] 
 **order** | **str**| Sort order (ASC or DESC). | [optional] [default to DESC]

### Return type

[**GetPositionsResponse**](GetPositionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted access. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist. |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earn_providers**
> GetProvidersResponse get_earn_providers(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get list of earn providers

Get list of earn providers.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.get_providers_response import GetProvidersResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor for the next or previous page of results. (optional)
    page_size = 100 # int | Number of items per page. (optional) (default to 100)
    sort_by = 'sort_by_example' # str | Field to sort results by. (optional)
    order = DESC # str | Sort order (ASC or DESC). (optional) (default to DESC)

    try:
        # Get list of earn providers
        api_response = fireblocks.earn_beta.get_earn_providers(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of EarnBetaApi->get_earn_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EarnBetaApi->get_earn_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor for the next or previous page of results. | [optional] 
 **page_size** | **int**| Number of items per page. | [optional] [default to 100]
 **sort_by** | **str**| Field to sort results by. | [optional] 
 **order** | **str**| Sort order (ASC or DESC). | [optional] [default to DESC]

### Return type

[**GetProvidersResponse**](GetProvidersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted access. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist. |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

