# fireblocks_client.ContractsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_to_contract**](ContractsApi.md#add_asset_to_contract) | **POST** /contracts/{contractId}/{assetId} | Add an asset to a contract
[**create_contract**](ContractsApi.md#create_contract) | **POST** /contracts | Create a contract
[**delete_contract**](ContractsApi.md#delete_contract) | **DELETE** /contracts/{contractId} | Delete a contract
[**get_asset_in_contract**](ContractsApi.md#get_asset_in_contract) | **GET** /contracts/{contractId}/{assetId} | Find a contract asset
[**get_contract_by_id**](ContractsApi.md#get_contract_by_id) | **GET** /contracts/{contractId} | Find a specific contract
[**get_contracts**](ContractsApi.md#get_contracts) | **GET** /contracts | List contracts
[**remove_asset_from_contract**](ContractsApi.md#remove_asset_from_contract) | **DELETE** /contracts/{contractId}/{assetId} | Delete a contract asset


# **add_asset_to_contract**
> ExternalWalletAsset add_asset_to_contract(contract_id, asset_id, add_asset_to_contract_request=add_asset_to_contract_request)

Add an asset to a contract

Adds an asset to an existing contract.

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
    api_instance = fireblocks_client.ContractsApi(api_client)
    contract_id = 'contract_id_example' # str | The ID of the contract
    asset_id = 'asset_id_example' # str | The ID of the asset to add
    add_asset_to_contract_request = fireblocks_client.AddAssetToContractRequest() # AddAssetToContractRequest |  (optional)

    try:
        # Add an asset to a contract
        api_response = api_instance.add_asset_to_contract(contract_id, asset_id, add_asset_to_contract_request=add_asset_to_contract_request)
        print("The response of ContractsApi->add_asset_to_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->add_asset_to_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| The ID of the contract | 
 **asset_id** | **str**| The ID of the asset to add | 
 **add_asset_to_contract_request** | [**AddAssetToContractRequest**](AddAssetToContractRequest.md)|  | [optional] 

### Return type

[**ExternalWalletAsset**](ExternalWalletAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contract**
> UnmanagedWallet create_contract(create_contract_request=create_contract_request)

Create a contract

Creates a new contract.

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
    api_instance = fireblocks_client.ContractsApi(api_client)
    create_contract_request = fireblocks_client.CreateContractRequest() # CreateContractRequest |  (optional)

    try:
        # Create a contract
        api_response = api_instance.create_contract(create_contract_request=create_contract_request)
        print("The response of ContractsApi->create_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contract_request** | [**CreateContractRequest**](CreateContractRequest.md)|  | [optional] 

### Return type

[**UnmanagedWallet**](UnmanagedWallet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contract**
> delete_contract(contract_id)

Delete a contract

Deletes a contract by ID.

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
    api_instance = fireblocks_client.ContractsApi(api_client)
    contract_id = 'contract_id_example' # str | The ID of the contract to delete

    try:
        # Delete a contract
        api_instance.delete_contract(contract_id)
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

# **get_asset_in_contract**
> ExternalWalletAsset get_asset_in_contract(contract_id, asset_id)

Find a contract asset

Returns a contract asset by ID.

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
    api_instance = fireblocks_client.ContractsApi(api_client)
    contract_id = 'contract_id_example' # str | The ID of the contract
    asset_id = 'asset_id_example' # str | The ID of the asset to return

    try:
        # Find a contract asset
        api_response = api_instance.get_asset_in_contract(contract_id, asset_id)
        print("The response of ContractsApi->get_asset_in_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_asset_in_contract: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet Asset object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_by_id**
> UnmanagedWallet get_contract_by_id(contract_id)

Find a specific contract

Returns a contract by ID.

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
    api_instance = fireblocks_client.ContractsApi(api_client)
    contract_id = 'contract_id_example' # str | The ID of the contract to return

    try:
        # Find a specific contract
        api_response = api_instance.get_contract_by_id(contract_id)
        print("The response of ContractsApi->get_contract_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contract_by_id: %s\n" % e)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Wallet object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts**
> List[UnmanagedWallet] get_contracts()

List contracts

Gets a list of contracts.

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
    api_instance = fireblocks_client.ContractsApi(api_client)

    try:
        # List contracts
        api_response = api_instance.get_contracts()
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of contracts |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_from_contract**
> remove_asset_from_contract(contract_id, asset_id)

Delete a contract asset

Deletes a contract asset by ID.

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
    api_instance = fireblocks_client.ContractsApi(api_client)
    contract_id = 'contract_id_example' # str | The ID of the contract
    asset_id = 'asset_id_example' # str | The ID of the asset to delete

    try:
        # Delete a contract asset
        api_instance.remove_asset_from_contract(contract_id, asset_id)
    except Exception as e:
        print("Exception when calling ContractsApi->remove_asset_from_contract: %s\n" % e)
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

