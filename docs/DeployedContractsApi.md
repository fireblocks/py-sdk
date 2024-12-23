# fireblocks.DeployedContractsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contract_abi**](DeployedContractsApi.md#add_contract_abi) | **POST** /tokenization/contracts/abi | Save contract ABI
[**fetch_contract_abi**](DeployedContractsApi.md#fetch_contract_abi) | **POST** /tokenization/contracts/fetch_abi | Fetch the contract ABI
[**get_deployed_contract_by_address**](DeployedContractsApi.md#get_deployed_contract_by_address) | **GET** /tokenization/contracts/{assetId}/{contractAddress} | Return deployed contract data
[**get_deployed_contract_by_id**](DeployedContractsApi.md#get_deployed_contract_by_id) | **GET** /tokenization/contracts/{id} | Return deployed contract data by id
[**get_deployed_contracts**](DeployedContractsApi.md#get_deployed_contracts) | **GET** /tokenization/contracts | List deployed contracts data


# **add_contract_abi**
> ContractWithAbiDto add_contract_abi(add_abi_request_dto, idempotency_key=idempotency_key)

Save contract ABI

Save contract ABI for the tenant

### Example


```python
from fireblocks.models.add_abi_request_dto import AddAbiRequestDto
from fireblocks.models.contract_with_abi_dto import ContractWithAbiDto
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
    add_abi_request_dto = fireblocks.AddAbiRequestDto() # AddAbiRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Save contract ABI
        api_response = fireblocks.deployed_contracts.add_contract_abi(add_abi_request_dto, idempotency_key=idempotency_key).result()
        print("The response of DeployedContractsApi->add_contract_abi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeployedContractsApi->add_contract_abi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_abi_request_dto** | [**AddAbiRequestDto**](AddAbiRequestDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ContractWithAbiDto**](ContractWithAbiDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract ABI created (or updated) for the tenant |  -  |
**409** | Contract ABI already exists. |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_contract_abi**
> ContractWithAbiDto fetch_contract_abi(fetch_abi_request_dto, idempotency_key=idempotency_key)

Fetch the contract ABI

Fetch the ABI. If not found fetch the ABI from the block explorer

### Example


```python
from fireblocks.models.contract_with_abi_dto import ContractWithAbiDto
from fireblocks.models.fetch_abi_request_dto import FetchAbiRequestDto
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
    fetch_abi_request_dto = fireblocks.FetchAbiRequestDto() # FetchAbiRequestDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Fetch the contract ABI
        api_response = fireblocks.deployed_contracts.fetch_contract_abi(fetch_abi_request_dto, idempotency_key=idempotency_key).result()
        print("The response of DeployedContractsApi->fetch_contract_abi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeployedContractsApi->fetch_contract_abi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_abi_request_dto** | [**FetchAbiRequestDto**](FetchAbiRequestDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ContractWithAbiDto**](ContractWithAbiDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract ABI found. |  -  |
**404** | Contract ABI not found |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_contract_by_address**
> DeployedContractResponseDto get_deployed_contract_by_address(contract_address, asset_id)

Return deployed contract data

Return deployed contract data by blockchain native asset id and contract address

### Example


```python
from fireblocks.models.deployed_contract_response_dto import DeployedContractResponseDto
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
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract's onchain address
    asset_id = 'asset_id_example' # str | 

    try:
        # Return deployed contract data
        api_response = fireblocks.deployed_contracts.get_deployed_contract_by_address(contract_address, asset_id).result()
        print("The response of DeployedContractsApi->get_deployed_contract_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeployedContractsApi->get_deployed_contract_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_address** | **str**| The contract&#39;s onchain address | 
 **asset_id** | **str**|  | 

### Return type

[**DeployedContractResponseDto**](DeployedContractResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_contract_by_id**
> DeployedContractResponseDto get_deployed_contract_by_id(id)

Return deployed contract data by id

Return deployed contract data by id

### Example


```python
from fireblocks.models.deployed_contract_response_dto import DeployedContractResponseDto
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
    id = 'b70701f4-d7b1-4795-a8ee-b09cdb5b850d' # str | The deployed contract data identifier

    try:
        # Return deployed contract data by id
        api_response = fireblocks.deployed_contracts.get_deployed_contract_by_id(id).result()
        print("The response of DeployedContractsApi->get_deployed_contract_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeployedContractsApi->get_deployed_contract_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The deployed contract data identifier | 

### Return type

[**DeployedContractResponseDto**](DeployedContractResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_contracts**
> DeployedContractsPaginatedResponse get_deployed_contracts(page_cursor=page_cursor, page_size=page_size, contract_address=contract_address, base_asset_id=base_asset_id, contract_template_id=contract_template_id)

List deployed contracts data

Return a filtered lean representation of the deployed contracts data on all blockchains (paginated)

### Example


```python
from fireblocks.models.deployed_contracts_paginated_response import DeployedContractsPaginatedResponse
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
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page (optional)
    page_size = 10 # float | Number of items per page, requesting more then max will return max items (optional)
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract's onchain address (optional)
    base_asset_id = 'base_asset_id_example' # str |  (optional)
    contract_template_id = 'contract_template_id_example' # str |  (optional)

    try:
        # List deployed contracts data
        api_response = fireblocks.deployed_contracts.get_deployed_contracts(page_cursor=page_cursor, page_size=page_size, contract_address=contract_address, base_asset_id=base_asset_id, contract_template_id=contract_template_id).result()
        print("The response of DeployedContractsApi->get_deployed_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeployedContractsApi->get_deployed_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Page cursor to get the next page | [optional] 
 **page_size** | **float**| Number of items per page, requesting more then max will return max items | [optional] 
 **contract_address** | **str**| The contract&#39;s onchain address | [optional] 
 **base_asset_id** | **str**|  | [optional] 
 **contract_template_id** | **str**|  | [optional] 

### Return type

[**DeployedContractsPaginatedResponse**](DeployedContractsPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deployed contracts fetched successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

