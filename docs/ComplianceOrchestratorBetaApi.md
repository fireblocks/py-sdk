# fireblocks.ComplianceOrchestratorBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_screening_result**](ComplianceOrchestratorBetaApi.md#get_screening_result) | **GET** /compliance/orchestrator/screenings/{screeningId} | Get a Compliance Orchestrator screening&#39;s result
[**get_workflow**](ComplianceOrchestratorBetaApi.md#get_workflow) | **GET** /compliance/orchestrator/workflows/{workflowId} | Get a Compliance Orchestrator workflow
[**trigger_screening**](ComplianceOrchestratorBetaApi.md#trigger_screening) | **POST** /compliance/orchestrator/screenings | Trigger a Compliance Orchestrator screening
[**update_workflow_status**](ComplianceOrchestratorBetaApi.md#update_workflow_status) | **PATCH** /compliance/orchestrator/workflows/{workflowId}/status | Update a Compliance Orchestrator workflow&#39;s status


# **get_screening_result**
> GetScreeningResultResponse get_screening_result(screening_id)

Get a Compliance Orchestrator screening's result

Returns the result of a screening started by `POST /v1/compliance/orchestrator/screenings`, with a result per workflow step and an audit log. Safe to poll: a screening still in flight reports `PENDING` or `RUNNING`. Only screenings owned by the requesting tenant are returned.

### Example


```python
from fireblocks.models.get_screening_result_response import GetScreeningResultResponse
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
    screening_id = 'a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d' # str | The screening's identifier, returned by `POST /v1/compliance/orchestrator/screenings`.

    try:
        # Get a Compliance Orchestrator screening's result
        api_response = fireblocks.compliance_orchestrator_beta.get_screening_result(screening_id).result()
        print("The response of ComplianceOrchestratorBetaApi->get_screening_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceOrchestratorBetaApi->get_screening_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_id** | **str**| The screening&#39;s identifier, returned by &#x60;POST /v1/compliance/orchestrator/screenings&#x60;. | 

### Return type

[**GetScreeningResultResponse**](GetScreeningResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screening result |  * X-Request-ID -  <br>  |
**400** | Invalid request arguments. |  * X-Request-ID -  <br>  |
**404** | Screening result not found. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow**
> GetWorkflowResponse get_workflow(workflow_id)

Get a Compliance Orchestrator workflow

Returns a workflow's status and its steps in execution order. Read it to see what a given `workflowId` will screen, and which fields its rules may reference.

### Example


```python
from fireblocks.models.get_workflow_response import GetWorkflowResponse
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
    workflow_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | The workflow's identifier.

    try:
        # Get a Compliance Orchestrator workflow
        api_response = fireblocks.compliance_orchestrator_beta.get_workflow(workflow_id).result()
        print("The response of ComplianceOrchestratorBetaApi->get_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceOrchestratorBetaApi->get_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| The workflow&#39;s identifier. | 

### Return type

[**GetWorkflowResponse**](GetWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workflow |  * X-Request-ID -  <br>  |
**400** | Invalid request arguments. |  * X-Request-ID -  <br>  |
**404** | Workflow not found. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_screening**
> TriggerScreeningResponse trigger_screening(trigger_screening_request, idempotency_key=idempotency_key)

Trigger a Compliance Orchestrator screening

Starts a compliance screening against an active workflow and returns a `screeningId`. The screening runs asynchronously — poll `GET /v1/compliance/orchestrator/screenings/{screeningId}` for the result.

Unlike the screening that applies automatically to submitted transactions under `/v1/screening`, this is called on demand, before anything exists on-chain.

### Example


```python
from fireblocks.models.trigger_screening_request import TriggerScreeningRequest
from fireblocks.models.trigger_screening_response import TriggerScreeningResponse
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
    trigger_screening_request = fireblocks.TriggerScreeningRequest() # TriggerScreeningRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Trigger a Compliance Orchestrator screening
        api_response = fireblocks.compliance_orchestrator_beta.trigger_screening(trigger_screening_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceOrchestratorBetaApi->trigger_screening:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceOrchestratorBetaApi->trigger_screening: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_screening_request** | [**TriggerScreeningRequest**](TriggerScreeningRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TriggerScreeningResponse**](TriggerScreeningResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Screening accepted |  * X-Request-ID -  <br>  |
**400** | Invalid or missing required input fields. |  * X-Request-ID -  <br>  |
**404** | Workflow not found. |  * X-Request-ID -  <br>  |
**409** | Workflow is not active. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow_status**
> UpdateWorkflowStatusResponse update_workflow_status(workflow_id, update_workflow_status_request, idempotency_key=idempotency_key)

Update a Compliance Orchestrator workflow's status

Moves a workflow between `DRAFT` and `ACTIVE`. A workflow must be `ACTIVE` before `POST /v1/compliance/orchestrator/screenings` will accept a screening against it. Returns the workflow's id and new status, not its full configuration.

### Example


```python
from fireblocks.models.update_workflow_status_request import UpdateWorkflowStatusRequest
from fireblocks.models.update_workflow_status_response import UpdateWorkflowStatusResponse
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
    workflow_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479' # str | The workflow's identifier.
    update_workflow_status_request = fireblocks.UpdateWorkflowStatusRequest() # UpdateWorkflowStatusRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update a Compliance Orchestrator workflow's status
        api_response = fireblocks.compliance_orchestrator_beta.update_workflow_status(workflow_id, update_workflow_status_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceOrchestratorBetaApi->update_workflow_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceOrchestratorBetaApi->update_workflow_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| The workflow&#39;s identifier. | 
 **update_workflow_status_request** | [**UpdateWorkflowStatusRequest**](UpdateWorkflowStatusRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**UpdateWorkflowStatusResponse**](UpdateWorkflowStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workflow status updated |  * X-Request-ID -  <br>  |
**400** | Invalid request arguments. |  * X-Request-ID -  <br>  |
**404** | Workflow not found. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

