<a id="__pageTop"></a>
# fireblocks_client.apis.tags.exchange_accounts_api.ExchangeAccountsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_assets**](#convert_assets) | **post** /exchange_accounts/{exchangeAccountId}/convert | Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.
[**get_exchange_account_asset**](#get_exchange_account_asset) | **get** /exchange_accounts/{exchangeAccountId}/{assetId} | Find an asset for an exchange account
[**get_exchange_account_by_id**](#get_exchange_account_by_id) | **get** /exchange_accounts/{exchangeAccountId} | Find a specific exchange account
[**get_exchange_accounts**](#get_exchange_accounts) | **get** /exchange_accounts | List exchange accounts
[**internal_transfer**](#internal_transfer) | **post** /exchange_accounts/{exchangeAccountId}/internal_transfer | Internal tranfer for exchange accounts

# **convert_assets**
<a id="convert_assets"></a>
> convert_assets(exchange_account_id)

Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import exchange_accounts_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = exchange_accounts_api.ExchangeAccountsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'exchangeAccountId': "exchangeAccountId_example",
    }
    try:
        # Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.
        api_response = api_instance.convert_assets(
            path_params=path_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling ExchangeAccountsApi->convert_assets: %s\n" % e)

    # example passing only optional values
    path_params = {
        'exchangeAccountId': "exchangeAccountId_example",
    }
    body = None
    try:
        # Convert exchange account funds from the source asset to the destination asset. Coinbase (USD to USDC, USDC to USD) and Bitso (MXN to USD) are supported conversions.
        api_response = api_instance.convert_assets(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling ExchangeAccountsApi->convert_assets: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount to transfer (in the currency of the source asset) | 
**destAsset** | str,  | str,  | Name of the destination asset (must be in a currency that is supported for conversions in the selected exchange type that corresponds to your exchange ID) | 
**srcAsset** | str,  | str,  | Name of the source asset (must be in a currency that is supported for conversions in the selected exchange type that corresponds to your exchange ID) | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
exchangeAccountId | ExchangeAccountIdSchema | | 

# ExchangeAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#convert_assets.ApiResponseFor200) | Conversion successful
default | [ApiResponseForDefault](#convert_assets.ApiResponseForDefault) | Error Response

#### convert_assets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor200 |  |
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### convert_assets.ApiResponseForDefault
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

# **get_exchange_account_asset**
<a id="get_exchange_account_asset"></a>
> ExchangeAsset get_exchange_account_asset(exchange_account_idasset_id)

Find an asset for an exchange account

Returns an asset for an exchange account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import exchange_accounts_api
from fireblocks_client.model.exchange_asset import ExchangeAsset
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = exchange_accounts_api.ExchangeAccountsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'exchangeAccountId': "exchangeAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Find an asset for an exchange account
        api_response = api_instance.get_exchange_account_asset(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_account_asset: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
exchangeAccountId | ExchangeAccountIdSchema | | 
assetId | AssetIdSchema | | 

# ExchangeAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_exchange_account_asset.ApiResponseFor200) | An ExchangeAccountAsset object
default | [ApiResponseForDefault](#get_exchange_account_asset.ApiResponseForDefault) | Error Response

#### get_exchange_account_asset.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ExchangeAsset**](../../models/ExchangeAsset.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_exchange_account_asset.ApiResponseForDefault
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

# **get_exchange_account_by_id**
<a id="get_exchange_account_by_id"></a>
> ExchangeAccount get_exchange_account_by_id(exchange_account_id)

Find a specific exchange account

Returns an exchange account by ID.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import exchange_accounts_api
from fireblocks_client.model.exchange_account import ExchangeAccount
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = exchange_accounts_api.ExchangeAccountsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'exchangeAccountId': "exchangeAccountId_example",
    }
    try:
        # Find a specific exchange account
        api_response = api_instance.get_exchange_account_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_account_by_id: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
exchangeAccountId | ExchangeAccountIdSchema | | 

# ExchangeAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_exchange_account_by_id.ApiResponseFor200) | An ExchangeAccount object
default | [ApiResponseForDefault](#get_exchange_account_by_id.ApiResponseForDefault) | Error Response

#### get_exchange_account_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ExchangeAccount**](../../models/ExchangeAccount.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_exchange_account_by_id.ApiResponseForDefault
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

# **get_exchange_accounts**
<a id="get_exchange_accounts"></a>
> [ExchangeAccount] get_exchange_accounts()

List exchange accounts

Returns all exchange accounts.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import exchange_accounts_api
from fireblocks_client.model.exchange_account import ExchangeAccount
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = exchange_accounts_api.ExchangeAccountsApi()

    # example, this endpoint has no required or optional parameters
    try:
        # List exchange accounts
        api_response = api_instance.get_exchange_accounts()
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling ExchangeAccountsApi->get_exchange_accounts: %s\n" % e)
```### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_exchange_accounts.ApiResponseFor200) | An ExchangeAccount object
default | [ApiResponseForDefault](#get_exchange_accounts.ApiResponseForDefault) | Error Response

#### get_exchange_accounts.ApiResponseFor200
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
[**ExchangeAccount**]({{complexTypePrefix}}ExchangeAccount.md) | [**ExchangeAccount**]({{complexTypePrefix}}ExchangeAccount.md) | [**ExchangeAccount**]({{complexTypePrefix}}ExchangeAccount.md) |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_exchange_accounts.ApiResponseForDefault
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

# **internal_transfer**
<a id="internal_transfer"></a>
> internal_transfer(exchange_account_id)

Internal tranfer for exchange accounts

Transfers funds between trading accounts under the same exchange account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import exchange_accounts_api
from fireblocks_client.model.create_internal_transfer_request import CreateInternalTransferRequest
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = exchange_accounts_api.ExchangeAccountsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'exchangeAccountId': "exchangeAccountId_example",
    }
    try:
        # Internal tranfer for exchange accounts
        api_response = api_instance.internal_transfer(
            path_params=path_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling ExchangeAccountsApi->internal_transfer: %s\n" % e)

    # example passing only optional values
    path_params = {
        'exchangeAccountId': "exchangeAccountId_example",
    }
    body = CreateInternalTransferRequest(
        asset="asset_example",
        amount="amount_example",
        source_type=TradingAccountType("COIN_FUTURES"),
        dest_type=TradingAccountType("COIN_FUTURES"),
    )
    try:
        # Internal tranfer for exchange accounts
        api_response = api_instance.internal_transfer(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling ExchangeAccountsApi->internal_transfer: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateInternalTransferRequest**](../../models/CreateInternalTransferRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
exchangeAccountId | ExchangeAccountIdSchema | | 

# ExchangeAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#internal_transfer.ApiResponseFor201) | Transfer succeeded
default | [ApiResponseForDefault](#internal_transfer.ApiResponseForDefault) | Error Response

#### internal_transfer.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### internal_transfer.ApiResponseForDefault
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

