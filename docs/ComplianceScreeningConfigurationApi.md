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
    api_instance = fireblocks_client.ComplianceScreeningConfigurationApi(api_client)

    try:
        # Get AML Screening Policy Configuration
        api_response = api_instance.get_aml_screening_configuration()
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
    api_instance = fireblocks_client.ComplianceScreeningConfigurationApi(api_client)

    try:
        # Get Travel Rule Screening Policy Configuration
        api_response = api_instance.get_screening_configuration()
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

