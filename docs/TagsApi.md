# fireblocks.TagsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_approval_request**](TagsApi.md#cancel_approval_request) | **POST** /tags/approval_requests/{id}/cancel | Cancel an approval request by id
[**create_tag**](TagsApi.md#create_tag) | **POST** /tags | Create a new tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tags/{tagId} | Delete a tag
[**get_approval_request**](TagsApi.md#get_approval_request) | **GET** /tags/approval_requests/{id} | Get an approval request by id
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{tagId} | Get a tag
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | Get list of tags
[**update_tag**](TagsApi.md#update_tag) | **PATCH** /tags/{tagId} | Update a tag


# **cancel_approval_request**
> cancel_approval_request(id, idempotency_key=idempotency_key)

Cancel an approval request by id

Cancel an approval request by id. Can only cancel requests in PENDING status. Returns 202 Accepted when the cancellation is processed.

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
    id = '12345' # str | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Cancel an approval request by id
        fireblocks.tags.cancel_approval_request(id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling TagsApi->cancel_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Approval request cancellation processed |  * X-Request-ID -  <br>  |
**401** | Unauthorized |  * X-Request-ID -  <br>  |
**404** | Approval request not found |  * X-Request-ID -  <br>  |
**409** | Invalid approval request state - cannot cancel request that is not in PENDING status |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> Tag create_tag(create_tag_request, idempotency_key=idempotency_key)

Create a new tag

Create a new tag.
Endpoint Permissions: For protected tags: ADMIN,NON_SIGNING_ADMIN,OWNER. For non protected tags: ADMIN,NON_SIGNING_ADMIN,OWNER,SIGNER,EDITOR,APPROVER.

### Example


```python
from fireblocks.models.create_tag_request import CreateTagRequest
from fireblocks.models.tag import Tag
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
    create_tag_request = fireblocks.CreateTagRequest() # CreateTagRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a new tag
        api_response = fireblocks.tags.create_tag(create_tag_request, idempotency_key=idempotency_key).result()
        print("The response of TagsApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_request** | [**CreateTagRequest**](CreateTagRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tag created successfully |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(tag_id)

Delete a tag

Delete the specified tag.
Endpoint Permission: For protected tags: Owner, Admin, Non-Signing Admin. For non protected tags: Owner, Admin, Non-Signing Admin, Signer, Editor, Approver.

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
    tag_id = 'tag_id_example' # str | The ID of the tag to retrieve

    try:
        # Delete a tag
        fireblocks.tags.delete_tag(tag_id).result()
    except Exception as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to retrieve | 

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
**204** | Tag was deleted successfully |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_request**
> ApprovalRequest get_approval_request(id)

Get an approval request by id

Get an approval request by id

### Example


```python
from fireblocks.models.approval_request import ApprovalRequest
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
    id = '12345' # str | 

    try:
        # Get an approval request by id
        api_response = fireblocks.tags.get_approval_request(id).result()
        print("The response of TagsApi->get_approval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_approval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApprovalRequest**](ApprovalRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval request fetched successfully |  * X-Request-ID -  <br>  |
**401** | Unauthorized |  * X-Request-ID -  <br>  |
**404** | Approval request not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag get_tag(tag_id)

Get a tag

Retrieve an existing tag by ID.

### Example


```python
from fireblocks.models.tag import Tag
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
    tag_id = 'tag_id_example' # str | The ID of the tag to retrieve

    try:
        # Get a tag
        api_response = fireblocks.tags.get_tag(tag_id).result()
        print("The response of TagsApi->get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to retrieve | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A tag object |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> TagsPagedResponse get_tags(page_cursor=page_cursor, page_size=page_size, label=label, tag_ids=tag_ids, include_pending_approvals_info=include_pending_approvals_info, is_protected=is_protected)

Get list of tags

Retrieve a paged list of all tags according to filters.

### Example


```python
from fireblocks.models.tags_paged_response import TagsPagedResponse
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
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Page cursor to get the next page. (optional)
    page_size = 100 # float | Maximum number of items in the page (optional) (default to 100)
    label = 'VIP' # str | Label prefix to filter by. (optional)
    tag_ids = ['tag_ids_example'] # List[str] | List of tag IDs to filter by. (optional)
    include_pending_approvals_info = False # bool | Whether to include pending approval requests info. (optional) (default to False)
    is_protected = True # bool |  (optional)

    try:
        # Get list of tags
        api_response = fireblocks.tags.get_tags(page_cursor=page_cursor, page_size=page_size, label=label, tag_ids=tag_ids, include_pending_approvals_info=include_pending_approvals_info, is_protected=is_protected).result()
        print("The response of TagsApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Page cursor to get the next page. | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 100]
 **label** | **str**| Label prefix to filter by. | [optional] 
 **tag_ids** | [**List[str]**](str.md)| List of tag IDs to filter by. | [optional] 
 **include_pending_approvals_info** | **bool**| Whether to include pending approval requests info. | [optional] [default to False]
 **is_protected** | **bool**|  | [optional] 

### Return type

[**TagsPagedResponse**](TagsPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tags fetched successfully |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> Tag update_tag(tag_id, update_tag_request, idempotency_key=idempotency_key)

Update a tag

Update an existing specified tag.
Endpoint Permission: For protected tags: Owner, Admin, Non-Signing Admin. For non protected tags: Owner, Admin, Non-Signing Admin, Signer, Editor, Approver.

### Example


```python
from fireblocks.models.tag import Tag
from fireblocks.models.update_tag_request import UpdateTagRequest
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
    tag_id = 'tag_id_example' # str | The ID of the tag to update
    update_tag_request = fireblocks.UpdateTagRequest() # UpdateTagRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update a tag
        api_response = fireblocks.tags.update_tag(tag_id, update_tag_request, idempotency_key=idempotency_key).result()
        print("The response of TagsApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The ID of the tag to update | 
 **update_tag_request** | [**UpdateTagRequest**](UpdateTagRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A tag object |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

