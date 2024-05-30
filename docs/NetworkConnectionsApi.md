# fireblocks.NetworkConnectionsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_third_party_routing**](NetworkConnectionsApi.md#check_third_party_routing) | **GET** /network_connections/{connectionId}/is_third_party_routing/{assetType} | Retrieve third-party network routing validation by asset type.
[**create_network_connection**](NetworkConnectionsApi.md#create_network_connection) | **POST** /network_connections | Creates a new network connection
[**create_network_id**](NetworkConnectionsApi.md#create_network_id) | **POST** /network_ids | Creates a new Network ID
[**delete_network_connection**](NetworkConnectionsApi.md#delete_network_connection) | **DELETE** /network_connections/{connectionId} | Deletes a network connection by ID
[**delete_network_id**](NetworkConnectionsApi.md#delete_network_id) | **DELETE** /network_ids/{networkId} | Deletes specific network ID.
[**get_network**](NetworkConnectionsApi.md#get_network) | **GET** /network_connections/{connectionId} | Get a network connection
[**get_network_connections**](NetworkConnectionsApi.md#get_network_connections) | **GET** /network_connections | List network connections
[**get_network_id**](NetworkConnectionsApi.md#get_network_id) | **GET** /network_ids/{networkId} | Returns specific network ID.
[**get_network_ids**](NetworkConnectionsApi.md#get_network_ids) | **GET** /network_ids | Returns all network IDs, both local IDs and discoverable remote IDs
[**get_routing_policy_asset_groups**](NetworkConnectionsApi.md#get_routing_policy_asset_groups) | **GET** /network_ids/routing_policy_asset_groups | Returns all enabled routing policy asset groups
[**set_network_id_discoverability**](NetworkConnectionsApi.md#set_network_id_discoverability) | **PATCH** /network_ids/{networkId}/set_discoverability | Update network ID&#39;s discoverability.
[**set_network_id_name**](NetworkConnectionsApi.md#set_network_id_name) | **PATCH** /network_ids/{networkId}/set_name | Update network ID&#39;s name.
[**set_network_id_routing_policy**](NetworkConnectionsApi.md#set_network_id_routing_policy) | **PATCH** /network_ids/{networkId}/set_routing_policy | Update network id routing policy.
[**set_routing_policy**](NetworkConnectionsApi.md#set_routing_policy) | **PATCH** /network_connections/{connectionId}/set_routing_policy | Update network connection routing policy.


# **check_third_party_routing**
> ThirdPartyRouting check_third_party_routing(connection_id, asset_type)

Retrieve third-party network routing validation by asset type.

The Fireblocks Network allows for flexibility around incoming deposits. A receiver can receive network deposits to locations other than Fireblocks. This endpoint validates whether future transactions are routed to the displayed recipient or to a 3rd party.

### Example


```python
from fireblocks.models.third_party_routing import ThirdPartyRouting
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
    connection_id = 'connection_id_example' # str | The ID of the network connection
    asset_type = 'asset_type_example' # str | The destination asset type

    try:
        # Retrieve third-party network routing validation by asset type.
        api_response = fireblocks.network_connections.check_third_party_routing(connection_id, asset_type).result()
        print("The response of NetworkConnectionsApi->check_third_party_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->check_third_party_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the network connection | 
 **asset_type** | **str**| The destination asset type | 

### Return type

[**ThirdPartyRouting**](ThirdPartyRouting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | result for the validation |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_connection**
> NetworkConnectionResponse create_network_connection(idempotency_key=idempotency_key, network_connection=network_connection)

Creates a new network connection

Initiates a new network connection.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**  Supported asset groups for routing police can be found at `/network_ids/routing_policy_asset_groups`      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.network_connection import NetworkConnection
from fireblocks.models.network_connection_response import NetworkConnectionResponse
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
    network_connection = fireblocks.NetworkConnection() # NetworkConnection |  (optional)

    try:
        # Creates a new network connection
        api_response = fireblocks.network_connections.create_network_connection(idempotency_key=idempotency_key, network_connection=network_connection).result()
        print("The response of NetworkConnectionsApi->create_network_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->create_network_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **network_connection** | [**NetworkConnection**](NetworkConnection.md)|  | [optional] 

### Return type

[**NetworkConnectionResponse**](NetworkConnectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Network Connection object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_id**
> NetworkIdResponse create_network_id(idempotency_key=idempotency_key, create_network_id_request=create_network_id_request)

Creates a new Network ID

Creates a new Network ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**  Supported asset groups for routing police can be found at `/network_ids/routing_policy_asset_groups`      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.create_network_id_request import CreateNetworkIdRequest
from fireblocks.models.network_id_response import NetworkIdResponse
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
    create_network_id_request = fireblocks.CreateNetworkIdRequest() # CreateNetworkIdRequest |  (optional)

    try:
        # Creates a new Network ID
        api_response = fireblocks.network_connections.create_network_id(idempotency_key=idempotency_key, create_network_id_request=create_network_id_request).result()
        print("The response of NetworkConnectionsApi->create_network_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->create_network_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_network_id_request** | [**CreateNetworkIdRequest**](CreateNetworkIdRequest.md)|  | [optional] 

### Return type

[**NetworkIdResponse**](NetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the new network ID in your workspace |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_connection**
> DeleteNetworkConnectionResponse delete_network_connection(connection_id)

Deletes a network connection by ID

Deletes an existing network connection specified by its connection ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.delete_network_connection_response import DeleteNetworkConnectionResponse
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
    connection_id = 'connection_id_example' # str | The ID of the network connection to delete

    try:
        # Deletes a network connection by ID
        api_response = fireblocks.network_connections.delete_network_connection(connection_id).result()
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

[**DeleteNetworkConnectionResponse**](DeleteNetworkConnectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_id**
> DeleteNetworkIdResponse delete_network_id(network_id)

Deletes specific network ID.

Deletes a network by its ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.delete_network_id_response import DeleteNetworkIdResponse
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
    network_id = 'network_id_example' # str | The ID of the network

    try:
        # Deletes specific network ID.
        api_response = fireblocks.network_connections.delete_network_id(network_id).result()
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

[**DeleteNetworkIdResponse**](DeleteNetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network**
> NetworkConnectionResponse get_network(connection_id)

Get a network connection

Gets a network connection by ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.network_connection_response import NetworkConnectionResponse
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
    connection_id = 'connection_id_example' # str | The ID of the connection

    try:
        # Get a network connection
        api_response = fireblocks.network_connections.get_network(connection_id).result()
        print("The response of NetworkConnectionsApi->get_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_network: %s\n" % e)
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
 - **Accept**: application/json

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
from fireblocks.models.network_connection_response import NetworkConnectionResponse
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
        # List network connections
        api_response = fireblocks.network_connections.get_network_connections().result()
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of network connections |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_id**
> NetworkIdResponse get_network_id(network_id)

Returns specific network ID.

Retrieves a network by its ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.network_id_response import NetworkIdResponse
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
    network_id = 'network_id_example' # str | The ID of the network

    try:
        # Returns specific network ID.
        api_response = fireblocks.network_connections.get_network_id(network_id).result()
        print("The response of NetworkConnectionsApi->get_network_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_network_id: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_ids**
> List[NetworkIdResponse] get_network_ids()

Returns all network IDs, both local IDs and discoverable remote IDs

Retrieves a list of all local and discoverable remote network IDs.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.network_id_response import NetworkIdResponse
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
        # Returns all network IDs, both local IDs and discoverable remote IDs
        api_response = fireblocks.network_connections.get_network_ids().result()
        print("The response of NetworkConnectionsApi->get_network_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_network_ids: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[NetworkIdResponse]**](NetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of network IDs |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_policy_asset_groups**
> List[str] get_routing_policy_asset_groups()

Returns all enabled routing policy asset groups

Retrieves a list of all enabled routing policy asset groups. Your routing policy defines how your transactions are routed. You can use one or more enabled routing policy asset groups to describe connection or network id routing policy. 

### Example


```python
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
        # Returns all enabled routing policy asset groups
        api_response = fireblocks.network_connections.get_routing_policy_asset_groups().result()
        print("The response of NetworkConnectionsApi->get_routing_policy_asset_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->get_routing_policy_asset_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of enabled routing policy asset groups |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_network_id_discoverability**
> SetNetworkIdResponse set_network_id_discoverability(network_id, set_network_id_discoverability_request)

Update network ID's discoverability.

Update whether or not the network ID is discoverable by others.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.set_network_id_discoverability_request import SetNetworkIdDiscoverabilityRequest
from fireblocks.models.set_network_id_response import SetNetworkIdResponse
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
    network_id = 'network_id_example' # str | The ID of the network
    set_network_id_discoverability_request = fireblocks.SetNetworkIdDiscoverabilityRequest() # SetNetworkIdDiscoverabilityRequest | 

    try:
        # Update network ID's discoverability.
        api_response = fireblocks.network_connections.set_network_id_discoverability(network_id, set_network_id_discoverability_request).result()
        print("The response of NetworkConnectionsApi->set_network_id_discoverability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->set_network_id_discoverability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The ID of the network | 
 **set_network_id_discoverability_request** | [**SetNetworkIdDiscoverabilityRequest**](SetNetworkIdDiscoverabilityRequest.md)|  | 

### Return type

[**SetNetworkIdResponse**](SetNetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_network_id_name**
> SetNetworkIdResponse set_network_id_name(network_id, set_network_id_name_request)

Update network ID's name.

Updates name of a specified network ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.set_network_id_name_request import SetNetworkIdNameRequest
from fireblocks.models.set_network_id_response import SetNetworkIdResponse
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
    network_id = 'network_id_example' # str | The ID of the network
    set_network_id_name_request = fireblocks.SetNetworkIdNameRequest() # SetNetworkIdNameRequest | 

    try:
        # Update network ID's name.
        api_response = fireblocks.network_connections.set_network_id_name(network_id, set_network_id_name_request).result()
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

[**SetNetworkIdResponse**](SetNetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_network_id_routing_policy**
> SetNetworkIdResponse set_network_id_routing_policy(network_id, set_network_id_routing_policy_request=set_network_id_routing_policy_request)

Update network id routing policy.

Updates the routing policy of a specified network ID.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**  Supported asset groups for routing police can be found at `/network_ids/routing_policy_asset_groups`      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.set_network_id_response import SetNetworkIdResponse
from fireblocks.models.set_network_id_routing_policy_request import SetNetworkIdRoutingPolicyRequest
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
    network_id = 'network_id_example' # str | The ID of the network
    set_network_id_routing_policy_request = fireblocks.SetNetworkIdRoutingPolicyRequest() # SetNetworkIdRoutingPolicyRequest |  (optional)

    try:
        # Update network id routing policy.
        api_response = fireblocks.network_connections.set_network_id_routing_policy(network_id, set_network_id_routing_policy_request=set_network_id_routing_policy_request).result()
        print("The response of NetworkConnectionsApi->set_network_id_routing_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->set_network_id_routing_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| The ID of the network | 
 **set_network_id_routing_policy_request** | [**SetNetworkIdRoutingPolicyRequest**](SetNetworkIdRoutingPolicyRequest.md)|  | [optional] 

### Return type

[**SetNetworkIdResponse**](SetNetworkIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_routing_policy**
> SetRoutingPolicyResponse set_routing_policy(connection_id, set_routing_policy_request=set_routing_policy_request)

Update network connection routing policy.

Updates an existing network connection's routing policy.  **Note:** This API call is subject to Flexible Routing Schemes.  Your routing policy defines how your transactions are routed. You can choose 1 of the 3 different schemes mentioned below for each asset type:   - **None**; Defines the profile routing to no destination for that asset type. Incoming transactions to asset types routed to `None` will fail.   - **Custom**; Route to an account that you choose. If you remove the account, incoming transactions will fail until you choose another one.   - **Default**; Use the routing specified by the network profile the connection is connected to. This scheme is also referred to as \"Profile Routing\"  Default Workspace Presets:   - Network Profile Crypto → **Custom**   - Network Profile FIAT → **None**   - Network Connection Crypto → **Default**   - Network Connection FIAT → **Default**  Supported asset groups for routing police can be found at `/network_ids/routing_policy_asset_groups`      - **Note**: By default, Custom routing scheme uses (`dstId` = `0`, `dstType` = `VAULT`). 

### Example


```python
from fireblocks.models.set_routing_policy_request import SetRoutingPolicyRequest
from fireblocks.models.set_routing_policy_response import SetRoutingPolicyResponse
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
    connection_id = 'connection_id_example' # str | The ID of the network connection
    set_routing_policy_request = fireblocks.SetRoutingPolicyRequest() # SetRoutingPolicyRequest |  (optional)

    try:
        # Update network connection routing policy.
        api_response = fireblocks.network_connections.set_routing_policy(connection_id, set_routing_policy_request=set_routing_policy_request).result()
        print("The response of NetworkConnectionsApi->set_routing_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkConnectionsApi->set_routing_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the network connection | 
 **set_routing_policy_request** | [**SetRoutingPolicyRequest**](SetRoutingPolicyRequest.md)|  | [optional] 

### Return type

[**SetRoutingPolicyResponse**](SetRoutingPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network ID |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

