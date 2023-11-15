<a id="__pageTop"></a>
# fireblocks_client.apis.tags.off_exchanges_api.OffExchangesApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_off_exchange**](#add_off_exchange) | **post** /off_exchange/add | add collateral
[**get_off_exchange_collateral_accounts**](#get_off_exchange_collateral_accounts) | **get** /off_exchange/collateral_accounts/{mainExchangeAccountId} | Find a specific collateral exchange account
[**get_off_exchange_settlement_transactions**](#get_off_exchange_settlement_transactions) | **get** /off_exchange/settlements/transactions | get settlements transactions from exchange
[**remove_off_exchange**](#remove_off_exchange) | **post** /off_exchange/remove | remove collateral
[**settle_off_exchange_trades**](#settle_off_exchange_trades) | **post** /off_exchange/settlements/trader | create settlement for a trader

# **add_off_exchange**
<a id="add_off_exchange"></a>
> CreateTransactionResponse add_off_exchange()

add collateral

add collateral, create deposit request

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import off_exchanges_api
from fireblocks_client.model.add_collateral_request_body import AddCollateralRequestBody
from fireblocks_client.model.error import Error
from fireblocks_client.model.create_transaction_response import CreateTransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = off_exchanges_api.OffExchangesApi()

    # example passing only optional values
    body = AddCollateralRequestBody(
        transaction_request=TransactionRequest(
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
        ),
        is_src_collateral=True,
    )
    try:
        # add collateral
        api_response = api_instance.add_off_exchange(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling OffExchangesApi->add_off_exchange: %s\n" % e)
```### Parameters

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
[**AddCollateralRequestBody**](../../models/AddCollateralRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_off_exchange.ApiResponseFor200) | A transaction object
default | [ApiResponseForDefault](#add_off_exchange.ApiResponseForDefault) | Error Response

#### add_off_exchange.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTransactionResponse**](../../models/CreateTransactionResponse.md) |  | 


#### add_off_exchange.ApiResponseForDefault
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

# **get_off_exchange_collateral_accounts**
<a id="get_off_exchange_collateral_accounts"></a>
> ExchangeAccount get_off_exchange_collateral_accounts(main_exchange_account_id)

Find a specific collateral exchange account

Returns a collateral account by mainExchangeAccountId.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import off_exchanges_api
from fireblocks_client.model.exchange_account import ExchangeAccount
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = off_exchanges_api.OffExchangesApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'mainExchangeAccountId': "mainExchangeAccountId_example",
    }
    try:
        # Find a specific collateral exchange account
        api_response = api_instance.get_off_exchange_collateral_accounts(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling OffExchangesApi->get_off_exchange_collateral_accounts: %s\n" % e)
```### Parameters

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
mainExchangeAccountId | MainExchangeAccountIdSchema | | 

# MainExchangeAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_off_exchange_collateral_accounts.ApiResponseFor200) | An ExchangeAccount object
default | [ApiResponseForDefault](#get_off_exchange_collateral_accounts.ApiResponseForDefault) | Error Response

#### get_off_exchange_collateral_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**ExchangeAccount**](../../models/ExchangeAccount.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_off_exchange_collateral_accounts.ApiResponseForDefault
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

# **get_off_exchange_settlement_transactions**
<a id="get_off_exchange_settlement_transactions"></a>
> SettlementResponse get_off_exchange_settlement_transactions(main_exchange_account_id)

get settlements transactions from exchange

get settlements transactions from exchange

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import off_exchanges_api
from fireblocks_client.model.error import Error
from fireblocks_client.model.settlement_response import SettlementResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = off_exchanges_api.OffExchangesApi()
    # example passing only required values which don't have defaults set
    query_params = {
        'mainExchangeAccountId': "mainExchangeAccountId_example",
    }
    try:
        # get settlements transactions from exchange
        api_response = api_instance.get_off_exchange_settlement_transactions(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling OffExchangesApi->get_off_exchange_settlement_transactions: %s\n" % e)
```### Parameters

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
mainExchangeAccountId | MainExchangeAccountIdSchema | | 


# MainExchangeAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_off_exchange_settlement_transactions.ApiResponseFor200) | A settlement transactions
default | [ApiResponseForDefault](#get_off_exchange_settlement_transactions.ApiResponseForDefault) | Error Response

#### get_off_exchange_settlement_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**SettlementResponse**](../../models/SettlementResponse.md) |  | 


#### get_off_exchange_settlement_transactions.ApiResponseForDefault
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

# **remove_off_exchange**
<a id="remove_off_exchange"></a>
> CreateTransactionResponse remove_off_exchange()

remove collateral

remove collateral, create withdraw request

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import off_exchanges_api
from fireblocks_client.model.remove_collateral_request_body import RemoveCollateralRequestBody
from fireblocks_client.model.error import Error
from fireblocks_client.model.create_transaction_response import CreateTransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = off_exchanges_api.OffExchangesApi()

    # example passing only optional values
    body = RemoveCollateralRequestBody(
        transaction_request=TransactionRequest(
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
        ),
        is_dst_collateral=True,
    )
    try:
        # remove collateral
        api_response = api_instance.remove_off_exchange(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling OffExchangesApi->remove_off_exchange: %s\n" % e)
```### Parameters

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
[**RemoveCollateralRequestBody**](../../models/RemoveCollateralRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#remove_off_exchange.ApiResponseFor200) | A transaction object
default | [ApiResponseForDefault](#remove_off_exchange.ApiResponseForDefault) | Error Response

#### remove_off_exchange.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTransactionResponse**](../../models/CreateTransactionResponse.md) |  | 


#### remove_off_exchange.ApiResponseForDefault
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

# **settle_off_exchange_trades**
<a id="settle_off_exchange_trades"></a>
> SettlementResponse settle_off_exchange_trades()

create settlement for a trader

create settlement for a trader

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import off_exchanges_api
from fireblocks_client.model.settlement_request_body import SettlementRequestBody
from fireblocks_client.model.error import Error
from fireblocks_client.model.settlement_response import SettlementResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = off_exchanges_api.OffExchangesApi()

    # example passing only optional values
    body = SettlementRequestBody(
        main_exchange_account_id="main_exchange_account_id_example",
    )
    try:
        # create settlement for a trader
        api_response = api_instance.settle_off_exchange_trades(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling OffExchangesApi->settle_off_exchange_trades: %s\n" % e)
```### Parameters

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
[**SettlementRequestBody**](../../models/SettlementRequestBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#settle_off_exchange_trades.ApiResponseFor201) | A settlement object
default | [ApiResponseForDefault](#settle_off_exchange_trades.ApiResponseForDefault) | Error Response

#### settle_off_exchange_trades.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**SettlementResponse**](../../models/SettlementResponse.md) |  | 


#### settle_off_exchange_trades.ApiResponseForDefault
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

