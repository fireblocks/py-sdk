# fireblocks_client.GasStationsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_gas_station**](GasStationsApi.md#get_gas_station) | **GET** /gas_station | Get gas station settings
[**get_gas_station_by_asset_id**](GasStationsApi.md#get_gas_station_by_asset_id) | **GET** /gas_station/{assetId} | Get gas station settings by asset
[**update_gas_station_configuration**](GasStationsApi.md#update_gas_station_configuration) | **PUT** /gas_station/configuration | Edit gas station settings
[**update_gas_station_configuration_by_asset_id**](GasStationsApi.md#update_gas_station_configuration_by_asset_id) | **PUT** /gas_station/configuration/{assetId} | Edit gas station settings for an asset


# **get_gas_station**
> GasStationPropertiesResponse get_gas_station()

Get gas station settings

Returns gas station settings and ETH balance.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.GasStationsApi(api_client)

    try:
        # Get gas station settings
        api_response = api_instance.get_gas_station()
        print("The response of GasStationsApi->get_gas_station:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GasStationsApi->get_gas_station: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GasStationPropertiesResponse**](GasStationPropertiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gas Station properties |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gas_station_by_asset_id**
> GasStationPropertiesResponse get_gas_station_by_asset_id(asset_id)

Get gas station settings by asset

Returns gas station settings and balances for a requested asset.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.GasStationsApi(api_client)
    asset_id = 'asset_id_example' # str | The ID of the asset

    try:
        # Get gas station settings by asset
        api_response = api_instance.get_gas_station_by_asset_id(asset_id)
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
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gas Station properties |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gas_station_configuration**
> update_gas_station_configuration(gas_station_configuration)

Edit gas station settings

Configures gas station settings for ETH.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.GasStationsApi(api_client)
    gas_station_configuration = fireblocks_client.GasStationConfiguration() # GasStationConfiguration | 

    try:
        # Edit gas station settings
        api_instance.update_gas_station_configuration(gas_station_configuration)
    except Exception as e:
        print("Exception when calling GasStationsApi->update_gas_station_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gas_station_configuration** | [**GasStationConfiguration**](GasStationConfiguration.md)|  | 

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
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gas_station_configuration_by_asset_id**
> update_gas_station_configuration_by_asset_id(asset_id, gas_station_configuration)

Edit gas station settings for an asset

Configures gas station settings for a requested asset.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.GasStationsApi(api_client)
    asset_id = 'asset_id_example' # str | The ID of the asset
    gas_station_configuration = fireblocks_client.GasStationConfiguration() # GasStationConfiguration | 

    try:
        # Edit gas station settings for an asset
        api_instance.update_gas_station_configuration_by_asset_id(asset_id, gas_station_configuration)
    except Exception as e:
        print("Exception when calling GasStationsApi->update_gas_station_configuration_by_asset_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The ID of the asset | 
 **gas_station_configuration** | [**GasStationConfiguration**](GasStationConfiguration.md)|  | 

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
**201** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

