# fireblocks.OnchainDataApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_registry_current_state**](OnchainDataApi.md#get_access_registry_current_state) | **GET** /onchain_data/base_asset_id/{baseAssetId}/access_registry_address/{accessRegistryAddress}/list | Get the current state of addresses in an access registry
[**get_access_registry_summary**](OnchainDataApi.md#get_access_registry_summary) | **GET** /onchain_data/base_asset_id/{baseAssetId}/access_registry_address/{accessRegistryAddress}/summary | Summary of access registry state
[**get_active_roles_for_contract**](OnchainDataApi.md#get_active_roles_for_contract) | **GET** /onchain_data/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/roles | List of active roles for a given contract address and base asset ID
[**get_contract_balance_history**](OnchainDataApi.md#get_contract_balance_history) | **GET** /onchain_data/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/account_address/{accountAddress}/balance_history | Get historical balance data for a specific account in a contract
[**get_contract_balances_summary**](OnchainDataApi.md#get_contract_balances_summary) | **GET** /onchain_data/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/summary | Get summary for the token contract
[**get_contract_total_supply**](OnchainDataApi.md#get_contract_total_supply) | **GET** /onchain_data/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/total_supply | Get historical total supply data for a contract
[**get_latest_balances_for_contract**](OnchainDataApi.md#get_latest_balances_for_contract) | **GET** /onchain_data/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/balances | Get latest balances for all addresses holding tokens from a contract
[**get_onchain_transactions**](OnchainDataApi.md#get_onchain_transactions) | **GET** /onchain_data/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/transactions | Fetch onchain transactions for a contract


# **get_access_registry_current_state**
> AccessRegistryCurrentStateResponse get_access_registry_current_state(base_asset_id, access_registry_address, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get the current state of addresses in an access registry

Returns the current state of addresses in the specified access registry. Only addresses that are currently active (added but not removed) are included.

### Example


```python
from fireblocks.models.access_registry_current_state_response import AccessRegistryCurrentStateResponse
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    access_registry_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The access registry address
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page\" (optional)
    page_size = 10 # int | Number of items per page (max 100), requesting more then 100 will return 100 items (optional)
    sort_by = dateAdded # str | Sorting field (enum). (optional) (default to dateAdded)
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)

    try:
        # Get the current state of addresses in an access registry
        api_response = fireblocks.onchain_data.get_access_registry_current_state(base_asset_id, access_registry_address, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of OnchainDataApi->get_access_registry_current_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_access_registry_current_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **access_registry_address** | **str**| The access registry address | 
 **page_cursor** | **str**| Page cursor to get the next page\&quot; | [optional] 
 **page_size** | **int**| Number of items per page (max 100), requesting more then 100 will return 100 items | [optional] 
 **sort_by** | **str**| Sorting field (enum). | [optional] [default to dateAdded]
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]

### Return type

[**AccessRegistryCurrentStateResponse**](AccessRegistryCurrentStateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access registry current state retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_registry_summary**
> AccessRegistrySummaryResponse get_access_registry_summary(base_asset_id, access_registry_address)

Summary of access registry state

Returns a summary of the current state of the access registry for the specified baseAssetId and accessRegistryAddress.

### Example


```python
from fireblocks.models.access_registry_summary_response import AccessRegistrySummaryResponse
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    access_registry_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The access registry address

    try:
        # Summary of access registry state
        api_response = fireblocks.onchain_data.get_access_registry_summary(base_asset_id, access_registry_address).result()
        print("The response of OnchainDataApi->get_access_registry_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_access_registry_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **access_registry_address** | **str**| The access registry address | 

### Return type

[**AccessRegistrySummaryResponse**](AccessRegistrySummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the summary of the access registry state |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_roles_for_contract**
> Dict[str, RoleDetails] get_active_roles_for_contract(base_asset_id, contract_address)

List of active roles for a given contract address and base asset ID

Returns a list of currently active roles for the specified baseAssetId and contractAddress.

### Example


```python
from fireblocks.models.role_details import RoleDetails
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract address

    try:
        # List of active roles for a given contract address and base asset ID
        api_response = fireblocks.onchain_data.get_active_roles_for_contract(base_asset_id, contract_address).result()
        print("The response of OnchainDataApi->get_active_roles_for_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_active_roles_for_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **contract_address** | **str**| The contract address | 

### Return type

[**Dict[str, RoleDetails]**](RoleDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list of active roles |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_balance_history**
> BalanceHistoryPagedResponse get_contract_balance_history(base_asset_id, contract_address, account_address, start_date=start_date, end_date=end_date, interval=interval, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get historical balance data for a specific account in a contract

Returns the paginated balance history of the specified account in a contract with optional date range and interval filtering.

### Example


```python
from fireblocks.models.balance_history_paged_response import BalanceHistoryPagedResponse
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract address
    account_address = '0x1234567890abcdef1234567890abcdef12345678' # str | The account address to get balance history for
    start_date = '2025-01-16T15:45:00Z' # datetime | Start date of the time range in ISO 8601 format (optional)
    end_date = '2025-01-16T15:45:00Z' # datetime | End date of the time range in ISO 8601 format (optional)
    interval = day # str | Time interval for grouping data (optional) (default to day)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page\" (optional)
    page_size = 10 # int | Number of items per page (max 100), requesting more then 100 will return 100 items (optional)
    sort_by = blockTimestamp # str | Sorting field (enum). Sorting only supported by 'blockTimestamp' (optional) (default to blockTimestamp)
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)

    try:
        # Get historical balance data for a specific account in a contract
        api_response = fireblocks.onchain_data.get_contract_balance_history(base_asset_id, contract_address, account_address, start_date=start_date, end_date=end_date, interval=interval, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of OnchainDataApi->get_contract_balance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_contract_balance_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **contract_address** | **str**| The contract address | 
 **account_address** | **str**| The account address to get balance history for | 
 **start_date** | **datetime**| Start date of the time range in ISO 8601 format | [optional] 
 **end_date** | **datetime**| End date of the time range in ISO 8601 format | [optional] 
 **interval** | **str**| Time interval for grouping data | [optional] [default to day]
 **page_cursor** | **str**| Page cursor to get the next page\&quot; | [optional] 
 **page_size** | **int**| Number of items per page (max 100), requesting more then 100 will return 100 items | [optional] 
 **sort_by** | **str**| Sorting field (enum). Sorting only supported by &#39;blockTimestamp&#39; | [optional] [default to blockTimestamp]
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]

### Return type

[**BalanceHistoryPagedResponse**](BalanceHistoryPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the contract balance history |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_balances_summary**
> TokenContractSummaryResponse get_contract_balances_summary(base_asset_id, contract_address)

Get summary for the token contract

Returns the total number of unique addresses holding balances and the total supply for the specified contract.

### Example


```python
from fireblocks.models.token_contract_summary_response import TokenContractSummaryResponse
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract address

    try:
        # Get summary for the token contract
        api_response = fireblocks.onchain_data.get_contract_balances_summary(base_asset_id, contract_address).result()
        print("The response of OnchainDataApi->get_contract_balances_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_contract_balances_summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **contract_address** | **str**| The contract address | 

### Return type

[**TokenContractSummaryResponse**](TokenContractSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the summary for the token contract |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_total_supply**
> TotalSupplyPagedResponse get_contract_total_supply(base_asset_id, contract_address, start_date=start_date, end_date=end_date, interval=interval, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get historical total supply data for a contract

Returns the paginated total supply history of the specified contract with optional date range and interval filtering.

### Example


```python
from fireblocks.models.total_supply_paged_response import TotalSupplyPagedResponse
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract address
    start_date = '2025-01-16T15:45:00Z' # datetime | Start date of the time range in ISO 8601 format (optional)
    end_date = '2025-01-16T15:45:00Z' # datetime | End date of the time range in ISO 8601 format (optional)
    interval = day # str | Time interval for grouping data (optional) (default to day)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page\" (optional)
    page_size = 10 # int | Number of items per page (max 100), requesting more then 100 will return 100 items (optional)
    sort_by = blockTimestamp # str | Sorting field (enum). Sorting only supported by 'blockTimestamp' (optional) (default to blockTimestamp)
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)

    try:
        # Get historical total supply data for a contract
        api_response = fireblocks.onchain_data.get_contract_total_supply(base_asset_id, contract_address, start_date=start_date, end_date=end_date, interval=interval, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of OnchainDataApi->get_contract_total_supply:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_contract_total_supply: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **contract_address** | **str**| The contract address | 
 **start_date** | **datetime**| Start date of the time range in ISO 8601 format | [optional] 
 **end_date** | **datetime**| End date of the time range in ISO 8601 format | [optional] 
 **interval** | **str**| Time interval for grouping data | [optional] [default to day]
 **page_cursor** | **str**| Page cursor to get the next page\&quot; | [optional] 
 **page_size** | **int**| Number of items per page (max 100), requesting more then 100 will return 100 items | [optional] 
 **sort_by** | **str**| Sorting field (enum). Sorting only supported by &#39;blockTimestamp&#39; | [optional] [default to blockTimestamp]
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]

### Return type

[**TotalSupplyPagedResponse**](TotalSupplyPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the contract total supply history |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_balances_for_contract**
> AddressBalancePagedResponse get_latest_balances_for_contract(base_asset_id, contract_address, account_address=account_address, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get latest balances for all addresses holding tokens from a contract

Returns the latest balance for each unique address with support for numeric balance sorting. The `prev` cursor is reserved for future support.

### Example


```python
from fireblocks.models.address_balance_paged_response import AddressBalancePagedResponse
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract address
    account_address = '0x1234567890abcdef1234567890abcdef12345678' # str | Optional filter to get balance for a specific account address (optional)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page\" (optional)
    page_size = 10 # int | Number of items per page (max 100), requesting more then 100 will return 100 items (optional)
    sort_by = blockTimestamp # str | Sorting field for balances (optional) (default to blockTimestamp)
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)

    try:
        # Get latest balances for all addresses holding tokens from a contract
        api_response = fireblocks.onchain_data.get_latest_balances_for_contract(base_asset_id, contract_address, account_address=account_address, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of OnchainDataApi->get_latest_balances_for_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_latest_balances_for_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **contract_address** | **str**| The contract address | 
 **account_address** | **str**| Optional filter to get balance for a specific account address | [optional] 
 **page_cursor** | **str**| Page cursor to get the next page\&quot; | [optional] 
 **page_size** | **int**| Number of items per page (max 100), requesting more then 100 will return 100 items | [optional] 
 **sort_by** | **str**| Sorting field for balances | [optional] [default to blockTimestamp]
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]

### Return type

[**AddressBalancePagedResponse**](AddressBalancePagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the latest balances for the contract |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_onchain_transactions**
> OnchainTransactionsPagedResponse get_onchain_transactions(base_asset_id, contract_address, start_date=start_date, end_date=end_date, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Fetch onchain transactions for a contract

Returns a paginated list of onchain transactions for the specified contract address and base asset ID, optionally filtered by date range.

### Example


```python
from fireblocks.models.onchain_transactions_paged_response import OnchainTransactionsPagedResponse
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
    base_asset_id = 'ETH_TEST3' # str | The blockchain base assetId
    contract_address = '0xC2c4e1Db41F0bB97996D0eD0542D2170d146FB66' # str | The contract address
    start_date = '2025-01-16T15:45:00Z' # datetime | Start date of the time range in ISO 8601 format (optional)
    end_date = '2025-01-16T15:45:00Z' # datetime | End date of the time range in ISO 8601 format (optional)
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page\" (optional)
    page_size = 10 # int | Number of items per page (max 100), requesting more then 100 will return 100 items (optional)
    sort_by = blockTimestamp # str | Sorting field (enum). (optional) (default to blockTimestamp)
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)

    try:
        # Fetch onchain transactions for a contract
        api_response = fireblocks.onchain_data.get_onchain_transactions(base_asset_id, contract_address, start_date=start_date, end_date=end_date, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of OnchainDataApi->get_onchain_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnchainDataApi->get_onchain_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_asset_id** | **str**| The blockchain base assetId | 
 **contract_address** | **str**| The contract address | 
 **start_date** | **datetime**| Start date of the time range in ISO 8601 format | [optional] 
 **end_date** | **datetime**| End date of the time range in ISO 8601 format | [optional] 
 **page_cursor** | **str**| Page cursor to get the next page\&quot; | [optional] 
 **page_size** | **int**| Number of items per page (max 100), requesting more then 100 will return 100 items | [optional] 
 **sort_by** | **str**| Sorting field (enum). | [optional] [default to blockTimestamp]
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]

### Return type

[**OnchainTransactionsPagedResponse**](OnchainTransactionsPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Onchain transactions fetched successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

