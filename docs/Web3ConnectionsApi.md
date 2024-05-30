# fireblocks.Web3ConnectionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](Web3ConnectionsApi.md#create) | **POST** /connections/wc | Create a new Web3 connection.
[**get**](Web3ConnectionsApi.md#get) | **GET** /connections | List all open Web3 connections.
[**remove**](Web3ConnectionsApi.md#remove) | **DELETE** /connections/wc/{id} | Remove an existing Web3 connection.
[**submit**](Web3ConnectionsApi.md#submit) | **PUT** /connections/wc/{id} | Respond to a pending Web3 connection request.


# **create**
> CreateConnectionResponse create(create_connection_request, idempotency_key=idempotency_key)

Create a new Web3 connection.

Initiate a new Web3 connection.  * Note: After this succeeds, make a request to `PUT /v1/connections/wc/{id}` (below) to approve or reject the new Web3 connection.

### Example


```python
from fireblocks.models.create_connection_request import CreateConnectionRequest
from fireblocks.models.create_connection_response import CreateConnectionResponse
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
    create_connection_request = fireblocks.CreateConnectionRequest() # CreateConnectionRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a new Web3 connection.
        api_response = fireblocks.web3_connections.create(create_connection_request, idempotency_key=idempotency_key).result()
        print("The response of Web3ConnectionsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Web3ConnectionsApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connection_request** | [**CreateConnectionRequest**](CreateConnectionRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateConnectionResponse**](CreateConnectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Web3 connection initiated successfully |  * X-Request-ID -  <br>  |
**400** | Invalid data sent |  * X-Request-ID -  <br>  |
**500** | Something went wrong |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> GetConnectionsResponse get(order=order, filter=filter, sort=sort, page_size=page_size, next=next)

List all open Web3 connections.

Get open Web3 connections.

### Example


```python
from fireblocks.models.get_connections_response import GetConnectionsResponse
from fireblocks.models.get_filter_parameter import GetFilterParameter
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
    order = 'ASC' # str | List order; ascending or descending. (optional) (default to 'ASC')
    filter = fireblocks.GetFilterParameter() # GetFilterParameter | Parsed filter object (optional)
    sort = 'createdAt' # str | Property to sort Web3 connections by. (optional) (default to 'createdAt')
    page_size = 10 # float | Amount of results to return in the next page. (optional) (default to 10)
    next = 'next_example' # str | Cursor to the next page (optional)

    try:
        # List all open Web3 connections.
        api_response = fireblocks.web3_connections.get(order=order, filter=filter, sort=sort, page_size=page_size, next=next).result()
        print("The response of Web3ConnectionsApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Web3ConnectionsApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| List order; ascending or descending. | [optional] [default to &#39;ASC&#39;]
 **filter** | [**GetFilterParameter**](.md)| Parsed filter object | [optional] 
 **sort** | **str**| Property to sort Web3 connections by. | [optional] [default to &#39;createdAt&#39;]
 **page_size** | **float**| Amount of results to return in the next page. | [optional] [default to 10]
 **next** | **str**| Cursor to the next page | [optional] 

### Return type

[**GetConnectionsResponse**](GetConnectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Request-ID -  <br>  |
**400** | Query parameters were invalid |  * X-Request-ID -  <br>  |
**500** | Something went wrong |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove(id)

Remove an existing Web3 connection.

Remove a Web3 connection

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
    id = 'id_example' # str | The ID of the existing Web3 connection to remove.

    try:
        # Remove an existing Web3 connection.
        fireblocks.web3_connections.remove(id).result()
    except Exception as e:
        print("Exception when calling Web3ConnectionsApi->remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the existing Web3 connection to remove. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection removed successfully |  * X-Request-ID -  <br>  |
**404** | Connection not found |  * X-Request-ID -  <br>  |
**500** | Something went wrong |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit**
> submit(id, respond_to_connection_request, idempotency_key=idempotency_key)

Respond to a pending Web3 connection request.

Submit a response to *approve* or *reject* an initiated Web3 connection. * Note: This call is used to complete your `POST /v1/connections/wc/` request.  After this succeeds, your new Web3 connection is created and functioning.

### Example


```python
from fireblocks.models.respond_to_connection_request import RespondToConnectionRequest
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
    id = 'id_example' # str | The ID of the initiated Web3 connection to approve.
    respond_to_connection_request = fireblocks.RespondToConnectionRequest() # RespondToConnectionRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Respond to a pending Web3 connection request.
        fireblocks.web3_connections.submit(id, respond_to_connection_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling Web3ConnectionsApi->submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the initiated Web3 connection to approve. | 
 **respond_to_connection_request** | [**RespondToConnectionRequest**](RespondToConnectionRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection submitted successfully |  * X-Request-ID -  <br>  |
**400** | Invalid data sent |  * X-Request-ID -  <br>  |
**404** | Connection not found |  * X-Request-ID -  <br>  |
**500** | Something went wrong |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

