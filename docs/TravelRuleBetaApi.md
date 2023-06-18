# fireblocks_client.TravelRuleBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vaspby_did**](TravelRuleBetaApi.md#get_vaspby_did) | **GET** /screening/travel_rule/vasp/{did} | Get VASP details
[**get_vasps**](TravelRuleBetaApi.md#get_vasps) | **GET** /screening/travel_rule/vasp | Get All VASPs
[**travel_rule_api_controller_update_vasp**](TravelRuleBetaApi.md#travel_rule_api_controller_update_vasp) | **PUT** /screeening/travel_rule/vasp/update | Add jsonDidKey to VASP details
[**validate_full_travel_rule_transaction**](TravelRuleBetaApi.md#validate_full_travel_rule_transaction) | **POST** /screening/travel_rule/transaction/validate/full | Validate Full Travel Rule Transaction
[**validate_travel_rule_transaction**](TravelRuleBetaApi.md#validate_travel_rule_transaction) | **POST** /screening/travel_rule/transaction/validate | Validate Travel Rule Transaction


# **get_vaspby_did**
> TravelRuleVASP get_vaspby_did(did, fields=fields)

Get VASP details

Get VASP Details.  Returns information about a VASP that has the specified DID.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

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
    api_instance = fireblocks_client.TravelRuleBetaApi(api_client)
    did = 'did_example' # str | 
    fields = 'fields_example' # str | CSV of fields to return (all, \"blank\" or see list of all field names below) (optional)

    try:
        # Get VASP details
        api_response = api_instance.get_vaspby_did(did, fields=fields)
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
    api_instance = fireblocks_client.TravelRuleBetaApi(api_client)
    order = 'order_example' # str | Field to order by (optional)
    per_page = 3.4 # float | Records per page (optional)
    page = 3.4 # float | Page number (optional)
    fields = 'fields_example' # str | CSV of fields to return (all, \"blank\" or see list of all field names below) (optional)

    try:
        # Get All VASPs
        api_response = api_instance.get_vasps(order=order, per_page=per_page, page=page, fields=fields)
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

# **travel_rule_api_controller_update_vasp**
> TravelRuleUpdateVASPDetails travel_rule_api_controller_update_vasp(travel_rule_update_vasp_details)

Add jsonDidKey to VASP details

Update VASP Details.  Updates a VASP with the provided parameters. Use this endpoint to add your public jsonDIDkey generated by Notabene.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

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
    api_instance = fireblocks_client.TravelRuleBetaApi(api_client)
    travel_rule_update_vasp_details = fireblocks_client.TravelRuleUpdateVASPDetails() # TravelRuleUpdateVASPDetails | 

    try:
        # Add jsonDidKey to VASP details
        api_response = api_instance.travel_rule_api_controller_update_vasp(travel_rule_update_vasp_details)
        print("The response of TravelRuleBetaApi->travel_rule_api_controller_update_vasp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->travel_rule_api_controller_update_vasp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_update_vasp_details** | [**TravelRuleUpdateVASPDetails**](TravelRuleUpdateVASPDetails.md)|  | 

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
> TravelRuleValidateTransactionResponse validate_full_travel_rule_transaction(travel_rule_validate_full_transaction_request)

Validate Full Travel Rule Transaction

Validate Full Travel Rule transactions.  Checks for all required information on the originator and beneficiary VASPs.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

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
    api_instance = fireblocks_client.TravelRuleBetaApi(api_client)
    travel_rule_validate_full_transaction_request = fireblocks_client.TravelRuleValidateFullTransactionRequest() # TravelRuleValidateFullTransactionRequest | 

    try:
        # Validate Full Travel Rule Transaction
        api_response = api_instance.validate_full_travel_rule_transaction(travel_rule_validate_full_transaction_request)
        print("The response of TravelRuleBetaApi->validate_full_travel_rule_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->validate_full_travel_rule_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_validate_full_transaction_request** | [**TravelRuleValidateFullTransactionRequest**](TravelRuleValidateFullTransactionRequest.md)|  | 

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
> TravelRuleValidateTransactionResponse validate_travel_rule_transaction(travel_rule_validate_transaction_request)

Validate Travel Rule Transaction

Validate Travel Rule transactions.  Checks what beneficiary VASP details are required by your jurisdiction and the beneficiary's jurisdiction.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

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
    api_instance = fireblocks_client.TravelRuleBetaApi(api_client)
    travel_rule_validate_transaction_request = fireblocks_client.TravelRuleValidateTransactionRequest() # TravelRuleValidateTransactionRequest | 

    try:
        # Validate Travel Rule Transaction
        api_response = api_instance.validate_travel_rule_transaction(travel_rule_validate_transaction_request)
        print("The response of TravelRuleBetaApi->validate_travel_rule_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TravelRuleBetaApi->validate_travel_rule_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **travel_rule_validate_transaction_request** | [**TravelRuleValidateTransactionRequest**](TravelRuleValidateTransactionRequest.md)|  | 

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

