# fireblocks.ContractsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contract_asset**](ContractsApi.md#add_contract_asset) | **POST** /contracts/{contractId}/{assetId} | Add an asset to a whitelisted contract
[**create_contract**](ContractsApi.md#create_contract) | **POST** /contracts | Add a contract
[**delete_contract**](ContractsApi.md#delete_contract) | **DELETE** /contracts/{contractId} | Delete a contract
[**delete_contract_asset**](ContractsApi.md#delete_contract_asset) | **DELETE** /contracts/{contractId}/{assetId} | Delete an asset from a whitelisted contract
[**get_contract**](ContractsApi.md#get_contract) | **GET** /contracts/{contractId} | Find a Specific Whitelisted Contract
[**get_contract_asset**](ContractsApi.md#get_contract_asset) | **GET** /contracts/{contractId}/{assetId} | Find a whitelisted contract&#39;s asset
[**get_contracts**](ContractsApi.md#get_contracts) | **GET** /contracts | List Whitelisted Contracts


# **add_contract_asset**
> ExternalWalletAsset add_contract_asset(contract_id, asset_id, idempotency_key=idempotency_key, add_contract_asset_request=add_contract_asset_request)

Add an asset to a whitelisted contract

Adds an asset to a whitelisted contract. </br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.add_contract_asset_request import AddContractAssetRequest
from fireblocks.models.external_wallet_asset import ExternalWalletAsset
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
    contract_id = 'contract_id_example' # str | The ID of the contract
    asset_id = 'asset_id_example' # str | The ID of the asset to add
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    add_contract_asset_request = fireblocks.AddContractAssetRequest() # AddContractAssetRequest |  (optional)

    try:
        # Add an asset to a whitelisted contract
        api_response = fireblocks.contracts.add_contract_asset(contract_id, asset_id, idempotency_key=idempotency_key, add_contract_asset_request=add_contract_asset_request).result()
        print("The response of ContractsApi->add_contract_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->add_contract_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| The ID of the contract | 
 **asset_id** | **str**| The ID of the asset to add | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **add_contract_asset_request** | [**AddContractAssetRequest**](AddContractAssetRequest.md)|  | [optional] 

### Return type

[**ExternalWalletAsset**](ExternalWalletAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contract**
> UnmanagedWallet create_contract(idempotency_key=idempotency_key, create_contract_request=create_contract_request)

Add a contract

Adds a contract to the workspace whitelist. </br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.create_contract_request import CreateContractRequest
from fireblocks.models.unmanaged_wallet import UnmanagedWallet
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
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_contract_request = fireblocks.CreateContractRequest() # CreateContractRequest |  (optional)

    try:
        # Add a contract
        api_response = fireblocks.contracts.create_contract(idempotency_key=idempotency_key, create_contract_request=create_contract_request).result()
        print("The response of ContractsApi->create_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_contract_request** | [**CreateContractRequest**](CreateContractRequest.md)|  | [optional] 

### Return type

[**UnmanagedWallet**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract**
> delete_contract(contract_id)

Delete a contract

Deletes a contract by ID. </br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    contract_id = 'contract_id_example' # str | The ID of the contract to delete

    try:
        # Delete a contract
        fireblocks.contracts.delete_contract(contract_id).result()
    except Exception as e:
        print("Exception when calling ContractsApi->delete_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| The ID of the contract to delete | 

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
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract_asset**
> delete_contract_asset(contract_id, asset_id)

Delete an asset from a whitelisted contract

Deletes a whitelisted contract asset by ID. </br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    contract_id = 'contract_id_example' # str | The ID of the contract
    asset_id = 'asset_id_example' # str | The ID of the asset to delete

    try:
        # Delete an asset from a whitelisted contract
        fireblocks.contracts.delete_contract_asset(contract_id, asset_id).result()
    except Exception as e:
        print("Exception when calling ContractsApi->delete_contract_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| The ID of the contract | 
 **asset_id** | **str**| The ID of the asset to delete | 

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
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract**
> UnmanagedWallet get_contract(contract_id)

Find a Specific Whitelisted Contract

Returns a whitelisted contract by Fireblocks Contract ID. </br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.unmanaged_wallet import UnmanagedWallet
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
    contract_id = 'contract_id_example' # str | The ID of the contract to return

    try:
        # Find a Specific Whitelisted Contract
        api_response = fireblocks.contracts.get_contract(contract_id).result()
        print("The response of ContractsApi->get_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| The ID of the contract to return | 

### Return type

[**UnmanagedWallet**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_asset**
> ExternalWalletAsset get_contract_asset(contract_id, asset_id)

Find a whitelisted contract's asset

Returns a whitelisted contract's asset by ID. </br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.external_wallet_asset import ExternalWalletAsset
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
    contract_id = 'contract_id_example' # str | The ID of the contract
    asset_id = 'asset_id_example' # str | The ID of the asset to return

    try:
        # Find a whitelisted contract's asset
        api_response = fireblocks.contracts.get_contract_asset(contract_id, asset_id).result()
        print("The response of ContractsApi->get_contract_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contract_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| The ID of the contract | 
 **asset_id** | **str**| The ID of the asset to return | 

### Return type

[**ExternalWalletAsset**](ExternalWalletAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts**
> List[UnmanagedWallet] get_contracts()

List Whitelisted Contracts

Gets a list of whitelisted contracts. </br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.unmanaged_wallet import UnmanagedWallet
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

    try:
        # List Whitelisted Contracts
        api_response = fireblocks.contracts.get_contracts().result()
        print("The response of ContractsApi->get_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contracts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UnmanagedWallet]**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contracts |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

