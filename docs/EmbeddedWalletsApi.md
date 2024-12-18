# fireblocks.EmbeddedWalletsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_key_info_for_address_ncw**](EmbeddedWalletsApi.md#get_public_key_info_for_address_ncw) | **GET** /ncw/{walletId}/accounts/{accountId}/{assetId}/{change}/{addressIndex}/public_key_info | Get the public key of an asset
[**get_public_key_info_ncw**](EmbeddedWalletsApi.md#get_public_key_info_ncw) | **GET** /ncw/{walletId}/public_key_info | Get the public key for a derivation path


# **get_public_key_info_for_address_ncw**
> PublicKeyInformation get_public_key_info_for_address_ncw(wallet_id, account_id, asset_id, change, address_index, compressed=compressed)

Get the public key of an asset

Gets the public key of an asset associated with a specific account within a Non-Custodial Wallet

### Example


```python
from fireblocks.models.public_key_information import PublicKeyInformation
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | The ID of the Non-Custodial wallet
    account_id = '0' # str | The ID of the account
    asset_id = 'BTC' # str | The ID of the asset
    change = 0 # float | BIP44 derivation path - change value
    address_index = 0 # float | BIP44 derivation path - index value
    compressed = True # bool | Compressed/Uncompressed public key format (optional)

    try:
        # Get the public key of an asset
        api_response = fireblocks.embedded_wallets.get_public_key_info_for_address_ncw(wallet_id, account_id, asset_id, change, address_index, compressed=compressed).result()
        print("The response of EmbeddedWalletsApi->get_public_key_info_for_address_ncw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_public_key_info_for_address_ncw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the Non-Custodial wallet | 
 **account_id** | **str**| The ID of the account | 
 **asset_id** | **str**| The ID of the asset | 
 **change** | **float**| BIP44 derivation path - change value | 
 **address_index** | **float**| BIP44 derivation path - index value | 
 **compressed** | **bool**| Compressed/Uncompressed public key format | [optional] 

### Return type

[**PublicKeyInformation**](PublicKeyInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public Key Information |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_key_info_ncw**
> PublicKeyInformation get_public_key_info_ncw(wallet_id, derivation_path, algorithm, compressed=compressed)

Get the public key for a derivation path

Gets the public key information based on derivation path and signing algorithm within a Non-Custodial Wallet

### Example


```python
from fireblocks.models.public_key_information import PublicKeyInformation
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
    wallet_id = '550e8400-e29b-41d4-a716-446655440000' # str | The ID of the Non-Custodial wallet
    derivation_path = '[44,0,0,0,0]' # str | An array of integers (passed as JSON stringified array) representing the full BIP44 derivation path of the requested public key.  The first element must always be 44. 
    algorithm = 'algorithm_example' # str | Elliptic Curve
    compressed = True # bool |  (optional)

    try:
        # Get the public key for a derivation path
        api_response = fireblocks.embedded_wallets.get_public_key_info_ncw(wallet_id, derivation_path, algorithm, compressed=compressed).result()
        print("The response of EmbeddedWalletsApi->get_public_key_info_ncw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmbeddedWalletsApi->get_public_key_info_ncw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **str**| The ID of the Non-Custodial wallet | 
 **derivation_path** | **str**| An array of integers (passed as JSON stringified array) representing the full BIP44 derivation path of the requested public key.  The first element must always be 44.  | 
 **algorithm** | **str**| Elliptic Curve | 
 **compressed** | **bool**|  | [optional] 

### Return type

[**PublicKeyInformation**](PublicKeyInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public key information |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

