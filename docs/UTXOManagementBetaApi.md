# fireblocks.UTXOManagementBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_utxos**](UTXOManagementBetaApi.md#get_utxos) | **GET** /utxo_management/{vaultAccountId}/{assetId}/unspent_outputs | List unspent outputs (UTXOs)
[**update_utxo_labels**](UTXOManagementBetaApi.md#update_utxo_labels) | **PATCH** /utxo_management/{vaultAccountId}/{assetId}/labels | Attach or detach labels to/from UTXOs


# **get_utxos**
> ListUtxosResponse get_utxos(vault_account_id, asset_id, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, include_all_labels=include_all_labels, include_any_labels=include_any_labels, exclude_any_labels=exclude_any_labels, include_statuses=include_statuses, address=address, min_amount=min_amount, max_amount=max_amount)

List unspent outputs (UTXOs)

Returns a paginated list of unspent transaction outputs (UTXOs) for a UTXO-based asset in a vault account, with optional filters for labels, statuses, amounts, and more.
**Note:** These endpoints are currently in beta and might be subject to changes.
Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.list_utxos_response import ListUtxosResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    page_cursor = 'MjAyNS0wNy0wOSAxMDo1MzoxMy40NTI=:NA==' # str | Cursor for the next page of results (optional)
    page_size = 50 # int | Number of results per page (max 250, default 50) (optional) (default to 50)
    sort = 'AMOUNT' # str | Field to sort by (optional)
    order = 'ASC' # str | Sort order (optional)
    include_all_labels = ['[\"cold-storage\"]'] # List[str] | Only return UTXOs that have ALL of these labels (AND logic). (optional)
    include_any_labels = ['[\"vip\",\"high-value\"]'] # List[str] | Return UTXOs that have ANY of these labels (OR logic). (optional)
    exclude_any_labels = ['[\"deprecated\"]'] # List[str] | Exclude UTXOs that have ANY of these labels. (optional)
    include_statuses = ['[\"AVAILABLE\",\"PENDING\"]'] # List[str] | Filter by UTXO statuses to include. (optional)
    address = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa' # str | Filter by address (optional)
    min_amount = '0.001' # str | Minimum amount filter (optional)
    max_amount = '1.0' # str | Maximum amount filter (optional)

    try:
        # List unspent outputs (UTXOs)
        api_response = fireblocks.utxo_management_beta.get_utxos(vault_account_id, asset_id, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, include_all_labels=include_all_labels, include_any_labels=include_any_labels, exclude_any_labels=exclude_any_labels, include_statuses=include_statuses, address=address, min_amount=min_amount, max_amount=max_amount).result()
        print("The response of UTXOManagementBetaApi->get_utxos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UTXOManagementBetaApi->get_utxos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **page_cursor** | **str**| Cursor for the next page of results | [optional] 
 **page_size** | **int**| Number of results per page (max 250, default 50) | [optional] [default to 50]
 **sort** | **str**| Field to sort by | [optional] 
 **order** | **str**| Sort order | [optional] 
 **include_all_labels** | [**List[str]**](str.md)| Only return UTXOs that have ALL of these labels (AND logic). | [optional] 
 **include_any_labels** | [**List[str]**](str.md)| Return UTXOs that have ANY of these labels (OR logic). | [optional] 
 **exclude_any_labels** | [**List[str]**](str.md)| Exclude UTXOs that have ANY of these labels. | [optional] 
 **include_statuses** | [**List[str]**](str.md)| Filter by UTXO statuses to include. | [optional] 
 **address** | **str**| Filter by address | [optional] 
 **min_amount** | **str**| Minimum amount filter | [optional] 
 **max_amount** | **str**| Maximum amount filter | [optional] 

### Return type

[**ListUtxosResponse**](ListUtxosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of UTXOs |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_utxo_labels**
> AttachDetachUtxoLabelsResponse update_utxo_labels(vault_account_id, asset_id, attach_detach_utxo_labels_request, idempotency_key=idempotency_key)

Attach or detach labels to/from UTXOs

Attach or detach labels to/from UTXOs in a vault account. Labels can be used for organizing and filtering UTXOs.
Labels are applied additively — `labelsToAttach` adds to the existing label set and `labelsToDetach` removes from it. Neither operation replaces the full set.
**Note:** These endpoints are currently in beta and might be subject to changes.
Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.attach_detach_utxo_labels_request import AttachDetachUtxoLabelsRequest
from fireblocks.models.attach_detach_utxo_labels_response import AttachDetachUtxoLabelsResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    asset_id = 'asset_id_example' # str | The ID of the asset
    attach_detach_utxo_labels_request = fireblocks.AttachDetachUtxoLabelsRequest() # AttachDetachUtxoLabelsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Attach or detach labels to/from UTXOs
        api_response = fireblocks.utxo_management_beta.update_utxo_labels(vault_account_id, asset_id, attach_detach_utxo_labels_request, idempotency_key=idempotency_key).result()
        print("The response of UTXOManagementBetaApi->update_utxo_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UTXOManagementBetaApi->update_utxo_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **asset_id** | **str**| The ID of the asset | 
 **attach_detach_utxo_labels_request** | [**AttachDetachUtxoLabelsRequest**](AttachDetachUtxoLabelsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AttachDetachUtxoLabelsResponse**](AttachDetachUtxoLabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UTXOs with updated labels |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

