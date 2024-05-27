# fireblocks_client.PolicyEditorBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_policy**](PolicyEditorBetaApi.md#get_active_policy) | **GET** /tap/active_policy | Get the active policy and its validation
[**get_draft**](PolicyEditorBetaApi.md#get_draft) | **GET** /tap/draft | Get the active draft
[**publish_draft**](PolicyEditorBetaApi.md#publish_draft) | **POST** /tap/draft | Send publish request for a certain draft id
[**publish_policy_rules**](PolicyEditorBetaApi.md#publish_policy_rules) | **POST** /tap/publish | Send publish request for a set of policy rules
[**update_draft**](PolicyEditorBetaApi.md#update_draft) | **PUT** /tap/draft | Update the draft with a new set of rules


# **get_active_policy**
> PolicyAndValidationResponse get_active_policy()

Get the active policy and its validation

Returns the active policy and its validation. </br> **Note:** These endpoints are currently in beta and might be subject to changes. If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example


```python
import fireblocks_client
from fireblocks_client.models.policy_and_validation_response import PolicyAndValidationResponse
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
    api_instance = fireblocks_client.PolicyEditorBetaApi(api_client)

    try:
        # Get the active policy and its validation
        api_response = api_instance.get_active_policy()
        print("The response of PolicyEditorBetaApi->get_active_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->get_active_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | A policy object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft**
> DraftReviewAndValidationResponse get_draft()

Get the active draft

Returns the active draft and its validation. </br> **Note:** These endpoints are currently in beta and might be subject to changes. If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example


```python
import fireblocks_client
from fireblocks_client.models.draft_review_and_validation_response import DraftReviewAndValidationResponse
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
    api_instance = fireblocks_client.PolicyEditorBetaApi(api_client)

    try:
        # Get the active draft
        api_response = api_instance.get_draft()
        print("The response of PolicyEditorBetaApi->get_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->get_draft: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

Send publish request of certain draft id and returns the response. </br> **Note:** These endpoints are currently in beta and might be subject to changes. If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example


```python
import fireblocks_client
from fireblocks_client.models.publish_draft_request import PublishDraftRequest
from fireblocks_client.models.publish_result import PublishResult
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
    api_instance = fireblocks_client.PolicyEditorBetaApi(api_client)
    publish_draft_request = fireblocks_client.PublishDraftRequest() # PublishDraftRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Send publish request for a certain draft id
        api_response = api_instance.publish_draft(publish_draft_request, idempotency_key=idempotency_key)
        print("The response of PolicyEditorBetaApi->publish_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->publish_draft: %s\n" % e)
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

# **publish_policy_rules**
> PublishResult publish_policy_rules(policy_rules, idempotency_key=idempotency_key)

Send publish request for a set of policy rules

Send publish request of set of policy rules and returns the response. </br> **Note:** These endpoints are currently in beta and might be subject to changes. If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example


```python
import fireblocks_client
from fireblocks_client.models.policy_rules import PolicyRules
from fireblocks_client.models.publish_result import PublishResult
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
    api_instance = fireblocks_client.PolicyEditorBetaApi(api_client)
    policy_rules = fireblocks_client.PolicyRules() # PolicyRules | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Send publish request for a set of policy rules
        api_response = api_instance.publish_policy_rules(policy_rules, idempotency_key=idempotency_key)
        print("The response of PolicyEditorBetaApi->publish_policy_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->publish_policy_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_rules** | [**PolicyRules**](PolicyRules.md)|  | 
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
> DraftReviewAndValidationResponse update_draft(policy_rules, idempotency_key=idempotency_key)

Update the draft with a new set of rules

Update the draft and return its validation. </br> **Note:** These endpoints are currently in beta and might be subject to changes. If you want to participate and learn more about the Fireblocks TAP, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com. 

### Example


```python
import fireblocks_client
from fireblocks_client.models.draft_review_and_validation_response import DraftReviewAndValidationResponse
from fireblocks_client.models.policy_rules import PolicyRules
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
    api_instance = fireblocks_client.PolicyEditorBetaApi(api_client)
    policy_rules = fireblocks_client.PolicyRules() # PolicyRules | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update the draft with a new set of rules
        api_response = api_instance.update_draft(policy_rules, idempotency_key=idempotency_key)
        print("The response of PolicyEditorBetaApi->update_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorBetaApi->update_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_rules** | [**PolicyRules**](PolicyRules.md)|  | 
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

