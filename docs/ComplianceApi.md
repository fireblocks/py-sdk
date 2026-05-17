# fireblocks.ComplianceApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_ars_config**](ComplianceApi.md#activate_ars_config) | **POST** /screening/ars/config/activate | Activate ARS (Address Registry Screening)
[**activate_byork_config**](ComplianceApi.md#activate_byork_config) | **POST** /screening/byork/config/activate | Activate BYORK Light
[**add_address_registry_vault_opt_outs**](ComplianceApi.md#add_address_registry_vault_opt_outs) | **POST** /address_registry/vaults | Add vault accounts to the address registry opt-out list
[**assign_vaults_to_legal_entity**](ComplianceApi.md#assign_vaults_to_legal_entity) | **POST** /legal_entities/{legalEntityId}/vaults | Assign vault accounts to a legal entity
[**create_counterparty_group**](ComplianceApi.md#create_counterparty_group) | **POST** /counterparty_groups | Create a counterparty group
[**deactivate_ars_config**](ComplianceApi.md#deactivate_ars_config) | **POST** /screening/ars/config/deactivate | Deactivate ARS (Address Registry Screening)
[**deactivate_byork_config**](ComplianceApi.md#deactivate_byork_config) | **POST** /screening/byork/config/deactivate | Deactivate BYORK Light
[**delete_counterparty_group**](ComplianceApi.md#delete_counterparty_group) | **DELETE** /counterparty_groups/{groupId} | Delete a counterparty group
[**get_address_registry_tenant_participation_status**](ComplianceApi.md#get_address_registry_tenant_participation_status) | **GET** /address_registry/tenant | Get address registry participation status for the authenticated workspace
[**get_address_registry_vault_opt_out**](ComplianceApi.md#get_address_registry_vault_opt_out) | **GET** /address_registry/vaults/{vaultAccountId} | Get whether a vault account is opted out of the address registry
[**get_aml_post_screening_policy**](ComplianceApi.md#get_aml_post_screening_policy) | **GET** /screening/aml/post_screening_policy | AML - View Post-Screening Policy
[**get_aml_screening_policy**](ComplianceApi.md#get_aml_screening_policy) | **GET** /screening/aml/screening_policy | AML - View Screening Policy
[**get_byork_config**](ComplianceApi.md#get_byork_config) | **GET** /screening/byork/config | Get BYORK Light configuration
[**get_byork_verdict**](ComplianceApi.md#get_byork_verdict) | **GET** /screening/byork/verdict | Get BYORK Light verdict
[**get_counterparty_group**](ComplianceApi.md#get_counterparty_group) | **GET** /counterparty_groups/{groupId} | Get a counterparty group
[**get_legal_entity**](ComplianceApi.md#get_legal_entity) | **GET** /legal_entities/{legalEntityId} | Get a legal entity
[**get_legal_entity_for_address**](ComplianceApi.md#get_legal_entity_for_address) | **GET** /address_registry/legal_entities/{address} | Look up legal entity by blockchain address
[**get_post_screening_policy**](ComplianceApi.md#get_post_screening_policy) | **GET** /screening/travel_rule/post_screening_policy | Travel Rule - View Post-Screening Policy
[**get_screening_full_details**](ComplianceApi.md#get_screening_full_details) | **GET** /screening/transaction/{txId} | Provides all the compliance details for the given screened transaction.
[**get_screening_policy**](ComplianceApi.md#get_screening_policy) | **GET** /screening/travel_rule/screening_policy | Travel Rule - View Screening Policy
[**list_address_registry_vault_opt_outs**](ComplianceApi.md#list_address_registry_vault_opt_outs) | **GET** /address_registry/vaults | List vault-level address registry opt-outs (paginated)
[**list_counterparty_groups**](ComplianceApi.md#list_counterparty_groups) | **GET** /counterparty_groups | List counterparty groups
[**list_legal_entities**](ComplianceApi.md#list_legal_entities) | **GET** /legal_entities | List legal entities (Paginated)
[**list_vaults_for_legal_entity**](ComplianceApi.md#list_vaults_for_legal_entity) | **GET** /legal_entities/{legalEntityId}/vaults | List vault accounts for a legal entity (Paginated)
[**opt_in_address_registry_tenant**](ComplianceApi.md#opt_in_address_registry_tenant) | **POST** /address_registry/tenant | Opt the workspace in to the address registry
[**opt_out_address_registry_tenant**](ComplianceApi.md#opt_out_address_registry_tenant) | **DELETE** /address_registry/tenant | Opt the workspace out of the address registry
[**register_legal_entity**](ComplianceApi.md#register_legal_entity) | **POST** /legal_entities | Register a new legal entity
[**remove_address_registry_vault_opt_out**](ComplianceApi.md#remove_address_registry_vault_opt_out) | **DELETE** /address_registry/vaults/{vaultAccountId} | Remove a single vault account from the address registry opt-out list
[**remove_all_address_registry_vault_opt_outs**](ComplianceApi.md#remove_all_address_registry_vault_opt_outs) | **DELETE** /address_registry/vaults | Remove all vault-level address registry opt-outs for the workspace
[**retry_rejected_transaction_bypass_screening_checks**](ComplianceApi.md#retry_rejected_transaction_bypass_screening_checks) | **POST** /screening/transaction/{txId}/bypass_screening_policy | Bypass Screening Policy
[**set_aml_verdict**](ComplianceApi.md#set_aml_verdict) | **POST** /screening/aml/verdict/manual | Set AML Verdict (BYORK Super Light)
[**set_byork_timeouts**](ComplianceApi.md#set_byork_timeouts) | **PUT** /screening/byork/config/timeouts | Set BYORK Light timeouts
[**set_byork_verdict**](ComplianceApi.md#set_byork_verdict) | **POST** /screening/byork/verdict | Set BYORK Light verdict
[**update_aml_screening_configuration**](ComplianceApi.md#update_aml_screening_configuration) | **PUT** /screening/aml/policy_configuration | Update AML Configuration
[**update_counterparty_group**](ComplianceApi.md#update_counterparty_group) | **PATCH** /counterparty_groups/{groupId} | Update a counterparty group
[**update_legal_entity**](ComplianceApi.md#update_legal_entity) | **PUT** /legal_entities/{legalEntityId} | Update legal entity
[**update_screening_configuration**](ComplianceApi.md#update_screening_configuration) | **PUT** /screening/configurations | Tenant - Screening Configuration
[**update_travel_rule_config**](ComplianceApi.md#update_travel_rule_config) | **PUT** /screening/travel_rule/policy_configuration | Update Travel Rule Configuration


# **activate_ars_config**
> ArsConfigResponse activate_ars_config(idempotency_key=idempotency_key)

Activate ARS (Address Registry Screening)

Activates ARS (Address Registry Screening) for the authenticated tenant (sets config.active to true). Once activated, ARS screening applies to matching transactions.

### Example


```python
from fireblocks.models.ars_config_response import ArsConfigResponse
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
        # Activate ARS (Address Registry Screening)
        api_response = fireblocks.compliance.activate_ars_config(idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->activate_ars_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->activate_ars_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ArsConfigResponse**](ArsConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ARS configuration activated. |  * X-Request-ID -  <br>  |
**400** | Tenant not opted-in for address registry. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_byork_config**
> ByorkConfigResponse activate_byork_config(idempotency_key=idempotency_key)

Activate BYORK Light

Activates BYORK Light for the authenticated tenant (sets config.active to true). Once activated, BYORK screening applies to matching transactions. Requires BYORK Light to be enabled for the tenant (contact your CSM to enable).

### Example


```python
from fireblocks.models.byork_config_response import ByorkConfigResponse
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
        # Activate BYORK Light
        api_response = fireblocks.compliance.activate_byork_config(idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->activate_byork_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->activate_byork_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ByorkConfigResponse**](ByorkConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BYORK configuration activated. |  * X-Request-ID -  <br>  |
**400** | BYORK Light not enabled for tenant. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_address_registry_vault_opt_outs**
> AddressRegistryAddVaultOptOutsResponse add_address_registry_vault_opt_outs(address_registry_add_vault_opt_outs_request, idempotency_key=idempotency_key)

Add vault accounts to the address registry opt-out list

Adds one or more vault account ids to the workspace opt-out list for the address registry.

### Example


```python
from fireblocks.models.address_registry_add_vault_opt_outs_request import AddressRegistryAddVaultOptOutsRequest
from fireblocks.models.address_registry_add_vault_opt_outs_response import AddressRegistryAddVaultOptOutsResponse
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
    address_registry_add_vault_opt_outs_request = fireblocks.AddressRegistryAddVaultOptOutsRequest() # AddressRegistryAddVaultOptOutsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add vault accounts to the address registry opt-out list
        api_response = fireblocks.compliance.add_address_registry_vault_opt_outs(address_registry_add_vault_opt_outs_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->add_address_registry_vault_opt_outs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->add_address_registry_vault_opt_outs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_registry_add_vault_opt_outs_request** | [**AddressRegistryAddVaultOptOutsRequest**](AddressRegistryAddVaultOptOutsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AddressRegistryAddVaultOptOutsResponse**](AddressRegistryAddVaultOptOutsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Opt-outs recorded; response body includes &#x60;acceptedCount&#x60;. |  * X-Request-ID -  <br>  |
**400** | Validation error (e.g. empty list or invalid vault ids) |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_vaults_to_legal_entity**
> AssignVaultsToLegalEntityResponse assign_vaults_to_legal_entity(legal_entity_id, assign_vaults_to_legal_entity_request, idempotency_key=idempotency_key)

Assign vault accounts to a legal entity

Assigns one or more vault accounts to a specific legal entity registration. Explicitly mapped vault accounts take precedence over the workspace default legal entity.
Endpoint Permission: Admin, Non-Signing Admin.

### Example


```python
from fireblocks.models.assign_vaults_to_legal_entity_request import AssignVaultsToLegalEntityRequest
from fireblocks.models.assign_vaults_to_legal_entity_response import AssignVaultsToLegalEntityResponse
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
    legal_entity_id = 'legal_entity_id_example' # str | The unique ID of the legal entity registration
    assign_vaults_to_legal_entity_request = fireblocks.AssignVaultsToLegalEntityRequest() # AssignVaultsToLegalEntityRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Assign vault accounts to a legal entity
        api_response = fireblocks.compliance.assign_vaults_to_legal_entity(legal_entity_id, assign_vaults_to_legal_entity_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->assign_vaults_to_legal_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->assign_vaults_to_legal_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legal_entity_id** | **str**| The unique ID of the legal entity registration | 
 **assign_vaults_to_legal_entity_request** | [**AssignVaultsToLegalEntityRequest**](AssignVaultsToLegalEntityRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AssignVaultsToLegalEntityResponse**](AssignVaultsToLegalEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Vault accounts assigned successfully |  * X-Request-ID -  <br>  |
**404** | Legal entity registration not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_counterparty_group**
> CounterpartyGroup create_counterparty_group(create_counterparty_group_request, idempotency_key=idempotency_key)

Create a counterparty group

Creates a new counterparty group.

**Endpoint Permissions:** Admin, Non-Signing Admin.


### Example


```python
from fireblocks.models.counterparty_group import CounterpartyGroup
from fireblocks.models.create_counterparty_group_request import CreateCounterpartyGroupRequest
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
    create_counterparty_group_request = fireblocks.CreateCounterpartyGroupRequest() # CreateCounterpartyGroupRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a counterparty group
        api_response = fireblocks.compliance.create_counterparty_group(create_counterparty_group_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->create_counterparty_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->create_counterparty_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_counterparty_group_request** | [**CreateCounterpartyGroupRequest**](CreateCounterpartyGroupRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CounterpartyGroup**](CounterpartyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Counterparty group created successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_ars_config**
> ArsConfigResponse deactivate_ars_config(idempotency_key=idempotency_key)

Deactivate ARS (Address Registry Screening)

Deactivates ARS (Address Registry Screening) for the authenticated tenant (sets config.active to false). Once deactivated, ARS screening no longer applies until activated again.

### Example


```python
from fireblocks.models.ars_config_response import ArsConfigResponse
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
        # Deactivate ARS (Address Registry Screening)
        api_response = fireblocks.compliance.deactivate_ars_config(idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->deactivate_ars_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->deactivate_ars_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ArsConfigResponse**](ArsConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ARS configuration deactivated. |  * X-Request-ID -  <br>  |
**400** | Tenant not opted-in for address registry. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_byork_config**
> ByorkConfigResponse deactivate_byork_config(idempotency_key=idempotency_key)

Deactivate BYORK Light

Deactivates BYORK Light for the authenticated tenant (sets config.active to false). Once deactivated, BYORK screening no longer applies until activated again. Requires BYORK Light to be enabled for the tenant (contact your CSM to enable).

### Example


```python
from fireblocks.models.byork_config_response import ByorkConfigResponse
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
        # Deactivate BYORK Light
        api_response = fireblocks.compliance.deactivate_byork_config(idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->deactivate_byork_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->deactivate_byork_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ByorkConfigResponse**](ByorkConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BYORK configuration deactivated. |  * X-Request-ID -  <br>  |
**400** | BYORK Light not enabled for tenant. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_counterparty_group**
> delete_counterparty_group(group_id)

Delete a counterparty group

Permanently deletes a counterparty group.

**Endpoint Permissions:** Admin, Non-Signing Admin.


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
    group_id = 'group_id_example' # str | The unique identifier of the counterparty group

    try:
        # Delete a counterparty group
        fireblocks.compliance.delete_counterparty_group(group_id).result()
    except Exception as e:
        print("Exception when calling ComplianceApi->delete_counterparty_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the counterparty group | 

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
**204** | Counterparty group deleted successfully |  * X-Request-ID -  <br>  |
**404** | Counterparty group not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_registry_tenant_participation_status**
> AddressRegistryTenantRegistryResponse get_address_registry_tenant_participation_status()

Get address registry participation status for the authenticated workspace

Returns whether the workspace is `OPTED_IN` or `OPTED_OUT` of the address registry.

### Example


```python
from fireblocks.models.address_registry_tenant_registry_response import AddressRegistryTenantRegistryResponse
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
        # Get address registry participation status for the authenticated workspace
        api_response = fireblocks.compliance.get_address_registry_tenant_participation_status().result()
        print("The response of ComplianceApi->get_address_registry_tenant_participation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_address_registry_tenant_participation_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AddressRegistryTenantRegistryResponse**](AddressRegistryTenantRegistryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Participation status in the response body |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_registry_vault_opt_out**
> AddressRegistryGetVaultOptOutResponse get_address_registry_vault_opt_out(vault_account_id)

Get whether a vault account is opted out of the address registry

Returns whether this vault account is on the workspace opt-out list (`optedOut` true or false). List, add, and clear-all are available on `/v1/address_registry/vaults`; this path reads or removes one vault.

### Example


```python
from fireblocks.models.address_registry_get_vault_opt_out_response import AddressRegistryGetVaultOptOutResponse
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
    vault_account_id = 10001 # int | Vault account id (non-negative integer).

    try:
        # Get whether a vault account is opted out of the address registry
        api_response = fireblocks.compliance.get_address_registry_vault_opt_out(vault_account_id).result()
        print("The response of ComplianceApi->get_address_registry_vault_opt_out:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_address_registry_vault_opt_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **int**| Vault account id (non-negative integer). | 

### Return type

[**AddressRegistryGetVaultOptOutResponse**](AddressRegistryGetVaultOptOutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current opt-out flag for the vault |  * X-Request-ID -  <br>  |
**400** | Invalid path parameter (e.g. negative or out-of-range vault account id) |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_byork_config**
> ByorkConfigResponse get_byork_config()

Get BYORK Light configuration

Retrieves BYORK Light configuration for the authenticated tenant (timeouts, active flag, allowed timeout ranges). Returns default config when none exists. Requires BYORK Light to be enabled for the tenant.

### Example


```python
from fireblocks.models.byork_config_response import ByorkConfigResponse
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
        # Get BYORK Light configuration
        api_response = fireblocks.compliance.get_byork_config().result()
        print("The response of ComplianceApi->get_byork_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_byork_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ByorkConfigResponse**](ByorkConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BYORK configuration (or default). |  * X-Request-ID -  <br>  |
**400** | BYORK Light not enabled for tenant. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_byork_verdict**
> GetByorkVerdictResponse get_byork_verdict(tx_id)

Get BYORK Light verdict

Returns the current BYORK verdict and status for a transaction. Status can be PRE_ACCEPTED, PENDING, RECEIVED (verdict is final but processing not yet complete), or COMPLETED. Requires BYORK Light to be enabled for the tenant. Returns 404 if no BYORK verdict is found for the transaction.

### Example


```python
from fireblocks.models.get_byork_verdict_response import GetByorkVerdictResponse
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
    tx_id = '550e8400-e29b-41d4-a716-446655440000' # str | Transaction ID

    try:
        # Get BYORK Light verdict
        api_response = fireblocks.compliance.get_byork_verdict(tx_id).result()
        print("The response of ComplianceApi->get_byork_verdict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_byork_verdict: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| Transaction ID | 

### Return type

[**GetByorkVerdictResponse**](GetByorkVerdictResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current verdict and status. |  * X-Request-ID -  <br>  |
**400** | BYORK Light not enabled for tenant or txId missing. |  * X-Request-ID -  <br>  |
**404** | No BYORK verdict found for this transaction. |  * X-Request-ID -  <br>  |
**500** | Internal server error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counterparty_group**
> CounterpartyGroup get_counterparty_group(group_id)

Get a counterparty group

Returns the details of a specific counterparty group.

**Endpoint Permissions:** Admin, Non-Signing Admin, Viewer.


### Example


```python
from fireblocks.models.counterparty_group import CounterpartyGroup
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
    group_id = 'group_id_example' # str | The unique identifier of the counterparty group

    try:
        # Get a counterparty group
        api_response = fireblocks.compliance.get_counterparty_group(group_id).result()
        print("The response of ComplianceApi->get_counterparty_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_counterparty_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the counterparty group | 

### Return type

[**CounterpartyGroup**](CounterpartyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A counterparty group object |  * X-Request-ID -  <br>  |
**404** | Counterparty group not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_entity**
> LegalEntityRegistration get_legal_entity(legal_entity_id)

Get a legal entity

Returns details of a specific legal entity registration, including GLEIF data when available.
Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.legal_entity_registration import LegalEntityRegistration
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
    legal_entity_id = 'legal_entity_id_example' # str | The unique ID of the legal entity registration

    try:
        # Get a legal entity
        api_response = fireblocks.compliance.get_legal_entity(legal_entity_id).result()
        print("The response of ComplianceApi->get_legal_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_legal_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legal_entity_id** | **str**| The unique ID of the legal entity registration | 

### Return type

[**LegalEntityRegistration**](LegalEntityRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Legal entity registration details |  * X-Request-ID -  <br>  |
**404** | Legal entity registration not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_entity_for_address**
> AddressRegistryLegalEntity get_legal_entity_for_address(address)

Look up legal entity by blockchain address

Returns legal entity information for the given blockchain address (verification status, LEI, Travel Rule providers, contact email, and related fields — see response schema). URL-encode `{address}` when required.

### Example


```python
from fireblocks.models.address_registry_legal_entity import AddressRegistryLegalEntity
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
    address = '0x742d35cc6634c0532925a3b844bc9e7595f0beb0' # str | Blockchain address to look up

    try:
        # Look up legal entity by blockchain address
        api_response = fireblocks.compliance.get_legal_entity_for_address(address).result()
        print("The response of ComplianceApi->get_legal_entity_for_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_legal_entity_for_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Blockchain address to look up | 

### Return type

[**AddressRegistryLegalEntity**](AddressRegistryLegalEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Legal entity found |  * X-Request-ID -  <br>  |
**400** | Bad request — either request validation (path &#x60;{address}&#x60; empty or whitespace-only after trim, e.g. encoded spaces only; numeric code 4100), or the authenticated workspace is not opted in to the address registry (numeric code 2140). The &#x60;message&#x60; field describes the failure; use &#x60;code&#x60; to distinguish. |  * X-Request-ID -  <br>  |
**404** | Not found (error code 2142) — unresolved address, no legal entity for a resolved address, or the same not-found outcome in other cases. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

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

# **get_screening_full_details**
> ComplianceResultFullPayload get_screening_full_details(tx_id)

Provides all the compliance details for the given screened transaction.

Provides all the compliance details for the given screened transaction.

### Example


```python
from fireblocks.models.compliance_result_full_payload import ComplianceResultFullPayload
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
    tx_id = '550e8400-e29b-41d4-a716-446655440000' # str | Fireblocks transaction ID of the screened transaction

    try:
        # Provides all the compliance details for the given screened transaction.
        api_response = fireblocks.compliance.get_screening_full_details(tx_id).result()
        print("The response of ComplianceApi->get_screening_full_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_screening_full_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| Fireblocks transaction ID of the screened transaction | 

### Return type

[**ComplianceResultFullPayload**](ComplianceResultFullPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A compliance object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

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

# **list_address_registry_vault_opt_outs**
> AddressRegistryListVaultOptOutsResponse list_address_registry_vault_opt_outs(page_cursor=page_cursor, page_size=page_size, order=order)

List vault-level address registry opt-outs (paginated)

Lists vault accounts that are opted out of the address registry for this workspace. Pagination uses `next` and `prev` cursors from the response. If `pageSize` is omitted, **50** items are returned per page; allowed range is **1–100** per request.

### Example


```python
from fireblocks.models.address_registry_list_vault_opt_outs_response import AddressRegistryListVaultOptOutsResponse
from fireblocks.models.address_registry_vault_list_order import AddressRegistryVaultListOrder
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
    page_cursor = 'eyJvZmZzZXQiOjAsInBhZ2VTaXplIjoxMH0' # str | Opaque cursor from a previous response (`next` or `prev`). Omit for the first page. (optional)
    page_size = 50 # int | Page size. Default **50** if omitted; must be between **1** and **100**. (optional) (default to 50)
    order = VAULT_OPT_OUT_LIST_ORDER_ASC # AddressRegistryVaultListOrder | Sort direction by vault account id. Omit for ascending; use the enum value for descending. (optional) (default to VAULT_OPT_OUT_LIST_ORDER_ASC)

    try:
        # List vault-level address registry opt-outs (paginated)
        api_response = fireblocks.compliance.list_address_registry_vault_opt_outs(page_cursor=page_cursor, page_size=page_size, order=order).result()
        print("The response of ComplianceApi->list_address_registry_vault_opt_outs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_address_registry_vault_opt_outs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Opaque cursor from a previous response (&#x60;next&#x60; or &#x60;prev&#x60;). Omit for the first page. | [optional] 
 **page_size** | **int**| Page size. Default **50** if omitted; must be between **1** and **100**. | [optional] [default to 50]
 **order** | [**AddressRegistryVaultListOrder**](.md)| Sort direction by vault account id. Omit for ascending; use the enum value for descending. | [optional] [default to VAULT_OPT_OUT_LIST_ORDER_ASC]

### Return type

[**AddressRegistryListVaultOptOutsResponse**](AddressRegistryListVaultOptOutsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page of vault opt-out rows |  * X-Request-ID -  <br>  |
**400** | Validation error (e.g. invalid or malformed pageCursor) |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_counterparty_groups**
> CounterpartyGroupsPaginatedResponse list_counterparty_groups(page_cursor=page_cursor, page_size=page_size)

List counterparty groups

Returns a paginated list of counterparty groups.

**Endpoint Permissions:** Admin, Non-Signing Admin, Viewer.


### Example


```python
from fireblocks.models.counterparty_groups_paginated_response import CounterpartyGroupsPaginatedResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 50 # int | Maximum number of items in the page (optional) (default to 50)

    try:
        # List counterparty groups
        api_response = fireblocks.compliance.list_counterparty_groups(page_cursor=page_cursor, page_size=page_size).result()
        print("The response of ComplianceApi->list_counterparty_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_counterparty_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **int**| Maximum number of items in the page | [optional] [default to 50]

### Return type

[**CounterpartyGroupsPaginatedResponse**](CounterpartyGroupsPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of counterparty groups |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_legal_entities**
> ListLegalEntitiesResponse list_legal_entities(vault_account_id=vault_account_id, page_cursor=page_cursor, page_size=page_size)

List legal entities (Paginated)

Returns legal entity registrations for the workspace with cursor-based pagination.
If query parameter vaultAccountId is used it returns the legal entity registration associated with a specific vault account. If no explicit mapping exists for the vault, the workspace default legal entity is returned. Returns an empty response if neither a vault mapping nor a default legal entity is configured.
Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.list_legal_entities_response import ListLegalEntitiesResponse
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account. When provided, returns the legal entity associated with that vault account and pagination parameters are ignored. (optional)
    page_cursor = 'page_cursor_example' # str | Cursor string returned in `next` or `prev` of a previous response. Ignored when `vaultAccountId` is provided. (optional)
    page_size = 50 # int | Maximum number of registrations to return. Ignored when `vaultAccountId` is provided. (optional) (default to 50)

    try:
        # List legal entities (Paginated)
        api_response = fireblocks.compliance.list_legal_entities(vault_account_id=vault_account_id, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of ComplianceApi->list_legal_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_legal_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account. When provided, returns the legal entity associated with that vault account and pagination parameters are ignored. | [optional] 
 **page_cursor** | **str**| Cursor string returned in &#x60;next&#x60; or &#x60;prev&#x60; of a previous response. Ignored when &#x60;vaultAccountId&#x60; is provided. | [optional] 
 **page_size** | **int**| Maximum number of registrations to return. Ignored when &#x60;vaultAccountId&#x60; is provided. | [optional] [default to 50]

### Return type

[**ListLegalEntitiesResponse**](ListLegalEntitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of legal entity registrations. When &#x60;vaultAccountId&#x60; is provided, &#x60;data&#x60; contains at most one item. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vaults_for_legal_entity**
> ListVaultsForRegistrationResponse list_vaults_for_legal_entity(legal_entity_id, page_cursor=page_cursor, page_size=page_size)

List vault accounts for a legal entity (Paginated)

Returns vault account IDs explicitly assigned to a specific legal entity registration, with cursor-based pagination.
Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

### Example


```python
from fireblocks.models.list_vaults_for_registration_response import ListVaultsForRegistrationResponse
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
    legal_entity_id = 'legal_entity_id_example' # str | The unique ID of the legal entity registration
    page_cursor = 'page_cursor_example' # str | Cursor string returned in `next` or `prev` of a previous response (optional)
    page_size = 50 # int | Maximum number of registrations to return (optional) (default to 50)

    try:
        # List vault accounts for a legal entity (Paginated)
        api_response = fireblocks.compliance.list_vaults_for_legal_entity(legal_entity_id, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of ComplianceApi->list_vaults_for_legal_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->list_vaults_for_legal_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legal_entity_id** | **str**| The unique ID of the legal entity registration | 
 **page_cursor** | **str**| Cursor string returned in &#x60;next&#x60; or &#x60;prev&#x60; of a previous response | [optional] 
 **page_size** | **int**| Maximum number of registrations to return | [optional] [default to 50]

### Return type

[**ListVaultsForRegistrationResponse**](ListVaultsForRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of vault account IDs assigned to the legal entity |  * X-Request-ID -  <br>  |
**404** | Legal entity registration not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opt_in_address_registry_tenant**
> AddressRegistryTenantRegistryResponse opt_in_address_registry_tenant(idempotency_key=idempotency_key)

Opt the workspace in to the address registry

Opts the workspace in. No request body. Response uses the same JSON shape as GET; status is OPTED_IN.

### Example


```python
from fireblocks.models.address_registry_tenant_registry_response import AddressRegistryTenantRegistryResponse
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
        # Opt the workspace in to the address registry
        api_response = fireblocks.compliance.opt_in_address_registry_tenant(idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->opt_in_address_registry_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->opt_in_address_registry_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AddressRegistryTenantRegistryResponse**](AddressRegistryTenantRegistryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success; response body includes status OPTED_IN |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opt_out_address_registry_tenant**
> AddressRegistryTenantRegistryResponse opt_out_address_registry_tenant()

Opt the workspace out of the address registry

Opts the workspace out. No request body. Response uses the same JSON shape as GET; status is OPTED_OUT.

### Example


```python
from fireblocks.models.address_registry_tenant_registry_response import AddressRegistryTenantRegistryResponse
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
        # Opt the workspace out of the address registry
        api_response = fireblocks.compliance.opt_out_address_registry_tenant().result()
        print("The response of ComplianceApi->opt_out_address_registry_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->opt_out_address_registry_tenant: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AddressRegistryTenantRegistryResponse**](AddressRegistryTenantRegistryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success; response body includes status OPTED_OUT |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_legal_entity**
> LegalEntityRegistration register_legal_entity(register_legal_entity_request, idempotency_key=idempotency_key)

Register a new legal entity

Registers a new legal entity for the workspace using its LEI (Legal Entity Identifier) code. The LEI is validated against the GLEIF registry. Each workspace can register multiple legal entities.
Endpoint Permission: Admin, Non-Signing Admin.

### Example


```python
from fireblocks.models.legal_entity_registration import LegalEntityRegistration
from fireblocks.models.register_legal_entity_request import RegisterLegalEntityRequest
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
    register_legal_entity_request = fireblocks.RegisterLegalEntityRequest() # RegisterLegalEntityRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Register a new legal entity
        api_response = fireblocks.compliance.register_legal_entity(register_legal_entity_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->register_legal_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->register_legal_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_legal_entity_request** | [**RegisterLegalEntityRequest**](RegisterLegalEntityRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**LegalEntityRegistration**](LegalEntityRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Legal entity registered successfully |  * X-Request-ID -  <br>  |
**400** | Invalid LEI or request parameters |  * X-Request-ID -  <br>  |
**404** | LEI not found in the GLEIF registry |  * X-Request-ID -  <br>  |
**409** | A legal entity with this LEI is already registered for the workspace |  * X-Request-ID -  <br>  |
**500** | Internal Server Error |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_address_registry_vault_opt_out**
> AddressRegistryRemoveVaultOptOutResponse remove_address_registry_vault_opt_out(vault_account_id)

Remove a single vault account from the address registry opt-out list

Removes this vault account id from the workspace opt-out list if it is present; otherwise the call still succeeds. Response body matches GET (`optedOut` is `false` after success). To clear the whole list, use `DELETE /v1/address_registry/vaults`.

### Example


```python
from fireblocks.models.address_registry_remove_vault_opt_out_response import AddressRegistryRemoveVaultOptOutResponse
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
    vault_account_id = 10001 # int | Vault account id (non-negative integer).

    try:
        # Remove a single vault account from the address registry opt-out list
        api_response = fireblocks.compliance.remove_address_registry_vault_opt_out(vault_account_id).result()
        print("The response of ComplianceApi->remove_address_registry_vault_opt_out:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->remove_address_registry_vault_opt_out: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **int**| Vault account id (non-negative integer). | 

### Return type

[**AddressRegistryRemoveVaultOptOutResponse**](AddressRegistryRemoveVaultOptOutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success; &#x60;optedOut&#x60; is false (list entry removed if it existed) |  * X-Request-ID -  <br>  |
**400** | Invalid path parameter (e.g. negative or out-of-range vault account id) |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_address_registry_vault_opt_outs**
> AddressRegistryRemoveAllVaultOptOutsResponse remove_all_address_registry_vault_opt_outs()

Remove all vault-level address registry opt-outs for the workspace

Removes all vault accounts from the workspace opt-out list.

### Example


```python
from fireblocks.models.address_registry_remove_all_vault_opt_outs_response import AddressRegistryRemoveAllVaultOptOutsResponse
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
        # Remove all vault-level address registry opt-outs for the workspace
        api_response = fireblocks.compliance.remove_all_address_registry_vault_opt_outs().result()
        print("The response of ComplianceApi->remove_all_address_registry_vault_opt_outs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->remove_all_address_registry_vault_opt_outs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AddressRegistryRemoveAllVaultOptOutsResponse**](AddressRegistryRemoveAllVaultOptOutsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All opt-outs cleared; response body includes &#x60;removedCount&#x60;. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_rejected_transaction_bypass_screening_checks**
> CreateTransactionResponse retry_rejected_transaction_bypass_screening_checks(tx_id, idempotency_key=idempotency_key)

Bypass Screening Policy

Triggers a new transaction, with the API user as the initiator, bypassing the screening policy checks. This endpoint is restricted to Admin API users and is only applicable to outgoing transactions.

### Example


```python
from fireblocks.models.create_transaction_response import CreateTransactionResponse
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
    tx_id = '550e8400-e29b-41d4-a716-446655440000' # str | The transaction id that was rejected by screening checks
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Bypass Screening Policy
        api_response = fireblocks.compliance.retry_rejected_transaction_bypass_screening_checks(tx_id, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->retry_rejected_transaction_bypass_screening_checks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->retry_rejected_transaction_bypass_screening_checks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The transaction id that was rejected by screening checks | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A transaction object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_aml_verdict**
> AmlVerdictManualResponse set_aml_verdict(aml_verdict_manual_request, idempotency_key=idempotency_key)

Set AML Verdict (BYORK Super Light)

Set AML verdict for incoming transactions when **BYORK Super Light** (Manual Screening Verdict) is enabled. This endpoint is for Super Light only. For **BYORK Light**, use POST /screening/byork/verdict instead. When Super Light is retired, this endpoint will be deprecated; use the BYORK Light verdict API for new integrations.

### Example


```python
from fireblocks.models.aml_verdict_manual_request import AmlVerdictManualRequest
from fireblocks.models.aml_verdict_manual_response import AmlVerdictManualResponse
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
    aml_verdict_manual_request = fireblocks.AmlVerdictManualRequest() # AmlVerdictManualRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set AML Verdict (BYORK Super Light)
        api_response = fireblocks.compliance.set_aml_verdict(aml_verdict_manual_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->set_aml_verdict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->set_aml_verdict: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aml_verdict_manual_request** | [**AmlVerdictManualRequest**](AmlVerdictManualRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**AmlVerdictManualResponse**](AmlVerdictManualResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AML verdict set successfully. |  -  |
**400** | Feature not enabled for tenant. |  * X-Request-ID -  <br>  |
**425** | Too Early - transaction not yet in pending screening. |  * X-Request-ID -  <br>  |
**500** | Internal server error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_byork_timeouts**
> ByorkConfigResponse set_byork_timeouts(byork_set_timeouts_request, idempotency_key=idempotency_key)

Set BYORK Light timeouts

Updates timeout values for BYORK wait-for-response (incoming and/or outgoing). At least one of incomingTimeoutSeconds or outgoingTimeoutSeconds is required. Values must be within the ranges returned in GET config (timeoutRangeIncoming for incomingTimeoutSeconds, timeoutRangeOutgoing for outgoingTimeoutSeconds). Requires BYORK Light to be enabled for the tenant (contact your CSM to enable).

### Example


```python
from fireblocks.models.byork_config_response import ByorkConfigResponse
from fireblocks.models.byork_set_timeouts_request import ByorkSetTimeoutsRequest
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
    byork_set_timeouts_request = fireblocks.ByorkSetTimeoutsRequest() # ByorkSetTimeoutsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set BYORK Light timeouts
        api_response = fireblocks.compliance.set_byork_timeouts(byork_set_timeouts_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->set_byork_timeouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->set_byork_timeouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **byork_set_timeouts_request** | [**ByorkSetTimeoutsRequest**](ByorkSetTimeoutsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ByorkConfigResponse**](ByorkConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timeouts updated. |  * X-Request-ID -  <br>  |
**400** | BYORK Light not enabled, or timeout value out of range, or missing both timeouts. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_byork_verdict**
> ByorkVerdictResponse set_byork_verdict(byork_verdict_request, idempotency_key=idempotency_key)

Set BYORK Light verdict

Submit verdict (ACCEPT or REJECT) for a transaction in the BYORK Light flow. If the transaction is awaiting your decision, the verdict is applied immediately (response status COMPLETED). If processing has not yet reached that point, the verdict is stored and applied when it does (response status PRE_ACCEPTED). Requires BYORK Light to be enabled for the tenant.

### Example


```python
from fireblocks.models.byork_verdict_request import ByorkVerdictRequest
from fireblocks.models.byork_verdict_response import ByorkVerdictResponse
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
    byork_verdict_request = fireblocks.ByorkVerdictRequest() # ByorkVerdictRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set BYORK Light verdict
        api_response = fireblocks.compliance.set_byork_verdict(byork_verdict_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->set_byork_verdict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->set_byork_verdict: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **byork_verdict_request** | [**ByorkVerdictRequest**](ByorkVerdictRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ByorkVerdictResponse**](ByorkVerdictResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verdict applied (COMPLETED) or pre-accepted (PRE_ACCEPTED). |  * X-Request-ID -  <br>  |
**400** | BYORK Light not enabled for tenant or invalid verdict. |  * X-Request-ID -  <br>  |
**409** | BYORK decision already final, screening already completed, or state inconsistent. |  * X-Request-ID -  <br>  |
**425** | Too Early - transaction not found (screening not started yet). |  * X-Request-ID -  <br>  |
**500** | Internal server error. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

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

# **update_counterparty_group**
> CounterpartyGroup update_counterparty_group(group_id, update_counterparty_group_request, idempotency_key=idempotency_key)

Update a counterparty group

Updates an existing counterparty group.

**Endpoint Permissions:** Admin, Non-Signing Admin.


### Example


```python
from fireblocks.models.counterparty_group import CounterpartyGroup
from fireblocks.models.update_counterparty_group_request import UpdateCounterpartyGroupRequest
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
    group_id = 'group_id_example' # str | The unique identifier of the counterparty group
    update_counterparty_group_request = fireblocks.UpdateCounterpartyGroupRequest() # UpdateCounterpartyGroupRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update a counterparty group
        api_response = fireblocks.compliance.update_counterparty_group(group_id, update_counterparty_group_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->update_counterparty_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_counterparty_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The unique identifier of the counterparty group | 
 **update_counterparty_group_request** | [**UpdateCounterpartyGroupRequest**](UpdateCounterpartyGroupRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CounterpartyGroup**](CounterpartyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Counterparty group updated successfully |  * X-Request-ID -  <br>  |
**404** | Counterparty group not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_legal_entity**
> LegalEntityRegistration update_legal_entity(legal_entity_id, update_legal_entity_request, idempotency_key=idempotency_key)

Update legal entity

Updates the status of a legal entity registration. Setting isDefault to true marks the registration as the workspace default, which is applied to vault accounts that have no explicit legal entity mapping.
Endpoint Permission: Admin, Non-Signing Admin.

### Example


```python
from fireblocks.models.legal_entity_registration import LegalEntityRegistration
from fireblocks.models.update_legal_entity_request import UpdateLegalEntityRequest
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
    legal_entity_id = 'legal_entity_id_example' # str | The unique ID of the legal entity registration
    update_legal_entity_request = fireblocks.UpdateLegalEntityRequest() # UpdateLegalEntityRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update legal entity
        api_response = fireblocks.compliance.update_legal_entity(legal_entity_id, update_legal_entity_request, idempotency_key=idempotency_key).result()
        print("The response of ComplianceApi->update_legal_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->update_legal_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **legal_entity_id** | **str**| The unique ID of the legal entity registration | 
 **update_legal_entity_request** | [**UpdateLegalEntityRequest**](UpdateLegalEntityRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**LegalEntityRegistration**](LegalEntityRegistration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated legal entity registration |  * X-Request-ID -  <br>  |
**400** | Registration is not in APPROVED status |  * X-Request-ID -  <br>  |
**404** | Legal entity registration not found |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

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

