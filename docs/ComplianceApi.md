# fireblocks.ComplianceApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_address_registry_vault_opt_outs**](ComplianceApi.md#add_address_registry_vault_opt_outs) | **POST** /address_registry/vaults | Add vault accounts to the address registry opt-out list
[**assign_vaults_to_legal_entity**](ComplianceApi.md#assign_vaults_to_legal_entity) | **POST** /legal_entities/{legalEntityId}/vaults | Assign vault accounts to a legal entity
[**get_address_registry_tenant_participation_status**](ComplianceApi.md#get_address_registry_tenant_participation_status) | **GET** /address_registry/tenant | Get address registry participation status for the authenticated workspace
[**get_address_registry_vault_opt_out**](ComplianceApi.md#get_address_registry_vault_opt_out) | **GET** /address_registry/vaults/{vaultAccountId} | Get whether a vault account is opted out of the address registry
[**get_aml_post_screening_policy**](ComplianceApi.md#get_aml_post_screening_policy) | **GET** /screening/aml/post_screening_policy | AML - View Post-Screening Policy
[**get_aml_screening_policy**](ComplianceApi.md#get_aml_screening_policy) | **GET** /screening/aml/screening_policy | AML - View Screening Policy
[**get_legal_entity**](ComplianceApi.md#get_legal_entity) | **GET** /legal_entities/{legalEntityId} | Get a legal entity
[**get_legal_entity_by_address**](ComplianceApi.md#get_legal_entity_by_address) | **GET** /address_registry/legal_entity | [Deprecated] Look up legal entity by address (query parameter)
[**get_legal_entity_for_address**](ComplianceApi.md#get_legal_entity_for_address) | **GET** /address_registry/legal_entities/{address} | Look up legal entity by blockchain address
[**get_post_screening_policy**](ComplianceApi.md#get_post_screening_policy) | **GET** /screening/travel_rule/post_screening_policy | Travel Rule - View Post-Screening Policy
[**get_screening_full_details**](ComplianceApi.md#get_screening_full_details) | **GET** /screening/transaction/{txId} | Provides all the compliance details for the given screened transaction.
[**get_screening_policy**](ComplianceApi.md#get_screening_policy) | **GET** /screening/travel_rule/screening_policy | Travel Rule - View Screening Policy
[**list_address_registry_vault_opt_outs**](ComplianceApi.md#list_address_registry_vault_opt_outs) | **GET** /address_registry/vaults | List vault-level address registry opt-outs (paginated)
[**list_legal_entities**](ComplianceApi.md#list_legal_entities) | **GET** /legal_entities | List legal entities (Paginated)
[**list_vaults_for_legal_entity**](ComplianceApi.md#list_vaults_for_legal_entity) | **GET** /legal_entities/{legalEntityId}/vaults | List vault accounts for a legal entity (Paginated)
[**opt_in_address_registry_tenant**](ComplianceApi.md#opt_in_address_registry_tenant) | **POST** /address_registry/tenant | Opt the workspace in to the address registry
[**opt_out_address_registry_tenant**](ComplianceApi.md#opt_out_address_registry_tenant) | **DELETE** /address_registry/tenant | Opt the workspace out of the address registry
[**register_legal_entity**](ComplianceApi.md#register_legal_entity) | **POST** /legal_entities | Register a new legal entity
[**remove_address_registry_vault_opt_out**](ComplianceApi.md#remove_address_registry_vault_opt_out) | **DELETE** /address_registry/vaults/{vaultAccountId} | Remove a single vault account from the address registry opt-out list
[**remove_all_address_registry_vault_opt_outs**](ComplianceApi.md#remove_all_address_registry_vault_opt_outs) | **DELETE** /address_registry/vaults | Remove all vault-level address registry opt-outs for the workspace
[**retry_rejected_transaction_bypass_screening_checks**](ComplianceApi.md#retry_rejected_transaction_bypass_screening_checks) | **POST** /screening/transaction/{txId}/bypass_screening_policy | Calling the \&quot;Bypass Screening Policy\&quot; API endpoint triggers a new transaction, with the API user as the initiator, bypassing the screening policy check
[**set_aml_verdict**](ComplianceApi.md#set_aml_verdict) | **POST** /screening/aml/verdict/manual | Set AML Verdict for Manual Screening Verdict.
[**update_aml_screening_configuration**](ComplianceApi.md#update_aml_screening_configuration) | **PUT** /screening/aml/policy_configuration | Update AML Configuration
[**update_legal_entity**](ComplianceApi.md#update_legal_entity) | **PUT** /legal_entities/{legalEntityId} | Update legal entity
[**update_screening_configuration**](ComplianceApi.md#update_screening_configuration) | **PUT** /screening/configurations | Tenant - Screening Configuration
[**update_travel_rule_config**](ComplianceApi.md#update_travel_rule_config) | **PUT** /screening/travel_rule/policy_configuration | Update Travel Rule Configuration


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
</br>Endpoint Permission: Admin, Non-Signing Admin.

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

# **get_legal_entity**
> LegalEntityRegistration get_legal_entity(legal_entity_id)

Get a legal entity

Returns details of a specific legal entity registration, including GLEIF data when available.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

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

# **get_legal_entity_by_address**
> AddressRegistryLegalEntityLegacy get_legal_entity_by_address(address, asset=asset)

[Deprecated] Look up legal entity by address (query parameter)

**Deprecated** — use `GET /v1/address_registry/legal_entities/{address}` instead.
Here `address` is a **query** parameter; the replacement uses a path segment.
The response includes only `companyName`, `countryCode`, and `companyId`. The replacement returns additional fields documented on that operation.
Optional **`asset`** is supported here only (not on the replacement path).

### Example


```python
from fireblocks.models.address_registry_legal_entity_legacy import AddressRegistryLegalEntityLegacy
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
    asset = 'ETH' # str | Optional asset identifier (this deprecated operation only). (optional)

    try:
        # [Deprecated] Look up legal entity by address (query parameter)
        api_response = fireblocks.compliance.get_legal_entity_by_address(address, asset=asset).result()
        print("The response of ComplianceApi->get_legal_entity_by_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComplianceApi->get_legal_entity_by_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Blockchain address to look up | 
 **asset** | **str**| Optional asset identifier (this deprecated operation only). | [optional] 

### Return type

[**AddressRegistryLegalEntityLegacy**](AddressRegistryLegalEntityLegacy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Legal entity found |  * X-Request-ID -  <br>  |
**400** | Bad request – missing or invalid address |  * X-Request-ID -  <br>  |
**403** | Forbidden – the authenticated workspace is not opted in to the address registry (error code 2140) |  * X-Request-ID -  <br>  |
**404** | Not found (error code 2142) — unresolved address, no legal entity for a resolved address, or the same not-found outcome in other cases. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_entity_for_address**
> AddressRegistryLegalEntity get_legal_entity_for_address(address)

Look up legal entity by blockchain address

Returns legal entity information for the given blockchain address. URL-encode `{address}` when required.
Prefer this operation over the deprecated `GET /v1/address_registry/legal_entity?address=…`, which returns only `companyName`, `countryCode`, and `companyId`. This operation adds verification status, LEI, Travel Rule providers, and contact email (see response properties).

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
**400** | Bad request – missing or invalid address |  * X-Request-ID -  <br>  |
**403** | Forbidden – the authenticated workspace is not opted in to the address registry (error code 2140) |  * X-Request-ID -  <br>  |
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

# **list_legal_entities**
> ListLegalEntitiesResponse list_legal_entities(vault_account_id=vault_account_id, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

List legal entities (Paginated)

Returns legal entity registrations for the workspace with cursor-based pagination.
If query parameter vaultAccountId is used it returns the legal entity registration associated with a specific vault account. If no explicit mapping exists for the vault, the workspace default legal entity is returned. Returns an empty response if neither a vault mapping nor a default legal entity is configured.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

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
    sort_by = 'sort_by_example' # str | Field to sort results by. Ignored when `vaultAccountId` is provided. (optional)
    order = DESC # str | Sort order. Ignored when `vaultAccountId` is provided. (optional) (default to DESC)

    try:
        # List legal entities (Paginated)
        api_response = fireblocks.compliance.list_legal_entities(vault_account_id=vault_account_id, page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
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
 **sort_by** | **str**| Field to sort results by. Ignored when &#x60;vaultAccountId&#x60; is provided. | [optional] 
 **order** | **str**| Sort order. Ignored when &#x60;vaultAccountId&#x60; is provided. | [optional] [default to DESC]

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
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor, Viewer.

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
</br>Endpoint Permission: Admin, Non-Signing Admin.

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

Calling the \"Bypass Screening Policy\" API endpoint triggers a new transaction, with the API user as the initiator, bypassing the screening policy check

This endpoint is restricted to Admin API users and is only applicable to outgoing transactions.

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
        # Calling the \"Bypass Screening Policy\" API endpoint triggers a new transaction, with the API user as the initiator, bypassing the screening policy check
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

Set AML Verdict for Manual Screening Verdict.

Set AML verdict for incoming transactions when Manual Screening Verdict feature is enabled.

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
        # Set AML Verdict for Manual Screening Verdict.
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

# **update_legal_entity**
> LegalEntityRegistration update_legal_entity(legal_entity_id, update_legal_entity_request, idempotency_key=idempotency_key)

Update legal entity

Updates the status of a legal entity registration. Setting isDefault to true marks the registration as the workspace default, which is applied to vault accounts that have no explicit legal entity mapping.
</br>Endpoint Permission: Admin, Non-Signing Admin.

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

