<a id="__pageTop"></a>
# fireblocks_client.apis.tags.transactions_api.TransactionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_transaction**](#cancel_transaction) | **post** /transactions/{txId}/cancel | Cancel a transaction
[**create_transaction**](#create_transaction) | **post** /transactions | Create a new transaction
[**drop_transaction**](#drop_transaction) | **post** /transactions/{txId}/drop | Drop ETH transaction by ID
[**estimate_network_fee**](#estimate_network_fee) | **get** /estimate_network_fee | Estimate the required fee for an asset
[**estimate_transaction_fee**](#estimate_transaction_fee) | **post** /transactions/estimate_fee | Estimate transaction fee
[**freeze_transaction**](#freeze_transaction) | **post** /transactions/{txId}/freeze | Freeze a transaction
[**get_transaction_by_external_id**](#get_transaction_by_external_id) | **get** /transactions/external_tx_id/{externalTxId}/ | Find a specific transaction by external transaction ID
[**get_transaction_by_id**](#get_transaction_by_id) | **get** /transactions/{txId} | Find a specific transaction by Fireblocks transaction ID
[**get_transactions**](#get_transactions) | **get** /transactions | List transaction history
[**set_confirmation_threshold_for_transaction**](#set_confirmation_threshold_for_transaction) | **post** /transactions/{txId}/set_confirmation_threshold | Set confirmation threshold by transaction ID
[**set_confirmation_threshold_for_transaction_by_hash**](#set_confirmation_threshold_for_transaction_by_hash) | **post** /txHash/{txHash}/set_confirmation_threshold | Set confirmation threshold by transaction hash
[**unfreeze_transaction**](#unfreeze_transaction) | **post** /transactions/{txId}/unfreeze | Unfreeze a transaction
[**validate_address**](#validate_address) | **get** /transactions/validate_address/{assetId}/{address} | Validate destination address

# **cancel_transaction**
<a id="cancel_transaction"></a>
> CancelTransactionResponse cancel_transaction(tx_id)

Cancel a transaction

Cancels a transaction by ID.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.error import Error
from fireblocks_client.model.cancel_transaction_response import CancelTransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'txId': "txId_example",
    }
    try:
        # Cancel a transaction
        api_response = api_instance.cancel_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->cancel_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
txId | TxIdSchema | | 

# TxIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#cancel_transaction.ApiResponseFor200) | An Transaction object
default | [ApiResponseForDefault](#cancel_transaction.ApiResponseForDefault) | Error Response

#### cancel_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CancelTransactionResponse**](../../models/CancelTransactionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### cancel_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_transaction**
<a id="create_transaction"></a>
> CreateTransactionResponse create_transaction()

Create a new transaction

Creates a new transaction.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.transaction_request import TransactionRequest
from fireblocks_client.model.error import Error
from fireblocks_client.model.create_transaction_response import CreateTransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()

    # example passing only optional values
    body = TransactionRequest(
        operation=TransactionOperation("TRANSFER"),
        note="Ticket 123",
        external_tx_id="00000000-0000-0000-0000-000000000000",
        asset_id="ETH",
        source=TransferPeerPath(
            type="VAULT_ACCOUNT",
            sub_type="BINANCE",
            id="id_example",
            name="name_example",
            wallet_id="wallet_id_example",
        ),
        destination=DestinationTransferPeerPath(None),
        destinations=[
            TransactionRequestDestination(
                amount="amount_example",
,
            )
        ],
        amount=None,
        treat_as_gross_amount=False,
        force_sweep=False,
        fee_level="MEDIUM",
        fee=None,
        priority_fee=None,
        fail_on_low_fee=True,
        max_fee="120",
        gas_limit=None,
        gas_price=None,
        network_fee=None,
        replace_tx_by_hash="00000000-0000-0000-0000-000000000000",
        extra_parameters=dict(),
        customer_ref_id="abcdef",
        auto_staking=True,
        network_staking=None,
,
    )
    try:
        # Create a new transaction
        api_response = api_instance.create_transaction(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->create_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionRequest**](../../models/TransactionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_transaction.ApiResponseFor200) | A transaction object
default | [ApiResponseForDefault](#create_transaction.ApiResponseForDefault) | Error Response

#### create_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTransactionResponse**](../../models/CreateTransactionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **drop_transaction**
<a id="drop_transaction"></a>
> DropTransactionResponse drop_transaction(tx_id)

Drop ETH transaction by ID

Drops a stuck ETH transaction and creates a replacement transaction.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.drop_transaction_response import DropTransactionResponse
from fireblocks_client.model.drop_transaction_request import DropTransactionRequest
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'txId': "txId_example",
    }
    try:
        # Drop ETH transaction by ID
        api_response = api_instance.drop_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->drop_transaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'txId': "txId_example",
    }
    body = DropTransactionRequest(
        tx_id="tx_id_example",
        fee_level="fee_level_example",
        gas_price="gas_price_example",
    )
    try:
        # Drop ETH transaction by ID
        api_response = api_instance.drop_transaction(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->drop_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DropTransactionRequest**](../../models/DropTransactionRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
txId | TxIdSchema | | 

# TxIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#drop_transaction.ApiResponseFor200) | Created successfully
default | [ApiResponseForDefault](#drop_transaction.ApiResponseForDefault) | Error Response

#### drop_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**DropTransactionResponse**](../../models/DropTransactionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### drop_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **estimate_network_fee**
<a id="estimate_network_fee"></a>
> EstimatedNetworkFeeResponse estimate_network_fee(asset_id)

Estimate the required fee for an asset

Gets the estimated required fee for an asset. For UTXO based assets, the response will contain the suggested fee per byte, for ETH/ETC based assets, the suggested gas price, and for XRP/XLM, the transaction fee.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.estimated_network_fee_response import EstimatedNetworkFeeResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    query_params = {
        'assetId': "assetId_example",
    }
    try:
        # Estimate the required fee for an asset
        api_response = api_instance.estimate_network_fee(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->estimate_network_fee: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
assetId | AssetIdSchema | | 


# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#estimate_network_fee.ApiResponseFor200) | Estimated fees response
default | [ApiResponseForDefault](#estimate_network_fee.ApiResponseForDefault) | Error Response

#### estimate_network_fee.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**EstimatedNetworkFeeResponse**](../../models/EstimatedNetworkFeeResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### estimate_network_fee.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **estimate_transaction_fee**
<a id="estimate_transaction_fee"></a>
> EstimatedTransactionFeeResponse estimate_transaction_fee()

Estimate transaction fee

Estimates the transaction fee for a transaction request. * Note: Supports all Fireblocks assets except ZCash (ZEC).

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.transaction_request import TransactionRequest
from fireblocks_client.model.error import Error
from fireblocks_client.model.estimated_transaction_fee_response import EstimatedTransactionFeeResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()

    # example passing only optional values
    body = TransactionRequest(
        operation=TransactionOperation("TRANSFER"),
        note="Ticket 123",
        external_tx_id="00000000-0000-0000-0000-000000000000",
        asset_id="ETH",
        source=TransferPeerPath(
            type="VAULT_ACCOUNT",
            sub_type="BINANCE",
            id="id_example",
            name="name_example",
            wallet_id="wallet_id_example",
        ),
        destination=DestinationTransferPeerPath(None),
        destinations=[
            TransactionRequestDestination(
                amount="amount_example",
,
            )
        ],
        amount=None,
        treat_as_gross_amount=False,
        force_sweep=False,
        fee_level="MEDIUM",
        fee=None,
        priority_fee=None,
        fail_on_low_fee=True,
        max_fee="120",
        gas_limit=None,
        gas_price=None,
        network_fee=None,
        replace_tx_by_hash="00000000-0000-0000-0000-000000000000",
        extra_parameters=dict(),
        customer_ref_id="abcdef",
        auto_staking=True,
        network_staking=None,
,
    )
    try:
        # Estimate transaction fee
        api_response = api_instance.estimate_transaction_fee(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->estimate_transaction_fee: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionRequest**](../../models/TransactionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#estimate_transaction_fee.ApiResponseFor200) | Estimated fees response
default | [ApiResponseForDefault](#estimate_transaction_fee.ApiResponseForDefault) | Error Response

#### estimate_transaction_fee.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**EstimatedTransactionFeeResponse**](../../models/EstimatedTransactionFeeResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### estimate_transaction_fee.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **freeze_transaction**
<a id="freeze_transaction"></a>
> FreezeTransactionResponse freeze_transaction(tx_id)

Freeze a transaction

Freezes a transaction by ID.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.freeze_transaction_response import FreezeTransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'txId': "txId_example",
    }
    try:
        # Freeze a transaction
        api_response = api_instance.freeze_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->freeze_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
txId | TxIdSchema | | 

# TxIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#freeze_transaction.ApiResponseFor200) | freeze response

#### freeze_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**FreezeTransactionResponse**](../../models/FreezeTransactionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_transaction_by_external_id**
<a id="get_transaction_by_external_id"></a>
> TransactionResponse get_transaction_by_external_id(external_tx_id)

Find a specific transaction by external transaction ID

Returns transaction by external transaction ID.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.error import Error
from fireblocks_client.model.transaction_response import TransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'externalTxId': "00000000-0000-0000-0000-000000000000",
    }
    try:
        # Find a specific transaction by external transaction ID
        api_response = api_instance.get_transaction_by_external_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_by_external_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
externalTxId | ExternalTxIdSchema | | 

# ExternalTxIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_transaction_by_external_id.ApiResponseFor200) | An Transaction object
default | [ApiResponseForDefault](#get_transaction_by_external_id.ApiResponseForDefault) | Error Response

#### get_transaction_by_external_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionResponse**](../../models/TransactionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_transaction_by_external_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_transaction_by_id**
<a id="get_transaction_by_id"></a>
> TransactionResponse get_transaction_by_id(tx_id)

Find a specific transaction by Fireblocks transaction ID

Returns a transaction by ID.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.error import Error
from fireblocks_client.model.transaction_response import TransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'txId': "00000000-0000-0000-0000-000000000000",
    }
    try:
        # Find a specific transaction by Fireblocks transaction ID
        api_response = api_instance.get_transaction_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transaction_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
txId | TxIdSchema | | 

# TxIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_transaction_by_id.ApiResponseFor200) | An Transaction object
400 | [ApiResponseFor400](#get_transaction_by_id.ApiResponseFor400) | Error Response
default | [ApiResponseForDefault](#get_transaction_by_id.ApiResponseForDefault) | Error Response

#### get_transaction_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**TransactionResponse**](../../models/TransactionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_transaction_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor400 |  |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor400

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_transaction_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_transactions**
<a id="get_transactions"></a>
> [TransactionResponse] get_transactions()

List transaction history

Lists the transaction history for your workspace.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.error import Error
from fireblocks_client.model.transaction_response import TransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()

    # example passing only optional values
    query_params = {
        'before': "before_example",
        'after': "after_example",
        'status': "status_example",
        'orderBy': "createdAt",
        'sort': "ASC",
        'limit': 200,
        'sourceType': "VAULT_ACCOUNT",
        'sourceId': "sourceId_example",
        'destType': "VAULT_ACCOUNT",
        'destId': "destId_example",
        'assets': "assets_example",
        'txHash': "txHash_example",
        'sourceWalletId': "sourceWalletId_example",
        'destWalletId': "destWalletId_example",
    }
    try:
        # List transaction history
        api_response = api_instance.get_transactions(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
before | BeforeSchema | | optional
after | AfterSchema | | optional
status | StatusSchema | | optional
orderBy | OrderBySchema | | optional
sort | SortSchema | | optional
limit | LimitSchema | | optional
sourceType | SourceTypeSchema | | optional
sourceId | SourceIdSchema | | optional
destType | DestTypeSchema | | optional
destId | DestIdSchema | | optional
assets | AssetsSchema | | optional
txHash | TxHashSchema | | optional
sourceWalletId | SourceWalletIdSchema | | optional
destWalletId | DestWalletIdSchema | | optional


# BeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["createdAt", "lastUpdated", ] 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 200

# SourceTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["VAULT_ACCOUNT", "EXCHANGE_ACCOUNT", "INTERNAL_WALLET", "EXTERNAL_WALLET", "FIAT_ACCOUNT", "NETWORK_CONNECTION", "COMPOUND", "UNKNOWN", "GAS_STATION", "END_USER_WALLET", ] 

# SourceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DestTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["VAULT_ACCOUNT", "EXCHANGE_ACCOUNT", "INTERNAL_WALLET", "EXTERNAL_WALLET", "FIAT_ACCOUNT", "NETWORK_CONNECTION", "COMPOUND", "ONE_TIME_ADDRESS", "END_USER_WALLET", ] 

# DestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TxHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SourceWalletIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DestWalletIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_transactions.ApiResponseFor200) | A list of transactions
default | [ApiResponseForDefault](#get_transactions.ApiResponseForDefault) | Error Response

#### get_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransactionResponse**]({{complexTypePrefix}}TransactionResponse.md) | [**TransactionResponse**]({{complexTypePrefix}}TransactionResponse.md) | [**TransactionResponse**]({{complexTypePrefix}}TransactionResponse.md) |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional
next-page | NextPageSchema | | optional
prev-page | PrevPageSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NextPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PrevPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_transactions.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_confirmation_threshold_for_transaction**
<a id="set_confirmation_threshold_for_transaction"></a>
> SetConfirmationsThresholdResponse set_confirmation_threshold_for_transaction(tx_id)

Set confirmation threshold by transaction ID

Overrides the required number of confirmations for transaction completion by transaction ID.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.set_confirmations_threshold_response import SetConfirmationsThresholdResponse
from fireblocks_client.model.error import Error
from fireblocks_client.model.set_confirmations_threshold_request import SetConfirmationsThresholdRequest
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'txId': "txId_example",
    }
    try:
        # Set confirmation threshold by transaction ID
        api_response = api_instance.set_confirmation_threshold_for_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->set_confirmation_threshold_for_transaction: %s\n" % e)

    # example passing only optional values
    path_params = {
        'txId': "txId_example",
    }
    body = SetConfirmationsThresholdRequest(
        num_of_confirmations=3.14,
    )
    try:
        # Set confirmation threshold by transaction ID
        api_response = api_instance.set_confirmation_threshold_for_transaction(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->set_confirmation_threshold_for_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetConfirmationsThresholdRequest**](../../models/SetConfirmationsThresholdRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
txId | TxIdSchema | | 

# TxIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_confirmation_threshold_for_transaction.ApiResponseFor200) | Set successfully
default | [ApiResponseForDefault](#set_confirmation_threshold_for_transaction.ApiResponseForDefault) | Error Response

#### set_confirmation_threshold_for_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**SetConfirmationsThresholdResponse**](../../models/SetConfirmationsThresholdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### set_confirmation_threshold_for_transaction.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_confirmation_threshold_for_transaction_by_hash**
<a id="set_confirmation_threshold_for_transaction_by_hash"></a>
> SetConfirmationsThresholdResponse set_confirmation_threshold_for_transaction_by_hash(tx_hash)

Set confirmation threshold by transaction hash

Overrides the required number of confirmations for transaction completion by transaction hash.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.set_confirmations_threshold_response import SetConfirmationsThresholdResponse
from fireblocks_client.model.error import Error
from fireblocks_client.model.set_confirmations_threshold_request import SetConfirmationsThresholdRequest
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'txHash': "txHash_example",
    }
    try:
        # Set confirmation threshold by transaction hash
        api_response = api_instance.set_confirmation_threshold_for_transaction_by_hash(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->set_confirmation_threshold_for_transaction_by_hash: %s\n" % e)

    # example passing only optional values
    path_params = {
        'txHash': "txHash_example",
    }
    body = SetConfirmationsThresholdRequest(
        num_of_confirmations=3.14,
    )
    try:
        # Set confirmation threshold by transaction hash
        api_response = api_instance.set_confirmation_threshold_for_transaction_by_hash(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->set_confirmation_threshold_for_transaction_by_hash: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetConfirmationsThresholdRequest**](../../models/SetConfirmationsThresholdRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
txHash | TxHashSchema | | 

# TxHashSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_confirmation_threshold_for_transaction_by_hash.ApiResponseFor200) | A list of transactions affected by the change
default | [ApiResponseForDefault](#set_confirmation_threshold_for_transaction_by_hash.ApiResponseForDefault) | Error Response

#### set_confirmation_threshold_for_transaction_by_hash.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**SetConfirmationsThresholdResponse**](../../models/SetConfirmationsThresholdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### set_confirmation_threshold_for_transaction_by_hash.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **unfreeze_transaction**
<a id="unfreeze_transaction"></a>
> UnfreezeTransactionResponse unfreeze_transaction(tx_id)

Unfreeze a transaction

Unfreezes a transaction by ID and makes the transaction available again.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.unfreeze_transaction_response import UnfreezeTransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'txId': "txId_example",
    }
    try:
        # Unfreeze a transaction
        api_response = api_instance.unfreeze_transaction(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->unfreeze_transaction: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
txId | TxIdSchema | | 

# TxIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#unfreeze_transaction.ApiResponseFor200) | Unfreeze response

#### unfreeze_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**UnfreezeTransactionResponse**](../../models/UnfreezeTransactionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **validate_address**
<a id="validate_address"></a>
> ValidateAddressResponse validate_address(asset_idaddress)

Validate destination address

Checks if an address is valid (for XRP, DOT, XLM, and EOS).

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import transactions_api
from fireblocks_client.model.validate_address_response import ValidateAddressResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open(
    "./fireblocks_secret.key",
    "r",
).read()

    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'assetId': "assetId_example",
        'address': "address_example",
    }
    try:
        # Validate destination address
        api_response = api_instance.validate_address(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling TransactionsApi->validate_address: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
assetId | AssetIdSchema | | 
address | AddressSchema | | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#validate_address.ApiResponseFor200) | An Transaction object
default | [ApiResponseForDefault](#validate_address.ApiResponseForDefault) | Error Response

#### validate_address.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidateAddressResponse**](../../models/ValidateAddressResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### validate_address.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

