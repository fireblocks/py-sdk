# fireblocks_client.WorkspaceStatusBetaApi

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
import fireblocks_client
from fireblocks_client.models.get_workspace_status_response import GetWorkspaceStatusResponse
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
    api_instance = fireblocks_client.WorkspaceStatusBetaApi(api_client)

    try:
        # Returns current workspace status
        api_response = api_instance.get_workspace_status()
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

