# fireblocks_client.NFTsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nft**](NFTsBetaApi.md#get_nft) | **GET** /nfts/tokens/{id} | List token data by ID
[**get_nfts**](NFTsBetaApi.md#get_nfts) | **GET** /nfts/tokens | List tokens by IDs
[**get_ownership_tokens**](NFTsBetaApi.md#get_ownership_tokens) | **GET** /nfts/ownership/tokens | List all owned tokens (paginated)
[**list_owned_collections**](NFTsBetaApi.md#list_owned_collections) | **GET** /nfts/ownership/collections | List owned collections (paginated)
[**refresh_nft_metadata**](NFTsBetaApi.md#refresh_nft_metadata) | **PUT** /nfts/tokens/{id} | Refresh token metadata
[**update_ownership_tokens**](NFTsBetaApi.md#update_ownership_tokens) | **PUT** /nfts/ownership/tokens | Refresh vault account tokens
[**update_token_ownership_status**](NFTsBetaApi.md#update_token_ownership_status) | **PUT** /nfts/ownership/tokens/{id}/status | Update token ownership status


# **get_nft**
> TokenResponse get_nft(id)

List token data by ID

Returns the requested token data.  **Note**: This endpoint is now in Beta, disabled for general availability at this time.  To enroll in beta & enable this endpoint, contact your Fireblocks Customer Success Manager or reach out to [CSM@fireblocks.com](mailto:CSM@fireblocks.com). 

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
    api_instance = fireblocks_client.NFTsBetaApi(api_client)
    id = 'NFT-abcdefabcdefabcdefabcdefabcdefabcdefabcd' # str | NFT ID

    try:
        # List token data by ID
        api_response = api_instance.get_nft(id)
        print("The response of NFTsBetaApi->get_nft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->get_nft: %s\n" % e)
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
> GetNFTs200Response get_nfts(ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order)

List tokens by IDs

Returns the requested tokens data  **Note**: This endpoint is now in Beta, disabled for general availability at this time.  To enroll in beta & enable this endpoint, contact your Fireblocks Customer Success Manager or reach out to [CSM@fireblocks.com](mailto:CSM@fireblocks.com). 

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
    api_instance = fireblocks_client.NFTsBetaApi(api_client)
    ids = 'ids_example' # str | A comma separated list of NFT IDs. Up to 100 are allowed in a single request.
    page_cursor = 'page_cursor_example' # str | Page cursor to fetch (optional)
    page_size = 3.4 # float | Items per page (max 100) (optional)
    sort = ['sort_example'] # List[str] | Sort by param, it can be one param or a list of params separated by comma (optional)
    order = 'ASC' # str | Order direction, it can be `ASC` for ascending or `DESC` for descending (optional) (default to 'ASC')

    try:
        # List tokens by IDs
        api_response = api_instance.get_nfts(ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order)
        print("The response of NFTsBetaApi->get_nfts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->get_nfts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| A comma separated list of NFT IDs. Up to 100 are allowed in a single request. | 
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 100) | [optional] 
 **sort** | [**List[str]**](str.md)| Sort by param, it can be one param or a list of params separated by comma | [optional] 
 **order** | **str**| Order direction, it can be &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending | [optional] [default to &#39;ASC&#39;]

### Return type

[**GetNFTs200Response**](GetNFTs200Response.md)

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
> GetOwnershipTokens200Response get_ownership_tokens(blockchain_descriptor=blockchain_descriptor, vault_account_ids=vault_account_ids, ids=ids, collection_ids=collection_ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status, search=search)

List all owned tokens (paginated)

Returns all tokens and their data in your workspace.  **Note**: This endpoint is now in Beta, disabled for general availability at this time.  To enroll in beta & enable this endpoint, contact your Fireblocks Customer Success Manager or reach out to [CSM@fireblocks.com](mailto:CSM@fireblocks.com). 

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
    api_instance = fireblocks_client.NFTsBetaApi(api_client)
    blockchain_descriptor = 'blockchain_descriptor_example' # str | Blockchain descriptor filter (optional)
    vault_account_ids = 'vault_account_ids_example' # str | A comma separated list of Vault Account IDs. Up to 100 are allowed in a single request (optional)
    ids = 'ids_example' # str | A comma separated list of NFT IDs. Up to 100 are allowed in a single request. (optional)
    collection_ids = 'collection_ids_example' # str | A comma separated list of collection IDs. Up to 100 are allowed in a single request. (optional)
    page_cursor = 'page_cursor_example' # str | Page cursor to fetch (optional)
    page_size = 3.4 # float | Items per page (max 100) (optional)
    sort = ['sort_example'] # List[str] | Sort by param, it can be one param or a list of params separated by comma (optional)
    order = 'ASC' # str | Order direction, it can be `ASC` for ascending or `DESC` for descending (optional) (default to 'ASC')
    status = 'LISTED' # str | Token ownership status (optional) (default to 'LISTED')
    search = 'search_example' # str | Search owned tokens and their collections. Possible criteria for search:  token name and id within the contract/collection, collection name, blockchain descriptor and name. (optional)

    try:
        # List all owned tokens (paginated)
        api_response = api_instance.get_ownership_tokens(blockchain_descriptor=blockchain_descriptor, vault_account_ids=vault_account_ids, ids=ids, collection_ids=collection_ids, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order, status=status, search=search)
        print("The response of NFTsBetaApi->get_ownership_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->get_ownership_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_descriptor** | **str**| Blockchain descriptor filter | [optional] 
 **vault_account_ids** | **str**| A comma separated list of Vault Account IDs. Up to 100 are allowed in a single request | [optional] 
 **ids** | **str**| A comma separated list of NFT IDs. Up to 100 are allowed in a single request. | [optional] 
 **collection_ids** | **str**| A comma separated list of collection IDs. Up to 100 are allowed in a single request. | [optional] 
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 100) | [optional] 
 **sort** | [**List[str]**](str.md)| Sort by param, it can be one param or a list of params separated by comma | [optional] 
 **order** | **str**| Order direction, it can be &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending | [optional] [default to &#39;ASC&#39;]
 **status** | **str**| Token ownership status | [optional] [default to &#39;LISTED&#39;]
 **search** | **str**| Search owned tokens and their collections. Possible criteria for search:  token name and id within the contract/collection, collection name, blockchain descriptor and name. | [optional] 

### Return type

[**GetOwnershipTokens200Response**](GetOwnershipTokens200Response.md)

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
> ListOwnedCollections200Response list_owned_collections(search=search, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order)

List owned collections (paginated)

Returns all collections in your workspace  **Note**: This endpoint is now in Beta, disabled for general availability at this time.  To enroll in beta & enable this endpoint, contact your Fireblocks Customer Success Manager or reach out to [CSM@fireblocks.com](mailto:CSM@fireblocks.com). 

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
    api_instance = fireblocks_client.NFTsBetaApi(api_client)
    search = 'search_example' # str | Search owned collections. Possible criteria for search: collection name, collection contract address. (optional)
    page_cursor = 'page_cursor_example' # str | Page cursor to fetch (optional)
    page_size = 3.4 # float | Items per page (max 100) (optional)
    sort = ['sort_example'] # List[str] | Sort by param, it can be one param or a list of params separated by comma (optional)
    order = 'ASC' # str | Order direction, it can be `ASC` for ascending or `DESC` for descending (optional) (default to 'ASC')

    try:
        # List owned collections (paginated)
        api_response = api_instance.list_owned_collections(search=search, page_cursor=page_cursor, page_size=page_size, sort=sort, order=order)
        print("The response of NFTsBetaApi->list_owned_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->list_owned_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search owned collections. Possible criteria for search: collection name, collection contract address. | [optional] 
 **page_cursor** | **str**| Page cursor to fetch | [optional] 
 **page_size** | **float**| Items per page (max 100) | [optional] 
 **sort** | [**List[str]**](str.md)| Sort by param, it can be one param or a list of params separated by comma | [optional] 
 **order** | **str**| Order direction, it can be &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending | [optional] [default to &#39;ASC&#39;]

### Return type

[**ListOwnedCollections200Response**](ListOwnedCollections200Response.md)

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
> refresh_nft_metadata(id)

Refresh token metadata

Updates the latest token metadata.  **Note**: This endpoint is now in Beta, disabled for general availability at this time.  To enroll in beta & enable this endpoint, contact your Fireblocks Customer Success Manager or reach out to [CSM@fireblocks.com](mailto:CSM@fireblocks.com). 

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
    api_instance = fireblocks_client.NFTsBetaApi(api_client)
    id = 'NFT-abcdefabcdefabcdefabcdefabcdefabcdefabcd' # str | NFT ID

    try:
        # Refresh token metadata
        api_instance.refresh_nft_metadata(id)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->refresh_nft_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFT ID | 

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
> update_ownership_tokens(blockchain_descriptor, vault_account_id)

Refresh vault account tokens

Updates all tokens and balances per blockchain and vault account.  **Note**: This endpoint is now in Beta, disabled for general availability at this time.  To enroll in beta & enable this endpoint, contact your Fireblocks Customer Success Manager or reach out to [CSM@fireblocks.com](mailto:CSM@fireblocks.com). 

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
    api_instance = fireblocks_client.NFTsBetaApi(api_client)
    blockchain_descriptor = 'blockchain_descriptor_example' # str | Blockchain descriptor filter
    vault_account_id = 'vault_account_id_example' # str | Vault account filter

    try:
        # Refresh vault account tokens
        api_instance.update_ownership_tokens(blockchain_descriptor, vault_account_id)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->update_ownership_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockchain_descriptor** | **str**| Blockchain descriptor filter | 
 **vault_account_id** | **str**| Vault account filter | 

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
> update_token_ownership_status(id, update_token_ownership_status_dto)

Update token ownership status

Updates token ownership status for a tenant, in all tenant vaults.  **Note**: This endpoint is now in Beta, disabled for general availability at this time.  To enroll in beta & enable this endpoint, contact your Fireblocks Customer Success Manager or reach out to [CSM@fireblocks.com](mailto:CSM@fireblocks.com). 

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
    api_instance = fireblocks_client.NFTsBetaApi(api_client)
    id = 'NFT-abcdefabcdefabcdefabcdefabcdefabcdefabcd' # str | NFT ID
    update_token_ownership_status_dto = fireblocks_client.UpdateTokenOwnershipStatusDto() # UpdateTokenOwnershipStatusDto | 

    try:
        # Update token ownership status
        api_instance.update_token_ownership_status(id, update_token_ownership_status_dto)
    except Exception as e:
        print("Exception when calling NFTsBetaApi->update_token_ownership_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFT ID | 
 **update_token_ownership_status_dto** | [**UpdateTokenOwnershipStatusDto**](UpdateTokenOwnershipStatusDto.md)|  | 

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

