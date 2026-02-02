# fireblocks.TransactionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_transaction**](TransactionsApi.md#cancel_transaction) | **POST** /transactions/{txId}/cancel | Cancel a transaction
[**create_transaction**](TransactionsApi.md#create_transaction) | **POST** /transactions | Create a new transaction
[**drop_transaction**](TransactionsApi.md#drop_transaction) | **POST** /transactions/{txId}/drop | Drop ETH (EVM) transaction by ID
[**estimate_network_fee**](TransactionsApi.md#estimate_network_fee) | **GET** /estimate_network_fee | Estimate the required fee for an asset
[**estimate_transaction_fee**](TransactionsApi.md#estimate_transaction_fee) | **POST** /transactions/estimate_fee | Estimate transaction fee
[**freeze_transaction**](TransactionsApi.md#freeze_transaction) | **POST** /transactions/{txId}/freeze | Freeze a transaction
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /transactions/{txId} | Get a specific transaction by Fireblocks transaction ID
[**get_transaction_by_external_id**](TransactionsApi.md#get_transaction_by_external_id) | **GET** /transactions/external_tx_id/{externalTxId} | Get a specific transaction by external transaction ID
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /transactions | Get transaction history
[**set_confirmation_threshold_by_transaction_hash**](TransactionsApi.md#set_confirmation_threshold_by_transaction_hash) | **POST** /txHash/{txHash}/set_confirmation_threshold | Set confirmation threshold by transaction hash
[**set_transaction_confirmation_threshold**](TransactionsApi.md#set_transaction_confirmation_threshold) | **POST** /transactions/{txId}/set_confirmation_threshold | Set confirmation threshold by Fireblocks Transaction ID
[**unfreeze_transaction**](TransactionsApi.md#unfreeze_transaction) | **POST** /transactions/{txId}/unfreeze | Unfreeze a transaction
[**validate_address**](TransactionsApi.md#validate_address) | **GET** /transactions/validate_address/{assetId}/{address} | Validate destination address


# **cancel_transaction**
> CancelTransactionResponse cancel_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key)

Cancel a transaction

Cancels a transaction by Fireblocks Transaction ID.

Can be used only for transactions that did not get to the BROADCASTING state.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.cancel_transaction_response import CancelTransactionResponse
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
    tx_id = 'tx_id_example' # str | The ID of the transaction to cancel
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Cancel a transaction
        api_response = fireblocks.transactions.cancel_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key).result()
        print("The response of TransactionsApi->cancel_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->cancel_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction to cancel | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CancelTransactionResponse**](CancelTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Transaction object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction**
> CreateTransactionResponse create_transaction(x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key, transaction_request=transaction_request)

Create a new transaction

Creates a new transaction. This endpoint can be used for regular Transfers, Contract Calls, Raw & Typed message signing. - For Transfers, the required parameters are: `assetId`, `source`, `destination` and `amount`. - For Contract Calls, the required parameters are: `operation.CONTRACT_CALL`, `assetId` (Base Asset), `source`,

### Example


```python
from fireblocks.models.create_transaction_response import CreateTransactionResponse
from fireblocks.models.transaction_request import TransactionRequest
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
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    transaction_request = fireblocks.TransactionRequest() # TransactionRequest |  (optional)

    try:
        # Create a new transaction
        api_response = fireblocks.transactions.create_transaction(x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key, transaction_request=transaction_request).result()
        print("The response of TransactionsApi->create_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **transaction_request** | [**TransactionRequest**](TransactionRequest.md)|  | [optional] 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A transaction object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drop_transaction**
> DropTransactionResponse drop_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key, drop_transaction_request=drop_transaction_request)

Drop ETH (EVM) transaction by ID

Drops a stuck ETH (EVM) transaction and creates a replacement transaction with 0 amount.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.drop_transaction_request import DropTransactionRequest
from fireblocks.models.drop_transaction_response import DropTransactionResponse
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
    tx_id = 'tx_id_example' # str | The ID of the transaction
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    drop_transaction_request = fireblocks.DropTransactionRequest() # DropTransactionRequest |  (optional)

    try:
        # Drop ETH (EVM) transaction by ID
        api_response = fireblocks.transactions.drop_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key, drop_transaction_request=drop_transaction_request).result()
        print("The response of TransactionsApi->drop_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->drop_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **drop_transaction_request** | [**DropTransactionRequest**](DropTransactionRequest.md)|  | [optional] 

### Return type

[**DropTransactionResponse**](DropTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation completed successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_network_fee**
> EstimatedNetworkFeeResponse estimate_network_fee(asset_id)

Estimate the required fee for an asset

Gets the estimated required fee for an asset.
Fireblocks fetches, calculates and caches the result every 30 seconds.
Customers should query this API while taking the caching interval into consideration.
Notes:
- The `networkFee` parameter is the `gasPrice` with a given delta added, multiplied by the gasLimit plus the delta. - The estimation provided depends on the asset type.
    - For UTXO-based assets, the response contains the `feePerByte` parameter
    - For ETH-based and all EVM based assets, the response will contain `gasPrice` parameter. This is calculated by adding the `baseFee` to the `actualPriority` based on the latest 12 blocks. The response for ETH-based  contains the `baseFee`, `gasPrice`, and `priorityFee` parameters.
    - For ADA-based assets, the response will contain the parameter `networkFee` and `feePerByte` parameters.
    - For XRP and XLM, the response will contain the transaction fee.
    - For other assets, the response will contain the `networkFee` parameter.

Learn more about Fireblocks Fee Management in the following [guide](https://developers.fireblocks.com/reference/estimate-transaction-fee).
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.estimated_network_fee_response import EstimatedNetworkFeeResponse
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
    asset_id = 'asset_id_example' # str | The asset for which to estimate the fee

    try:
        # Estimate the required fee for an asset
        api_response = fireblocks.transactions.estimate_network_fee(asset_id).result()
        print("The response of TransactionsApi->estimate_network_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->estimate_network_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset for which to estimate the fee | 

### Return type

[**EstimatedNetworkFeeResponse**](EstimatedNetworkFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Estimated fees response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_transaction_fee**
> EstimatedTransactionFeeResponse estimate_transaction_fee(idempotency_key=idempotency_key, transaction_request=transaction_request)

Estimate transaction fee

Estimates the transaction fee for a specific transaction request.
This endpoint simulates a transaction which means that the system will expect to have the requested asset and balance in the specified wallet.


**Note**: Supports all Fireblocks assets except ZCash (ZEC).
Learn more about Fireblocks Fee Management in the following [guide](https://developers.fireblocks.com/reference/estimate-transaction-fee).
</br>Endpoint Permission: Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.estimated_transaction_fee_response import EstimatedTransactionFeeResponse
from fireblocks.models.transaction_request import TransactionRequest
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
    transaction_request = fireblocks.TransactionRequest() # TransactionRequest |  (optional)

    try:
        # Estimate transaction fee
        api_response = fireblocks.transactions.estimate_transaction_fee(idempotency_key=idempotency_key, transaction_request=transaction_request).result()
        print("The response of TransactionsApi->estimate_transaction_fee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->estimate_transaction_fee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **transaction_request** | [**TransactionRequest**](TransactionRequest.md)|  | [optional] 

### Return type

[**EstimatedTransactionFeeResponse**](EstimatedTransactionFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Estimated fees response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freeze_transaction**
> FreezeTransactionResponse freeze_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key)

Freeze a transaction

Freezes a transaction by ID.

Usually used for AML integrations when the incoming funds should be quarantined.
For account based assets - the entire amount of the transaction is frozen 
For UTXO based assets - all UTXOs of the specified transaction are frozen
</br>Endpoint Permission: Admin, Non-Signing Admin.

### Example


```python
from fireblocks.models.freeze_transaction_response import FreezeTransactionResponse
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
    tx_id = 'tx_id_example' # str | The ID of the transaction to freeze
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Freeze a transaction
        api_response = fireblocks.transactions.freeze_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key).result()
        print("The response of TransactionsApi->freeze_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->freeze_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction to freeze | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**FreezeTransactionResponse**](FreezeTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | freeze response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionResponse get_transaction(tx_id)

Get a specific transaction by Fireblocks transaction ID

Get a specific transaction data by Fireblocks Transaction ID
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.transaction_response import TransactionResponse
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
    tx_id = '00000000-0000-0000-0000-000000000000' # str | The ID of the transaction to return

    try:
        # Get a specific transaction by Fireblocks transaction ID
        api_response = fireblocks.transactions.get_transaction(tx_id).result()
        print("The response of TransactionsApi->get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction to return | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Transaction object |  * X-Request-ID -  <br>  |
**400** | Error Response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_external_id**
> TransactionResponse get_transaction_by_external_id(external_tx_id)

Get a specific transaction by external transaction ID

Returns transaction by external transaction ID.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.transaction_response import TransactionResponse
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
    external_tx_id = '00000000-0000-0000-0000-000000000000' # str | The external ID of the transaction to return

    try:
        # Get a specific transaction by external transaction ID
        api_response = fireblocks.transactions.get_transaction_by_external_id(external_tx_id).result()
        print("The response of TransactionsApi->get_transaction_by_external_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transaction_by_external_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_tx_id** | **str**| The external ID of the transaction to return | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Transaction object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> List[TransactionResponse] get_transactions(next=next, prev=prev, before=before, after=after, status=status, order_by=order_by, sort=sort, limit=limit, source_type=source_type, source_id=source_id, dest_type=dest_type, dest_id=dest_id, assets=assets, tx_hash=tx_hash, source_wallet_id=source_wallet_id, dest_wallet_id=dest_wallet_id)

Get transaction history

Get the transaction history for your workspace.

**Endpoint Permissions:** Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.


### Example


```python
from fireblocks.models.transaction_response import TransactionResponse
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
    next = 'next_example' # str | Cursor returned in next-page header that can be used to fetch the next page of results (optional)
    prev = 'prev_example' # str | Cursor returned in prev-page header that can be used to fetch the previous page of results (optional)
    before = 'before_example' # str | Unix timestamp in milliseconds. Returns only transactions created before the specified date. Provides an explicit end time. If not provided, default value will be applied, and may change over time.  The current default value is the past 90 days.  (optional)
    after = 'after_example' # str | Unix timestamp in milliseconds. Returns only transactions created after the specified date. Provides an explicit start time. If not provided, default value will be applied, and may change over time.  The current default value is the past 90 days.  (optional)
    status = 'status_example' # str | You can filter by one of the statuses. (optional)
    order_by = 'order_by_example' # str | The field to order the results by.  **Note:** Ordering by a field that is not `createdAt` may result in transactions that receive updates as you request the next or previous pages of results, resulting in missing those transactions.  (optional)
    sort = 'sort_example' # str | The direction to order the results by (optional)
    limit = 200 # int | Limits the number of results. If not provided, a limit of 200 will be used. The maximum allowed limit is 500 (optional) (default to 200)
    source_type = 'source_type_example' # str | The source type of the transaction (optional)
    source_id = 'source_id_example' # str | The source ID of the transaction (optional)
    dest_type = 'dest_type_example' # str | The destination type of the transaction (optional)
    dest_id = 'dest_id_example' # str | The destination ID of the transaction (optional)
    assets = 'assets_example' # str | A list of assets to filter by, seperated by commas (optional)
    tx_hash = 'tx_hash_example' # str | Returns only results with a specified txHash (optional)
    source_wallet_id = 'source_wallet_id_example' # str | Returns only results where the source is a specific end user wallet (optional)
    dest_wallet_id = 'dest_wallet_id_example' # str | Returns only results where the destination is a specific end user wallet (optional)

    try:
        # Get transaction history
        api_response = fireblocks.transactions.get_transactions(next=next, prev=prev, before=before, after=after, status=status, order_by=order_by, sort=sort, limit=limit, source_type=source_type, source_id=source_id, dest_type=dest_type, dest_id=dest_id, assets=assets, tx_hash=tx_hash, source_wallet_id=source_wallet_id, dest_wallet_id=dest_wallet_id).result()
        print("The response of TransactionsApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next** | **str**| Cursor returned in next-page header that can be used to fetch the next page of results | [optional] 
 **prev** | **str**| Cursor returned in prev-page header that can be used to fetch the previous page of results | [optional] 
 **before** | **str**| Unix timestamp in milliseconds. Returns only transactions created before the specified date. Provides an explicit end time. If not provided, default value will be applied, and may change over time.  The current default value is the past 90 days.  | [optional] 
 **after** | **str**| Unix timestamp in milliseconds. Returns only transactions created after the specified date. Provides an explicit start time. If not provided, default value will be applied, and may change over time.  The current default value is the past 90 days.  | [optional] 
 **status** | **str**| You can filter by one of the statuses. | [optional] 
 **order_by** | **str**| The field to order the results by.  **Note:** Ordering by a field that is not &#x60;createdAt&#x60; may result in transactions that receive updates as you request the next or previous pages of results, resulting in missing those transactions.  | [optional] 
 **sort** | **str**| The direction to order the results by | [optional] 
 **limit** | **int**| Limits the number of results. If not provided, a limit of 200 will be used. The maximum allowed limit is 500 | [optional] [default to 200]
 **source_type** | **str**| The source type of the transaction | [optional] 
 **source_id** | **str**| The source ID of the transaction | [optional] 
 **dest_type** | **str**| The destination type of the transaction | [optional] 
 **dest_id** | **str**| The destination ID of the transaction | [optional] 
 **assets** | **str**| A list of assets to filter by, seperated by commas | [optional] 
 **tx_hash** | **str**| Returns only results with a specified txHash | [optional] 
 **source_wallet_id** | **str**| Returns only results where the source is a specific end user wallet | [optional] 
 **dest_wallet_id** | **str**| Returns only results where the destination is a specific end user wallet | [optional] 

### Return type

[**List[TransactionResponse]**](TransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions |  * X-Request-ID -  <br>  * next-page -  <br>  * prev-page -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_confirmation_threshold_by_transaction_hash**
> SetConfirmationsThresholdResponse set_confirmation_threshold_by_transaction_hash(tx_hash, idempotency_key=idempotency_key, set_confirmations_threshold_request=set_confirmations_threshold_request)

Set confirmation threshold by transaction hash

Overrides the required number of confirmations for transaction completion by transaction hash.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.set_confirmations_threshold_request import SetConfirmationsThresholdRequest
from fireblocks.models.set_confirmations_threshold_response import SetConfirmationsThresholdResponse
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
    tx_hash = 'tx_hash_example' # str | The TxHash
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    set_confirmations_threshold_request = fireblocks.SetConfirmationsThresholdRequest() # SetConfirmationsThresholdRequest |  (optional)

    try:
        # Set confirmation threshold by transaction hash
        api_response = fireblocks.transactions.set_confirmation_threshold_by_transaction_hash(tx_hash, idempotency_key=idempotency_key, set_confirmations_threshold_request=set_confirmations_threshold_request).result()
        print("The response of TransactionsApi->set_confirmation_threshold_by_transaction_hash:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->set_confirmation_threshold_by_transaction_hash: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_hash** | **str**| The TxHash | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **set_confirmations_threshold_request** | [**SetConfirmationsThresholdRequest**](SetConfirmationsThresholdRequest.md)|  | [optional] 

### Return type

[**SetConfirmationsThresholdResponse**](SetConfirmationsThresholdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of transactions affected by the change |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_transaction_confirmation_threshold**
> SetConfirmationsThresholdResponse set_transaction_confirmation_threshold(tx_id, idempotency_key=idempotency_key, set_confirmations_threshold_request=set_confirmations_threshold_request)

Set confirmation threshold by Fireblocks Transaction ID

Overrides the required number of confirmations for transaction completion Fireblocks Transaction ID.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.set_confirmations_threshold_request import SetConfirmationsThresholdRequest
from fireblocks.models.set_confirmations_threshold_response import SetConfirmationsThresholdResponse
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
    tx_id = 'tx_id_example' # str | The ID of the transaction
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    set_confirmations_threshold_request = fireblocks.SetConfirmationsThresholdRequest() # SetConfirmationsThresholdRequest |  (optional)

    try:
        # Set confirmation threshold by Fireblocks Transaction ID
        api_response = fireblocks.transactions.set_transaction_confirmation_threshold(tx_id, idempotency_key=idempotency_key, set_confirmations_threshold_request=set_confirmations_threshold_request).result()
        print("The response of TransactionsApi->set_transaction_confirmation_threshold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->set_transaction_confirmation_threshold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **set_confirmations_threshold_request** | [**SetConfirmationsThresholdRequest**](SetConfirmationsThresholdRequest.md)|  | [optional] 

### Return type

[**SetConfirmationsThresholdResponse**](SetConfirmationsThresholdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unfreeze_transaction**
> UnfreezeTransactionResponse unfreeze_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key)

Unfreeze a transaction

Unfreezes a transaction by Fireblocks Transaction ID and makes the transaction available again.
</br>Endpoint Permission: Admin, Non-Signing Admin.

### Example


```python
from fireblocks.models.unfreeze_transaction_response import UnfreezeTransactionResponse
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
    tx_id = 'tx_id_example' # str | The ID of the transaction to unfreeze
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Unfreeze a transaction
        api_response = fireblocks.transactions.unfreeze_transaction(tx_id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key).result()
        print("The response of TransactionsApi->unfreeze_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->unfreeze_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction to unfreeze | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**UnfreezeTransactionResponse**](UnfreezeTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unfreeze response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_address**
> ValidateAddressResponse validate_address(asset_id, address)

Validate destination address

Checks if an address is valid and active (for XRP, DOT, XLM, and EOS).
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.validate_address_response import ValidateAddressResponse
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
    asset_id = 'asset_id_example' # str | The asset of the address
    address = 'address_example' # str | The address to validate

    try:
        # Validate destination address
        api_response = fireblocks.transactions.validate_address(asset_id, address).result()
        print("The response of TransactionsApi->validate_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->validate_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset of the address | 
 **address** | **str**| The address to validate | 

### Return type

[**ValidateAddressResponse**](ValidateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Transaction object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

