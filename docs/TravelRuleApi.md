# fireblocks.TravelRuleApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vasp_for_vault**](TravelRuleApi.md#get_vasp_for_vault) | **GET** /screening/travel_rule/vault/{vaultAccountId}/vasp | Get assigned VASP to vault
[**get_vaspby_did**](TravelRuleApi.md#get_vaspby_did) | **GET** /screening/travel_rule/vasp/{did} | Get VASP details
[**get_vasps**](TravelRuleApi.md#get_vasps) | **GET** /screening/travel_rule/vasp | Get All VASPs
[**set_vasp_for_vault**](TravelRuleApi.md#set_vasp_for_vault) | **POST** /screening/travel_rule/vault/{vaultAccountId}/vasp | Assign VASP to vault
[**update_vasp**](TravelRuleApi.md#update_vasp) | **PUT** /screening/travel_rule/vasp/update | Add jsonDidKey to VASP details
[**validate_full_travel_rule_transaction**](TravelRuleApi.md#validate_full_travel_rule_transaction) | **POST** /screening/travel_rule/transaction/validate/full | Validate Full Travel Rule Transaction


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
        api_response = fireblocks.travel_rule.get_vasp_for_vault(vault_account_id).result()
        print("The response of TravelRuleApi->get_vasp_for_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->get_vasp_for_vault: %s\n" % e)
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

Get VASP Details.

Returns information about a VASP that has the specified DID.

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
    fields = ['fields_example'] # List[str] | A CSV of fields to return. Choose from the following options: (optional)

    try:
        # Get VASP details
        api_response = fireblocks.travel_rule.get_vaspby_did(did, fields=fields).result()
        print("The response of TravelRuleApi->get_vaspby_did:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->get_vaspby_did: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**|  | 
 **fields** | [**List[str]**](str.md)| A CSV of fields to return. Choose from the following options: | [optional] 

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
> TravelRuleGetAllVASPsResponse get_vasps(order=order, page_size=page_size, fields=fields, search=search, review_value=review_value, page_cursor=page_cursor)

Get All VASPs

Get All VASPs.

Returns a list of VASPs. VASPs can be searched and sorted.

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
    order = 'ASC' # str | Field to order by (optional)
    page_size = 500 # float | Records per page (optional) (default to 500)
    fields = ['fields_example'] # List[str] | CSV of fields to return (all, \"blank\" or see list of all field names below) (optional)
    search = 'Fireblocks' # str | Search query (optional)
    review_value = 'TRUSTED' # str | Filter by the VASP's review status. Possible values include: \"TRUSTED\", \"BLOCKED\", \"MANUAL\", or \"NULL\". When provided, only VASPs that match the specified reviewValue will be returned (i.e., VASPs that have already been reviewed to this status). (optional)
    page_cursor = '100' # str | Cursor for pagination. When provided, the response will include the next page of results. (optional)

    try:
        # Get All VASPs
        api_response = fireblocks.travel_rule.get_vasps(order=order, page_size=page_size, fields=fields, search=search, review_value=review_value, page_cursor=page_cursor).result()
        print("The response of TravelRuleApi->get_vasps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->get_vasps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Field to order by | [optional] 
 **page_size** | **float**| Records per page | [optional] [default to 500]
 **fields** | [**List[str]**](str.md)| CSV of fields to return (all, \&quot;blank\&quot; or see list of all field names below) | [optional] 
 **search** | **str**| Search query | [optional] 
 **review_value** | **str**| Filter by the VASP&#39;s review status. Possible values include: \&quot;TRUSTED\&quot;, \&quot;BLOCKED\&quot;, \&quot;MANUAL\&quot;, or \&quot;NULL\&quot;. When provided, only VASPs that match the specified reviewValue will be returned (i.e., VASPs that have already been reviewed to this status). | [optional] 
 **page_cursor** | **str**| Cursor for pagination. When provided, the response will include the next page of results. | [optional] 

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
**0** | Error Response |  * X-Request-ID -  <br>  |

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
        api_response = fireblocks.travel_rule.set_vasp_for_vault(vault_account_id, travel_rule_vasp_for_vault, idempotency_key=idempotency_key).result()
        print("The response of TravelRuleApi->set_vasp_for_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->set_vasp_for_vault: %s\n" % e)
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

Update VASP Details.

Updates a VASP with the provided parameters. Use this endpoint to add your public jsonDIDkey generated by Notabene.

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
        api_response = fireblocks.travel_rule.update_vasp(travel_rule_update_vasp_details, idempotency_key=idempotency_key).result()
        print("The response of TravelRuleApi->update_vasp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->update_vasp: %s\n" % e)
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
> TravelRuleValidateTransactionResponse validate_full_travel_rule_transaction(travel_rule_validate_full_transaction_request, notation=notation, idempotency_key=idempotency_key)

Validate Full Travel Rule Transaction

Validate Full Travel Rule transactions.

Checks for all required information on the originator and beneficiary VASPs.

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
    notation = ['notation_example'] # List[str] | Specifies the notation of the transaction. Possible values are: - `notabene`: Uses Notabene notation (default behavior). - `fireblocks`: Uses Fireblocks notation, with automatic translation of asset tickers and amounts. - `<none>`: Defaults to `notabene` for backward compatibility. **Note:** The default value for the `notation` parameter will change from `notabene` to `fireblocks` Update your integrations accordingly. (optional)
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Validate Full Travel Rule Transaction
        api_response = fireblocks.travel_rule.validate_full_travel_rule_transaction(travel_rule_validate_full_transaction_request, notation=notation, idempotency_key=idempotency_key).result()
        print("The response of TravelRuleApi->validate_full_travel_rule_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleApi->validate_full_travel_rule_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_validate_full_transaction_request** | [**TravelRuleValidateFullTransactionRequest**](TravelRuleValidateFullTransactionRequest.md)|  | 
 **notation** | [**List[str]**](str.md)| Specifies the notation of the transaction. Possible values are: - &#x60;notabene&#x60;: Uses Notabene notation (default behavior). - &#x60;fireblocks&#x60;: Uses Fireblocks notation, with automatic translation of asset tickers and amounts. - &#x60;&lt;none&gt;&#x60;: Defaults to &#x60;notabene&#x60; for backward compatibility. **Note:** The default value for the &#x60;notation&#x60; parameter will change from &#x60;notabene&#x60; to &#x60;fireblocks&#x60; Update your integrations accordingly. | [optional] 
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
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

