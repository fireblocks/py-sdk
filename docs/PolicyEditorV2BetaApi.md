# fireblocks.PolicyEditorV2BetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_policy**](PolicyEditorV2BetaApi.md#get_active_policy) | **GET** /policy/active_policy | Get the active policy and its validation by policy type
[**get_draft**](PolicyEditorV2BetaApi.md#get_draft) | **GET** /policy/draft | Get the active draft by policy type
[**publish_draft**](PolicyEditorV2BetaApi.md#publish_draft) | **POST** /policy/draft | Send publish request for a certain draft id
[**update_draft**](PolicyEditorV2BetaApi.md#update_draft) | **PUT** /policy/draft | Update the draft with a new set of rules by policy types


# **get_active_policy**
> PolicyAndValidationResponse get_active_policy(policy_type)

Get the active policy and its validation by policy type

Returns the active policy and its validation for a specific policy type. </br>
**Note:** These endpoints are currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.policy_and_validation_response import PolicyAndValidationResponse
from fireblocks.models.policy_type import PolicyType
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
    policy_type = fireblocks.PolicyType() # PolicyType | The policy type(s) to retrieve. Can be a single type or multiple types by repeating the parameter (e.g., ?policyType=TRANSFER&policyType=MINT).

    try:
        # Get the active policy and its validation by policy type
        api_response = fireblocks.policy_editor_v2_beta.get_active_policy(policy_type).result()
        print("The response of PolicyEditorV2BetaApi->get_active_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorV2BetaApi->get_active_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_type** | [**PolicyType**](.md)| The policy type(s) to retrieve. Can be a single type or multiple types by repeating the parameter (e.g., ?policyType&#x3D;TRANSFER&amp;policyType&#x3D;MINT). | 

### Return type

[**PolicyAndValidationResponse**](PolicyAndValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A policy object with validation |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft**
> DraftReviewAndValidationResponse get_draft(policy_type)

Get the active draft by policy type

Returns the active draft and its validation for a specific policy type. </br>
**Note:** These endpoints are currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.draft_review_and_validation_response import DraftReviewAndValidationResponse
from fireblocks.models.policy_type import PolicyType
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
    policy_type = fireblocks.PolicyType() # PolicyType | The policy type(s) to retrieve. Can be a single type or multiple types by repeating the parameter (e.g., ?policyType=TRANSFER&policyType=MINT).

    try:
        # Get the active draft by policy type
        api_response = fireblocks.policy_editor_v2_beta.get_draft(policy_type).result()
        print("The response of PolicyEditorV2BetaApi->get_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorV2BetaApi->get_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_type** | [**PolicyType**](.md)| The policy type(s) to retrieve. Can be a single type or multiple types by repeating the parameter (e.g., ?policyType&#x3D;TRANSFER&amp;policyType&#x3D;MINT). | 

### Return type

[**DraftReviewAndValidationResponse**](DraftReviewAndValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A draft validation response object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_draft**
> PublishResult publish_draft(publish_draft_request, idempotency_key=idempotency_key)

Send publish request for a certain draft id

Send publish request of certain draft id and returns the response. </br>
**Note:** These endpoints are currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Policy Editor, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.


### Example


```python
from fireblocks.models.publish_draft_request import PublishDraftRequest
from fireblocks.models.publish_result import PublishResult
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
    publish_draft_request = fireblocks.PublishDraftRequest() # PublishDraftRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Send publish request for a certain draft id
        api_response = fireblocks.policy_editor_v2_beta.publish_draft(publish_draft_request, idempotency_key=idempotency_key).result()
        print("The response of PolicyEditorV2BetaApi->publish_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorV2BetaApi->publish_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_draft_request** | [**PublishDraftRequest**](PublishDraftRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**PublishResult**](PublishResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A policy publish result object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_draft**
> DraftReviewAndValidationResponse update_draft(update_draft_request, idempotency_key=idempotency_key)

Update the draft with a new set of rules by policy types

Update the draft and return its validation for specific policy types. </br>
**Note:** These endpoints are currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.draft_review_and_validation_response import DraftReviewAndValidationResponse
from fireblocks.models.update_draft_request import UpdateDraftRequest
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
    update_draft_request = fireblocks.UpdateDraftRequest() # UpdateDraftRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update the draft with a new set of rules by policy types
        api_response = fireblocks.policy_editor_v2_beta.update_draft(update_draft_request, idempotency_key=idempotency_key).result()
        print("The response of PolicyEditorV2BetaApi->update_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorV2BetaApi->update_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_draft_request** | [**UpdateDraftRequest**](UpdateDraftRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**DraftReviewAndValidationResponse**](DraftReviewAndValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A draft validation response object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

