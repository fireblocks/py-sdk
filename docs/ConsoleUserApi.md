# fireblocks.ConsoleUserApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_console_user**](ConsoleUserApi.md#create_console_user) | **POST** /management/users | Create console user
[**delete_console_user**](ConsoleUserApi.md#delete_console_user) | **DELETE** /management/users/{id} | Request deletion of a console user
[**get_console_users**](ConsoleUserApi.md#get_console_users) | **GET** /management/users | Get console users


# **create_console_user**
> create_console_user(idempotency_key=idempotency_key, create_console_user=create_console_user)

Create console user

Create console users in your workspace
- Please note that this endpoint is available only for API keys with Admin/Non Signing Admin permissions.
Learn more about Fireblocks Users management in the following [guide](https://developers.fireblocks.com/docs/manage-users).
Endpoint Permission: Admin, Non-Signing Admin.

### Example


```python
from fireblocks.models.create_console_user import CreateConsoleUser
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
    create_console_user = fireblocks.CreateConsoleUser() # CreateConsoleUser |  (optional)

    try:
        # Create console user
        fireblocks.console_user.create_console_user(idempotency_key=idempotency_key, create_console_user=create_console_user).result()
    except Exception as e:
        print("Exception when calling ConsoleUserApi->create_console_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_console_user** | [**CreateConsoleUser**](CreateConsoleUser.md)|  | [optional] 

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

# **delete_console_user**
> ConsoleUser delete_console_user(id, force=force)

Request deletion of a console user

Requests deletion of a console user. The request is asynchronous: it goes through the workspace's configured "Delete users" approval policy (Settings > Quorums), exactly as deleting a user from the console does, and the user is removed only once that approval completes.
- Track progress by polling GET /management/users; deletion is complete when the user is disabled.
- Please note that this endpoint is available only for API keys with Admin/Non Signing Admin permissions.
Endpoint Permission: Admin, Non-Signing Admin.
**Note:** This endpoint is currently in beta and might be subject to changes.

### Example


```python
from fireblocks.models.console_user import ConsoleUser
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
    id = 'id_example' # str | The ID of the console user to delete
    force = False # bool | Acknowledges the impact of removing this user and proceeds anyway. Overrides both USER_REFERENCED_IN_TAP and QUORUM_INTEGRITY, the same way the acknowledgement checkbox does in the console. (optional) (default to False)

    try:
        # Request deletion of a console user
        api_response = fireblocks.console_user.delete_console_user(id, force=force).result()
        print("The response of ConsoleUserApi->delete_console_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsoleUserApi->delete_console_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the console user to delete | 
 **force** | **bool**| Acknowledges the impact of removing this user and proceeds anyway. Overrides both USER_REFERENCED_IN_TAP and QUORUM_INTEGRITY, the same way the acknowledgement checkbox does in the console. | [optional] [default to False]

### Return type

[**ConsoleUser**](ConsoleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deletion request accepted. Returns the console user that will be removed once the workspace&#39;s configured approval completes. |  * X-Request-ID -  <br>  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  * X-Request-ID -  <br>  |
**403** | Lacking permissions, or the target cannot be deleted: the user is the workspace Owner, or the caller is the target. |  * X-Request-ID -  <br>  |
**404** | Console user not found. Also returned for users in other workspaces and for API users, so the endpoint does not reveal whether an ID exists. |  * X-Request-ID -  <br>  |
**409** | PENDING_REQUEST_EXISTS - a deletion request for this user is already awaiting approval; USER_REFERENCED_IN_TAP - the user is referenced by the workspace transaction authorization policy (can be overridden with force&#x3D;true); or USER_PENDING_ONBOARDING - the user has not completed onboarding, so there is nothing to delete yet. Revoke the invitation from the console instead. |  * X-Request-ID -  <br>  |
**422** | QUORUM_INTEGRITY - the user is required to complete the workspace&#39;s admin approval quorum. Can be overridden with force&#x3D;true, matching the console&#39;s acknowledgement checkbox. |  * X-Request-ID -  <br>  |
**5XX** | Internal error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_console_users**
> GetConsoleUsersResponse get_console_users()

Get console users

Get console users for your workspace.
- Please note that this endpoint is available only for API keys with Admin/Non Signing Admin permissions.
Endpoint Permission: Admin, Non-Signing Admin.

### Example


```python
from fireblocks.models.get_console_users_response import GetConsoleUsersResponse
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
        # Get console users
        api_response = fireblocks.console_user.get_console_users().result()
        print("The response of ConsoleUserApi->get_console_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsoleUserApi->get_console_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetConsoleUsersResponse**](GetConsoleUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | got console users |  * X-Request-ID -  <br>  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  * X-Request-ID -  <br>  |
**403** | Lacking permissions. |  * X-Request-ID -  <br>  |
**5XX** | Internal error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

