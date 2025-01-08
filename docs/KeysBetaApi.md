# fireblocks.KeysBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mpc_keys_list**](KeysBetaApi.md#get_mpc_keys_list) | **GET** /keys/mpc/list | Get list of mpc keys
[**get_mpc_keys_list_by_user**](KeysBetaApi.md#get_mpc_keys_list_by_user) | **GET** /keys/mpc/list/{userId} | Get list of mpc keys by &#x60;userId&#x60;


# **get_mpc_keys_list**
> GetMpcKeysResponse get_mpc_keys_list()

Get list of mpc keys

Returns a list of MPC signing keys of the workspace. For each key, the list of players associated with it is attached. **Note:**  This endpoint is currently in beta and might be subject to changes.

### Example


```python
from fireblocks.models.get_mpc_keys_response import GetMpcKeysResponse
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
        # Get list of mpc keys
        api_response = fireblocks.keys_beta.get_mpc_keys_list().result()
        print("The response of KeysBetaApi->get_mpc_keys_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeysBetaApi->get_mpc_keys_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMpcKeysResponse**](GetMpcKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of mpc keys |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mpc_keys_list_by_user**
> GetMpcKeysResponse get_mpc_keys_list_by_user(user_id)

Get list of mpc keys by `userId`

Returns a list of MPC signing keys of a specific user. For each key, the list of players associated with it is attached. **Note:** This endpoint is currently in beta and might be subject to changes.

### Example


```python
from fireblocks.models.get_mpc_keys_response import GetMpcKeysResponse
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
    user_id = '46a92767-5f93-4a46-9eed-f012196bb4fc' # str | The id for the user

    try:
        # Get list of mpc keys by `userId`
        api_response = fireblocks.keys_beta.get_mpc_keys_list_by_user(user_id).result()
        print("The response of KeysBetaApi->get_mpc_keys_list_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeysBetaApi->get_mpc_keys_list_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id for the user | 

### Return type

[**GetMpcKeysResponse**](GetMpcKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of mpc keys |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

