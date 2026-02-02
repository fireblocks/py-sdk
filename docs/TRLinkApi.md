# fireblocks.TRLinkApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assess_tr_link_travel_rule_requirement**](TRLinkApi.md#assess_tr_link_travel_rule_requirement) | **POST** /screening/trlink/customers/integration/{customerIntegrationId}/trm/assess | Assess Travel Rule requirement
[**cancel_tr_link_trm**](TRLinkApi.md#cancel_tr_link_trm) | **POST** /screening/trlink/customers/integration/{customerIntegrationId}/trm/{trmId}/cancel | Cancel Travel Rule Message
[**connect_tr_link_integration**](TRLinkApi.md#connect_tr_link_integration) | **PUT** /screening/trlink/customers/integration/{customerIntegrationId} | Connect customer integration
[**create_tr_link_customer**](TRLinkApi.md#create_tr_link_customer) | **POST** /screening/trlink/customers | Create customer
[**create_tr_link_integration**](TRLinkApi.md#create_tr_link_integration) | **POST** /screening/trlink/customers/integration | Create customer integration
[**create_tr_link_trm**](TRLinkApi.md#create_tr_link_trm) | **POST** /screening/trlink/customers/integration/{customerIntegrationId}/trm | Create Travel Rule Message
[**delete_tr_link_customer**](TRLinkApi.md#delete_tr_link_customer) | **DELETE** /screening/trlink/customers/{customerId} | Delete customer
[**disconnect_tr_link_integration**](TRLinkApi.md#disconnect_tr_link_integration) | **DELETE** /screening/trlink/customers/integration/{customerIntegrationId} | Disconnect customer integration
[**get_tr_link_customer_by_id**](TRLinkApi.md#get_tr_link_customer_by_id) | **GET** /screening/trlink/customers/{customerId} | Get customer by ID
[**get_tr_link_customer_integration_by_id**](TRLinkApi.md#get_tr_link_customer_integration_by_id) | **GET** /screening/trlink/customers/{customerId}/integrations/{customerIntegrationId} | Get customer integration by ID
[**get_tr_link_customer_integrations**](TRLinkApi.md#get_tr_link_customer_integrations) | **GET** /screening/trlink/customers/{customerId}/integrations | Get customer integrations
[**get_tr_link_customers**](TRLinkApi.md#get_tr_link_customers) | **GET** /screening/trlink/customers | Get all customers
[**get_tr_link_integration_public_key**](TRLinkApi.md#get_tr_link_integration_public_key) | **GET** /screening/trlink/customers/integration/{customerIntegrationId}/public_key | Get public key for PII encryption
[**get_tr_link_partners**](TRLinkApi.md#get_tr_link_partners) | **GET** /screening/trlink/partners | List available TRLink partners
[**get_tr_link_policy**](TRLinkApi.md#get_tr_link_policy) | **GET** /screening/trlink/policy | Get TRLink policy
[**get_tr_link_supported_asset**](TRLinkApi.md#get_tr_link_supported_asset) | **GET** /screening/trlink/customers/integration/{customerIntegrationId}/assets/{assetId} | Get supported asset by ID
[**get_tr_link_trm_by_id**](TRLinkApi.md#get_tr_link_trm_by_id) | **GET** /screening/trlink/customers/integration/{customerIntegrationId}/trm/{trmId} | Get TRM by ID
[**get_tr_link_vasp_by_id**](TRLinkApi.md#get_tr_link_vasp_by_id) | **GET** /screening/trlink/customers/integration/{customerIntegrationId}/vasps/{vaspId} | Get VASP by ID
[**list_tr_link_supported_assets**](TRLinkApi.md#list_tr_link_supported_assets) | **GET** /screening/trlink/customers/integration/{customerIntegrationId}/assets | List supported assets
[**list_tr_link_vasps**](TRLinkApi.md#list_tr_link_vasps) | **GET** /screening/trlink/customers/integration/{customerIntegrationId}/vasps | List VASPs
[**redirect_tr_link_trm**](TRLinkApi.md#redirect_tr_link_trm) | **POST** /screening/trlink/customers/integration/{customerIntegrationId}/trm/{trmId}/redirect | Redirect Travel Rule Message
[**set_tr_link_destination_travel_rule_message_id**](TRLinkApi.md#set_tr_link_destination_travel_rule_message_id) | **POST** /screening/trlink/transaction/{txId}/destination/travel_rule_message_id | Set destination travel rule message ID
[**set_tr_link_transaction_travel_rule_message_id**](TRLinkApi.md#set_tr_link_transaction_travel_rule_message_id) | **POST** /screening/trlink/transaction/{txId}/travel_rule_message_id | Set transaction travel rule message ID
[**test_tr_link_integration_connection**](TRLinkApi.md#test_tr_link_integration_connection) | **POST** /screening/trlink/customers/integration/{customerIntegrationId}/test_connection | Test connection
[**update_tr_link_customer**](TRLinkApi.md#update_tr_link_customer) | **PUT** /screening/trlink/customers/{customerId} | Update customer


# **assess_tr_link_travel_rule_requirement**
> TRLinkAssessTravelRuleResponse assess_tr_link_travel_rule_requirement(customer_integration_id, tr_link_assess_travel_rule_request, idempotency_key=idempotency_key)

Assess Travel Rule requirement

Assesses travel rule requirement for a transaction by validating stored credentials and determining whether Travel Rule compliance is required based on amount, jurisdiction, and partner thresholds.

### Example


```python
from fireblocks.models.tr_link_assess_travel_rule_request import TRLinkAssessTravelRuleRequest
from fireblocks.models.tr_link_assess_travel_rule_response import TRLinkAssessTravelRuleResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    tr_link_assess_travel_rule_request = fireblocks.TRLinkAssessTravelRuleRequest() # TRLinkAssessTravelRuleRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Assess Travel Rule requirement
        api_response = fireblocks.tr_link.assess_tr_link_travel_rule_requirement(customer_integration_id, tr_link_assess_travel_rule_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->assess_tr_link_travel_rule_requirement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->assess_tr_link_travel_rule_requirement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **tr_link_assess_travel_rule_request** | [**TRLinkAssessTravelRuleRequest**](TRLinkAssessTravelRuleRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkAssessTravelRuleResponse**](TRLinkAssessTravelRuleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Travel rule assessment completed |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_tr_link_trm**
> TRLinkTrmInfoResponse cancel_tr_link_trm(customer_integration_id, trm_id, tr_link_cancel_trm_request, idempotency_key=idempotency_key)

Cancel Travel Rule Message

Cancels a travel rule message. The TRM status will be updated to cancelled and the partner will be notified.

### Example


```python
from fireblocks.models.tr_link_cancel_trm_request import TRLinkCancelTrmRequest
from fireblocks.models.tr_link_trm_info_response import TRLinkTrmInfoResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    trm_id = 'trm_id_example' # str | Travel Rule Message unique identifier
    tr_link_cancel_trm_request = fireblocks.TRLinkCancelTrmRequest() # TRLinkCancelTrmRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Cancel Travel Rule Message
        api_response = fireblocks.tr_link.cancel_tr_link_trm(customer_integration_id, trm_id, tr_link_cancel_trm_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->cancel_tr_link_trm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->cancel_tr_link_trm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **trm_id** | **str**| Travel Rule Message unique identifier | 
 **tr_link_cancel_trm_request** | [**TRLinkCancelTrmRequest**](TRLinkCancelTrmRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkTrmInfoResponse**](TRLinkTrmInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Transaction cancellation request accepted |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_tr_link_integration**
> TRLinkCustomerIntegrationResponse connect_tr_link_integration(customer_integration_id, tr_link_connect_integration_request, idempotency_key=idempotency_key)

Connect customer integration

Connects a customer integration by providing API credentials. Stores encrypted credentials and enables the integration for use.

### Example


```python
from fireblocks.models.tr_link_connect_integration_request import TRLinkConnectIntegrationRequest
from fireblocks.models.tr_link_customer_integration_response import TRLinkCustomerIntegrationResponse
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
    customer_integration_id = '123e4567-e89b-12d3-a456-426614174000' # str | Customer integration unique identifier
    tr_link_connect_integration_request = fireblocks.TRLinkConnectIntegrationRequest() # TRLinkConnectIntegrationRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Connect customer integration
        api_response = fireblocks.tr_link.connect_tr_link_integration(customer_integration_id, tr_link_connect_integration_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->connect_tr_link_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->connect_tr_link_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **tr_link_connect_integration_request** | [**TRLinkConnectIntegrationRequest**](TRLinkConnectIntegrationRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkCustomerIntegrationResponse**](TRLinkCustomerIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer integration connected successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tr_link_customer**
> TRLinkCustomerResponse create_tr_link_customer(tr_link_create_customer_request, idempotency_key=idempotency_key)

Create customer

Creates a new customer (legal entity/VASP) for TRLink Travel Rule compliance operations. The customer represents your organization in the Travel Rule network and contains IVMS101-compliant identity information.

### Example


```python
from fireblocks.models.tr_link_create_customer_request import TRLinkCreateCustomerRequest
from fireblocks.models.tr_link_customer_response import TRLinkCustomerResponse
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
    tr_link_create_customer_request = fireblocks.TRLinkCreateCustomerRequest() # TRLinkCreateCustomerRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create customer
        api_response = fireblocks.tr_link.create_tr_link_customer(tr_link_create_customer_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->create_tr_link_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->create_tr_link_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_link_create_customer_request** | [**TRLinkCreateCustomerRequest**](TRLinkCreateCustomerRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkCustomerResponse**](TRLinkCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Customer created successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tr_link_integration**
> TRLinkCustomerIntegrationResponse create_tr_link_integration(tr_link_create_integration_request, idempotency_key=idempotency_key)

Create customer integration

Creates a new TRLink integration for a customer. This establishes a connection placeholder between a customer and a Travel Rule partner. Use the connect endpoint to provide credentials after creation.

### Example


```python
from fireblocks.models.tr_link_create_integration_request import TRLinkCreateIntegrationRequest
from fireblocks.models.tr_link_customer_integration_response import TRLinkCustomerIntegrationResponse
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
    tr_link_create_integration_request = fireblocks.TRLinkCreateIntegrationRequest() # TRLinkCreateIntegrationRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create customer integration
        api_response = fireblocks.tr_link.create_tr_link_integration(tr_link_create_integration_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->create_tr_link_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->create_tr_link_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tr_link_create_integration_request** | [**TRLinkCreateIntegrationRequest**](TRLinkCreateIntegrationRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkCustomerIntegrationResponse**](TRLinkCustomerIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Customer integration created successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tr_link_trm**
> TRLinkTrmInfoResponse create_tr_link_trm(customer_integration_id, tr_link_create_trm_request, idempotency_key=idempotency_key)

Create Travel Rule Message

Creates a new travel rule message with IVMS101-compliant PII data. Encrypts sensitive originator and beneficiary information before sending to partner.

### Example


```python
from fireblocks.models.tr_link_create_trm_request import TRLinkCreateTrmRequest
from fireblocks.models.tr_link_trm_info_response import TRLinkTrmInfoResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    tr_link_create_trm_request = fireblocks.TRLinkCreateTrmRequest() # TRLinkCreateTrmRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create Travel Rule Message
        api_response = fireblocks.tr_link.create_tr_link_trm(customer_integration_id, tr_link_create_trm_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->create_tr_link_trm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->create_tr_link_trm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **tr_link_create_trm_request** | [**TRLinkCreateTrmRequest**](TRLinkCreateTrmRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkTrmInfoResponse**](TRLinkTrmInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TRM created successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tr_link_customer**
> delete_tr_link_customer(customer_id)

Delete customer

Deletes a customer and all associated integrations. This action cannot be undone.

### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    customer_id = '550e8400-e29b-41d4-a716-446655440001' # str | Customer unique identifier

    try:
        # Delete customer
        fireblocks.tr_link.delete_tr_link_customer(customer_id).result()
    except Exception as e:
        print("Exception when calling TRLinkApi->delete_tr_link_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Customer deleted successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_tr_link_integration**
> disconnect_tr_link_integration(customer_integration_id)

Disconnect customer integration

Disconnects a customer integration by removing stored credentials. The integration record is deleted and cannot be recovered.

### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

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
    customer_integration_id = '123e4567-e89b-12d3-a456-426614174000' # str | Customer integration unique identifier

    try:
        # Disconnect customer integration
        fireblocks.tr_link.disconnect_tr_link_integration(customer_integration_id).result()
    except Exception as e:
        print("Exception when calling TRLinkApi->disconnect_tr_link_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Customer integration disconnected successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_customer_by_id**
> TRLinkCustomerResponse get_tr_link_customer_by_id(customer_id)

Get customer by ID

Retrieves detailed information about a specific customer by their unique identifier.

### Example


```python
from fireblocks.models.tr_link_customer_response import TRLinkCustomerResponse
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
    customer_id = '550e8400-e29b-41d4-a716-446655440001' # str | Customer unique identifier

    try:
        # Get customer by ID
        api_response = fireblocks.tr_link.get_tr_link_customer_by_id(customer_id).result()
        print("The response of TRLinkApi->get_tr_link_customer_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_customer_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer unique identifier | 

### Return type

[**TRLinkCustomerResponse**](TRLinkCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_customer_integration_by_id**
> TRLinkCustomerIntegrationResponse get_tr_link_customer_integration_by_id(customer_id, customer_integration_id)

Get customer integration by ID

Retrieves detailed information about a specific customer integration.

### Example


```python
from fireblocks.models.tr_link_customer_integration_response import TRLinkCustomerIntegrationResponse
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
    customer_id = '550e8400-e29b-41d4-a716-446655440001' # str | Customer unique identifier
    customer_integration_id = '123e4567-e89b-12d3-a456-426614174000' # str | Customer integration unique identifier

    try:
        # Get customer integration by ID
        api_response = fireblocks.tr_link.get_tr_link_customer_integration_by_id(customer_id, customer_integration_id).result()
        print("The response of TRLinkApi->get_tr_link_customer_integration_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_customer_integration_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer unique identifier | 
 **customer_integration_id** | **str**| Customer integration unique identifier | 

### Return type

[**TRLinkCustomerIntegrationResponse**](TRLinkCustomerIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer integration retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_customer_integrations**
> List[TRLinkCustomerIntegrationResponse] get_tr_link_customer_integrations(customer_id)

Get customer integrations

Retrieves all TRLink integrations for a specific customer. Returns a list of partner integrations configured for Travel Rule compliance.

### Example


```python
from fireblocks.models.tr_link_customer_integration_response import TRLinkCustomerIntegrationResponse
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
    customer_id = '550e8400-e29b-41d4-a716-446655440001' # str | Customer unique identifier

    try:
        # Get customer integrations
        api_response = fireblocks.tr_link.get_tr_link_customer_integrations(customer_id).result()
        print("The response of TRLinkApi->get_tr_link_customer_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_customer_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer unique identifier | 

### Return type

[**List[TRLinkCustomerIntegrationResponse]**](TRLinkCustomerIntegrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer integrations retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_customers**
> List[TRLinkCustomerResponse] get_tr_link_customers()

Get all customers

Retrieves all customers associated with the authenticated tenant. Returns a list of legal entities configured for Travel Rule compliance.

### Example


```python
from fireblocks.models.tr_link_customer_response import TRLinkCustomerResponse
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
        # Get all customers
        api_response = fireblocks.tr_link.get_tr_link_customers().result()
        print("The response of TRLinkApi->get_tr_link_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_customers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TRLinkCustomerResponse]**](TRLinkCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customers retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_integration_public_key**
> TRLinkPublicKeyResponse get_tr_link_integration_public_key(customer_integration_id)

Get public key for PII encryption

Retrieves the partner's public key in JWK format for encrypting PII data in Travel Rule Messages. Use this key to encrypt sensitive originator and beneficiary information before sending Travel Rule messages.

### Example


```python
from fireblocks.models.tr_link_public_key_response import TRLinkPublicKeyResponse
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
    customer_integration_id = '123e4567-e89b-12d3-a456-426614174000' # str | Customer integration unique identifier

    try:
        # Get public key for PII encryption
        api_response = fireblocks.tr_link.get_tr_link_integration_public_key(customer_integration_id).result()
        print("The response of TRLinkApi->get_tr_link_integration_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_integration_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 

### Return type

[**TRLinkPublicKeyResponse**](TRLinkPublicKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public key retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_partners**
> List[TRLinkPartnerResponse] get_tr_link_partners()

List available TRLink partners

Retrieves a list of all available Travel Rule Link integration partners. Partners provide Travel Rule compliance services such as VASP discovery, TRM exchange, and PII encryption.

### Example


```python
from fireblocks.models.tr_link_partner_response import TRLinkPartnerResponse
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
        # List available TRLink partners
        api_response = fireblocks.tr_link.get_tr_link_partners().result()
        print("The response of TRLinkApi->get_tr_link_partners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_partners: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TRLinkPartnerResponse]**](TRLinkPartnerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of partners retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_policy**
> TRLinkPolicyResponse get_tr_link_policy()

Get TRLink policy

Retrieves the complete TRLink policy for the authenticated tenant, including pre-screening rules, post-screening rules, and missing TRM rules. Pre-screening rules determine whether transactions should be screened. Post-screening rules determine actions based on screening results. Missing TRM rules handle cases when screening data is unavailable.

### Example


```python
from fireblocks.models.tr_link_policy_response import TRLinkPolicyResponse
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
        # Get TRLink policy
        api_response = fireblocks.tr_link.get_tr_link_policy().result()
        print("The response of TRLinkApi->get_tr_link_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_policy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TRLinkPolicyResponse**](TRLinkPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_supported_asset**
> TRLinkGetSupportedAssetResponse get_tr_link_supported_asset(customer_integration_id, asset_id)

Get supported asset by ID

Retrieves detailed information about a specific asset by its Fireblocks asset ID. Returns the transformed Fireblocks asset data, raw partner response, and support status.

### Example


```python
from fireblocks.models.tr_link_get_supported_asset_response import TRLinkGetSupportedAssetResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    asset_id = 'asset_id_example' # str | Fireblocks asset ID

    try:
        # Get supported asset by ID
        api_response = fireblocks.tr_link.get_tr_link_supported_asset(customer_integration_id, asset_id).result()
        print("The response of TRLinkApi->get_tr_link_supported_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_supported_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **asset_id** | **str**| Fireblocks asset ID | 

### Return type

[**TRLinkGetSupportedAssetResponse**](TRLinkGetSupportedAssetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_trm_by_id**
> TRLinkTrmInfoResponse get_tr_link_trm_by_id(customer_integration_id, trm_id)

Get TRM by ID

Retrieves a Travel Rule Message by its unique identifier from the partner provider. Returns full TRM details including status, IVMS101 data, and transaction information.

### Example


```python
from fireblocks.models.tr_link_trm_info_response import TRLinkTrmInfoResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    trm_id = 'trm_id_example' # str | Travel Rule Message unique identifier

    try:
        # Get TRM by ID
        api_response = fireblocks.tr_link.get_tr_link_trm_by_id(customer_integration_id, trm_id).result()
        print("The response of TRLinkApi->get_tr_link_trm_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_trm_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **trm_id** | **str**| Travel Rule Message unique identifier | 

### Return type

[**TRLinkTrmInfoResponse**](TRLinkTrmInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TRM retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tr_link_vasp_by_id**
> TRLinkVaspDto get_tr_link_vasp_by_id(customer_integration_id, vasp_id)

Get VASP by ID

Retrieves detailed information about a specific VASP by its unique identifier. Returns VASP details including public key if available.

### Example


```python
from fireblocks.models.tr_link_vasp_dto import TRLinkVaspDto
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    vasp_id = 'vasp_id_example' # str | VASP unique identifier (DID format)

    try:
        # Get VASP by ID
        api_response = fireblocks.tr_link.get_tr_link_vasp_by_id(customer_integration_id, vasp_id).result()
        print("The response of TRLinkApi->get_tr_link_vasp_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->get_tr_link_vasp_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **vasp_id** | **str**| VASP unique identifier (DID format) | 

### Return type

[**TRLinkVaspDto**](TRLinkVaspDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VASP retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tr_link_supported_assets**
> TRLinkAssetsListPagedResponse list_tr_link_supported_assets(customer_integration_id, page_size=page_size, page_cursor=page_cursor)

List supported assets

Retrieves a paginated list of assets supported by the partner integration. Includes a flag indicating whether the partner can handle assets not explicitly listed. Supports cursor-based pagination.

### Example


```python
from fireblocks.models.tr_link_assets_list_paged_response import TRLinkAssetsListPagedResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    page_size = 100 # int | Number of results per page (max 100) (optional) (default to 100)
    page_cursor = 'page_cursor_example' # str | Cursor for pagination (from previous response) (optional)

    try:
        # List supported assets
        api_response = fireblocks.tr_link.list_tr_link_supported_assets(customer_integration_id, page_size=page_size, page_cursor=page_cursor).result()
        print("The response of TRLinkApi->list_tr_link_supported_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->list_tr_link_supported_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **page_size** | **int**| Number of results per page (max 100) | [optional] [default to 100]
 **page_cursor** | **str**| Cursor for pagination (from previous response) | [optional] 

### Return type

[**TRLinkAssetsListPagedResponse**](TRLinkAssetsListPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported assets retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tr_link_vasps**
> TRLinkAPIPagedResponse list_tr_link_vasps(customer_integration_id, page_size=page_size, page_cursor=page_cursor)

List VASPs

Retrieves a paginated list of VASPs (Virtual Asset Service Providers) available through the partner integration. Supports cursor-based pagination.

### Example


```python
from fireblocks.models.tr_link_api_paged_response import TRLinkAPIPagedResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    page_size = 100 # int | Number of results per page (max 100) (optional) (default to 100)
    page_cursor = 'page_cursor_example' # str | Cursor for pagination (from previous response) (optional)

    try:
        # List VASPs
        api_response = fireblocks.tr_link.list_tr_link_vasps(customer_integration_id, page_size=page_size, page_cursor=page_cursor).result()
        print("The response of TRLinkApi->list_tr_link_vasps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->list_tr_link_vasps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **page_size** | **int**| Number of results per page (max 100) | [optional] [default to 100]
 **page_cursor** | **str**| Cursor for pagination (from previous response) | [optional] 

### Return type

[**TRLinkAPIPagedResponse**](TRLinkAPIPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VASPs retrieved successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_tr_link_trm**
> TRLinkTrmInfoResponse redirect_tr_link_trm(customer_integration_id, trm_id, tr_link_redirect_trm_request, idempotency_key=idempotency_key)

Redirect Travel Rule Message

Redirects a Travel Rule Message to a subsidiary VASP. This operation requires the partner to support nested VASPs functionality.

### Example


```python
from fireblocks.models.tr_link_redirect_trm_request import TRLinkRedirectTrmRequest
from fireblocks.models.tr_link_trm_info_response import TRLinkTrmInfoResponse
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
    customer_integration_id = 'customer_integration_id_example' # str | Customer integration unique identifier
    trm_id = 'trm_id_example' # str | Travel Rule Message unique identifier
    tr_link_redirect_trm_request = fireblocks.TRLinkRedirectTrmRequest() # TRLinkRedirectTrmRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Redirect Travel Rule Message
        api_response = fireblocks.tr_link.redirect_tr_link_trm(customer_integration_id, trm_id, tr_link_redirect_trm_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->redirect_tr_link_trm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->redirect_tr_link_trm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **trm_id** | **str**| Travel Rule Message unique identifier | 
 **tr_link_redirect_trm_request** | [**TRLinkRedirectTrmRequest**](TRLinkRedirectTrmRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkTrmInfoResponse**](TRLinkTrmInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Transaction redirect request accepted |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tr_link_destination_travel_rule_message_id**
> TRLinkSetDestinationTravelRuleMessageIdResponse set_tr_link_destination_travel_rule_message_id(tx_id, tr_link_set_destination_travel_rule_message_id_request, idempotency_key=idempotency_key)

Set destination travel rule message ID

Associates a Travel Rule Message ID with a specific destination in a multi-destination Fireblocks transaction. Matches destinations by amount and peer path.

### Example


```python
from fireblocks.models.tr_link_set_destination_travel_rule_message_id_request import TRLinkSetDestinationTravelRuleMessageIdRequest
from fireblocks.models.tr_link_set_destination_travel_rule_message_id_response import TRLinkSetDestinationTravelRuleMessageIdResponse
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
    tx_id = 'tx_id_example' # str | Fireblocks transaction unique identifier
    tr_link_set_destination_travel_rule_message_id_request = fireblocks.TRLinkSetDestinationTravelRuleMessageIdRequest() # TRLinkSetDestinationTravelRuleMessageIdRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set destination travel rule message ID
        api_response = fireblocks.tr_link.set_tr_link_destination_travel_rule_message_id(tx_id, tr_link_set_destination_travel_rule_message_id_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->set_tr_link_destination_travel_rule_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->set_tr_link_destination_travel_rule_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| Fireblocks transaction unique identifier | 
 **tr_link_set_destination_travel_rule_message_id_request** | [**TRLinkSetDestinationTravelRuleMessageIdRequest**](TRLinkSetDestinationTravelRuleMessageIdRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkSetDestinationTravelRuleMessageIdResponse**](TRLinkSetDestinationTravelRuleMessageIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Destination travel rule message ID set successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tr_link_transaction_travel_rule_message_id**
> TRLinkSetTransactionTravelRuleMessageIdResponse set_tr_link_transaction_travel_rule_message_id(tx_id, tr_link_set_transaction_travel_rule_message_id_request, idempotency_key=idempotency_key)

Set transaction travel rule message ID

Associates a Travel Rule Message ID with a Fireblocks transaction. This links the TRM compliance data to the blockchain transaction.

### Example


```python
from fireblocks.models.tr_link_set_transaction_travel_rule_message_id_request import TRLinkSetTransactionTravelRuleMessageIdRequest
from fireblocks.models.tr_link_set_transaction_travel_rule_message_id_response import TRLinkSetTransactionTravelRuleMessageIdResponse
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
    tx_id = 'tx_id_example' # str | Fireblocks transaction unique identifier
    tr_link_set_transaction_travel_rule_message_id_request = fireblocks.TRLinkSetTransactionTravelRuleMessageIdRequest() # TRLinkSetTransactionTravelRuleMessageIdRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set transaction travel rule message ID
        api_response = fireblocks.tr_link.set_tr_link_transaction_travel_rule_message_id(tx_id, tr_link_set_transaction_travel_rule_message_id_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->set_tr_link_transaction_travel_rule_message_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->set_tr_link_transaction_travel_rule_message_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| Fireblocks transaction unique identifier | 
 **tr_link_set_transaction_travel_rule_message_id_request** | [**TRLinkSetTransactionTravelRuleMessageIdRequest**](TRLinkSetTransactionTravelRuleMessageIdRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkSetTransactionTravelRuleMessageIdResponse**](TRLinkSetTransactionTravelRuleMessageIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Travel rule message ID set successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_tr_link_integration_connection**
> TRLinkTestConnectionResponse test_tr_link_integration_connection(customer_integration_id, idempotency_key=idempotency_key)

Test connection

Tests the connection to a customer integration by validating stored credentials and attempting communication with the Travel Rule partner. Returns connection status and any error messages.

### Example


```python
from fireblocks.models.tr_link_test_connection_response import TRLinkTestConnectionResponse
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
    customer_integration_id = '123e4567-e89b-12d3-a456-426614174000' # str | Customer integration unique identifier
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Test connection
        api_response = fireblocks.tr_link.test_tr_link_integration_connection(customer_integration_id, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->test_tr_link_integration_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->test_tr_link_integration_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_integration_id** | **str**| Customer integration unique identifier | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkTestConnectionResponse**](TRLinkTestConnectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection test completed (success or failure details in response body) |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tr_link_customer**
> TRLinkCustomerResponse update_tr_link_customer(customer_id, tr_link_update_customer_request, idempotency_key=idempotency_key)

Update customer

Updates an existing customer's information. All fields are optional - only provided fields will be updated.

### Example


```python
from fireblocks.models.tr_link_customer_response import TRLinkCustomerResponse
from fireblocks.models.tr_link_update_customer_request import TRLinkUpdateCustomerRequest
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
    customer_id = '550e8400-e29b-41d4-a716-446655440001' # str | Customer unique identifier
    tr_link_update_customer_request = fireblocks.TRLinkUpdateCustomerRequest() # TRLinkUpdateCustomerRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update customer
        api_response = fireblocks.tr_link.update_tr_link_customer(customer_id, tr_link_update_customer_request, idempotency_key=idempotency_key).result()
        print("The response of TRLinkApi->update_tr_link_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TRLinkApi->update_tr_link_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Customer unique identifier | 
 **tr_link_update_customer_request** | [**TRLinkUpdateCustomerRequest**](TRLinkUpdateCustomerRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TRLinkCustomerResponse**](TRLinkCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer updated successfully |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

