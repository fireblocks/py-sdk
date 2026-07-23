# fireblocks.PolicyEditorV2BetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_policy_rule_quota**](PolicyEditorV2BetaApi.md#get_policy_rule_quota) | **POST** /policy/rules/quota | Calculate the AOT quota for a policy rule


# **get_policy_rule_quota**
> PolicyRuleQuotaResponse get_policy_rule_quota(policy_rule_quota_request, idempotency_key=idempotency_key)

Calculate the AOT quota for a policy rule

Returns the Amount Over Time (AOT) quota calculated for a specific policy rule.

Endpoint Permissions: Owner, Admin, Non-Signing Admin.


### Example


```python
from fireblocks.models.policy_rule_quota_request import PolicyRuleQuotaRequest
from fireblocks.models.policy_rule_quota_response import PolicyRuleQuotaResponse
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
    policy_rule_quota_request = fireblocks.PolicyRuleQuotaRequest() # PolicyRuleQuotaRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Calculate the AOT quota for a policy rule
        api_response = fireblocks.policy_editor_v2_beta.get_policy_rule_quota(policy_rule_quota_request, idempotency_key=idempotency_key).result()
        print("The response of PolicyEditorV2BetaApi->get_policy_rule_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyEditorV2BetaApi->get_policy_rule_quota: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_rule_quota_request** | [**PolicyRuleQuotaRequest**](PolicyRuleQuotaRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**PolicyRuleQuotaResponse**](PolicyRuleQuotaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The calculated AOT quota for the rule |  * X-Request-ID -  <br>  |
**400** | Invalid request parameters or rule configuration prevents AOT calculation. |  * X-Request-ID -  <br>  |
**403** | Caller lacks permission to access the requested rule. |  * X-Request-ID -  <br>  |
**404** | The requested policy rule was not found. |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal server error while calculating AOT quota. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

