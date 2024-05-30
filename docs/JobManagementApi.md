# fireblocks_client.JobManagementApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobManagementApi.md#cancel_job) | **POST** /batch/{jobId}/cancel | Cancel a running job
[**continue_job**](JobManagementApi.md#continue_job) | **POST** /batch/{jobId}/continue | Continue a paused job
[**get_job**](JobManagementApi.md#get_job) | **GET** /batch/{jobId} | Get job details
[**get_job_tasks**](JobManagementApi.md#get_job_tasks) | **GET** /batch/{jobId}/tasks | Return a list of tasks for given job
[**get_jobs**](JobManagementApi.md#get_jobs) | **GET** /batch/jobs | Return a list of jobs belonging to tenant
[**pause_job**](JobManagementApi.md#pause_job) | **POST** /batch/{jobId}/pause | Pause a job


# **cancel_job**
> cancel_job(job_id, idempotency_key=idempotency_key)

Cancel a running job

Stop the given job immediately. If the job is in the ‘Active’ state, the job will be canceled after completing the current task. Vault accounts and Wallets that are already created will not be affected.

### Example


```python
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath

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
    job_id = 'job_id_example' # str | The requested job id
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Cancel a running job
        fireblocks.job_management.cancel_job(job_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling JobManagementApi->cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The requested job id | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | canceled successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **continue_job**
> continue_job(job_id, idempotency_key=idempotency_key)

Continue a paused job

Continue the given paused job.

### Example


```python
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath

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
    job_id = 'job_id_example' # str | The requested job id
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Continue a paused job
        fireblocks.job_management.continue_job(job_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling JobManagementApi->continue_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The requested job id | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | continued successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(job_id)

Get job details

Get an object describing the given job

### Example


```python
from fireblocks_client.models.job import Job
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
    job_id = 'job_id_example' # str | The requested job id

    try:
        # Get job details
        api_response = fireblocks.job_management.get_job(job_id).result()
        print("The response of JobManagementApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobManagementApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The requested job id | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON object that describes the job |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_tasks**
> List[Task] get_job_tasks(job_id)

Return a list of tasks for given job

Return a list of tasks for given job

### Example


```python
from fireblocks_client.models.task import Task
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
    job_id = 'job_id_example' # str | The requested job id

    try:
        # Return a list of tasks for given job
        api_response = fireblocks.job_management.get_job_tasks(job_id).result()
        print("The response of JobManagementApi->get_job_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobManagementApi->get_job_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The requested job id | 

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of tasks |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs**
> List[Job] get_jobs(from_time=from_time, to_time=to_time)

Return a list of jobs belonging to tenant

Get an array of objects including all active, paused, canceled, and complete jobs in a workspace.

### Example


```python
from fireblocks_client.models.job import Job
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
    from_time = 56 # int | Start of time range in ms since 1970 (optional)
    to_time = 56 # int | End of time range in ms since 1970 (optional)

    try:
        # Return a list of jobs belonging to tenant
        api_response = fireblocks.job_management.get_jobs(from_time=from_time, to_time=to_time).result()
        print("The response of JobManagementApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobManagementApi->get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_time** | **int**| Start of time range in ms since 1970 | [optional] 
 **to_time** | **int**| End of time range in ms since 1970 | [optional] 

### Return type

[**List[Job]**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of jobs |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_job**
> pause_job(job_id, idempotency_key=idempotency_key)

Pause a job

Pause the given job, after the current task is done. A paused job can later be resumed by calling ‘continue’, or canceled.

### Example


```python
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath

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
    job_id = 'job_id_example' # str | The requested job id
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Pause a job
        fireblocks.job_management.pause_job(job_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling JobManagementApi->pause_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The requested job id | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | paused successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

