<a id="__pageTop"></a>
# fireblocks_client.apis.tags.payments_payout_api.PaymentsPayoutApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payout**](#create_payout) | **post** /payments/payout | Create a payout instruction set
[**execute_payout_action**](#execute_payout_action) | **post** /payments/payout/{payoutId}/actions/execute | Execute a payout instruction set
[**get_payout_by_id**](#get_payout_by_id) | **get** /payments/payout/{payoutId} | Get the status of a payout instruction set

# **create_payout**
<a id="create_payout"></a>
> PayoutResponse create_payout()

Create a payout instruction set

**Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> </br> <b u>Create a payout instruction set.</b> </u></br> A payout instruction set is a set of instructions for distributing payments from a single payment account to a list of payee accounts. </br> The instruction set defines: </br> <ul> <li>the payment account and its account type (vault, exchange, or fiat). </li> <li>the account type (vault account, exchange account, whitelisted address, network connection, fiat account, or merchant account), the amount, and the asset of payment for each payee account.</li> </ul> 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_payout_api
from fireblocks_client.model.payout_response import PayoutResponse
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.create_payout_request import CreatePayoutRequest
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_payout_api.PaymentsPayoutApi()

    # example passing only optional values
    body = CreatePayoutRequest(
        payment_account=PaymentAccount(
            id="id_example",
            type=PaymentAccountType("VAULT_ACCOUNT"),
        ),
        instruction_set=[
            PayoutInstruction(
                id="id_example",
                payee_account=PayeeAccount(
                    id="id_example",
                    type=PayeeAccountType("VAULT_ACCOUNT"),
                ),
                amount=InstructionAmount(
                    amount="amount_example",
                    asset_id="asset_id_example",
                ),
            )
        ],
    )
    try:
        # Create a payout instruction set
        api_response = api_instance.create_payout(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsPayoutApi->create_payout: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatePayoutRequest**](../../models/CreatePayoutRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_payout.ApiResponseFor200) | The payout instruction set creation succeeded and returns the generated instruction set with a unique payout IDThe payout ID will be used for executing the payout and checking the payout status.
400 | [ApiResponseFor400](#create_payout.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#create_payout.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#create_payout.ApiResponseFor5XX) | Internal error.

#### create_payout.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PayoutResponse**](../../models/PayoutResponse.md) |  | 


#### create_payout.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_payout.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_payout.ApiResponseFor5XX
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor5XXResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor5XXResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **execute_payout_action**
<a id="execute_payout_action"></a>
> DispatchPayoutResponse execute_payout_action(payout_id)

Execute a payout instruction set

**Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> </br><b u>Execute a payout instruction set.</b> </u> </br> </br>The instruction set will be verified and executed.</br> <b><u>Source locking</br></b> </u> If you are executing a payout instruction set from a payment account with an already active payout the active payout will complete before the new payout instruction set can be executed. </br> You cannot execute the same payout instruction set more than once. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_payout_api
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.dispatch_payout_response import DispatchPayoutResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_payout_api.PaymentsPayoutApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'payoutId': "1fe3b61f-7e1f-4a19-aff0-4f0a524d44d7",
    }
    try:
        # Execute a payout instruction set
        api_response = api_instance.execute_payout_action(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsPayoutApi->execute_payout_action: %s\n" % e)
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
payoutId | PayoutIdSchema | | 

# PayoutIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#execute_payout_action.ApiResponseFor200) | Executed the payout instruction set
400 | [ApiResponseFor400](#execute_payout_action.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#execute_payout_action.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#execute_payout_action.ApiResponseFor5XX) | Internal error.

#### execute_payout_action.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DispatchPayoutResponse**](../../models/DispatchPayoutResponse.md) |  | 


#### execute_payout_action.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### execute_payout_action.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### execute_payout_action.ApiResponseFor5XX
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor5XXResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor5XXResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_payout_by_id**
<a id="get_payout_by_id"></a>
> PayoutResponse get_payout_by_id(payout_id)

Get the status of a payout instruction set

**Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_payout_api
from fireblocks_client.model.payout_response import PayoutResponse
from fireblocks_client.model.error_response import ErrorResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_payout_api.PaymentsPayoutApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'payoutId': "1fe3b61f-7e1f-4a19-aff0-4f0a524d44d7",
    }
    try:
        # Get the status of a payout instruction set
        api_response = api_instance.get_payout_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsPayoutApi->get_payout_by_id: %s\n" % e)
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
payoutId | PayoutIdSchema | | 

# PayoutIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_payout_by_id.ApiResponseFor200) | Returns the current status of the payout instruction set, including the status of each payout instruction and the transactions created in the process.
404 | [ApiResponseFor404](#get_payout_by_id.ApiResponseFor404) | No payout with the given payout ID exists.
401 | [ApiResponseFor401](#get_payout_by_id.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#get_payout_by_id.ApiResponseFor5XX) | Internal error.

#### get_payout_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PayoutResponse**](../../models/PayoutResponse.md) |  | 


#### get_payout_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_payout_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_payout_by_id.ApiResponseFor5XX
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor5XXResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor5XXResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

