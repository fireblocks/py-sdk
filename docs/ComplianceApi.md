# fireblocks.ComplianceApi

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
from fireblocks.models.screening_policy_response import ScreeningPolicyResponse
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
        # AML - View Post-Screening Policy
        api_response = fireblocks.compliance.get_aml_post_screening_policy().result()
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
from fireblocks.models.screening_provider_rules_configuration_response import ScreeningProviderRulesConfigurationResponse
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
        # AML - View Screening Policy
        api_response = fireblocks.compliance.get_aml_screening_policy().result()
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
from fireblocks.models.screening_policy_response import ScreeningPolicyResponse
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
        # Travel Rule - View Post-Screening Policy
        api_response = fireblocks.compliance.get_post_screening_policy().result()
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
from fireblocks.models.screening_provider_rules_configuration_response import ScreeningProviderRulesConfigurationResponse
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
        # Travel Rule - View Screening Policy
        api_response = fireblocks.compliance.get_screening_policy().result()
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
from fireblocks.models.screening_configurations_request import ScreeningConfigurationsRequest
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
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update AML Configuration
        api_response = fireblocks.compliance.update_aml_screening_configuration(idempotency_key=idempotency_key).result()
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
> ScreeningUpdateConfigurations update_screening_configuration(screening_update_configurations, idempotency_key=idempotency_key)

Tenant - Screening Configuration

Update tenant screening configuration.

### Example


```python
from fireblocks.models.screening_update_configurations import ScreeningUpdateConfigurations
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
    screening_update_configurations = fireblocks.ScreeningUpdateConfigurations() # ScreeningUpdateConfigurations | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Tenant - Screening Configuration
        api_response = fireblocks.compliance.update_screening_configuration(screening_update_configurations, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->update_screening_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_screening_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **screening_update_configurations** | [**ScreeningUpdateConfigurations**](ScreeningUpdateConfigurations.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ScreeningUpdateConfigurations**](ScreeningUpdateConfigurations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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
from fireblocks.models.screening_configurations_request import ScreeningConfigurationsRequest
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
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update Travel Rule Configuration
        api_response = fireblocks.compliance.update_travel_rule_config(idempotency_key=idempotency_key).result()
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

