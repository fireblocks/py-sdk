# fireblocks.FiatAccountsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fiat_accounts**](FiatAccountsApi.md#get_fiat_accounts) | **GET** /fiat_accounts | List fiat accounts


# **get_fiat_accounts**
> List[FiatAccount] get_fiat_accounts()

List fiat accounts

Returns all fiat accounts. </br>Endpoint Permission: Admin, Non-Signing Admin.

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

