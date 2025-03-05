# fireblocks.TravelRuleBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vasp_for_vault**](TravelRuleBetaApi.md#get_vasp_for_vault) | **GET** /screening/travel_rule/vault/{vaultAccountId}/vasp | Get assigned VASP to vault
[**get_vaspby_did**](TravelRuleBetaApi.md#get_vaspby_did) | **GET** /screening/travel_rule/vasp/{did} | Get VASP details
[**get_vasps**](TravelRuleBetaApi.md#get_vasps) | **GET** /screening/travel_rule/vasp | Get All VASPs
[**set_vasp_for_vault**](TravelRuleBetaApi.md#set_vasp_for_vault) | **POST** /screening/travel_rule/vault/{vaultAccountId}/vasp | Assign VASP to vault
[**update_vasp**](TravelRuleBetaApi.md#update_vasp) | **PUT** /screening/travel_rule/vasp/update | Add jsonDidKey to VASP details
[**validate_full_travel_rule_transaction**](TravelRuleBetaApi.md#validate_full_travel_rule_transaction) | **POST** /screening/travel_rule/transaction/validate/full | Validate Full Travel Rule Transaction
[**validate_travel_rule_transaction**](TravelRuleBetaApi.md#validate_travel_rule_transaction) | **POST** /screening/travel_rule/transaction/validate | Validate Travel Rule Transaction


# **get_vasp_for_vault**
> TravelRuleVaspForVault get_vasp_for_vault(vault_account_id)

Get assigned VASP to vault

Get assigned VASP Did for a specific vault. Returns empty string vaspDid value in response if none assigned.

### Example


```python
from fireblocks.models.travel_rule_vasp_for_vault import TravelRuleVaspForVault
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
    vault_account_id = '1' # str | The ID of the vault account

    try:
        # Get assigned VASP to vault
        api_response = fireblocks.travel_rule_beta.get_vasp_for_vault(vault_account_id).result()
        print("The response of TravelRuleBetaApi->get_vasp_for_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->get_vasp_for_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 

### Return type

[**TravelRuleVaspForVault**](TravelRuleVaspForVault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vaspby_did**
> TravelRuleVASP get_vaspby_did(did, fields=fields)

Get VASP details

Get VASP Details.  Returns information about a VASP that has the specified DID.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
from fireblocks.models.travel_rule_vasp import TravelRuleVASP
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
    did = 'did_example' # str | 
    fields = 'fields_example' # str | CSV of fields to return (all, \"blank\" or see list of all field names below) (optional)

    try:
        # Get VASP details
        api_response = fireblocks.travel_rule_beta.get_vaspby_did(did, fields=fields).result()
        print("The response of TravelRuleBetaApi->get_vaspby_did:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->get_vaspby_did: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **fields** | **str**| CSV of fields to return (all, \&quot;blank\&quot; or see list of all field names below) | [optional] 

### Return type

[**TravelRuleVASP**](TravelRuleVASP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction validated successfully |  -  |
**400** | Invalid request body |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vasps**
> TravelRuleGetAllVASPsResponse get_vasps(order=order, per_page=per_page, page=page, fields=fields)

Get All VASPs

Get All VASPs.  Returns a list of VASPs. VASPs can be searched and sorted and results are paginated.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
from fireblocks.models.travel_rule_get_all_vasps_response import TravelRuleGetAllVASPsResponse
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
    order = 'order_example' # str | Field to order by (optional)
    per_page = 3.4 # float | Records per page (optional)
    page = 3.4 # float | Page number (optional)
    fields = 'fields_example' # str | CSV of fields to return (all, \"blank\" or see list of all field names below) (optional)

    try:
        # Get All VASPs
        api_response = fireblocks.travel_rule_beta.get_vasps(order=order, per_page=per_page, page=page, fields=fields).result()
        print("The response of TravelRuleBetaApi->get_vasps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->get_vasps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Field to order by | [optional] 
 **per_page** | **float**| Records per page | [optional] 
 **page** | **float**| Page number | [optional] 
 **fields** | **str**| CSV of fields to return (all, \&quot;blank\&quot; or see list of all field names below) | [optional] 

### Return type

[**TravelRuleGetAllVASPsResponse**](TravelRuleGetAllVASPsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get all VASPs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vasp_for_vault**
> TravelRuleVaspForVault set_vasp_for_vault(vault_account_id, travel_rule_vasp_for_vault, idempotency_key=idempotency_key)

Assign VASP to vault

Sets the VASP Did for a specific vault. Pass empty string to remove existing one.

### Example


```python
from fireblocks.models.travel_rule_vasp_for_vault import TravelRuleVaspForVault
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
    vault_account_id = 'vault_account_id_example' # str | The ID of the vault account
    travel_rule_vasp_for_vault = fireblocks.TravelRuleVaspForVault() # TravelRuleVaspForVault | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Assign VASP to vault
        api_response = fireblocks.travel_rule_beta.set_vasp_for_vault(vault_account_id, travel_rule_vasp_for_vault, idempotency_key=idempotency_key).result()
        print("The response of TravelRuleBetaApi->set_vasp_for_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->set_vasp_for_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_account_id** | **str**| The ID of the vault account | 
 **travel_rule_vasp_for_vault** | [**TravelRuleVaspForVault**](TravelRuleVaspForVault.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TravelRuleVaspForVault**](TravelRuleVaspForVault.md)

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

# **update_vasp**
> TravelRuleUpdateVASPDetails update_vasp(travel_rule_update_vasp_details, idempotency_key=idempotency_key)

Add jsonDidKey to VASP details

Update VASP Details.  Updates a VASP with the provided parameters. Use this endpoint to add your public jsonDIDkey generated by Notabene.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
from fireblocks.models.travel_rule_update_vasp_details import TravelRuleUpdateVASPDetails
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
    travel_rule_update_vasp_details = fireblocks.TravelRuleUpdateVASPDetails() # TravelRuleUpdateVASPDetails | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add jsonDidKey to VASP details
        api_response = fireblocks.travel_rule_beta.update_vasp(travel_rule_update_vasp_details, idempotency_key=idempotency_key).result()
        print("The response of TravelRuleBetaApi->update_vasp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->update_vasp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_update_vasp_details** | [**TravelRuleUpdateVASPDetails**](TravelRuleUpdateVASPDetails.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TravelRuleUpdateVASPDetails**](TravelRuleUpdateVASPDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VASP updated successfully |  -  |
**400** | Invalid request body |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_full_travel_rule_transaction**
> TravelRuleValidateTransactionResponse validate_full_travel_rule_transaction(travel_rule_validate_full_transaction_request, idempotency_key=idempotency_key)

Validate Full Travel Rule Transaction

Validate Full Travel Rule transactions.  Checks for all required information on the originator and beneficiary VASPs.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
from fireblocks.models.travel_rule_validate_full_transaction_request import TravelRuleValidateFullTransactionRequest
from fireblocks.models.travel_rule_validate_transaction_response import TravelRuleValidateTransactionResponse
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
    travel_rule_validate_full_transaction_request = fireblocks.TravelRuleValidateFullTransactionRequest() # TravelRuleValidateFullTransactionRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Validate Full Travel Rule Transaction
        api_response = fireblocks.travel_rule_beta.validate_full_travel_rule_transaction(travel_rule_validate_full_transaction_request, idempotency_key=idempotency_key).result()
        print("The response of TravelRuleBetaApi->validate_full_travel_rule_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->validate_full_travel_rule_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_validate_full_transaction_request** | [**TravelRuleValidateFullTransactionRequest**](TravelRuleValidateFullTransactionRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TravelRuleValidateTransactionResponse**](TravelRuleValidateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction validated successfully |  -  |
**400** | Invalid request body |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_travel_rule_transaction**
> TravelRuleValidateTransactionResponse validate_travel_rule_transaction(travel_rule_validate_transaction_request, idempotency_key=idempotency_key)

Validate Travel Rule Transaction

Validate Travel Rule transactions.  Checks what beneficiary VASP details are required by your jurisdiction and the beneficiary's jurisdiction.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
from fireblocks.models.travel_rule_validate_transaction_request import TravelRuleValidateTransactionRequest
from fireblocks.models.travel_rule_validate_transaction_response import TravelRuleValidateTransactionResponse
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
    travel_rule_validate_transaction_request = fireblocks.TravelRuleValidateTransactionRequest() # TravelRuleValidateTransactionRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Validate Travel Rule Transaction
        api_response = fireblocks.travel_rule_beta.validate_travel_rule_transaction(travel_rule_validate_transaction_request, idempotency_key=idempotency_key).result()
        print("The response of TravelRuleBetaApi->validate_travel_rule_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->validate_travel_rule_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_validate_transaction_request** | [**TravelRuleValidateTransactionRequest**](TravelRuleValidateTransactionRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**TravelRuleValidateTransactionResponse**](TravelRuleValidateTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction validated successfully |  -  |
**400** | Invalid request body |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

