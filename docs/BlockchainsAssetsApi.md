# fireblocks_client.BlockchainsAssetsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_assets**](BlockchainsAssetsApi.md#get_supported_assets) | **GET** /supported_assets | List all asset types supported by Fireblocks


# **get_supported_assets**
> List[AssetTypeResponse] get_supported_assets()

List all asset types supported by Fireblocks

Returns all asset types supported by Fireblocks.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.BlockchainsAssetsApi(api_client)

    try:
        # List all asset types supported by Fireblocks
        api_response = api_instance.get_supported_assets()
        print("The response of BlockchainsAssetsApi->get_supported_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockchainsAssetsApi->get_supported_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[AssetTypeResponse]**](AssetTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Transaction object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

