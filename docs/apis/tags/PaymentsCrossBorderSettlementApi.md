<a id="__pageTop"></a>
# fireblocks_client.apis.tags.payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_xb_settlement_config**](#create_xb_settlement_config) | **post** /payments/xb-settlements/configs | Create a new cross-border settlement configuration
[**create_xb_settlement_flow**](#create_xb_settlement_flow) | **post** /payments/xb-settlements/flows | Create a new cross-border settlement flow
[**delete_xb_settlement_config**](#delete_xb_settlement_config) | **delete** /payments/xb-settlements/configs/{configId} | Delete a cross-border settlement configuration
[**execute_xb_settlement_flow_action**](#execute_xb_settlement_flow_action) | **post** /payments/xb-settlements/flows/{flowId}/actions/execute | Execute cross-border settlement flow
[**get_xb_settlement_config_by_id**](#get_xb_settlement_config_by_id) | **get** /payments/xb-settlements/configs/{configId} | Get a specific cross-border settlement configuration
[**get_xb_settlement_configs**](#get_xb_settlement_configs) | **get** /payments/xb-settlements/configs | Get all the cross-border settlement configurations
[**get_xb_settlement_flow_by_id**](#get_xb_settlement_flow_by_id) | **get** /payments/xb-settlements/flows/{flowId} | Get specific cross-border settlement flow details
[**update_xb_settlement_config**](#update_xb_settlement_config) | **put** /payments/xb-settlements/configs/{configId} | Edit a cross-border settlement configuration

# **create_xb_settlement_config**
<a id="create_xb_settlement_config"></a>
> XBSettlementConfigModel create_xb_settlement_config()

Create a new cross-border settlement configuration

<u><b>Create a new cross-border settlement configuration. </u></b></br>Configurations define the default assets, on-ramps, and off-ramps to use for the cross-border settlement. </br>  A configuration must contain at least two steps - `ON_RAMP` and `VAULT_ACCOUNT`. </br> All other steps (e.g., `OFF_RAMP`, `FIAT_DESTINATION`, etc.) are optional. </br> Every step must include the `accountId` to be used, while `inputAssetId` and `outputAssetId` are optional.  If those are not provided, a default value will be used from the Corridor Settings.</br> If the inputAssetId or the outputAssetId is provided for one of the objects, all assets in the objects must be consistent. For example, if the output asset of ON_RAMP is XLM_USDC_5F3T, then the input asset of the VAULT_ACCOUNT must also be XLM_USDC_5F3T..</br> You can set a slippage amount for your configuration. Slippage is defined by basis points (bps). This value can be overloaded on execution. If you do not configure a slippage amount, the default slippage of 10000 bps (10%) is used. </br> **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_config_model import XBSettlementConfigModel
from fireblocks_client.model.xb_settlement_config_creation_request_body import XBSettlementConfigCreationRequestBody
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()

    # example passing only optional values
    body = XBSettlementConfigCreationRequestBody(
        name="name_example",
        corridor_id=XBSettlementCorridorId("MX_US"),
        steps=XBSettlementConfigStepsRecord(
            step_type=XBSettlementStepType("ON_RAMP"),
        ),
        conversion_slippage_basis_points=XBSettlementConversionSlippageBasisPoints(10000),
    )
    try:
        # Create a new cross-border settlement configuration
        api_response = api_instance.create_xb_settlement_config(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->create_xb_settlement_config: %s\n" % e)
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
[**XBSettlementConfigCreationRequestBody**](../../models/XBSettlementConfigCreationRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_xb_settlement_config.ApiResponseFor200) | Cross-border settlement configuration created successfully
400 | [ApiResponseFor400](#create_xb_settlement_config.ApiResponseFor400) | Error creating cross-border request
401 | [ApiResponseFor401](#create_xb_settlement_config.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#create_xb_settlement_config.ApiResponseFor5XX) | Internal error.

#### create_xb_settlement_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementConfigModel**](../../models/XBSettlementConfigModel.md) |  | 


#### create_xb_settlement_config.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_xb_settlement_config.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_xb_settlement_config.ApiResponseFor5XX
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

# **create_xb_settlement_flow**
<a id="create_xb_settlement_flow"></a>
> XBSettlementFlowPreviewModel create_xb_settlement_flow()

Create a new cross-border settlement flow

Create a cross-border flow (based on a cross-border configuration) with an amount to transfer.  The assetId is defined by the cross-border configuration. Creating a flow triggers a calculation of the flow estimations, including FX rates, times, and fees based on the amount provided. Creating a cross-border flow will not execute the flow.  **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.xb_settlement_flow_preview_model import XBSettlementFlowPreviewModel
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_create_flow_request_body import XBSettlementCreateFlowRequestBody
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()

    # example passing only optional values
    body = XBSettlementCreateFlowRequestBody(
        config_id="config_id_example",
        amount="amount_example",
    )
    try:
        # Create a new cross-border settlement flow
        api_response = api_instance.create_xb_settlement_flow(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->create_xb_settlement_flow: %s\n" % e)
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
[**XBSettlementCreateFlowRequestBody**](../../models/XBSettlementCreateFlowRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_xb_settlement_flow.ApiResponseFor200) | Cross-border settlement flow created successfully
400 | [ApiResponseFor400](#create_xb_settlement_flow.ApiResponseFor400) | Unable to create cross-border flow, invalid configuration ID.
401 | [ApiResponseFor401](#create_xb_settlement_flow.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#create_xb_settlement_flow.ApiResponseFor5XX) | Internal error.

#### create_xb_settlement_flow.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementFlowPreviewModel**](../../models/XBSettlementFlowPreviewModel.md) |  | 


#### create_xb_settlement_flow.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_xb_settlement_flow.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### create_xb_settlement_flow.ApiResponseFor5XX
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

# **delete_xb_settlement_config**
<a id="delete_xb_settlement_config"></a>
> XBSettlementConfigModel delete_xb_settlement_config(config_id)

Delete a cross-border settlement configuration

Delete a cross-border settlement configuration. This does not delete or remove previously executed flows that used this configuration. **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_config_model import XBSettlementConfigModel
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "074791cc-ef32-4920-8373-95efbeea66c5",
    }
    try:
        # Delete a cross-border settlement configuration
        api_response = api_instance.delete_xb_settlement_config(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->delete_xb_settlement_config: %s\n" % e)
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
configId | ConfigIdSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_xb_settlement_config.ApiResponseFor200) | Cross-border settlement configuration deleted successfully. Returns the deleted configuration.
404 | [ApiResponseFor404](#delete_xb_settlement_config.ApiResponseFor404) | No cross-border settlement configuration exists with the provided ID.
401 | [ApiResponseFor401](#delete_xb_settlement_config.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#delete_xb_settlement_config.ApiResponseFor5XX) | Internal error.

#### delete_xb_settlement_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementConfigModel**](../../models/XBSettlementConfigModel.md) |  | 


#### delete_xb_settlement_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_xb_settlement_config.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_xb_settlement_config.ApiResponseFor5XX
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

# **execute_xb_settlement_flow_action**
<a id="execute_xb_settlement_flow_action"></a>
> XBSettlementFlowExecutionModel execute_xb_settlement_flow_action(flow_id)

Execute cross-border settlement flow

Send a payment flow with 'flowId' for execution. If a differet slippage configuraion is needed for this execution than configured in the flow configuration, the request body must define the desired slippage configuration for this execution.  **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.xb_settlement_flow_execution_request_body import XBSettlementFlowExecutionRequestBody
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_flow_execution_model import XBSettlementFlowExecutionModel
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'flowId': "98fb5a8b-65ff-4f15-b89c-80910aedbfb3",
    }
    try:
        # Execute cross-border settlement flow
        api_response = api_instance.execute_xb_settlement_flow_action(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->execute_xb_settlement_flow_action: %s\n" % e)

    # example passing only optional values
    path_params = {
        'flowId': "98fb5a8b-65ff-4f15-b89c-80910aedbfb3",
    }
    body = XBSettlementFlowExecutionRequestBody(
        conversion_slippage_basis_points=XBSettlementConversionSlippageBasisPoints(10000),
    )
    try:
        # Execute cross-border settlement flow
        api_response = api_instance.execute_xb_settlement_flow_action(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->execute_xb_settlement_flow_action: %s\n" % e)
```
### Parameters

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
[**XBSettlementFlowExecutionRequestBody**](../../models/XBSettlementFlowExecutionRequestBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
flowId | FlowIdSchema | | 

# FlowIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#execute_xb_settlement_flow_action.ApiResponseFor200) | Cross-border settlement flow started to execute successfully
400 | [ApiResponseFor400](#execute_xb_settlement_flow_action.ApiResponseFor400) | Error while trying to execute the cross-border flow
404 | [ApiResponseFor404](#execute_xb_settlement_flow_action.ApiResponseFor404) | Invalid flowId.
401 | [ApiResponseFor401](#execute_xb_settlement_flow_action.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#execute_xb_settlement_flow_action.ApiResponseFor5XX) | Internal error.

#### execute_xb_settlement_flow_action.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementFlowExecutionModel**](../../models/XBSettlementFlowExecutionModel.md) |  | 


#### execute_xb_settlement_flow_action.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### execute_xb_settlement_flow_action.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### execute_xb_settlement_flow_action.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### execute_xb_settlement_flow_action.ApiResponseFor5XX
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

# **get_xb_settlement_config_by_id**
<a id="get_xb_settlement_config_by_id"></a>
> XBSettlementConfigModel get_xb_settlement_config_by_id(config_id)

Get a specific cross-border settlement configuration

Get a specific cross-border settlement configuration.</br> **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_config_model import XBSettlementConfigModel
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "074791cc-ef32-4920-8373-95efbeea66c5",
    }
    try:
        # Get a specific cross-border settlement configuration
        api_response = api_instance.get_xb_settlement_config_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->get_xb_settlement_config_by_id: %s\n" % e)
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
configId | ConfigIdSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_xb_settlement_config_by_id.ApiResponseFor200) | Returns the requested cross-border settlement configuration
404 | [ApiResponseFor404](#get_xb_settlement_config_by_id.ApiResponseFor404) | No cross-border settlement configuration exists with the provided ID.
401 | [ApiResponseFor401](#get_xb_settlement_config_by_id.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#get_xb_settlement_config_by_id.ApiResponseFor5XX) | Internal error.

#### get_xb_settlement_config_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementConfigModel**](../../models/XBSettlementConfigModel.md) |  | 


#### get_xb_settlement_config_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_xb_settlement_config_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_xb_settlement_config_by_id.ApiResponseFor5XX
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

# **get_xb_settlement_configs**
<a id="get_xb_settlement_configs"></a>
> XBSettlementGetAllConfigsResponse get_xb_settlement_configs()

Get all the cross-border settlement configurations

Get all the cross-border settlement configurations. </br> **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_get_all_configs_response import XBSettlementGetAllConfigsResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()

    # example, this endpoint has no required or optional parameters
    try:
        # Get all the cross-border settlement configurations
        api_response = api_instance.get_xb_settlement_configs()
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->get_xb_settlement_configs: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_xb_settlement_configs.ApiResponseFor200) | Returns all the cross-border settlement configurations
401 | [ApiResponseFor401](#get_xb_settlement_configs.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#get_xb_settlement_configs.ApiResponseFor5XX) | Internal error.

#### get_xb_settlement_configs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementGetAllConfigsResponse**](../../models/XBSettlementGetAllConfigsResponse.md) |  | 


#### get_xb_settlement_configs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_xb_settlement_configs.ApiResponseFor5XX
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

# **get_xb_settlement_flow_by_id**
<a id="get_xb_settlement_flow_by_id"></a>
> XBSettlementGetFlowResponse get_xb_settlement_flow_by_id(flow_id)

Get specific cross-border settlement flow details

Gets details for a specific cross-border settlement flow **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.xb_settlement_get_flow_response import XBSettlementGetFlowResponse
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
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'flowId': "98fb5a8b-65ff-4f15-b89c-80910aedbfb3",
    }
    try:
        # Get specific cross-border settlement flow details
        api_response = api_instance.get_xb_settlement_flow_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->get_xb_settlement_flow_by_id: %s\n" % e)
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
flowId | FlowIdSchema | | 

# FlowIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_xb_settlement_flow_by_id.ApiResponseFor200) | Returns cross-border settlement flow details. For unexecuted flows, a preview object will return, showing the estimated time, amounts, and fees. Note that this data structure updates as the flow progresses, including the total fees (accumulated), state, and steps. 
404 | [ApiResponseFor404](#get_xb_settlement_flow_by_id.ApiResponseFor404) | Invalid flowId.
401 | [ApiResponseFor401](#get_xb_settlement_flow_by_id.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#get_xb_settlement_flow_by_id.ApiResponseFor5XX) | Internal error.

#### get_xb_settlement_flow_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementGetFlowResponse**](../../models/XBSettlementGetFlowResponse.md) |  | 


#### get_xb_settlement_flow_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_xb_settlement_flow_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_xb_settlement_flow_by_id.ApiResponseFor5XX
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

# **update_xb_settlement_config**
<a id="update_xb_settlement_config"></a>
> XBSettlementConfigModel update_xb_settlement_config(config_id)

Edit a cross-border settlement configuration

Edit a cross-border settlement configuration. Editing a configuration does not affect previously executed flows that used the configuration. **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import payments_cross_border_settlement_api
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_config_model import XBSettlementConfigModel
from fireblocks_client.model.xb_settlement_config_edit_request_body import XBSettlementConfigEditRequestBody
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'configId': "074791cc-ef32-4920-8373-95efbeea66c5",
    }
    try:
        # Edit a cross-border settlement configuration
        api_response = api_instance.update_xb_settlement_config(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->update_xb_settlement_config: %s\n" % e)

    # example passing only optional values
    path_params = {
        'configId': "074791cc-ef32-4920-8373-95efbeea66c5",
    }
    body = XBSettlementConfigEditRequestBody(
        name="name_example",
        steps=XBSettlementConfigStepsRecord(
            step_type=XBSettlementStepType("ON_RAMP"),
        ),
        conversion_slippage_basis_points=XBSettlementConversionSlippageBasisPoints(10000),
    )
    try:
        # Edit a cross-border settlement configuration
        api_response = api_instance.update_xb_settlement_config(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->update_xb_settlement_config: %s\n" % e)
```
### Parameters

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
[**XBSettlementConfigEditRequestBody**](../../models/XBSettlementConfigEditRequestBody.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
configId | ConfigIdSchema | | 

# ConfigIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_xb_settlement_config.ApiResponseFor200) | Cross-border settlement configuration edited successfully
404 | [ApiResponseFor404](#update_xb_settlement_config.ApiResponseFor404) | No cross-border settlement configuration exists with the provided ID.
400 | [ApiResponseFor400](#update_xb_settlement_config.ApiResponseFor400) | Error creating the cross-border request. Configuration not modified.
401 | [ApiResponseFor401](#update_xb_settlement_config.ApiResponseFor401) | Unauthorized. Missing / invalid JWT token in Authorization header.
5XX | [ApiResponseFor5XX](#update_xb_settlement_config.ApiResponseFor5XX) | Internal error.

#### update_xb_settlement_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**XBSettlementConfigModel**](../../models/XBSettlementConfigModel.md) |  | 


#### update_xb_settlement_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_xb_settlement_config.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_xb_settlement_config.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_xb_settlement_config.ApiResponseFor5XX
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

