<a id="__pageTop"></a>
# fireblocks_client.apis.tags.web3_connections_api.Web3ConnectionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](#create) | **post** /connections/wc | Create a new Web3 connection.
[**get**](#get) | **get** /connections | List all open Web3 connections.
[**remove**](#remove) | **delete** /connections/wc/{id} | Remove an existing Web3 connection.
[**submit**](#submit) | **put** /connections/wc/{id} | Respond to a pending Web3 connection request.

# **create**
<a id="create"></a>
> CreateConnectionResponse create(create_connection_request)

Create a new Web3 connection.

Initiate a new Web3 connection.  * Note: After this succeeds, make a request to `PUT /v1/connections/wc/{id}` (below) to approve or reject the new Web3 connection.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import web3_connections_api
from fireblocks_client.model.create_connection_request import CreateConnectionRequest
from fireblocks_client.model.create_connection_response import CreateConnectionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = web3_connections_api.Web3ConnectionsApi()
    # example passing only required values which don't have defaults set
    body = CreateConnectionRequest(
        vault_account_id=1,
        fee_level="MEDIUM",
        uri="wc:77752975-906f-48f5-b59f-047826ee947e@1?bridge=https%3A%2F%2F0.bridge.walletconnect.org&key=64be99adc6086b7a729b0ec8c7e1f174927ab92e84f5c6f9527050225344a637",
        chain_ids=["ETH","ETH_TEST"],
    )
    try:
        # Create a new Web3 connection.
        api_response = api_instance.create(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling Web3ConnectionsApi->create: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateConnectionRequest**](../../models/CreateConnectionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create.ApiResponseFor201) | Web3 connection initiated successfully
400 | [ApiResponseFor400](#create.ApiResponseFor400) | Invalid data sent
500 | [ApiResponseFor500](#create.ApiResponseFor500) | Something went wrong

#### create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateConnectionResponse**](../../models/CreateConnectionResponse.md) |  | 

#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor500 |  |
#### ResponseHeadersFor500

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

# **get**
<a id="get"></a>
> GetConnectionsResponse get()

List all open Web3 connections.

Get open Web3 connections.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import web3_connections_api
from fireblocks_client.model.get_connections_response import GetConnectionsResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = web3_connections_api.Web3ConnectionsApi()

    # example passing only optional values
    query_params = {
        'order': "ASC",
        'filter': dict(
        id="id_example",
        user_id="user_id_example",
        vault_account_id=3.14,
        connection_method="connection_method_example",
        fee_level="fee_level_example",
        app_url="app_url_example",
        app_name="app_name_example",
    ),
        'sort': "createdAt",
        'pageSize': 10,
        'next': "next_example",
    }
    try:
        # List all open Web3 connections.
        api_response = api_instance.get(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling Web3ConnectionsApi->get: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
order | OrderSchema | | optional
filter | FilterSchema | | optional
sort | SortSchema | | optional
pageSize | PageSizeSchema | | optional
next | NextSchema | | optional


# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "ASC"

# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**userId** | str,  | str,  |  | [optional] 
**vaultAccountId** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**connectionMethod** | str,  | str,  |  | [optional] 
**feeLevel** | str,  | str,  |  | [optional] 
**appUrl** | str,  | str,  |  | [optional] 
**appName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["id", "userId", "vaultAccountId", "createdAt", "feeLevel", "appUrl", "appName", ] if omitted the server will use the default value of "createdAt"

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 10

# NextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get.ApiResponseFor200) | 
400 | [ApiResponseFor400](#get.ApiResponseFor400) | Query parameters were invalid
500 | [ApiResponseFor500](#get.ApiResponseFor500) | Something went wrong

#### get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetConnectionsResponse**](../../models/GetConnectionsResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor500 |  |
#### ResponseHeadersFor500

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

# **remove**
<a id="remove"></a>
> remove(id)

Remove an existing Web3 connection.

Remove a Web3 connection

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import web3_connections_api
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = web3_connections_api.Web3ConnectionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    try:
        # Remove an existing Web3 connection.
        api_response = api_instance.remove(
            path_params=path_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling Web3ConnectionsApi->remove: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove.ApiResponseFor200) | Connection removed successfully
404 | [ApiResponseFor404](#remove.ApiResponseFor404) | Connection not found
500 | [ApiResponseFor500](#remove.ApiResponseFor500) | Something went wrong

#### remove.ApiResponseFor200
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


#### remove.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### remove.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor500 |  |
#### ResponseHeadersFor500

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

# **submit**
<a id="submit"></a>
> submit(idrespond_to_connection_request)

Respond to a pending Web3 connection request.

Submit a response to *approve* or *reject* an initiated Web3 connection. * Note: This call is used to complete your `POST /v1/connections/wc/` request.  After this succeeds, your new Web3 connection is created and functioning.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import web3_connections_api
from fireblocks_client.model.respond_to_connection_request import RespondToConnectionRequest
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = web3_connections_api.Web3ConnectionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    body = RespondToConnectionRequest(
        approve=True,
    )
    try:
        # Respond to a pending Web3 connection request.
        api_response = api_instance.submit(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling Web3ConnectionsApi->submit: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RespondToConnectionRequest**](../../models/RespondToConnectionRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#submit.ApiResponseFor200) | Connection submitted successfully
400 | [ApiResponseFor400](#submit.ApiResponseFor400) | Invalid data sent
404 | [ApiResponseFor404](#submit.ApiResponseFor404) | Connection not found
500 | [ApiResponseFor500](#submit.ApiResponseFor500) | Something went wrong

#### submit.ApiResponseFor200
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


#### submit.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor400 |  |
#### ResponseHeadersFor400

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### submit.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor404 |  |
#### ResponseHeadersFor404

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### submit.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor500 |  |
#### ResponseHeadersFor500

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

