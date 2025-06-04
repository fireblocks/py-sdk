# fireblocks.NFTsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nft**](NFTsApi.md#get_nft) | **GET** /nfts/tokens/{id} | List token data by ID
[**get_nfts**](NFTsApi.md#get_nfts) | **GET** /nfts/tokens | List tokens by IDs
[**get_ownership_tokens**](NFTsApi.md#get_ownership_tokens) | **GET** /nfts/ownership/tokens | List all owned tokens (paginated)
[**list_owned_collections**](NFTsApi.md#list_owned_collections) | **GET** /nfts/ownership/collections | List owned collections (paginated)
[**list_owned_tokens**](NFTsApi.md#list_owned_tokens) | **GET** /nfts/ownership/assets | List all distinct owned tokens (paginated)
[**refresh_nft_metadata**](NFTsApi.md#refresh_nft_metadata) | **PUT** /nfts/tokens/{id} | Refresh token metadata
[**update_ownership_tokens**](NFTsApi.md#update_ownership_tokens) | **PUT** /nfts/ownership/tokens | Refresh vault account tokens
[**update_token_ownership_status**](NFTsApi.md#update_token_ownership_status) | **PUT** /nfts/ownership/tokens/{id}/status | Update token ownership status
[**update_tokens_ownership_spam**](NFTsApi.md#update_tokens_ownership_spam) | **PUT** /nfts/ownership/tokens/spam | Update tokens ownership spam property
[**update_tokens_ownership_status**](NFTsApi.md#update_tokens_ownership_status) | **PUT** /nfts/ownership/tokens/status | Update tokens ownership status


# **get_nft**
> TokenResponse get_nft(id)

List token data by ID

Returns the requested token data.


### Example


```python
from fireblocks.models.token_response import TokenResponse
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
    id = 'NFT-abcdefabcdefabcdefabcdefabcdefabcdefabcd' # str | NFT ID

    try:
        # List token data by ID
        api_response = fireblocks.nfts.get_nft(id).result()
        print("The response of NFTsApi->get_nft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsApi->get_nft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFT ID | 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfts**
> GetNFTsResponse get_nfts(ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order)

List tokens by IDs

Returns the requested tokens data.


### Example


```python
from fireblocks.models.get_nfts_response import GetNFTsResponse
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
    ids = 'ids_example' # str | A comma separated list of NFT IDs. Up to 100 are allowed in a single request.
    page_cursor = 'page_cursor_example' # str | Page cursor to fetch (optional)
    page_size = 3.4 # float | Items per page (max 100) (optional)
    sort = ['sort_example'] # List[str] | Sort by param, it can be one param or a list of params separated by comma (optional)
    order = ASC # str | Order direction, it can be `ASC` for ascending or `DESC` for descending (optional) (default to ASC)

    try:
        # List tokens by IDs
        api_response = fireblocks.nfts.get_nfts(ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order).result()
        print("The response of NFTsApi->get_nfts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsApi->get_nfts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| A comma separated list of NFT IDs. Up to 100 are allowed in a single request. | 
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 100) | [optional] 
 **sort** | [**List[str]**](str.md)| Sort by param, it can be one param or a list of params separated by comma | [optional] 
 **order** | **str**| Order direction, it can be &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending | [optional] [default to ASC]

### Return type

[**GetNFTsResponse**](GetNFTsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ownership_tokens**
> GetOwnershipTokensResponse get_ownership_tokens(blockchain_descriptor=blockchain_descriptor, vault_account_ids=vault_account_ids, ncw_id=ncw_id, ncw_account_ids=ncw_account_ids, wallet_type=wallet_type, ids=ids, collection_ids=collection_ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status, search=search, spam=spam)

List all owned tokens (paginated)

Returns all tokens and their data in your workspace.


### Example


```python
from fireblocks.models.get_ownership_tokens_response import GetOwnershipTokensResponse
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
    blockchain_descriptor = 'blockchain_descriptor_example' # str | Blockchain descriptor filter (optional)
    vault_account_ids = 'vault_account_ids_example' # str | A comma separated list of Vault Account IDs. Up to 100 are allowed in a single request.  This field will be ignored when walletType=END_USER_WALLET or ncwId is provided. (optional)
    ncw_id = 'ncw_id_example' # str | Tenant's Non-Custodial Wallet ID (optional)
    ncw_account_ids = 'ncw_account_ids_example' # str | A comma separated list of Non-Custodial account IDs. Up to 100 are allowed in a single request. This field will be ignored when walletType=VAULT_ACCOUNT or ncwId is not provided. (optional)
    wallet_type = VAULT_ACCOUNT # str | Wallet type, it can be `VAULT_ACCOUNT` or `END_USER_WALLET` (optional) (default to VAULT_ACCOUNT)
    ids = 'ids_example' # str | A comma separated list of NFT IDs. Up to 100 are allowed in a single request. (optional)
    collection_ids = 'collection_ids_example' # str | A comma separated list of collection IDs. Up to 100 are allowed in a single request. (optional)
    page_cursor = 'page_cursor_example' # str | Page cursor to fetch (optional)
    page_size = 3.4 # float | Items per page (max 100) (optional)
    sort = ['sort_example'] # List[str] | Sort by param, it can be one param or a list of params separated by comma (optional)
    order = ASC # str | Order direction, it can be `ASC` for ascending or `DESC` for descending (optional) (default to ASC)
    status = LISTED # str | Token ownership status (optional) (default to LISTED)
    search = 'search_example' # str | Search owned tokens and their collections. Possible criteria for search:  token name and id within the contract/collection, collection name, blockchain descriptor and name. (optional)
    spam = 'spam_example' # str | Token ownership spam status. (optional)

    try:
        # List all owned tokens (paginated)
        api_response = fireblocks.nfts.get_ownership_tokens(blockchain_descriptor=blockchain_descriptor, vault_account_ids=vault_account_ids, ncw_id=ncw_id, ncw_account_ids=ncw_account_ids, wallet_type=wallet_type, ids=ids, collection_ids=collection_ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status, search=search, spam=spam).result()
        print("The response of NFTsApi->get_ownership_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsApi->get_ownership_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_descriptor** | **str**| Blockchain descriptor filter | [optional] 
 **vault_account_ids** | **str**| A comma separated list of Vault Account IDs. Up to 100 are allowed in a single request.  This field will be ignored when walletType&#x3D;END_USER_WALLET or ncwId is provided. | [optional] 
 **ncw_id** | **str**| Tenant&#39;s Non-Custodial Wallet ID | [optional] 
 **ncw_account_ids** | **str**| A comma separated list of Non-Custodial account IDs. Up to 100 are allowed in a single request. This field will be ignored when walletType&#x3D;VAULT_ACCOUNT or ncwId is not provided. | [optional] 
 **wallet_type** | **str**| Wallet type, it can be &#x60;VAULT_ACCOUNT&#x60; or &#x60;END_USER_WALLET&#x60; | [optional] [default to VAULT_ACCOUNT]
 **ids** | **str**| A comma separated list of NFT IDs. Up to 100 are allowed in a single request. | [optional] 
 **collection_ids** | **str**| A comma separated list of collection IDs. Up to 100 are allowed in a single request. | [optional] 
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 100) | [optional] 
 **sort** | [**List[str]**](str.md)| Sort by param, it can be one param or a list of params separated by comma | [optional] 
 **order** | **str**| Order direction, it can be &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending | [optional] [default to ASC]
 **status** | **str**| Token ownership status | [optional] [default to LISTED]
 **search** | **str**| Search owned tokens and their collections. Possible criteria for search:  token name and id within the contract/collection, collection name, blockchain descriptor and name. | [optional] 
 **spam** | **str**| Token ownership spam status. | [optional] 

### Return type

[**GetOwnershipTokensResponse**](GetOwnershipTokensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_owned_collections**
> ListOwnedCollectionsResponse list_owned_collections(ncw_id=ncw_id, wallet_type=wallet_type, search=search, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status)

List owned collections (paginated)

Returns all collections in your workspace


### Example


```python
from fireblocks.models.list_owned_collections_response import ListOwnedCollectionsResponse
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
    ncw_id = 'ncw_id_example' # str | Tenant's Non-Custodial Wallet ID (optional)
    wallet_type = VAULT_ACCOUNT # str | Wallet type, it can be `VAULT_ACCOUNT` or `END_USER_WALLET` (optional) (default to VAULT_ACCOUNT)
    search = 'search_example' # str | Search owned collections. Possible criteria for search: collection name, collection contract address. (optional)
    page_cursor = 'page_cursor_example' # str | Page cursor to fetch (optional)
    page_size = 3.4 # float | Items per page (max 100) (optional)
    sort = ['sort_example'] # List[str] | Sort by param, it can be one param or a list of params separated by comma (optional)
    order = ASC # str | Order direction, it can be `ASC` for ascending or `DESC` for descending (optional) (default to ASC)
    status = LISTED # str | Token ownership status (optional) (default to LISTED)

    try:
        # List owned collections (paginated)
        api_response = fireblocks.nfts.list_owned_collections(ncw_id=ncw_id, wallet_type=wallet_type, search=search, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status).result()
        print("The response of NFTsApi->list_owned_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsApi->list_owned_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ncw_id** | **str**| Tenant&#39;s Non-Custodial Wallet ID | [optional] 
 **wallet_type** | **str**| Wallet type, it can be &#x60;VAULT_ACCOUNT&#x60; or &#x60;END_USER_WALLET&#x60; | [optional] [default to VAULT_ACCOUNT]
 **search** | **str**| Search owned collections. Possible criteria for search: collection name, collection contract address. | [optional] 
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 100) | [optional] 
 **sort** | [**List[str]**](str.md)| Sort by param, it can be one param or a list of params separated by comma | [optional] 
 **order** | **str**| Order direction, it can be &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending | [optional] [default to ASC]
 **status** | **str**| Token ownership status | [optional] [default to LISTED]

### Return type

[**ListOwnedCollectionsResponse**](ListOwnedCollectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_owned_tokens**
> ListOwnedTokensResponse list_owned_tokens(ncw_id=ncw_id, wallet_type=wallet_type, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status, search=search, spam=spam)

List all distinct owned tokens (paginated)

Returns all owned distinct tokens (for your tenant) and their data in your workspace.


### Example


```python
from fireblocks.models.list_owned_tokens_response import ListOwnedTokensResponse
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
    ncw_id = 'ncw_id_example' # str | Tenant's Non-Custodial Wallet ID (optional)
    wallet_type = VAULT_ACCOUNT # str | Wallet type, it can be `VAULT_ACCOUNT` or `END_USER_WALLET` (optional) (default to VAULT_ACCOUNT)
    page_cursor = 'page_cursor_example' # str | Page cursor to fetch (optional)
    page_size = 3.4 # float | Items per page (max 100) (optional)
    sort = ['sort_example'] # List[str] | Sort by param, it can be one param or a list of params separated by comma (optional)
    order = ASC # str | Order direction, it can be `ASC` for ascending or `DESC` for descending (optional) (default to ASC)
    status = LISTED # str | Token ownership status (optional) (default to LISTED)
    search = 'search_example' # str | Search owned tokens by token name (optional)
    spam = 'spam_example' # str | Token ownership spam status. (optional)

    try:
        # List all distinct owned tokens (paginated)
        api_response = fireblocks.nfts.list_owned_tokens(ncw_id=ncw_id, wallet_type=wallet_type, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status, search=search, spam=spam).result()
        print("The response of NFTsApi->list_owned_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsApi->list_owned_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ncw_id** | **str**| Tenant&#39;s Non-Custodial Wallet ID | [optional] 
 **wallet_type** | **str**| Wallet type, it can be &#x60;VAULT_ACCOUNT&#x60; or &#x60;END_USER_WALLET&#x60; | [optional] [default to VAULT_ACCOUNT]
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 100) | [optional] 
 **sort** | [**List[str]**](str.md)| Sort by param, it can be one param or a list of params separated by comma | [optional] 
 **order** | **str**| Order direction, it can be &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending | [optional] [default to ASC]
 **status** | **str**| Token ownership status | [optional] [default to LISTED]
 **search** | **str**| Search owned tokens by token name | [optional] 
 **spam** | **str**| Token ownership spam status. | [optional] 

### Return type

[**ListOwnedTokensResponse**](ListOwnedTokensResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_nft_metadata**
> refresh_nft_metadata(id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key)

Refresh token metadata

Updates the latest token metadata.


### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    id = 'NFT-abcdefabcdefabcdefabcdefabcdefabcdefabcd' # str | NFT ID
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Refresh token metadata
        fireblocks.nfts.refresh_nft_metadata(id, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling NFTsApi->refresh_nft_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFT ID | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ownership_tokens**
> update_ownership_tokens(blockchain_descriptor, vault_account_id, idempotency_key=idempotency_key)

Refresh vault account tokens

Updates all tokens and balances per blockchain and vault account.


### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    blockchain_descriptor = 'blockchain_descriptor_example' # str | Blockchain descriptor filter
    vault_account_id = 'vault_account_id_example' # str | Vault account filter
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Refresh vault account tokens
        fireblocks.nfts.update_ownership_tokens(blockchain_descriptor, vault_account_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling NFTsApi->update_ownership_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_descriptor** | **str**| Blockchain descriptor filter | 
 **vault_account_id** | **str**| Vault account filter | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token_ownership_status**
> update_token_ownership_status(id, update_token_ownership_status_dto, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key)

Update token ownership status

Updates token status for a tenant, in all tenant vaults.


### Example


```python
from fireblocks.models.update_token_ownership_status_dto import UpdateTokenOwnershipStatusDto
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    id = 'NFT-abcdefabcdefabcdefabcdefabcdefabcdefabcd' # str | NFT ID
    update_token_ownership_status_dto = fireblocks.UpdateTokenOwnershipStatusDto() # UpdateTokenOwnershipStatusDto | 
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update token ownership status
        fireblocks.nfts.update_token_ownership_status(id, update_token_ownership_status_dto, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling NFTsApi->update_token_ownership_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFT ID | 
 **update_token_ownership_status_dto** | [**UpdateTokenOwnershipStatusDto**](UpdateTokenOwnershipStatusDto.md)|  | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tokens_ownership_spam**
> update_tokens_ownership_spam(token_ownership_spam_update_payload, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key)

Update tokens ownership spam property

Updates tokens spam property for a tenant's token ownerships, in all tenant vaults.

### Example


```python
from fireblocks.models.token_ownership_spam_update_payload import TokenOwnershipSpamUpdatePayload
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    token_ownership_spam_update_payload = [fireblocks.TokenOwnershipSpamUpdatePayload()] # List[TokenOwnershipSpamUpdatePayload] | 
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update tokens ownership spam property
        fireblocks.nfts.update_tokens_ownership_spam(token_ownership_spam_update_payload, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling NFTsApi->update_tokens_ownership_spam: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_ownership_spam_update_payload** | [**List[TokenOwnershipSpamUpdatePayload]**](TokenOwnershipSpamUpdatePayload.md)|  | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All token spam properties have been updated |  * X-Request-ID -  <br>  |
**400** | Invalid data sent |  * X-Request-ID -  <br>  |
**404** | When ownership for token ID is not found |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tokens_ownership_status**
> update_tokens_ownership_status(token_ownership_status_update_payload, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key)

Update tokens ownership status

Updates tokens status for a tenant, in all tenant vaults.

### Example


```python
from fireblocks.models.token_ownership_status_update_payload import TokenOwnershipStatusUpdatePayload
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    token_ownership_status_update_payload = [fireblocks.TokenOwnershipStatusUpdatePayload()] # List[TokenOwnershipStatusUpdatePayload] | 
    x_end_user_wallet_id = 'x_end_user_wallet_id_example' # str | Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update tokens ownership status
        fireblocks.nfts.update_tokens_ownership_status(token_ownership_status_update_payload, x_end_user_wallet_id=x_end_user_wallet_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling NFTsApi->update_tokens_ownership_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_ownership_status_update_payload** | [**List[TokenOwnershipStatusUpdatePayload]**](TokenOwnershipStatusUpdatePayload.md)|  | 
 **x_end_user_wallet_id** | **str**| Unique ID of the End-User wallet to the API request. Required for end-user wallet operations. | [optional] 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All token statuses have been updated |  * X-Request-ID -  <br>  |
**400** | Invalid data sent |  * X-Request-ID -  <br>  |
**404** | When ownership for token ID is not found |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

