# fireblocks_client.ContractInteractionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deployed_contract_abi**](ContractInteractionsApi.md#get_deployed_contract_abi) | **GET** /contract_interactions/base_asset_id/{assetId}/contract_address/{contractAddress}/functions | Return deployed contract&#39;s ABI
[**read_call_function**](ContractInteractionsApi.md#read_call_function) | **POST** /contract_interactions/base_asset_id/{assetId}/contract_address/{contractAddress}/functions/read | Call a read function on a deployed contract
[**write_call_function**](ContractInteractionsApi.md#write_call_function) | **POST** /contract_interactions/base_asset_id/{assetId}/contract_address/{contractAddress}/functions/write | Call a write function on a deployed contract


# **get_deployed_contract_abi**
> ContractAbiResponseDto get_deployed_contract_abi(contract_address, asset_id, idempotency_key=idempotency_key)

Return deployed contract's ABI

Return deployed contract's ABI by blockchain native asset id and contract address

### Example


```python
import fireblocks_client
from fireblocks_client.models.contract_abi_response_dto import ContractAbiResponseDto
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
    api_instance = fireblocks_client.ContractInteractionsApi(api_client)
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract's onchain address
    asset_id = 'asset_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Return deployed contract's ABI
        api_response = api_instance.get_deployed_contract_abi(contract_address, asset_id, idempotency_key=idempotency_key)
        print("The response of ContractInteractionsApi->get_deployed_contract_abi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractInteractionsApi->get_deployed_contract_abi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_address** | **str**| The contract&#39;s onchain address | 
 **asset_id** | **str**|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ContractAbiResponseDto**](ContractAbiResponseDto.md)

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

# **read_call_function**
> List[ParameterWithValue] read_call_function(contract_address, asset_id, read_call_function_dto, idempotency_key=idempotency_key)

Call a read function on a deployed contract

Call a read function on a deployed contract by blockchain native asset id and contract address

### Example


```python
import fireblocks_client
from fireblocks_client.models.parameter_with_value import ParameterWithValue
from fireblocks_client.models.read_call_function_dto import ReadCallFunctionDto
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
    api_instance = fireblocks_client.ContractInteractionsApi(api_client)
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract's onchain address
    asset_id = 'asset_id_example' # str | 
    read_call_function_dto = fireblocks_client.ReadCallFunctionDto() # ReadCallFunctionDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Call a read function on a deployed contract
        api_response = api_instance.read_call_function(contract_address, asset_id, read_call_function_dto, idempotency_key=idempotency_key)
        print("The response of ContractInteractionsApi->read_call_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractInteractionsApi->read_call_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_address** | **str**| The contract&#39;s onchain address | 
 **asset_id** | **str**|  | 
 **read_call_function_dto** | [**ReadCallFunctionDto**](ReadCallFunctionDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**List[ParameterWithValue]**](ParameterWithValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Read Call Retrieved Successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_call_function**
> WriteCallFunctionResponseDto write_call_function(contract_address, asset_id, write_call_function_dto, idempotency_key=idempotency_key)

Call a write function on a deployed contract

Call a write function on a deployed contract by blockchain native asset id and contract address. This creates an onchain transaction, thus it is an async operation. It returns a transaction id that can be polled for status check

### Example


```python
import fireblocks_client
from fireblocks_client.models.write_call_function_dto import WriteCallFunctionDto
from fireblocks_client.models.write_call_function_response_dto import WriteCallFunctionResponseDto
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
    api_instance = fireblocks_client.ContractInteractionsApi(api_client)
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract's onchain address
    asset_id = 'asset_id_example' # str | 
    write_call_function_dto = fireblocks_client.WriteCallFunctionDto() # WriteCallFunctionDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Call a write function on a deployed contract
        api_response = api_instance.write_call_function(contract_address, asset_id, write_call_function_dto, idempotency_key=idempotency_key)
        print("The response of ContractInteractionsApi->write_call_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractInteractionsApi->write_call_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_address** | **str**| The contract&#39;s onchain address | 
 **asset_id** | **str**|  | 
 **write_call_function_dto** | [**WriteCallFunctionDto**](WriteCallFunctionDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**WriteCallFunctionResponseDto**](WriteCallFunctionResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

