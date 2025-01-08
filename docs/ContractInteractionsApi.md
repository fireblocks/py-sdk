# fireblocks.ContractInteractionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deployed_contract_abi**](ContractInteractionsApi.md#get_deployed_contract_abi) | **GET** /contract_interactions/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/functions | Return deployed contract&#39;s ABI
[**get_transaction_receipt**](ContractInteractionsApi.md#get_transaction_receipt) | **GET** /contract_interactions/base_asset_id/{baseAssetId}/tx_hash/{txHash}/receipt | Get transaction receipt
[**read_call_function**](ContractInteractionsApi.md#read_call_function) | **POST** /contract_interactions/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/functions/read | Call a read function on a deployed contract
[**write_call_function**](ContractInteractionsApi.md#write_call_function) | **POST** /contract_interactions/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/functions/write | Call a write function on a deployed contract


# **get_deployed_contract_abi**
> ContractAbiResponseDto get_deployed_contract_abi(contract_address, base_asset_id, idempotency_key=idempotency_key)

Return deployed contract's ABI

Return deployed contract's ABI by blockchain native asset id and contract address

### Example


```python
from fireblocks.models.contract_abi_response_dto import ContractAbiResponseDto
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
    base_asset_id = 'base_asset_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Return deployed contract's ABI
        api_response = fireblocks.contract_interactions.get_deployed_contract_abi(contract_address, base_asset_id, idempotency_key=idempotency_key).result()
        print("The response of ContractInteractionsApi->get_deployed_contract_abi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractInteractionsApi->get_deployed_contract_abi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_address** | **str**| The contract&#39;s onchain address | 
 **base_asset_id** | **str**|  | 
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

# **get_transaction_receipt**
> TransactionReceiptResponse get_transaction_receipt(base_asset_id, tx_hash)

Get transaction receipt

Retrieve the transaction receipt by blockchain native asset ID and transaction hash

### Example


```python
from fireblocks.models.transaction_receipt_response import TransactionReceiptResponse
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
    base_asset_id = 'ETH_TEST6' # str | The blockchain base assetId
    tx_hash = '0x3b015ca0518c55d7bff4e3f5aa5d0431705771553ba8a95cf20e34cb597f57f6' # str | The transaction hash

    try:
        # Get transaction receipt
        api_response = fireblocks.contract_interactions.get_transaction_receipt(base_asset_id, tx_hash).result()
        print("The response of ContractInteractionsApi->get_transaction_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractInteractionsApi->get_transaction_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **tx_hash** | **str**| The transaction hash | 

### Return type

[**TransactionReceiptResponse**](TransactionReceiptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved The Transaction Receipt Successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_call_function**
> List[ParameterWithValue] read_call_function(contract_address, base_asset_id, read_call_function_dto, idempotency_key=idempotency_key)

Call a read function on a deployed contract

Call a read function on a deployed contract by blockchain native asset id and contract address

### Example


```python
from fireblocks.models.parameter_with_value import ParameterWithValue
from fireblocks.models.read_call_function_dto import ReadCallFunctionDto
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
    base_asset_id = 'base_asset_id_example' # str | 
    read_call_function_dto = fireblocks.ReadCallFunctionDto() # ReadCallFunctionDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Call a read function on a deployed contract
        api_response = fireblocks.contract_interactions.read_call_function(contract_address, base_asset_id, read_call_function_dto, idempotency_key=idempotency_key).result()
        print("The response of ContractInteractionsApi->read_call_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractInteractionsApi->read_call_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_address** | **str**| The contract&#39;s onchain address | 
 **base_asset_id** | **str**|  | 
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
> WriteCallFunctionResponseDto write_call_function(contract_address, base_asset_id, write_call_function_dto, idempotency_key=idempotency_key)

Call a write function on a deployed contract

Call a write function on a deployed contract by blockchain native asset id and contract address. This creates an onchain transaction, thus it is an async operation. It returns a transaction id that can be polled for status check

### Example


```python
from fireblocks.models.write_call_function_dto import WriteCallFunctionDto
from fireblocks.models.write_call_function_response_dto import WriteCallFunctionResponseDto
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
    base_asset_id = 'base_asset_id_example' # str | 
    write_call_function_dto = fireblocks.WriteCallFunctionDto() # WriteCallFunctionDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Call a write function on a deployed contract
        api_response = fireblocks.contract_interactions.write_call_function(contract_address, base_asset_id, write_call_function_dto, idempotency_key=idempotency_key).result()
        print("The response of ContractInteractionsApi->write_call_function:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractInteractionsApi->write_call_function: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_address** | **str**| The contract&#39;s onchain address | 
 **base_asset_id** | **str**|  | 
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

