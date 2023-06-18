# fireblocks_client.FiatAccountsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deposit_funds_from_linked_dda**](FiatAccountsApi.md#deposit_funds_from_linked_dda) | **POST** /fiat_accounts/{accountId}/deposit_from_linked_dda | Deposit funds from DDA
[**get_fiat_account_by_id**](FiatAccountsApi.md#get_fiat_account_by_id) | **GET** /fiat_accounts/{accountId} | Find a specific fiat account
[**get_fiat_accounts**](FiatAccountsApi.md#get_fiat_accounts) | **GET** /fiat_accounts | List fiat accounts
[**redeem_funds_to_linked_dda**](FiatAccountsApi.md#redeem_funds_to_linked_dda) | **POST** /fiat_accounts/{accountId}/redeem_to_linked_dda | Redeem funds to DDA


# **deposit_funds_from_linked_dda**
> deposit_funds_from_linked_dda(account_id, redeem_funds_to_linked_dda_request=redeem_funds_to_linked_dda_request)

Deposit funds from DDA

Deposits funds from the linked DDA.

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
    api_instance = fireblocks_client.FiatAccountsApi(api_client)
    account_id = 'account_id_example' # str | The ID of the fiat account to use
    redeem_funds_to_linked_dda_request = fireblocks_client.RedeemFundsToLinkedDDARequest() # RedeemFundsToLinkedDDARequest |  (optional)

    try:
        # Deposit funds from DDA
        api_instance.deposit_funds_from_linked_dda(account_id, redeem_funds_to_linked_dda_request=redeem_funds_to_linked_dda_request)
    except Exception as e:
        print("Exception when calling FiatAccountsApi->deposit_funds_from_linked_dda: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the fiat account to use | 
 **redeem_funds_to_linked_dda_request** | [**RedeemFundsToLinkedDDARequest**](RedeemFundsToLinkedDDARequest.md)|  | [optional] 

### Return type

void (empty response body)

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

# **get_fiat_account_by_id**
> FiatAccount get_fiat_account_by_id(account_id)

Find a specific fiat account

Returns a fiat account by ID.

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
    api_instance = fireblocks_client.FiatAccountsApi(api_client)
    account_id = 'account_id_example' # str | The ID of the fiat account to return

    try:
        # Find a specific fiat account
        api_response = api_instance.get_fiat_account_by_id(account_id)
        print("The response of FiatAccountsApi->get_fiat_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FiatAccountsApi->get_fiat_account_by_id: %s\n" % e)
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
 - **Accept**: */*, application/json

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
    api_instance = fireblocks_client.FiatAccountsApi(api_client)

    try:
        # List fiat accounts
        api_response = api_instance.get_fiat_accounts()
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A fiat account object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_funds_to_linked_dda**
> redeem_funds_to_linked_dda(account_id, redeem_funds_to_linked_dda_request=redeem_funds_to_linked_dda_request)

Redeem funds to DDA

Redeems funds to the linked DDA.

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
    api_instance = fireblocks_client.FiatAccountsApi(api_client)
    account_id = 'account_id_example' # str | The ID of the fiat account to use
    redeem_funds_to_linked_dda_request = fireblocks_client.RedeemFundsToLinkedDDARequest() # RedeemFundsToLinkedDDARequest |  (optional)

    try:
        # Redeem funds to DDA
        api_instance.redeem_funds_to_linked_dda(account_id, redeem_funds_to_linked_dda_request=redeem_funds_to_linked_dda_request)
    except Exception as e:
        print("Exception when calling FiatAccountsApi->redeem_funds_to_linked_dda: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The ID of the fiat account to use | 
 **redeem_funds_to_linked_dda_request** | [**RedeemFundsToLinkedDDARequest**](RedeemFundsToLinkedDDARequest.md)|  | [optional] 

### Return type

void (empty response body)

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

