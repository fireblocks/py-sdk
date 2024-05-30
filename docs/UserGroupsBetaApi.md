# fireblocks.UserGroupsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_group**](UserGroupsBetaApi.md#create_user_group) | **POST** /management/user_groups | Create user group
[**delete_user_group**](UserGroupsBetaApi.md#delete_user_group) | **DELETE** /management/user_groups/{groupId} | Delete user group
[**get_user_group**](UserGroupsBetaApi.md#get_user_group) | **GET** /management/user_groups/{groupId} | Get user group
[**get_user_groups**](UserGroupsBetaApi.md#get_user_groups) | **GET** /management/user_groups | List user groups
[**update_user_group**](UserGroupsBetaApi.md#update_user_group) | **PUT** /management/user_groups/{groupId} | Update user group


# **create_user_group**
> CreateUserGroupResponse create_user_group(user_group_create_request, idempotency_key=idempotency_key)

Create user group

Create a new user group.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example


```python
from fireblocks.models.create_user_group_response import CreateUserGroupResponse
from fireblocks.models.user_group_create_request import UserGroupCreateRequest
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
    user_group_create_request = fireblocks.UserGroupCreateRequest() # UserGroupCreateRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create user group
        api_response = fireblocks.user_groups_beta.create_user_group(user_group_create_request, idempotency_key=idempotency_key).result()
        print("The response of UserGroupsBetaApi->create_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupsBetaApi->create_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_create_request** | [**UserGroupCreateRequest**](UserGroupCreateRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateUserGroupResponse**](CreateUserGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User group created and pending approval |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_group**
> delete_user_group(group_id)

Delete user group

Delete a user group by ID.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

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
    group_id = 'group_id_example' # str | The ID of the user group

    try:
        # Delete user group
        fireblocks.user_groups_beta.delete_user_group(group_id).result()
    except Exception as e:
        print("Exception when calling UserGroupsBetaApi->delete_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the user group | 

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
**204** | Request to delete user group submitted for approval |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> UserGroupResponse get_user_group(group_id)

Get user group

Get a user group by ID.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example


```python
from fireblocks.models.user_group_response import UserGroupResponse
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
    group_id = 'group_id_example' # str | The ID of the user group

    try:
        # Get user group
        api_response = fireblocks.user_groups_beta.get_user_group(group_id).result()
        print("The response of UserGroupsBetaApi->get_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupsBetaApi->get_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the user group | 

### Return type

[**UserGroupResponse**](UserGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_groups**
> List[UserGroupResponse] get_user_groups()

List user groups

Get all user groups in your workspace. </br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example


```python
from fireblocks.models.user_group_response import UserGroupResponse
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
        # List user groups
        api_response = fireblocks.user_groups_beta.get_user_groups().result()
        print("The response of UserGroupsBetaApi->get_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupsBetaApi->get_user_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserGroupResponse]**](UserGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the user groups in your workspace |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_group**
> UserGroupCreateResponse update_user_group(group_id, user_group_update_request, idempotency_key=idempotency_key)

Update user group

Update a user group by ID.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example


```python
from fireblocks.models.user_group_create_response import UserGroupCreateResponse
from fireblocks.models.user_group_update_request import UserGroupUpdateRequest
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
    group_id = 'group_id_example' # str | The ID of the user group
    user_group_update_request = fireblocks.UserGroupUpdateRequest() # UserGroupUpdateRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update user group
        api_response = fireblocks.user_groups_beta.update_user_group(group_id, user_group_update_request, idempotency_key=idempotency_key).result()
        print("The response of UserGroupsBetaApi->update_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserGroupsBetaApi->update_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The ID of the user group | 
 **user_group_update_request** | [**UserGroupUpdateRequest**](UserGroupUpdateRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**UserGroupCreateResponse**](UserGroupCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group updated and the changes are pending approval |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

