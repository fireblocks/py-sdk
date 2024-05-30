# fireblocks_client.GasStationsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gas_station_by_asset_id**](GasStationsApi.md#get_gas_station_by_asset_id) | **GET** /gas_station/{assetId} | Get gas station settings by asset
[**get_gas_station_info**](GasStationsApi.md#get_gas_station_info) | **GET** /gas_station | Get gas station settings
[**update_gas_station_configuration**](GasStationsApi.md#update_gas_station_configuration) | **PUT** /gas_station/configuration | Edit gas station settings
[**update_gas_station_configuration_by_asset_id**](GasStationsApi.md#update_gas_station_configuration_by_asset_id) | **PUT** /gas_station/configuration/{assetId} | Edit gas station settings for an asset


# **get_gas_station_by_asset_id**
> GasStationPropertiesResponse get_gas_station_by_asset_id(asset_id)

Get gas station settings by asset

Returns gas station settings and balances for a requested asset.

### Example


```python
from fireblocks_client.models.gas_station_properties_response import GasStationPropertiesResponse
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
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Get gas station settings by asset
        api_response = fireblocks.gas_stations.get_gas_station_by_asset_id(asset_id).result()
        print("The response of GasStationsApi->get_gas_station_by_asset_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GasStationsApi->get_gas_station_by_asset_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset | 

### Return type

[**GasStationPropertiesResponse**](GasStationPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gas Station properties |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gas_station_info**
> GasStationPropertiesResponse get_gas_station_info()

Get gas station settings

Returns gas station settings and ETH balance.

### Example


```python
from fireblocks_client.models.gas_station_properties_response import GasStationPropertiesResponse
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
        # Get gas station settings
        api_response = fireblocks.gas_stations.get_gas_station_info().result()
        print("The response of GasStationsApi->get_gas_station_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GasStationsApi->get_gas_station_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GasStationPropertiesResponse**](GasStationPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gas Station properties |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gas_station_configuration**
> EditGasStationConfigurationResponse update_gas_station_configuration(gas_station_configuration, idempotency_key=idempotency_key)

Edit gas station settings

Configures gas station settings for ETH.

### Example


```python
from fireblocks_client.models.edit_gas_station_configuration_response import EditGasStationConfigurationResponse
from fireblocks_client.models.gas_station_configuration import GasStationConfiguration
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
    gas_station_configuration = fireblocks_client.GasStationConfiguration() # GasStationConfiguration | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Edit gas station settings
        api_response = fireblocks.gas_stations.update_gas_station_configuration(gas_station_configuration, idempotency_key=idempotency_key).result()
        print("The response of GasStationsApi->update_gas_station_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GasStationsApi->update_gas_station_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gas_station_configuration** | [**GasStationConfiguration**](GasStationConfiguration.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**EditGasStationConfigurationResponse**](EditGasStationConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gas_station_configuration_by_asset_id**
> EditGasStationConfigurationResponse update_gas_station_configuration_by_asset_id(asset_id, gas_station_configuration, idempotency_key=idempotency_key)

Edit gas station settings for an asset

Configures gas station settings for a requested asset.

### Example


```python
from fireblocks_client.models.edit_gas_station_configuration_response import EditGasStationConfigurationResponse
from fireblocks_client.models.gas_station_configuration import GasStationConfiguration
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
    asset_id = 'asset_id_example' # str | The ID of the asset
    gas_station_configuration = fireblocks_client.GasStationConfiguration() # GasStationConfiguration | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Edit gas station settings for an asset
        api_response = fireblocks.gas_stations.update_gas_station_configuration_by_asset_id(asset_id, gas_station_configuration, idempotency_key=idempotency_key).result()
        print("The response of GasStationsApi->update_gas_station_configuration_by_asset_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GasStationsApi->update_gas_station_configuration_by_asset_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset | 
 **gas_station_configuration** | [**GasStationConfiguration**](GasStationConfiguration.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**EditGasStationConfigurationResponse**](EditGasStationConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

