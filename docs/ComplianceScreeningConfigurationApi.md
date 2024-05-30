# fireblocks_client.ComplianceScreeningConfigurationApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aml_screening_configuration**](ComplianceScreeningConfigurationApi.md#get_aml_screening_configuration) | **GET** /screening/aml/policy_configuration | Get AML Screening Policy Configuration
[**get_screening_configuration**](ComplianceScreeningConfigurationApi.md#get_screening_configuration) | **GET** /screening/travel_rule/policy_configuration | Get Travel Rule Screening Policy Configuration


# **get_aml_screening_configuration**
> ScreeningConfigurationsRequest get_aml_screening_configuration()

Get AML Screening Policy Configuration

Retrieves the configuration for Travel Rule screening policy.

### Example


```python
from fireblocks_client.models.screening_configurations_request import ScreeningConfigurationsRequest
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
        # Get AML Screening Policy Configuration
        api_response = fireblocks.compliance_screening_configuration.get_aml_screening_configuration().result()
        print("The response of ComplianceScreeningConfigurationApi->get_aml_screening_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceScreeningConfigurationApi->get_aml_screening_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Screening policy configuration retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_screening_configuration**
> ScreeningConfigurationsRequest get_screening_configuration()

Get Travel Rule Screening Policy Configuration

Retrieves the configuration for Travel Rule screening policy.

### Example


```python
from fireblocks_client.models.screening_configurations_request import ScreeningConfigurationsRequest
from fireblocks_client.fireblocks import Fireblocks
from fireblocks_client.client_configuration import ClientConfiguration
from fireblocks_client.exceptions import ApiException
from fireblocks_client.base_path import BasePath
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
        # Get Travel Rule Screening Policy Configuration
        api_response = fireblocks.compliance_screening_configuration.get_screening_configuration().result()
        print("The response of ComplianceScreeningConfigurationApi->get_screening_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceScreeningConfigurationApi->get_screening_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Screening policy configuration retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

