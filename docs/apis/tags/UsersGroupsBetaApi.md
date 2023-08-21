<a id="__pageTop"></a>
# fireblocks_client.apis.tags.users_groups_beta_api.UsersGroupsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_group**](#create_user_group) | **post** /users_groups | Create users group
[**delete_user_group**](#delete_user_group) | **delete** /users_groups/{groupId} | Delete users group
[**get_user_group**](#get_user_group) | **get** /users_groups/{groupId} | Get users group
[**get_user_groups**](#get_user_groups) | **get** /users_groups | List users groups
[**update_user_group**](#update_user_group) | **put** /users_groups/{groupId} | Update users group

# **create_user_group**
<a id="create_user_group"></a>
> CreateUsersGroupResponse create_user_group(user_group_create_request)

Create users group

Create a new users group.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import users_groups_beta_api
from fireblocks_client.model.user_group_create_request import UserGroupCreateRequest
from fireblocks_client.model.create_users_group_response import CreateUsersGroupResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = users_groups_beta_api.UsersGroupsBetaApi()
    # example passing only required values which don't have defaults set
    body = UserGroupCreateRequest(
        group_name="group_name_example",
        member_ids=[
            "member_ids_example"
        ],
    )
    try:
        # Create users group
        api_response = api_instance.create_user_group(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling UsersGroupsBetaApi->create_user_group: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroupCreateRequest**](../../models/UserGroupCreateRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_user_group.ApiResponseFor201) | Users group created and pending approval
default | [ApiResponseForDefault](#create_user_group.ApiResponseForDefault) | Error Response

#### create_user_group.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBody, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateUsersGroupResponse**](../../models/CreateUsersGroupResponse.md) |  | 

#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_user_group.ApiResponseForDefault
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

# **delete_user_group**
<a id="delete_user_group"></a>
> delete_user_group(group_id)

Delete users group

Delete a users group by ID.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import users_groups_beta_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = users_groups_beta_api.UsersGroupsBetaApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "groupId_example",
    }
    try:
        # Delete users group
        api_response = api_instance.delete_user_group(
            path_params=path_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling UsersGroupsBetaApi->delete_user_group: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_user_group.ApiResponseFor204) | Request to delete users group submitted for approval
default | [ApiResponseForDefault](#delete_user_group.ApiResponseForDefault) | Error Response

#### delete_user_group.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor204 |  |
#### ResponseHeadersFor204

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### delete_user_group.ApiResponseForDefault
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

# **get_user_group**
<a id="get_user_group"></a>
> UsersGroupResponse get_user_group(group_id)

Get users group

Get a users group by ID.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import users_groups_beta_api
from fireblocks_client.model.users_group_response import UsersGroupResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = users_groups_beta_api.UsersGroupsBetaApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "groupId_example",
    }
    try:
        # Get users group
        api_response = api_instance.get_user_group(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling UsersGroupsBetaApi->get_user_group: %s\n" % e)
```
### Parameters

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
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_group.ApiResponseFor200) | Users group
default | [ApiResponseForDefault](#get_user_group.ApiResponseForDefault) | Error Response

#### get_user_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UsersGroupResponse**](../../models/UsersGroupResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_user_group.ApiResponseForDefault
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

# **get_user_groups**
<a id="get_user_groups"></a>
> UsersGroupsResponse get_user_groups()

List users groups

Get all user groups in your workspace. </br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import users_groups_beta_api
from fireblocks_client.model.users_groups_response import UsersGroupsResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = users_groups_beta_api.UsersGroupsBetaApi()

    # example, this endpoint has no required or optional parameters
    try:
        # List users groups
        api_response = api_instance.get_user_groups()
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling UsersGroupsBetaApi->get_user_groups: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_groups.ApiResponseFor200) | List of the users groups in your workspace
default | [ApiResponseForDefault](#get_user_groups.ApiResponseForDefault) | Error Response

#### get_user_groups.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UsersGroupsResponse**](../../models/UsersGroupsResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_user_groups.ApiResponseForDefault
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

# **update_user_group**
<a id="update_user_group"></a>
> UserGroupCreateResponse update_user_group(group_iduser_group_update_request)

Update users group

Update a users group by ID.</br>  **Note**: - This endpoint is now in Beta, disabled for general availability at this time. - Please note that this endpoint is available only for API keys with Admin permissions. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import users_groups_beta_api
from fireblocks_client.model.user_group_update_request import UserGroupUpdateRequest
from fireblocks_client.model.user_group_create_response import UserGroupCreateResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = users_groups_beta_api.UsersGroupsBetaApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "groupId_example",
    }
    body = UserGroupUpdateRequest(
        group_name="group_name_example",
        member_ids=[
            "member_ids_example"
        ],
    )
    try:
        # Update users group
        api_response = api_instance.update_user_group(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling UsersGroupsBetaApi->update_user_group: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroupUpdateRequest**](../../models/UserGroupUpdateRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_user_group.ApiResponseFor200) | Users group updated and the changes are pending approval
default | [ApiResponseForDefault](#update_user_group.ApiResponseForDefault) | Error Response

#### update_user_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroupCreateResponse**](../../models/UserGroupCreateResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### update_user_group.ApiResponseForDefault
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

