# fireblocks_client.WhitelistIpAddressesApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_whitelist_ip_addresses**](WhitelistIpAddressesApi.md#get_whitelist_ip_addresses) | **GET** /management/api_users/{userId}/whitelist_ip_addresses | Gets whitelisted ip addresses


# **get_whitelist_ip_addresses**
> GetWhitelistIpAddressesResponse get_whitelist_ip_addresses(user_id)

Gets whitelisted ip addresses

Gets whitelisted ip addresses for given Api user.

### Example


```python
from fireblocks_client.models.get_whitelist_ip_addresses_response import GetWhitelistIpAddressesResponse
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
    user_id = 'user_id_example' # str | The ID of the api user

    try:
        # Gets whitelisted ip addresses
        api_response = fireblocks.whitelist_ip_addresses.get_whitelist_ip_addresses(user_id).result()
        print("The response of WhitelistIpAddressesApi->get_whitelist_ip_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhitelistIpAddressesApi->get_whitelist_ip_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the api user | 

### Return type

[**GetWhitelistIpAddressesResponse**](GetWhitelistIpAddressesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully got whitelisted ip addresses |  * X-Request-ID -  <br>  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  * X-Request-ID -  <br>  |
**403** | Lacking permissions. |  * X-Request-ID -  <br>  |
**5XX** | Internal error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

