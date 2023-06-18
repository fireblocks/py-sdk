# fireblocks_client.PaymentsCrossBorderSettlementApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_xb_settlement_config**](PaymentsCrossBorderSettlementApi.md#create_xb_settlement_config) | **POST** /payments/xb-settlements/configs | Create a new cross-border settlement configuration
[**create_xb_settlement_flow**](PaymentsCrossBorderSettlementApi.md#create_xb_settlement_flow) | **POST** /payments/xb-settlements/flows | Create a new cross-border settlement flow
[**delete_xb_settlement_config**](PaymentsCrossBorderSettlementApi.md#delete_xb_settlement_config) | **DELETE** /payments/xb-settlements/configs/{configId} | Delete a cross-border settlement configuration
[**execute_xb_settlement_flow_action**](PaymentsCrossBorderSettlementApi.md#execute_xb_settlement_flow_action) | **POST** /payments/xb-settlements/flows/{flowId}/actions/execute | Execute cross-border settlement flow
[**get_xb_settlement_config_by_id**](PaymentsCrossBorderSettlementApi.md#get_xb_settlement_config_by_id) | **GET** /payments/xb-settlements/configs/{configId} | Get a specific cross-border settlement configuration
[**get_xb_settlement_configs**](PaymentsCrossBorderSettlementApi.md#get_xb_settlement_configs) | **GET** /payments/xb-settlements/configs | Get all the cross-border settlement configurations
[**get_xb_settlement_flow_by_id**](PaymentsCrossBorderSettlementApi.md#get_xb_settlement_flow_by_id) | **GET** /payments/xb-settlements/flows/{flowId} | Get specific cross-border settlement flow details
[**update_xb_settlement_config**](PaymentsCrossBorderSettlementApi.md#update_xb_settlement_config) | **PUT** /payments/xb-settlements/configs/{configId} | Edit a cross-border settlement configuration


# **create_xb_settlement_config**
> XBSettlementConfigModel create_xb_settlement_config(xb_settlement_config_creation_request_body=xb_settlement_config_creation_request_body)

Create a new cross-border settlement configuration

<u><b>Create a new cross-border settlement configuration. </u></b></br>Configurations define the default assets, on-ramps, and off-ramps to use for the cross-border settlement. </br>  A configuration must contain at least two steps - `ON_RAMP` and `VAULT_ACCOUNT`. </br> All other steps (e.g., `OFF_RAMP`, `FIAT_DESTINATION`, etc.) are optional. </br> Every step must include the `accountId` to be used, while `inputAssetId` and `outputAssetId` are optional.  If those are not provided, a default value will be used from the Corridor Settings.</br> If the inputAssetId or the outputAssetId is provided for one of the objects, all assets in the objects must be consistent. For example, if the output asset of ON_RAMP is XLM_USDC_5F3T, then the input asset of the VAULT_ACCOUNT must also be XLM_USDC_5F3T..</br> You can set a slippage amount for your configuration. Slippage is defined by basis points (bps). This value can be overloaded on execution. If you do not configure a slippage amount, the default slippage of 10000 bps (10%) is used. </br> **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)
    xb_settlement_config_creation_request_body = {"name":"Flow Config Example","corridorId":"CO_US","steps":{"ON_RAMP":{"accountId":"3b7a1451-3453-4c96-a6a5-683cc8971d04"},"VAULT_ACCOUNT":{"accountId":"2"},"OFF_RAMP":{"accountId":"f2f74204-93ec-4614-870a-4ea2ad13aa0b"}},"conversionSlippageBasisPoints":75} # XBSettlementConfigCreationRequestBody |  (optional)

    try:
        # Create a new cross-border settlement configuration
        api_response = api_instance.create_xb_settlement_config(xb_settlement_config_creation_request_body=xb_settlement_config_creation_request_body)
        print("The response of PaymentsCrossBorderSettlementApi->create_xb_settlement_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->create_xb_settlement_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xb_settlement_config_creation_request_body** | [**XBSettlementConfigCreationRequestBody**](XBSettlementConfigCreationRequestBody.md)|  | [optional] 

### Return type

[**XBSettlementConfigModel**](XBSettlementConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cross-border settlement configuration created successfully |  -  |
**400** | Error creating cross-border request |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_xb_settlement_flow**
> XBSettlementFlowPreviewModel create_xb_settlement_flow(xb_settlement_create_flow_request_body=xb_settlement_create_flow_request_body)

Create a new cross-border settlement flow

Create a cross-border flow (based on a cross-border configuration) with an amount to transfer.  The assetId is defined by the cross-border configuration. Creating a flow triggers a calculation of the flow estimations, including FX rates, times, and fees based on the amount provided. Creating a cross-border flow will not execute the flow.  **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)
    xb_settlement_create_flow_request_body = {"configId":"a4b0a706-4578-4467-bd5b-a852761dd2aa","amount":"100"} # XBSettlementCreateFlowRequestBody |  (optional)

    try:
        # Create a new cross-border settlement flow
        api_response = api_instance.create_xb_settlement_flow(xb_settlement_create_flow_request_body=xb_settlement_create_flow_request_body)
        print("The response of PaymentsCrossBorderSettlementApi->create_xb_settlement_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->create_xb_settlement_flow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xb_settlement_create_flow_request_body** | [**XBSettlementCreateFlowRequestBody**](XBSettlementCreateFlowRequestBody.md)|  | [optional] 

### Return type

[**XBSettlementFlowPreviewModel**](XBSettlementFlowPreviewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cross-border settlement flow created successfully |  -  |
**400** | Unable to create cross-border flow, invalid configuration ID. |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_xb_settlement_config**
> XBSettlementConfigModel delete_xb_settlement_config(config_id)

Delete a cross-border settlement configuration

Delete a cross-border settlement configuration. This does not delete or remove previously executed flows that used this configuration. **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)
    config_id = '074791cc-ef32-4920-8373-95efbeea66c5' # str | The cross-border settlement configuration ID.

    try:
        # Delete a cross-border settlement configuration
        api_response = api_instance.delete_xb_settlement_config(config_id)
        print("The response of PaymentsCrossBorderSettlementApi->delete_xb_settlement_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->delete_xb_settlement_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The cross-border settlement configuration ID. | 

### Return type

[**XBSettlementConfigModel**](XBSettlementConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cross-border settlement configuration deleted successfully. Returns the deleted configuration. |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | No cross-border settlement configuration exists with the provided ID. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_xb_settlement_flow_action**
> XBSettlementFlowExecutionModel execute_xb_settlement_flow_action(flow_id, xb_settlement_flow_execution_request_body=xb_settlement_flow_execution_request_body)

Execute cross-border settlement flow

Send a payment flow with 'flowId' for execution. If a differet slippage configuraion is needed for this execution than configured in the flow configuration, the request body must define the desired slippage configuration for this execution.  **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)
    flow_id = '98fb5a8b-65ff-4f15-b89c-80910aedbfb3' # str | The cross-border settlement flow ID.
    xb_settlement_flow_execution_request_body = {"conversionSlippageBasisPoints":10} # XBSettlementFlowExecutionRequestBody |  (optional)

    try:
        # Execute cross-border settlement flow
        api_response = api_instance.execute_xb_settlement_flow_action(flow_id, xb_settlement_flow_execution_request_body=xb_settlement_flow_execution_request_body)
        print("The response of PaymentsCrossBorderSettlementApi->execute_xb_settlement_flow_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->execute_xb_settlement_flow_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**| The cross-border settlement flow ID. | 
 **xb_settlement_flow_execution_request_body** | [**XBSettlementFlowExecutionRequestBody**](XBSettlementFlowExecutionRequestBody.md)|  | [optional] 

### Return type

[**XBSettlementFlowExecutionModel**](XBSettlementFlowExecutionModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cross-border settlement flow started to execute successfully |  -  |
**400** | Error while trying to execute the cross-border flow |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | Invalid flowId. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xb_settlement_config_by_id**
> XBSettlementConfigModel get_xb_settlement_config_by_id(config_id)

Get a specific cross-border settlement configuration

Get a specific cross-border settlement configuration.</br> **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)
    config_id = '074791cc-ef32-4920-8373-95efbeea66c5' # str | The cross-border settlement configuration ID.

    try:
        # Get a specific cross-border settlement configuration
        api_response = api_instance.get_xb_settlement_config_by_id(config_id)
        print("The response of PaymentsCrossBorderSettlementApi->get_xb_settlement_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->get_xb_settlement_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The cross-border settlement configuration ID. | 

### Return type

[**XBSettlementConfigModel**](XBSettlementConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested cross-border settlement configuration |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | No cross-border settlement configuration exists with the provided ID. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xb_settlement_configs**
> XBSettlementGetAllConfigsResponse get_xb_settlement_configs()

Get all the cross-border settlement configurations

Get all the cross-border settlement configurations. </br> **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)

    try:
        # Get all the cross-border settlement configurations
        api_response = api_instance.get_xb_settlement_configs()
        print("The response of PaymentsCrossBorderSettlementApi->get_xb_settlement_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->get_xb_settlement_configs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**XBSettlementGetAllConfigsResponse**](XBSettlementGetAllConfigsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all the cross-border settlement configurations |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xb_settlement_flow_by_id**
> XBSettlementGetFlowResponse get_xb_settlement_flow_by_id(flow_id)

Get specific cross-border settlement flow details

Gets details for a specific cross-border settlement flow **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)
    flow_id = '98fb5a8b-65ff-4f15-b89c-80910aedbfb3' # str | The cross-border settlement flow ID.

    try:
        # Get specific cross-border settlement flow details
        api_response = api_instance.get_xb_settlement_flow_by_id(flow_id)
        print("The response of PaymentsCrossBorderSettlementApi->get_xb_settlement_flow_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->get_xb_settlement_flow_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_id** | **str**| The cross-border settlement flow ID. | 

### Return type

[**XBSettlementGetFlowResponse**](XBSettlementGetFlowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns cross-border settlement flow details. For unexecuted flows, a preview object will return, showing the estimated time, amounts, and fees. Note that this data structure updates as the flow progresses, including the total fees (accumulated), state, and steps.  |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | Invalid flowId. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_xb_settlement_config**
> XBSettlementConfigModel update_xb_settlement_config(config_id, xb_settlement_config_edit_request_body=xb_settlement_config_edit_request_body)

Edit a cross-border settlement configuration

Edit a cross-border settlement configuration. Editing a configuration does not affect previously executed flows that used the configuration. **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoint includes APIs available only for customers with the Payments Engine enabled on their accounts. These endpoints are currently in beta and might be subject to changes. If you want to learn more about the Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

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
    api_instance = fireblocks_client.PaymentsCrossBorderSettlementApi(api_client)
    config_id = '074791cc-ef32-4920-8373-95efbeea66c5' # str | The cross-border settlement configuration ID.
    xb_settlement_config_edit_request_body = {"name":"Flow Config Example - Edited","steps":{"ON_RAMP":{"accountId":"e9dec04a-3c57-4052-a89a-288c545f6430"},"VAULT_ACCOUNT":{"accountId":"2"},"OFF_RAMP":{"accountId":"f2f74204-93ec-4614-870a-4ea2ad13aa0b"}},"corridorId":"CO_US","conversionSlippageBasisPoints":30} # XBSettlementConfigEditRequestBody |  (optional)

    try:
        # Edit a cross-border settlement configuration
        api_response = api_instance.update_xb_settlement_config(config_id, xb_settlement_config_edit_request_body=xb_settlement_config_edit_request_body)
        print("The response of PaymentsCrossBorderSettlementApi->update_xb_settlement_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsCrossBorderSettlementApi->update_xb_settlement_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| The cross-border settlement configuration ID. | 
 **xb_settlement_config_edit_request_body** | [**XBSettlementConfigEditRequestBody**](XBSettlementConfigEditRequestBody.md)|  | [optional] 

### Return type

[**XBSettlementConfigModel**](XBSettlementConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cross-border settlement configuration edited successfully |  -  |
**400** | Error creating the cross-border request. Configuration not modified. |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | No cross-border settlement configuration exists with the provided ID. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

