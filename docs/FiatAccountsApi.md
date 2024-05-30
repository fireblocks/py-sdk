# fireblocks.FiatAccountsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deposit_funds_from_linked_dda**](FiatAccountsApi.md#deposit_funds_from_linked_dda) | **POST** /fiat_accounts/{accountId}/deposit_from_linked_dda | Deposit funds from DDA
[**get_fiat_account**](FiatAccountsApi.md#get_fiat_account) | **GET** /fiat_accounts/{accountId} | Find a specific fiat account
[**get_fiat_accounts**](FiatAccountsApi.md#get_fiat_accounts) | **GET** /fiat_accounts | List fiat accounts
[**redeem_funds_to_linked_dda**](FiatAccountsApi.md#redeem_funds_to_linked_dda) | **POST** /fiat_accounts/{accountId}/redeem_to_linked_dda | Redeem funds to DDA


# **deposit_funds_from_linked_dda**
> DepositFundsFromLinkedDDAResponse deposit_funds_from_linked_dda(account_id, idempotency_key=idempotency_key, funds=funds)

Deposit funds from DDA

Deposits funds from the linked DDA.

### Example


```python
from fireblocks.models.deposit_funds_from_linked_dda_response import DepositFundsFromLinkedDDAResponse
from fireblocks.models.funds import Funds
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
    account_id = 'account_id_example' # str | The ID of the fiat account to use
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    funds = fireblocks.Funds() # Funds |  (optional)

    try:
        # Deposit funds from DDA
        api_response = fireblocks.fiat_accounts.deposit_funds_from_linked_dda(account_id, idempotency_key=idempotency_key, funds=funds).result()
        print("The response of FiatAccountsApi->deposit_funds_from_linked_dda:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiatAccountsApi->deposit_funds_from_linked_dda: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the fiat account to use | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **funds** | [**Funds**](Funds.md)|  | [optional] 

### Return type

[**DepositFundsFromLinkedDDAResponse**](DepositFundsFromLinkedDDAResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer succeeded |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiat_account**
> FiatAccount get_fiat_account(account_id)

Find a specific fiat account

Returns a fiat account by ID.

### Example


```python
from fireblocks.models.fiat_account import FiatAccount
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
    account_id = 'account_id_example' # str | The ID of the fiat account to return

    try:
        # Find a specific fiat account
        api_response = fireblocks.fiat_accounts.get_fiat_account(account_id).result()
        print("The response of FiatAccountsApi->get_fiat_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiatAccountsApi->get_fiat_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the fiat account to return | 

### Return type

[**FiatAccount**](FiatAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A fiat account object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fiat_accounts**
> List[FiatAccount] get_fiat_accounts()

List fiat accounts

Returns all fiat accounts.

### Example


```python
from fireblocks.models.fiat_account import FiatAccount
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
        # List fiat accounts
        api_response = fireblocks.fiat_accounts.get_fiat_accounts().result()
        print("The response of FiatAccountsApi->get_fiat_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiatAccountsApi->get_fiat_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FiatAccount]**](FiatAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A fiat account object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_funds_to_linked_dda**
> RedeemFundsToLinkedDDAResponse redeem_funds_to_linked_dda(account_id, idempotency_key=idempotency_key, funds=funds)

Redeem funds to DDA

Redeems funds to the linked DDA.

### Example


```python
from fireblocks.models.funds import Funds
from fireblocks.models.redeem_funds_to_linked_dda_response import RedeemFundsToLinkedDDAResponse
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
    account_id = 'account_id_example' # str | The ID of the fiat account to use
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    funds = fireblocks.Funds() # Funds |  (optional)

    try:
        # Redeem funds to DDA
        api_response = fireblocks.fiat_accounts.redeem_funds_to_linked_dda(account_id, idempotency_key=idempotency_key, funds=funds).result()
        print("The response of FiatAccountsApi->redeem_funds_to_linked_dda:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiatAccountsApi->redeem_funds_to_linked_dda: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the fiat account to use | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **funds** | [**Funds**](Funds.md)|  | [optional] 

### Return type

[**RedeemFundsToLinkedDDAResponse**](RedeemFundsToLinkedDDAResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transfer succeeded |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

