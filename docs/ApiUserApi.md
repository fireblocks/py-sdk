# fireblocks_client.ApiUserApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_user**](ApiUserApi.md#create_api_user) | **POST** /management/api_users | Create Api user
[**get_api_users**](ApiUserApi.md#get_api_users) | **GET** /management/api_users | Get Api users


# **create_api_user**
> create_api_user(idempotency_key=idempotency_key, create_api_user=create_api_user)

Create Api user

Creates Api user in your tenant

### Example


```python
import fireblocks_client
from fireblocks_client.models.create_api_user import CreateAPIUser
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
    api_instance = fireblocks_client.ApiUserApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_api_user = fireblocks_client.CreateAPIUser() # CreateAPIUser |  (optional)

    try:
        # Create Api user
        api_instance.create_api_user(idempotency_key=idempotency_key, create_api_user=create_api_user)
    except Exception as e:
        print("Exception when calling ApiUserApi->create_api_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_api_user** | [**CreateAPIUser**](CreateAPIUser.md)|  | [optional] 

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
**200** | User creation approval request has been sent |  * X-Request-ID -  <br>  |
**400** | bad request |  * X-Request-ID -  <br>  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  * X-Request-ID -  <br>  |
**403** | Lacking permissions. |  * X-Request-ID -  <br>  |
**5XX** | Internal error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_users**
> GetAPIUsersResponse get_api_users()

Get Api users

Get Api users of your tenant

### Example


```python
import fireblocks_client
from fireblocks_client.models.get_api_users_response import GetAPIUsersResponse
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
    api_instance = fireblocks_client.ApiUserApi(api_client)

    try:
        # Get Api users
        api_response = api_instance.get_api_users()
        print("The response of ApiUserApi->get_api_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiUserApi->get_api_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAPIUsersResponse**](GetAPIUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | got api users |  * X-Request-ID -  <br>  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  * X-Request-ID -  <br>  |
**403** | Lacking permissions. |  * X-Request-ID -  <br>  |
**5XX** | Internal error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

