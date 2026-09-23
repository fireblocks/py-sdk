# fireblocks.ApprovalsBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_approval**](ApprovalsBetaApi.md#approve_approval) | **POST** /approvals/{requestId}/approve | Approve an approval request
[**create_approval_key**](ApprovalsBetaApi.md#create_approval_key) | **POST** /management/api_users/{userId}/approval_keys | Register an approval key
[**delete_approval_key**](ApprovalsBetaApi.md#delete_approval_key) | **DELETE** /management/api_users/{userId}/approval_keys/{keyId} | Delete an approval key
[**get_approval_by_id**](ApprovalsBetaApi.md#get_approval_by_id) | **GET** /approvals/{requestId} | Get a single approval request
[**get_approval_keys**](ApprovalsBetaApi.md#get_approval_keys) | **GET** /management/api_users/{userId}/approval_keys | List approval keys
[**get_approvals**](ApprovalsBetaApi.md#get_approvals) | **GET** /approvals | List approval requests
[**reject_approval**](ApprovalsBetaApi.md#reject_approval) | **POST** /approvals/{requestId}/reject | Reject an approval request


# **approve_approval**
> approve_approval(request_id, approve_approval_request, idempotency_key=idempotency_key)

Approve an approval request

Approve a pending approval request as the authenticated API user. The caller signs the request's signable data with the private key of a registered approval API key and submits the base64url-encoded signature, optionally with the key ID. The server verifies the signature against the registered public key — using the given key ID, or matching against all of the user's registered keys when the key ID is omitted — and advances the approval quorum.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Approver, Signer, Security Admin.

### Example


```python
from fireblocks.models.approve_approval_request import ApproveApprovalRequest
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
    request_id = '18055' # str | The approval request ID.
    approve_approval_request = fireblocks.ApproveApprovalRequest() # ApproveApprovalRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Approve an approval request
        fireblocks.approvals_beta.approve_approval(request_id, approve_approval_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->approve_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The approval request ID. | 
 **approve_approval_request** | [**ApproveApprovalRequest**](ApproveApprovalRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**204** | The approval request was approved. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_approval_key**
> RegisterApprovalApiKeyResponse create_approval_key(user_id, register_approval_api_key_request, idempotency_key=idempotency_key)

Register an approval key

Register an approval public key for an API user, used to sign approval requests. Up to 2 active keys are supported per API user. Returns the server-generated key ID used for deletion.

The `userId` must be the authenticated API user's own ID. Registering a key for another user is not supported and is rejected.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Approver, Signer, Security Admin.

### Example


```python
from fireblocks.models.register_approval_api_key_request import RegisterApprovalApiKeyRequest
from fireblocks.models.register_approval_api_key_response import RegisterApprovalApiKeyResponse
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
    user_id = '8f3c1a2e-4b7d-4c91-a0e5-2d6f8b1c3a94' # str | The ID of the API user to register the approval key for.
    register_approval_api_key_request = fireblocks.RegisterApprovalApiKeyRequest() # RegisterApprovalApiKeyRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Register an approval key
        api_response = fireblocks.approvals_beta.create_approval_key(user_id, register_approval_api_key_request, idempotency_key=idempotency_key).result()
        print("The response of ApprovalsBetaApi->create_approval_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->create_approval_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the API user to register the approval key for. | 
 **register_approval_api_key_request** | [**RegisterApprovalApiKeyRequest**](RegisterApprovalApiKeyRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**RegisterApprovalApiKeyResponse**](RegisterApprovalApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The approval key was registered. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_approval_key**
> delete_approval_key(user_id, key_id, idempotency_key=idempotency_key)

Delete an approval key

Delete (revoke) an approval public key for the specified API user. Revoking the last key disables the API user's ability to sign approvals.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Approver, Signer, Security Admin.

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
    user_id = '8f3c1a2e-4b7d-4c91-a0e5-2d6f8b1c3a94' # str | The ID of the API user whose approval key to delete.
    key_id = 'fab543c0-d6be-414c-aa05-5c6c84269d7a' # str | The ID of the approval key to delete.
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Delete an approval key
        fireblocks.approvals_beta.delete_approval_key(user_id, key_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->delete_approval_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the API user whose approval key to delete. | 
 **key_id** | **str**| The ID of the approval key to delete. | 
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
**204** | The approval key was deleted. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_by_id**
> ApprovalRequestItem get_approval_by_id(request_id, user_id=user_id, quorum_status_mode=quorum_status_mode)

Get a single approval request

Retrieve full detail for a single approval request by ID, including the payload to sign and, when requested, the request's `quorumStatus`.

Because this endpoint addresses one request, it accepts `quorumStatusMode=FULL`, which adds the participating approvers and their individual approval state.

`userStatus` reflects the authenticated user by default. Pass `userId` to report it for another user instead.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Approver, Signer, Security Admin, Security Auditor.

### Example


```python
from fireblocks.models.approval_request_item import ApprovalRequestItem
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
    request_id = 'request_id_example' # str | The approval request ID.
    user_id = '8f3c1a2e-4b7d-4c91-a0e5-2d6f8b1c3a94' # str | Report `userStatus` for this user instead of the authenticated user. This selects whose approval state is returned; it does not change which requests can be fetched. Requires an Admin, Non-Signing Admin, Security Admin or Security Auditor role; other roles are rejected with 403. (optional)
    quorum_status_mode = NONE # str | How much quorum detail to include in `quorumStatus`. `NONE` (the default) returns it as `null`. `SUMMARY` returns the approval thresholds, current counts and status. `FULL` adds `users` and the per-group `members` indexes identifying who may approve and who already has. Any other value is rejected with 400; the parameter is case-sensitive. (optional) (default to NONE)

    try:
        # Get a single approval request
        api_response = fireblocks.approvals_beta.get_approval_by_id(request_id, user_id=user_id, quorum_status_mode=quorum_status_mode).result()
        print("The response of ApprovalsBetaApi->get_approval_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->get_approval_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The approval request ID. | 
 **user_id** | **str**| Report &#x60;userStatus&#x60; for this user instead of the authenticated user. This selects whose approval state is returned; it does not change which requests can be fetched. Requires an Admin, Non-Signing Admin, Security Admin or Security Auditor role; other roles are rejected with 403. | [optional] 
 **quorum_status_mode** | **str**| How much quorum detail to include in &#x60;quorumStatus&#x60;. &#x60;NONE&#x60; (the default) returns it as &#x60;null&#x60;. &#x60;SUMMARY&#x60; returns the approval thresholds, current counts and status. &#x60;FULL&#x60; adds &#x60;users&#x60; and the per-group &#x60;members&#x60; indexes identifying who may approve and who already has. Any other value is rejected with 400; the parameter is case-sensitive. | [optional] [default to NONE]

### Return type

[**ApprovalRequestItem**](ApprovalRequestItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested approval request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approval_keys**
> ListApprovalApiKeysResponse get_approval_keys(user_id, page_size=page_size, page_cursor=page_cursor)

List approval keys

List the approval public keys registered for the specified API user.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Approver, Signer, Security Admin, Security Auditor.

### Example


```python
from fireblocks.models.list_approval_api_keys_response import ListApprovalApiKeysResponse
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
    user_id = '8f3c1a2e-4b7d-4c91-a0e5-2d6f8b1c3a94' # str | The ID of the API user whose approval keys to list.
    page_size = 10 # int | Number of results per page. Maximum 15. Defaults to 10. (optional) (default to 10)
    page_cursor = 'page_cursor_example' # str | Cursor returned from the previous response (the `next` field) to fetch the next page. (optional)

    try:
        # List approval keys
        api_response = fireblocks.approvals_beta.get_approval_keys(user_id, page_size=page_size, page_cursor=page_cursor).result()
        print("The response of ApprovalsBetaApi->get_approval_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->get_approval_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the API user whose approval keys to list. | 
 **page_size** | **int**| Number of results per page. Maximum 15. Defaults to 10. | [optional] [default to 10]
 **page_cursor** | **str**| Cursor returned from the previous response (the &#x60;next&#x60; field) to fetch the next page. | [optional] 

### Return type

[**ListApprovalApiKeysResponse**](ListApprovalApiKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The API user&#39;s approval keys. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_approvals**
> ListApprovalsResponse get_approvals(include_user_approved=include_user_approved, user_id=user_id, include_all_users=include_all_users, quorum_status_mode=quorum_status_mode, page_size=page_size, page_cursor=page_cursor)

List approval requests

Retrieve the pending approval requests the authenticated API user is eligible to act on, including requests the user has already approved that are still pending overall.

The response is scoped to the authenticated user by default. Pass `userId` to read another user's queue, or `includeAllUsers=true` to read every pending request in the workspace. Both require an Admin, Non-Signing Admin, Security Admin or Security Auditor role and are rejected with 403 otherwise.

Set `quorumStatusMode=SUMMARY` to include each request's approval thresholds and counts. The per-approver breakdown is available only when fetching a single request — see `GET /approvals/{requestId}`.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Approver, Signer, Security Admin, Security Auditor.

### Example


```python
from fireblocks.models.list_approvals_response import ListApprovalsResponse
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
    include_user_approved = True # bool | When true, also include requests the authenticated user has already approved that are still pending overall. Defaults to false (only requests the user has not yet acted on). (optional)
    user_id = '8f3c1a2e-4b7d-4c91-a0e5-2d6f8b1c3a94' # str | Return the pending requests for this user instead of the authenticated user. Requires an Admin, Non-Signing Admin, Security Admin or Security Auditor role; other roles are rejected with 403. Cannot be combined with `includeAllUsers=true` — sending both is rejected with 400. (optional)
    include_all_users = False # bool | When true, return every pending request in the workspace instead of a single user's queue. Defaults to false. Requires an Admin, Non-Signing Admin, Security Admin or Security Auditor role; other roles are rejected with 403. In this mode `userStatus` is always `USER_STATUS_NOT_APPLICABLE`, because the response is not scoped to one user, and `includeUserApproved` has no effect. Cannot be combined with `userId`. (optional) (default to False)
    quorum_status_mode = NONE # str | How much quorum detail to include in each request's `quorumStatus`. `NONE` (the default) returns it as `null`. `SUMMARY` returns the approval thresholds, current counts and status. `FULL` is rejected with 400 on this endpoint because the per-approver breakdown requires a single request — use `GET /approvals/{requestId}` for it. Any other value is rejected with 400; the parameter is case-sensitive. (optional) (default to NONE)
    page_size = 20 # int | Number of results per page. Maximum 30. Defaults to 20. (optional) (default to 20)
    page_cursor = 'page_cursor_example' # str | Cursor returned from the previous response (the `next` field) to fetch the next page. (optional)

    try:
        # List approval requests
        api_response = fireblocks.approvals_beta.get_approvals(include_user_approved=include_user_approved, user_id=user_id, include_all_users=include_all_users, quorum_status_mode=quorum_status_mode, page_size=page_size, page_cursor=page_cursor).result()
        print("The response of ApprovalsBetaApi->get_approvals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->get_approvals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_user_approved** | **bool**| When true, also include requests the authenticated user has already approved that are still pending overall. Defaults to false (only requests the user has not yet acted on). | [optional] 
 **user_id** | **str**| Return the pending requests for this user instead of the authenticated user. Requires an Admin, Non-Signing Admin, Security Admin or Security Auditor role; other roles are rejected with 403. Cannot be combined with &#x60;includeAllUsers&#x3D;true&#x60; — sending both is rejected with 400. | [optional] 
 **include_all_users** | **bool**| When true, return every pending request in the workspace instead of a single user&#39;s queue. Defaults to false. Requires an Admin, Non-Signing Admin, Security Admin or Security Auditor role; other roles are rejected with 403. In this mode &#x60;userStatus&#x60; is always &#x60;USER_STATUS_NOT_APPLICABLE&#x60;, because the response is not scoped to one user, and &#x60;includeUserApproved&#x60; has no effect. Cannot be combined with &#x60;userId&#x60;. | [optional] [default to False]
 **quorum_status_mode** | **str**| How much quorum detail to include in each request&#39;s &#x60;quorumStatus&#x60;. &#x60;NONE&#x60; (the default) returns it as &#x60;null&#x60;. &#x60;SUMMARY&#x60; returns the approval thresholds, current counts and status. &#x60;FULL&#x60; is rejected with 400 on this endpoint because the per-approver breakdown requires a single request — use &#x60;GET /approvals/{requestId}&#x60; for it. Any other value is rejected with 400; the parameter is case-sensitive. | [optional] [default to NONE]
 **page_size** | **int**| Number of results per page. Maximum 30. Defaults to 20. | [optional] [default to 20]
 **page_cursor** | **str**| Cursor returned from the previous response (the &#x60;next&#x60; field) to fetch the next page. | [optional] 

### Return type

[**ListApprovalsResponse**](ListApprovalsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Approval requests the authenticated user is eligible to act on. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_approval**
> reject_approval(request_id, idempotency_key=idempotency_key)

Reject an approval request

Reject a pending approval request as the authenticated API user. No signature is required (unlike approve). The caller must be eligible to act on the request; rejecting finalizes the request as rejected per the approval policy.

Endpoint Permission: Owner, Admin, Non-Signing Admin, Approver, Signer, Security Admin.

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
    request_id = '18055' # str | The approval request ID.
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Reject an approval request
        fireblocks.approvals_beta.reject_approval(request_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling ApprovalsBetaApi->reject_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| The approval request ID. | 
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
**204** | The approval request was rejected. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

