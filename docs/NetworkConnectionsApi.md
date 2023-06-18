# fireblocks_client.NetworkConnectionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_third_party_routing_for_network_connection**](NetworkConnectionsApi.md#check_third_party_routing_for_network_connection) | **GET** /network_connections/{connectionId}/is_third_party_routing/{assetType} | Retrieve third-party network routing validation by asset type.
[**create_network_connection**](NetworkConnectionsApi.md#create_network_connection) | **POST** /network_connections | Creates a new network connection
[**create_network_id**](NetworkConnectionsApi.md#create_network_id) | **POST** /network_ids | Creates a new Network ID
[**delete_network_connection**](NetworkConnectionsApi.md#delete_network_connection) | **DELETE** /network_connections/{connectionId} | Deletes a network connection by ID
[**delete_network_id**](NetworkConnectionsApi.md#delete_network_id) | **DELETE** /network_ids/{networkId} | Deletes specific network ID.
[**get_network_connection_by_id**](NetworkConnectionsApi.md#get_network_connection_by_id) | **GET** /network_connections/{connectionId} | Get a network connection
[**get_network_connections**](NetworkConnectionsApi.md#get_network_connections) | **GET** /network_connections | List network connections
[**get_network_id_by_id**](NetworkConnectionsApi.md#get_network_id_by_id) | **GET** /network_ids/{networkId} | Returns specific network ID.
[**get_network_ids**](NetworkConnectionsApi.md#get_network_ids) | **GET** /network_ids | Returns all network IDs, both local IDs and discoverable remote IDs
[**set_discoverability_for_network_id**](NetworkConnectionsApi.md#set_discoverability_for_network_id) | **PATCH** /network_ids/{networkId}/set_discoverability | Update network ID&#39;s discoverability.
[**set_network_id_name**](NetworkConnectionsApi.md#set_network_id_name) | **PATCH** /network_ids/{networkId}/set_name | Update network ID&#39;s name.
[**set_routing_policy_for_network_connection**](NetworkConnectionsApi.md#set_routing_policy_for_network_connection) | **PATCH** /network_connections/{connectionId}/set_routing_policy | Update network connection routing policy.
[**set_routing_policy_for_network_id**](NetworkConnectionsApi.md#set_routing_policy_for_network_id) | **PATCH** /network_ids/{networkId}/set_routing_policy | Update network id routing policy.


# **check_third_party_routing_for_network_connection**
> CheckThirdPartyRoutingForNetworkConnection200Response check_third_party_routing_for_network_connection(connection_id, asset_type)

Retrieve third-party network routing validation by asset type.

The Fireblocks Network allows for flexibility around incoming deposits. A receiver can receive network deposits to locations other than Fireblocks. This endpoint validates whether future transactions are routed to the displayed recipient or to a 3rd party.

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | The ID of the network connection
    asset_type = 'asset_type_example' # str | The destination asset type

    try:
        # Retrieve third-party network routing validation by asset type.
        api_response = api_instance.check_third_party_routing_for_network_connection(connection_id, asset_type)
        print("The response of NetworkConnectionsApi->check_third_party_routing_for_network_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->check_third_party_routing_for_network_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the network connection | 
 **asset_type** | **str**| The destination asset type | 

### Return type

[**CheckThirdPartyRoutingForNetworkConnection200Response**](CheckThirdPartyRoutingForNetworkConnection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | result for the validation |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_connection**
> NetworkConnectionResponse create_network_connection(network_connection=network_connection)

Creates a new network connection

Initiates a new network connection.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    network_connection = fireblocks_client.NetworkConnection() # NetworkConnection |  (optional)

    try:
        # Creates a new network connection
        api_response = api_instance.create_network_connection(network_connection=network_connection)
        print("The response of NetworkConnectionsApi->create_network_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->create_network_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_connection** | [**NetworkConnection**](NetworkConnection.md)|  | [optional] 

### Return type

[**NetworkConnectionResponse**](NetworkConnectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Network Connection object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_id**
> NetworkIdResponse create_network_id(create_network_id_request=create_network_id_request)

Creates a new Network ID

Creates a new Network ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    create_network_id_request = fireblocks_client.CreateNetworkIdRequest() # CreateNetworkIdRequest |  (optional)

    try:
        # Creates a new Network ID
        api_response = api_instance.create_network_id(create_network_id_request=create_network_id_request)
        print("The response of NetworkConnectionsApi->create_network_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->create_network_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_id_request** | [**CreateNetworkIdRequest**](CreateNetworkIdRequest.md)|  | [optional] 

### Return type

[**NetworkIdResponse**](NetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the new network ID in your workspace |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_connection**
> SetRoutingPolicyForNetworkConnection200Response delete_network_connection(connection_id)

Deletes a network connection by ID

Deletes an existing network connection specified by its connection ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | The ID of the network connection to delete

    try:
        # Deletes a network connection by ID
        api_response = api_instance.delete_network_connection(connection_id)
        print("The response of NetworkConnectionsApi->delete_network_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->delete_network_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the network connection to delete | 

### Return type

[**SetRoutingPolicyForNetworkConnection200Response**](SetRoutingPolicyForNetworkConnection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_id**
> SetRoutingPolicyForNetworkConnection200Response delete_network_id(network_id)

Deletes specific network ID.

Deletes a network by its ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    network_id = 'network_id_example' # str | The ID of the network

    try:
        # Deletes specific network ID.
        api_response = api_instance.delete_network_id(network_id)
        print("The response of NetworkConnectionsApi->delete_network_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->delete_network_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The ID of the network | 

### Return type

[**SetRoutingPolicyForNetworkConnection200Response**](SetRoutingPolicyForNetworkConnection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_connection_by_id**
> NetworkConnectionResponse get_network_connection_by_id(connection_id)

Get a network connection

Gets a network connection by ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | The ID of the connection

    try:
        # Get a network connection
        api_response = api_instance.get_network_connection_by_id(connection_id)
        print("The response of NetworkConnectionsApi->get_network_connection_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_network_connection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the connection | 

### Return type

[**NetworkConnectionResponse**](NetworkConnectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A network connection |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_connections**
> List[NetworkConnectionResponse] get_network_connections()

List network connections

Returns all network connections.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)

    try:
        # List network connections
        api_response = api_instance.get_network_connections()
        print("The response of NetworkConnectionsApi->get_network_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_network_connections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[NetworkConnectionResponse]**](NetworkConnectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of network connections |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_id_by_id**
> NetworkIdResponse get_network_id_by_id(network_id)

Returns specific network ID.

Retrieves a network by its ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    network_id = 'network_id_example' # str | The ID of the network

    try:
        # Returns specific network ID.
        api_response = api_instance.get_network_id_by_id(network_id)
        print("The response of NetworkConnectionsApi->get_network_id_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_network_id_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The ID of the network | 

### Return type

[**NetworkIdResponse**](NetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_ids**
> List[GetNetworkIds200ResponseInner] get_network_ids()

Returns all network IDs, both local IDs and discoverable remote IDs

Retrieves a list of all local and discoverable remote network IDs.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)

    try:
        # Returns all network IDs, both local IDs and discoverable remote IDs
        api_response = api_instance.get_network_ids()
        print("The response of NetworkConnectionsApi->get_network_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_network_ids: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[GetNetworkIds200ResponseInner]**](GetNetworkIds200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of network IDs |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_discoverability_for_network_id**
> SetRoutingPolicyForNetworkConnection200Response set_discoverability_for_network_id(network_id, set_discoverability_for_network_id_request)

Update network ID's discoverability.

Update whether or not the network ID is discoverable by others.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    network_id = 'network_id_example' # str | The ID of the network
    set_discoverability_for_network_id_request = fireblocks_client.SetDiscoverabilityForNetworkIdRequest() # SetDiscoverabilityForNetworkIdRequest | 

    try:
        # Update network ID's discoverability.
        api_response = api_instance.set_discoverability_for_network_id(network_id, set_discoverability_for_network_id_request)
        print("The response of NetworkConnectionsApi->set_discoverability_for_network_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->set_discoverability_for_network_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The ID of the network | 
 **set_discoverability_for_network_id_request** | [**SetDiscoverabilityForNetworkIdRequest**](SetDiscoverabilityForNetworkIdRequest.md)|  | 

### Return type

[**SetRoutingPolicyForNetworkConnection200Response**](SetRoutingPolicyForNetworkConnection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_network_id_name**
> SetRoutingPolicyForNetworkConnection200Response set_network_id_name(network_id, set_network_id_name_request)

Update network ID's name.

Updates name of a specified network ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    network_id = 'network_id_example' # str | The ID of the network
    set_network_id_name_request = fireblocks_client.SetNetworkIdNameRequest() # SetNetworkIdNameRequest | 

    try:
        # Update network ID's name.
        api_response = api_instance.set_network_id_name(network_id, set_network_id_name_request)
        print("The response of NetworkConnectionsApi->set_network_id_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->set_network_id_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The ID of the network | 
 **set_network_id_name_request** | [**SetNetworkIdNameRequest**](SetNetworkIdNameRequest.md)|  | 

### Return type

[**SetRoutingPolicyForNetworkConnection200Response**](SetRoutingPolicyForNetworkConnection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_routing_policy_for_network_connection**
> SetRoutingPolicyForNetworkConnection200Response set_routing_policy_for_network_connection(connection_id, set_routing_policy_for_network_connection_request=set_routing_policy_for_network_connection_request)

Update network connection routing policy.

Updates an existing network connection's routing policy.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    connection_id = 'connection_id_example' # str | The ID of the network connection
    set_routing_policy_for_network_connection_request = fireblocks_client.SetRoutingPolicyForNetworkConnectionRequest() # SetRoutingPolicyForNetworkConnectionRequest |  (optional)

    try:
        # Update network connection routing policy.
        api_response = api_instance.set_routing_policy_for_network_connection(connection_id, set_routing_policy_for_network_connection_request=set_routing_policy_for_network_connection_request)
        print("The response of NetworkConnectionsApi->set_routing_policy_for_network_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->set_routing_policy_for_network_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the network connection | 
 **set_routing_policy_for_network_connection_request** | [**SetRoutingPolicyForNetworkConnectionRequest**](SetRoutingPolicyForNetworkConnectionRequest.md)|  | [optional] 

### Return type

[**SetRoutingPolicyForNetworkConnection200Response**](SetRoutingPolicyForNetworkConnection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_routing_policy_for_network_id**
> SetRoutingPolicyForNetworkConnection200Response set_routing_policy_for_network_id(network_id, set_routing_policy_for_network_id_request=set_routing_policy_for_network_id_request)

Update network id routing policy.

Updates the routing policy of a specified network ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

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
    api_instance = fireblocks_client.NetworkConnectionsApi(api_client)
    network_id = 'network_id_example' # str | The ID of the network
    set_routing_policy_for_network_id_request = fireblocks_client.SetRoutingPolicyForNetworkIdRequest() # SetRoutingPolicyForNetworkIdRequest |  (optional)

    try:
        # Update network id routing policy.
        api_response = api_instance.set_routing_policy_for_network_id(network_id, set_routing_policy_for_network_id_request=set_routing_policy_for_network_id_request)
        print("The response of NetworkConnectionsApi->set_routing_policy_for_network_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->set_routing_policy_for_network_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The ID of the network | 
 **set_routing_policy_for_network_id_request** | [**SetRoutingPolicyForNetworkIdRequest**](SetRoutingPolicyForNetworkIdRequest.md)|  | [optional] 

### Return type

[**SetRoutingPolicyForNetworkConnection200Response**](SetRoutingPolicyForNetworkConnection200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

