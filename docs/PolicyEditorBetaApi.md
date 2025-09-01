# fireblocks.PolicyEditorBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_policy_legacy**](PolicyEditorBetaApi.md#get_active_policy_legacy) | **GET** /tap/active_policy | Get the active policy and its validation
[**get_draft_legacy**](PolicyEditorBetaApi.md#get_draft_legacy) | **GET** /tap/draft | Get the active draft
[**publish_draft_legacy**](PolicyEditorBetaApi.md#publish_draft_legacy) | **POST** /tap/draft | Send publish request for a certain draft id
[**publish_policy_rules**](PolicyEditorBetaApi.md#publish_policy_rules) | **POST** /tap/publish | Send publish request for a set of policy rules
[**update_draft_legacy**](PolicyEditorBetaApi.md#update_draft_legacy) | **PUT** /tap/draft | Update the draft with a new set of rules


# **get_active_policy_legacy**
> LegacyPolicyAndValidationResponse get_active_policy_legacy()

Get the active policy and its validation

Legacy Endpoint – Returns the active policy and its validation. </br>
**Note:** 
- This endpoint will remain available for the foreseeable future and is not deprecated.</br> - The `getActivePolicy` endpoint under policy/paths provides policy type-specific operations and improved functionality.</br> - These endpoints are currently in beta and might be subject to changes.</br>
If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.


### Example


```python
from fireblocks.models.legacy_policy_and_validation_response import LegacyPolicyAndValidationResponse
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
        # Get the active policy and its validation
        api_response = fireblocks.policy_editor_beta.get_active_policy_legacy().result()
        print("The response of PolicyEditorBetaApi->get_active_policy_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->get_active_policy_legacy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LegacyPolicyAndValidationResponse**](LegacyPolicyAndValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A policy object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_legacy**
> LegacyDraftReviewAndValidationResponse get_draft_legacy()

Get the active draft

Legacy Endpoint – Returns the active draft and its validation. </br>
**Note:** 
- This endpoint will remain available for the foreseeable future and is not deprecated.</br> - The `getDraft` endpoint under policy/paths provides policy type-specific operations and improved functionality.</br> - These endpoints are currently in beta and might be subject to changes.</br>
If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.


### Example


```python
from fireblocks.models.legacy_draft_review_and_validation_response import LegacyDraftReviewAndValidationResponse
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
        # Get the active draft
        api_response = fireblocks.policy_editor_beta.get_draft_legacy().result()
        print("The response of PolicyEditorBetaApi->get_draft_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->get_draft_legacy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LegacyDraftReviewAndValidationResponse**](LegacyDraftReviewAndValidationResponse.md)

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

# **publish_draft_legacy**
> LegacyPublishResult publish_draft_legacy(legacy_publish_draft_request, idempotency_key=idempotency_key)

Send publish request for a certain draft id

Legacy Endpoint – Send publish request of certain draft id and returns the response. </br>
**Note:** 
- This endpoint will remain available for the foreseeable future and is not deprecated.</br> - The `publishDraft` endpoint under policy/paths provides improved functionality and better performance.</br> - These endpoints are currently in beta and might be subject to changes.</br>
If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.


### Example


```python
from fireblocks.models.legacy_publish_draft_request import LegacyPublishDraftRequest
from fireblocks.models.legacy_publish_result import LegacyPublishResult
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
    legacy_publish_draft_request = fireblocks.LegacyPublishDraftRequest() # LegacyPublishDraftRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Send publish request for a certain draft id
        api_response = fireblocks.policy_editor_beta.publish_draft_legacy(legacy_publish_draft_request, idempotency_key=idempotency_key).result()
        print("The response of PolicyEditorBetaApi->publish_draft_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->publish_draft_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_publish_draft_request** | [**LegacyPublishDraftRequest**](LegacyPublishDraftRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**LegacyPublishResult**](LegacyPublishResult.md)

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

# **publish_policy_rules**
> LegacyPublishResult publish_policy_rules(legacy_policy_rules, idempotency_key=idempotency_key)

Send publish request for a set of policy rules

Send publish request of set of policy rules and returns the response. </br>
**Note:** These endpoints are currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.


### Example


```python
from fireblocks.models.legacy_policy_rules import LegacyPolicyRules
from fireblocks.models.legacy_publish_result import LegacyPublishResult
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
    legacy_policy_rules = fireblocks.LegacyPolicyRules() # LegacyPolicyRules | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Send publish request for a set of policy rules
        api_response = fireblocks.policy_editor_beta.publish_policy_rules(legacy_policy_rules, idempotency_key=idempotency_key).result()
        print("The response of PolicyEditorBetaApi->publish_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->publish_policy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_policy_rules** | [**LegacyPolicyRules**](LegacyPolicyRules.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**LegacyPublishResult**](LegacyPublishResult.md)

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

# **update_draft_legacy**
> LegacyDraftReviewAndValidationResponse update_draft_legacy(legacy_policy_rules, idempotency_key=idempotency_key)

Update the draft with a new set of rules

Legacy Endpoint – Update the draft and return its validation. </br>
**Note:** 
- This endpoint will remain available for the foreseeable future and is not deprecated.</br> - The `updateDraft` endpoint under policy/paths provides policy type-specific operations and improved functionality.</br> - These endpoints are currently in beta and might be subject to changes.</br>
If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.


### Example


```python
from fireblocks.models.legacy_draft_review_and_validation_response import LegacyDraftReviewAndValidationResponse
from fireblocks.models.legacy_policy_rules import LegacyPolicyRules
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
    legacy_policy_rules = fireblocks.LegacyPolicyRules() # LegacyPolicyRules | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update the draft with a new set of rules
        api_response = fireblocks.policy_editor_beta.update_draft_legacy(legacy_policy_rules, idempotency_key=idempotency_key).result()
        print("The response of PolicyEditorBetaApi->update_draft_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->update_draft_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legacy_policy_rules** | [**LegacyPolicyRules**](LegacyPolicyRules.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**LegacyDraftReviewAndValidationResponse**](LegacyDraftReviewAndValidationResponse.md)

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

