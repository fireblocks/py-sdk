# fireblocks_client.ContractTemplatesApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contract_template_by_id**](ContractTemplatesApi.md#delete_contract_template_by_id) | **DELETE** /tokenization/templates/{contractTemplateId} | Delete a contract template by id
[**deploy_contract**](ContractTemplatesApi.md#deploy_contract) | **POST** /tokenization/templates/{contractTemplateId}/deploy | Deploy contract
[**get_constructor_by_contract_template_id**](ContractTemplatesApi.md#get_constructor_by_contract_template_id) | **GET** /tokenization/templates/{contractTemplateId}/constructor | Return contract template&#39;s constructor
[**get_contract_template_by_id**](ContractTemplatesApi.md#get_contract_template_by_id) | **GET** /tokenization/templates/{contractTemplateId} | Return contract template by id
[**get_contract_templates**](ContractTemplatesApi.md#get_contract_templates) | **GET** /tokenization/templates | List all contract templates
[**get_function_abi_by_contract_template_id**](ContractTemplatesApi.md#get_function_abi_by_contract_template_id) | **GET** /tokenization/templates/{contractTemplateId}/function | Return contract template&#39;s function
[**upload_contract_template**](ContractTemplatesApi.md#upload_contract_template) | **POST** /tokenization/templates | Upload contract template


# **delete_contract_template_by_id**
> delete_contract_template_by_id(contract_template_id)

Delete a contract template by id

Delete a contract by id. allowed only for private contract templates. Notice: it is irreversible!

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
    contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The Contract Template identifier

    try:
        # Delete a contract template by id
        fireblocks.contract_templates.delete_contract_template_by_id(contract_template_id).result()
    except Exception as e:
        print("Exception when calling ContractTemplatesApi->delete_contract_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_template_id** | **str**| The Contract Template identifier | 

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
**204** | Contract was deleted successfully |  -  |
**404** | Could not find contract. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_contract**
> ContractDeployResponse deploy_contract(contract_template_id, contract_deploy_request, idempotency_key=idempotency_key)

Deploy contract

Deploy a new contract by contract template id. If you wish to deploy a token (ERC20, ERC721 etc), and create asset please use POST /tokenization

### Example


```python
from fireblocks_client.models.contract_deploy_request import ContractDeployRequest
from fireblocks_client.models.contract_deploy_response import ContractDeployResponse
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
    contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The Contract Template identifier
    contract_deploy_request = fireblocks_client.ContractDeployRequest() # ContractDeployRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Deploy contract
        api_response = fireblocks.contract_templates.deploy_contract(contract_template_id, contract_deploy_request, idempotency_key=idempotency_key).result()
        print("The response of ContractTemplatesApi->deploy_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractTemplatesApi->deploy_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_template_id** | **str**| The Contract Template identifier | 
 **contract_deploy_request** | [**ContractDeployRequest**](ContractDeployRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ContractDeployResponse**](ContractDeployResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Contract was deployed successfully |  -  |
**404** | Could not find contract. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constructor_by_contract_template_id**
> AbiFunction get_constructor_by_contract_template_id(contract_template_id, with_docs=with_docs)

Return contract template's constructor

Return contract template's constructor ABI

### Example


```python
from fireblocks_client.models.abi_function import AbiFunction
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
    contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The Contract Template identifier
    with_docs = False # bool | true if you want to get the abi with its docs (optional) (default to False)

    try:
        # Return contract template's constructor
        api_response = fireblocks.contract_templates.get_constructor_by_contract_template_id(contract_template_id, with_docs=with_docs).result()
        print("The response of ContractTemplatesApi->get_constructor_by_contract_template_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractTemplatesApi->get_constructor_by_contract_template_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_template_id** | **str**| The Contract Template identifier | 
 **with_docs** | **bool**| true if you want to get the abi with its docs | [optional] [default to False]

### Return type

[**AbiFunction**](AbiFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract template&#39;s constructor ABI was returned successfully |  -  |
**404** | Could not find contract. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_template_by_id**
> ContractTemplateDto get_contract_template_by_id(contract_template_id)

Return contract template by id

Return detailed information about the contract template

### Example


```python
from fireblocks_client.models.contract_template_dto import ContractTemplateDto
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
    contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The Contract Template identifier

    try:
        # Return contract template by id
        api_response = fireblocks.contract_templates.get_contract_template_by_id(contract_template_id).result()
        print("The response of ContractTemplatesApi->get_contract_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractTemplatesApi->get_contract_template_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_template_id** | **str**| The Contract Template identifier | 

### Return type

[**ContractTemplateDto**](ContractTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract template was returned successfully |  -  |
**404** | Could not find contract. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_templates**
> TemplatesPaginatedResponse get_contract_templates(limit=limit, offset=offset, page_cursor=page_cursor, page_size=page_size, type=type, initialization_phase=initialization_phase)

List all contract templates

Return minimal representation of all the contract templates available for the workspace

### Example


```python
from fireblocks_client.models.templates_paginated_response import TemplatesPaginatedResponse
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
    limit = 100 # float | Items per page (max 100) (optional) (default to 100)
    offset = 0 # float | Paging offset (optional) (default to 0)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page (optional)
    page_size = 10 # float | Number of items per page, requesting more then max will return max items (optional)
    type = 'FUNGIBLE_TOKEN' # str | The type of the contract templates you wish to retrieve. Can accept one type, more or none (optional)
    initialization_phase = 'initialization_phase_example' # str |  (optional)

    try:
        # List all contract templates
        api_response = fireblocks.contract_templates.get_contract_templates(limit=limit, offset=offset, page_cursor=page_cursor, page_size=page_size, type=type, initialization_phase=initialization_phase).result()
        print("The response of ContractTemplatesApi->get_contract_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractTemplatesApi->get_contract_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Items per page (max 100) | [optional] [default to 100]
 **offset** | **float**| Paging offset | [optional] [default to 0]
 **page_cursor** | **str**| Page cursor to get the next page | [optional] 
 **page_size** | **float**| Number of items per page, requesting more then max will return max items | [optional] 
 **type** | **str**| The type of the contract templates you wish to retrieve. Can accept one type, more or none | [optional] 
 **initialization_phase** | **str**|  | [optional] 

### Return type

[**TemplatesPaginatedResponse**](TemplatesPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of contract templates was returned successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_function_abi_by_contract_template_id**
> AbiFunction get_function_abi_by_contract_template_id(contract_template_id, function_signature)

Return contract template's function

Return contract template`s function ABI by signature

### Example


```python
from fireblocks_client.models.abi_function import AbiFunction
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
    contract_template_id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The Contract Template identifier
    function_signature = 'function_signature_example' # str | 

    try:
        # Return contract template's function
        api_response = fireblocks.contract_templates.get_function_abi_by_contract_template_id(contract_template_id, function_signature).result()
        print("The response of ContractTemplatesApi->get_function_abi_by_contract_template_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractTemplatesApi->get_function_abi_by_contract_template_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_template_id** | **str**| The Contract Template identifier | 
 **function_signature** | **str**|  | 

### Return type

[**AbiFunction**](AbiFunction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract template&#x60;s function ABI was returned successfully |  -  |
**404** | Could not find contract. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_contract_template**
> ContractTemplateDto upload_contract_template(contract_upload_request, idempotency_key=idempotency_key)

Upload contract template

Upload a new contract template. This contract template will be available for the workspace

### Example


```python
from fireblocks_client.models.contract_template_dto import ContractTemplateDto
from fireblocks_client.models.contract_upload_request import ContractUploadRequest
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
    contract_upload_request = fireblocks_client.ContractUploadRequest() # ContractUploadRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Upload contract template
        api_response = fireblocks.contract_templates.upload_contract_template(contract_upload_request, idempotency_key=idempotency_key).result()
        print("The response of ContractTemplatesApi->upload_contract_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractTemplatesApi->upload_contract_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_upload_request** | [**ContractUploadRequest**](ContractUploadRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ContractTemplateDto**](ContractTemplateDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contract was uploaded successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

