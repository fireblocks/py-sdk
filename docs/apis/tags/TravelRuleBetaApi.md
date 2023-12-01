<a id="__pageTop"></a>
# fireblocks_client.apis.tags.travel_rule_beta_api.TravelRuleBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vaspby_did**](#get_vaspby_did) | **get** /screening/travel_rule/vasp/{did} | Get VASP details
[**get_vasps**](#get_vasps) | **get** /screening/travel_rule/vasp | Get All VASPs
[**travel_rule_api_controller_update_vasp**](#travel_rule_api_controller_update_vasp) | **put** /screeening/travel_rule/vasp/update | Add jsonDidKey to VASP details
[**validate_full_travel_rule_transaction**](#validate_full_travel_rule_transaction) | **post** /screening/travel_rule/transaction/validate/full | Validate Full Travel Rule Transaction
[**validate_travel_rule_transaction**](#validate_travel_rule_transaction) | **post** /screening/travel_rule/transaction/validate | Validate Travel Rule Transaction

# **get_vaspby_did**
<a id="get_vaspby_did"></a>
> TravelRuleVASP get_vaspby_did(did)

Get VASP details

Get VASP Details.  Returns information about a VASP that has the specified DID.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
import fireblocks_client
from fireblocks_client.apis.tags import travel_rule_beta_api
from fireblocks_client.model.travel_rule_vasp import TravelRuleVASP
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

# Create an instance of the API class
api_instance = travel_rule_beta_api.TravelRuleBetaApi()
# example passing only required values which don't have defaults set
params = {
    'did': "did_example",
}
try:
    # Get VASP details
    api_response = api_instance.get_vaspby_did(params)
    pprint(api_response)
except fireblocks_client.ApiException as e:
    print("Exception when calling TravelRuleBetaApi->get_vaspby_did: %s\n" % e)

```
### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
fields | FieldsSchema | | optional


# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
did | DidSchema | | 

# DidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vaspby_did.ApiResponseFor200) | Transaction validated successfully
400 | [ApiResponseFor400](#get_vaspby_did.ApiResponseFor400) | Invalid request body
500 | [ApiResponseFor500](#get_vaspby_did.ApiResponseFor500) | Internal server error

#### get_vaspby_did.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleVASP**](../../models/TravelRuleVASP.md) |  | 


#### get_vaspby_did.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_vaspby_did.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vasps**
<a id="get_vasps"></a>
> TravelRuleGetAllVASPsResponse get_vasps()

Get All VASPs

Get All VASPs.  Returns a list of VASPs. VASPs can be searched and sorted and results are paginated.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
import fireblocks_client
from fireblocks_client.apis.tags import travel_rule_beta_api
from fireblocks_client.model.travel_rule_get_all_vasps_response import TravelRuleGetAllVASPsResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

# Create an instance of the API class
api_instance = travel_rule_beta_api.TravelRuleBetaApi()

```
### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
order | OrderSchema | | optional
per_page | PerPageSchema | | optional
page | PageSchema | | optional
fields | FieldsSchema | | optional


# OrderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vasps.ApiResponseFor200) | Get all VASPs

#### get_vasps.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleGetAllVASPsResponse**](../../models/TravelRuleGetAllVASPsResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **travel_rule_api_controller_update_vasp**
<a id="travel_rule_api_controller_update_vasp"></a>
> TravelRuleUpdateVASPDetails travel_rule_api_controller_update_vasp(travel_rule_update_vasp_details)

Add jsonDidKey to VASP details

Update VASP Details.  Updates a VASP with the provided parameters. Use this endpoint to add your public jsonDIDkey generated by Notabene.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
import fireblocks_client
from fireblocks_client.apis.tags import travel_rule_beta_api
from fireblocks_client.model.travel_rule_update_vasp_details import TravelRuleUpdateVASPDetails
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

# Create an instance of the API class
api_instance = travel_rule_beta_api.TravelRuleBetaApi()
# example passing only required values which don't have defaults set
params = {
    'travel_rule_update_vasp_details': TravelRuleUpdateVASPDetails(
        did="did:ethr:0x44957e75d6ce4a5bf37aae117da86422c848f7c2",
        pii_didkey="did:key:z6Mks5CZRaiooKYhq5TwtXQC1gWhwiZnmiKfFrMnYY62MhYf",
    )
}
try:
    # Add jsonDidKey to VASP details
    api_response = api_instance.travel_rule_api_controller_update_vasp(params)
    pprint(api_response)
except fireblocks_client.ApiException as e:
    print("Exception when calling TravelRuleBetaApi->travel_rule_api_controller_update_vasp: %s\n" % e)

```
### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleUpdateVASPDetails**](../../models/TravelRuleUpdateVASPDetails.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#travel_rule_api_controller_update_vasp.ApiResponseFor200) | VASP updated successfully
400 | [ApiResponseFor400](#travel_rule_api_controller_update_vasp.ApiResponseFor400) | Invalid request body
500 | [ApiResponseFor500](#travel_rule_api_controller_update_vasp.ApiResponseFor500) | Internal server error

#### travel_rule_api_controller_update_vasp.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleUpdateVASPDetails**](../../models/TravelRuleUpdateVASPDetails.md) |  | 


#### travel_rule_api_controller_update_vasp.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### travel_rule_api_controller_update_vasp.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **validate_full_travel_rule_transaction**
<a id="validate_full_travel_rule_transaction"></a>
> TravelRuleValidateTransactionResponse validate_full_travel_rule_transaction(travel_rule_validate_full_transaction_request)

Validate Full Travel Rule Transaction

Validate Full Travel Rule transactions.  Checks for all required information on the originator and beneficiary VASPs.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
import fireblocks_client
from fireblocks_client.apis.tags import travel_rule_beta_api
from fireblocks_client.model.travel_rule_validate_full_transaction_request import TravelRuleValidateFullTransactionRequest
from fireblocks_client.model.travel_rule_validate_transaction_response import TravelRuleValidateTransactionResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

# Create an instance of the API class
api_instance = travel_rule_beta_api.TravelRuleBetaApi()
# example passing only required values which don't have defaults set
params = {
    'travel_rule_validate_full_transaction_request': TravelRuleValidateFullTransactionRequest(
        transaction_asset="transaction_asset_example",
        transaction_amount="transaction_amount_example",
        originator_did="originator_did_example",
        beneficiary_did="beneficiary_did_example",
        originator_vas_pdid="originator_vas_pdid_example",
        beneficiary_vas_pdid="beneficiary_vas_pdid_example",
        beneficiary_vas_pname="beneficiary_vas_pname_example",
        transaction_blockchain_info=None,
        originator=None,
        beneficiary=None,
        encrypted="encrypted_example",
        protocol="protocol_example",
        notification_email="notification_email_example",
        skip_beneficiary_data_validation=True,
        travel_rule_behavior=True,
        originator_proof=None,
        beneficiary_proof=None,
        pii=None,
    )
}
try:
    # Validate Full Travel Rule Transaction
    api_response = api_instance.validate_full_travel_rule_transaction(params)
    pprint(api_response)
except fireblocks_client.ApiException as e:
    print("Exception when calling TravelRuleBetaApi->validate_full_travel_rule_transaction: %s\n" % e)

```
### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleValidateFullTransactionRequest**](../../models/TravelRuleValidateFullTransactionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#validate_full_travel_rule_transaction.ApiResponseFor200) | Transaction validated successfully
400 | [ApiResponseFor400](#validate_full_travel_rule_transaction.ApiResponseFor400) | Invalid request body
500 | [ApiResponseFor500](#validate_full_travel_rule_transaction.ApiResponseFor500) | Internal server error

#### validate_full_travel_rule_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleValidateTransactionResponse**](../../models/TravelRuleValidateTransactionResponse.md) |  | 


#### validate_full_travel_rule_transaction.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### validate_full_travel_rule_transaction.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **validate_travel_rule_transaction**
<a id="validate_travel_rule_transaction"></a>
> TravelRuleValidateTransactionResponse validate_travel_rule_transaction(travel_rule_validate_transaction_request)

Validate Travel Rule Transaction

Validate Travel Rule transactions.  Checks what beneficiary VASP details are required by your jurisdiction and the beneficiary's jurisdiction.  **Note:** The reference content in this section documents the Travel Rule beta endpoint. The beta endpoint includes APIs that are currently in preview and aren't yet generally available.  To enroll in the beta and enable this endpoint, contact your Fireblocks Customer Success Manager or send an email to [CSM@fireblocks.com](mailto:CSM@fireblocks.com).

### Example


```python
import fireblocks_client
from fireblocks_client.apis.tags import travel_rule_beta_api
from fireblocks_client.model.travel_rule_validate_transaction_response import TravelRuleValidateTransactionResponse
from fireblocks_client.model.travel_rule_validate_transaction_request import TravelRuleValidateTransactionRequest
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

# Create an instance of the API class
api_instance = travel_rule_beta_api.TravelRuleBetaApi()
# example passing only required values which don't have defaults set
params = {
    'travel_rule_validate_transaction_request': TravelRuleValidateTransactionRequest(
        transaction_asset="BTC",
        destination="bc1qxy2kgdygjrsqtzq2n0yrf1234p83kkfjhx0wlh",
        transaction_amount="10",
        originator_vas_pdid="did:ethr:0x44957e75d6ce4a5bf37aae117da86422c848f7c2",
        originator_equals_beneficiary=False,
        travel_rule_behavior=True,
        beneficiary_vas_pdid="did:ethr:0x46a7ed5813ce735387df2bfb245bd7722e0de992",
        beneficiary_vas_pname="HelloCrypto",
        beneficiary_name="John Doe",
        beneficiary_account_number="1234-1234-1234-12234",
        beneficiary_address=None,
    )
}
try:
    # Validate Travel Rule Transaction
    api_response = api_instance.validate_travel_rule_transaction(params)
    pprint(api_response)
except fireblocks_client.ApiException as e:
    print("Exception when calling TravelRuleBetaApi->validate_travel_rule_transaction: %s\n" % e)

```
### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleValidateTransactionRequest**](../../models/TravelRuleValidateTransactionRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#validate_travel_rule_transaction.ApiResponseFor200) | Transaction validated successfully
400 | [ApiResponseFor400](#validate_travel_rule_transaction.ApiResponseFor400) | Invalid request body
500 | [ApiResponseFor500](#validate_travel_rule_transaction.ApiResponseFor500) | Internal server error

#### validate_travel_rule_transaction.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TravelRuleValidateTransactionResponse**](../../models/TravelRuleValidateTransactionResponse.md) |  | 


#### validate_travel_rule_transaction.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### validate_travel_rule_transaction.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

