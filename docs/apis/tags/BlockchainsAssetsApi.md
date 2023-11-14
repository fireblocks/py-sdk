<a id="__pageTop"></a>
# fireblocks_client.apis.tags.blockchains_assets_api.BlockchainsAssetsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_supported_assets**](#get_supported_assets) | **get** /supported_assets | List all asset types supported by Fireblocks

# **get_supported_assets**
<a id="get_supported_assets"></a>
> [AssetTypeResponse] get_supported_assets()

List all asset types supported by Fireblocks

Returns all asset types supported by Fireblocks.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import blockchains_assets_api
from fireblocks_client.model.asset_type_response import AssetTypeResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = blockchains_assets_api.BlockchainsAssetsApi()

    # example, this endpoint has no required or optional parameters
    try:
        # List all asset types supported by Fireblocks
        api_response = api_instance.get_supported_assets()
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling BlockchainsAssetsApi->get_supported_assets: %s\n" % e)
```### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_supported_assets.ApiResponseFor200) | A Transaction object
default | [ApiResponseForDefault](#get_supported_assets.ApiResponseForDefault) | Error Response

#### get_supported_assets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AssetTypeResponse**]({{complexTypePrefix}}AssetTypeResponse.md) | [**AssetTypeResponse**]({{complexTypePrefix}}AssetTypeResponse.md) | [**AssetTypeResponse**]({{complexTypePrefix}}AssetTypeResponse.md) |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_supported_assets.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

