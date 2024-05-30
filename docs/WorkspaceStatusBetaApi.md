# fireblocks.WorkspaceStatusBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace_status**](WorkspaceStatusBetaApi.md#get_workspace_status) | **GET** /management/workspace_status | Returns current workspace status


# **get_workspace_status**
> GetWorkspaceStatusResponse get_workspace_status()

Returns current workspace status

Returns current workspace status

### Example


```python
from fireblocks.models.get_workspace_status_response import GetWorkspaceStatusResponse
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
        # Returns current workspace status
        api_response = fireblocks.workspace_status_beta.get_workspace_status().result()
        print("The response of WorkspaceStatusBetaApi->get_workspace_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceStatusBetaApi->get_workspace_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetWorkspaceStatusResponse**](GetWorkspaceStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current workspace status |  -  |
**404** | Workspace not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

