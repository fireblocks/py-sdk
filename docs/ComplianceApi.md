# fireblocks_client.ComplianceApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aml_post_screening_policy**](ComplianceApi.md#get_aml_post_screening_policy) | **GET** /screening/aml/post_screening_policy | AML - View Post-Screening Policy
[**get_aml_screening_policy**](ComplianceApi.md#get_aml_screening_policy) | **GET** /screening/aml/screening_policy | AML - View Screening Policy
[**get_post_screening_policy**](ComplianceApi.md#get_post_screening_policy) | **GET** /screening/travel_rule/post_screening_policy | Travel Rule - View Post-Screening Policy
[**get_screening_policy**](ComplianceApi.md#get_screening_policy) | **GET** /screening/travel_rule/screening_policy | Travel Rule - View Screening Policy
[**update_aml_screening_configuration**](ComplianceApi.md#update_aml_screening_configuration) | **PUT** /screening/aml/policy_configuration | Update AML Configuration
[**update_screening_configuration**](ComplianceApi.md#update_screening_configuration) | **PUT** /screening/configurations | Tenant - Screening Configuration
[**update_travel_rule_config**](ComplianceApi.md#update_travel_rule_config) | **PUT** /screening/travel_rule/policy_configuration | Update Travel Rule Configuration


# **get_aml_post_screening_policy**
> ScreeningPolicyResponse get_aml_post_screening_policy()

AML - View Post-Screening Policy

Get the post-screening policy for AML.

### Example


```python
import fireblocks_client
from fireblocks_client.models.screening_policy_response import ScreeningPolicyResponse
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
    api_instance = fireblocks_client.ComplianceApi(api_client)

    try:
        # AML - View Post-Screening Policy
        api_response = api_instance.get_aml_post_screening_policy()
        print("The response of ComplianceApi->get_aml_post_screening_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_aml_post_screening_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScreeningPolicyResponse**](ScreeningPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Post-screening policy retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aml_screening_policy**
> ScreeningProviderRulesConfigurationResponse get_aml_screening_policy()

AML - View Screening Policy

Get the screening policy for AML.

### Example


```python
import fireblocks_client
from fireblocks_client.models.screening_provider_rules_configuration_response import ScreeningProviderRulesConfigurationResponse
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
    api_instance = fireblocks_client.ComplianceApi(api_client)

    try:
        # AML - View Screening Policy
        api_response = api_instance.get_aml_screening_policy()
        print("The response of ComplianceApi->get_aml_screening_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_aml_screening_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScreeningProviderRulesConfigurationResponse**](ScreeningProviderRulesConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screening policy retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_screening_policy**
> ScreeningPolicyResponse get_post_screening_policy()

Travel Rule - View Post-Screening Policy

Get the post-screening policy for Travel Rule.

### Example


```python
import fireblocks_client
from fireblocks_client.models.screening_policy_response import ScreeningPolicyResponse
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
    api_instance = fireblocks_client.ComplianceApi(api_client)

    try:
        # Travel Rule - View Post-Screening Policy
        api_response = api_instance.get_post_screening_policy()
        print("The response of ComplianceApi->get_post_screening_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_post_screening_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScreeningPolicyResponse**](ScreeningPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Post-screening policy retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screening_policy**
> ScreeningProviderRulesConfigurationResponse get_screening_policy()

Travel Rule - View Screening Policy

Get the screening policy for Travel Rule.

### Example


```python
import fireblocks_client
from fireblocks_client.models.screening_provider_rules_configuration_response import ScreeningProviderRulesConfigurationResponse
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
    api_instance = fireblocks_client.ComplianceApi(api_client)

    try:
        # Travel Rule - View Screening Policy
        api_response = api_instance.get_screening_policy()
        print("The response of ComplianceApi->get_screening_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_screening_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScreeningProviderRulesConfigurationResponse**](ScreeningProviderRulesConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screening policy retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aml_screening_configuration**
> ScreeningConfigurationsRequest update_aml_screening_configuration(idempotency_key=idempotency_key)

Update AML Configuration

Updates bypass screening, inbound delay, or outbound delay configurations for AML.

### Example


```python
import fireblocks_client
from fireblocks_client.models.screening_configurations_request import ScreeningConfigurationsRequest
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
    api_instance = fireblocks_client.ComplianceApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update AML Configuration
        api_response = api_instance.update_aml_screening_configuration(idempotency_key=idempotency_key)
        print("The response of ComplianceApi->update_aml_screening_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_aml_screening_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ScreeningConfigurationsRequest**](ScreeningConfigurationsRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_screening_configuration**
> ScreeningUpdateConfigurationsRequest update_screening_configuration(idempotency_key=idempotency_key)

Tenant - Screening Configuration

Update tenant screening configuration.

### Example


```python
import fireblocks_client
from fireblocks_client.models.screening_update_configurations_request import ScreeningUpdateConfigurationsRequest
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
    api_instance = fireblocks_client.ComplianceApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Tenant - Screening Configuration
        api_response = api_instance.update_screening_configuration(idempotency_key=idempotency_key)
        print("The response of ComplianceApi->update_screening_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_screening_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ScreeningUpdateConfigurationsRequest**](ScreeningUpdateConfigurationsRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tenant Screening configuration updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_travel_rule_config**
> ScreeningConfigurationsRequest update_travel_rule_config(idempotency_key=idempotency_key)

Update Travel Rule Configuration

Updates bypass screening, inbound delay, or outbound delay configurations for Travel Rule.

### Example


```python
import fireblocks_client
from fireblocks_client.models.screening_configurations_request import ScreeningConfigurationsRequest
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
    api_instance = fireblocks_client.ComplianceApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update Travel Rule Configuration
        api_response = api_instance.update_travel_rule_config(idempotency_key=idempotency_key)
        print("The response of ComplianceApi->update_travel_rule_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_travel_rule_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ScreeningConfigurationsRequest**](ScreeningConfigurationsRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

