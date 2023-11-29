<a id="__pageTop"></a>
# fireblocks_client.apis.tags.vaults_api.VaultsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_asset_for_vault_account**](#activate_asset_for_vault_account) | **post** /vault/accounts/{vaultAccountId}/{assetId}/activate | Activate a wallet in a vault account
[**create_legacy_address_for_vault_account_asset**](#create_legacy_address_for_vault_account_asset) | **post** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/create_legacy | Convert a segwit address to legacy format
[**create_vault_account**](#create_vault_account) | **post** /vault/accounts | Create a new vault account
[**create_vault_account_asset**](#create_vault_account_asset) | **post** /vault/accounts/{vaultAccountId}/{assetId} | Create a new wallet
[**create_vault_account_asset_address**](#create_vault_account_asset_address) | **post** /vault/accounts/{vaultAccountId}/{assetId}/addresses | Create new asset deposit address
[**get_asset_wallets**](#get_asset_wallets) | **get** /vault/asset_wallets | List asset wallets (Paginated)
[**get_max_spendable_amount**](#get_max_spendable_amount) | **get** /vault/accounts/{vaultAccountId}/{assetId}/max_spendable_amount | Get the maximum spendable amount in a single transaction.
[**get_paged_vault_accounts**](#get_paged_vault_accounts) | **get** /vault/accounts_paged | List vault acounts (Paginated)
[**get_public_key_info**](#get_public_key_info) | **get** /vault/public_key_info/ | Get the public key information
[**get_public_key_info_for_address**](#get_public_key_info_for_address) | **get** /vault/accounts/{vaultAccountId}/{assetId}/{change}/{addressIndex}/public_key_info | Get the public key for a vault account
[**get_vault_account_asset**](#get_vault_account_asset) | **get** /vault/accounts/{vaultAccountId}/{assetId} | Get the asset balance for a vault account
[**get_vault_account_asset_addresses**](#get_vault_account_asset_addresses) | **get** /vault/accounts/{vaultAccountId}/{assetId}/addresses | Get asset addresses
[**get_vault_account_asset_unspent_inputs**](#get_vault_account_asset_unspent_inputs) | **get** /vault/accounts/{vaultAccountId}/{assetId}/unspent_inputs | Get UTXO unspent inputs information
[**get_vault_account_by_id**](#get_vault_account_by_id) | **get** /vault/accounts/{vaultAccountId} | Find a vault account by ID
[**get_vault_accounts**](#get_vault_accounts) | **get** /vault/accounts | List vault accounts
[**get_vault_asset_by_id**](#get_vault_asset_by_id) | **get** /vault/assets/{assetId} | Get vault balance by asset
[**get_vault_assets**](#get_vault_assets) | **get** /vault/assets | Get asset balance for chosen assets
[**hide_vault_account**](#hide_vault_account) | **post** /vault/accounts/{vaultAccountId}/hide | Hide a vault account in the console
[**set_auto_fuel_for_vault_account**](#set_auto_fuel_for_vault_account) | **post** /vault/accounts/{vaultAccountId}/set_auto_fuel | Turn autofueling on or off
[**set_customer_ref_id_for_vault_account**](#set_customer_ref_id_for_vault_account) | **post** /vault/accounts/{vaultAccountId}/set_customer_ref_id | Set an AML/KYT customer reference ID for a vault account
[**set_customer_ref_id_for_vault_account_asset_address**](#set_customer_ref_id_for_vault_account_asset_address) | **post** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId}/set_customer_ref_id | Assign AML customer reference ID
[**unhide_vault_account**](#unhide_vault_account) | **post** /vault/accounts/{vaultAccountId}/unhide | Unhide a vault account in the console
[**update_vault_account**](#update_vault_account) | **put** /vault/accounts/{vaultAccountId} | Rename a vault account
[**update_vault_account_asset_address**](#update_vault_account_asset_address) | **put** /vault/accounts/{vaultAccountId}/{assetId}/addresses/{addressId} | Update address description
[**update_vault_account_asset_balance**](#update_vault_account_asset_balance) | **post** /vault/accounts/{vaultAccountId}/{assetId}/balance | Refresh asset balance data

# **activate_asset_for_vault_account**
<a id="activate_asset_for_vault_account"></a>
> CreateVaultAssetResponse activate_asset_for_vault_account(vault_account_idasset_id)

Activate a wallet in a vault account

Initiates activation for a wallet in a vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.create_vault_asset_response import CreateVaultAssetResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Activate a wallet in a vault account
        api_response = api_instance.activate_asset_for_vault_account(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->activate_asset_for_vault_account: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#activate_asset_for_vault_account.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#activate_asset_for_vault_account.ApiResponseForDefault) | Error Response

#### activate_asset_for_vault_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateVaultAssetResponse**](../../models/CreateVaultAssetResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### activate_asset_for_vault_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_legacy_address_for_vault_account_asset**
<a id="create_legacy_address_for_vault_account_asset"></a>
> CreateAddressResponse create_legacy_address_for_vault_account_asset(vault_account_idasset_idaddress_id)

Convert a segwit address to legacy format

Converts an existing segwit address to the legacy format.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.create_address_response import CreateAddressResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
        'addressId': "addressId_example",
    }
    try:
        # Convert a segwit address to legacy format
        api_response = api_instance.create_legacy_address_for_vault_account_asset(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->create_legacy_address_for_vault_account_asset: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 
addressId | AddressIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AddressIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_legacy_address_for_vault_account_asset.ApiResponseFor200) | The created address
default | [ApiResponseForDefault](#create_legacy_address_for_vault_account_asset.ApiResponseForDefault) | Error Response

#### create_legacy_address_for_vault_account_asset.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateAddressResponse**](../../models/CreateAddressResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_legacy_address_for_vault_account_asset.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_vault_account**
<a id="create_vault_account"></a>
> VaultAccount create_vault_account(any_type)

Create a new vault account

Creates a new vault account with the requested name.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_account import VaultAccount
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    body = None
    try:
        # Create a new vault account
        api_response = api_instance.create_vault_account(
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->create_vault_account: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Account Name | [optional] 
**hiddenOnUI** | bool,  | BoolClass,  | Optional - if true, the created account and all related transactions will not be shown on Fireblocks console | [optional] 
**customerRefId** | str,  | str,  | Optional - Sets a customer reference ID | [optional] 
**autoFuel** | bool,  | BoolClass,  | Optional - Sets the autoFuel property of the vault account | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_vault_account.ApiResponseFor200) | A Vault Account object
default | [ApiResponseForDefault](#create_vault_account.ApiResponseForDefault) | Error Response

#### create_vault_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultAccount**](../../models/VaultAccount.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_vault_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_vault_account_asset**
<a id="create_vault_account_asset"></a>
> CreateVaultAssetResponse create_vault_account_asset(vault_account_idasset_id)

Create a new wallet

Creates a wallet for a specific asset in a vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.create_vault_asset_response import CreateVaultAssetResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Create a new wallet
        api_response = api_instance.create_vault_account_asset(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->create_vault_account_asset: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    body = None
    try:
        # Create a new wallet
        api_response = api_instance.create_vault_account_asset(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->create_vault_account_asset: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**eosAccountName** | str,  | str,  | Optional - when creating an EOS wallet, the account name. If not provided, a random name will be generated | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_vault_account_asset.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#create_vault_account_asset.ApiResponseForDefault) | Error Response

#### create_vault_account_asset.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateVaultAssetResponse**](../../models/CreateVaultAssetResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_vault_account_asset.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_vault_account_asset_address**
<a id="create_vault_account_asset_address"></a>
> CreateAddressResponse create_vault_account_asset_address(vault_account_idasset_id)

Create new asset deposit address

Creates a new deposit address for an asset of a vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.create_address_response import CreateAddressResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Create new asset deposit address
        api_response = api_instance.create_vault_account_asset_address(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->create_vault_account_asset_address: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    body = None
    try:
        # Create new asset deposit address
        api_response = api_instance.create_vault_account_asset_address(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->create_vault_account_asset_address: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  | (Optional) Attach a description to the new address | [optional] 
**customerRefId** | str,  | str,  | Optional - Sets a customer reference ID | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_vault_account_asset_address.ApiResponseFor200) | The created address
default | [ApiResponseForDefault](#create_vault_account_asset_address.ApiResponseForDefault) | Error Response

#### create_vault_account_asset_address.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateAddressResponse**](../../models/CreateAddressResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_vault_account_asset_address.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_asset_wallets**
<a id="get_asset_wallets"></a>
> PaginatedAssetWalletResponse get_asset_wallets()

List asset wallets (Paginated)

Gets all asset wallets at all of the vault accounts in your workspace. An asset wallet is an asset at a vault account. This method allows fast traversal of all account balances. **Note:**   - This API endpoint is in limited availability and available for selected customers. If you would like to get early access to this endpoint, please reach out to [Fireblocks Support](https://support.fireblocks.io/hc/en-us/requests/new?ticket_form_id=36000337220)   - This API call is subject to [rate limits](https://developers.fireblocks.com/reference/rate-limiting). 

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.paginated_asset_wallet_response import PaginatedAssetWalletResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()

    # example passing only optional values
    query_params = {
        'totalAmountLargerThan': 3.14,
        'assetId': "assetId_example",
        'before': "before_example",
        'after': "after_example",
        'limit': 200,
    }
    try:
        # List asset wallets (Paginated)
        api_response = api_instance.get_asset_wallets(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_asset_wallets: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
totalAmountLargerThan | TotalAmountLargerThanSchema | | optional
assetId | AssetIdSchema | | optional
before | BeforeSchema | | optional
after | AfterSchema | | optional
limit | LimitSchema | | optional


# TotalAmountLargerThanSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 200

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_asset_wallets.ApiResponseFor200) | A PaginatedAssetWalletResponse object

#### get_asset_wallets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedAssetWalletResponse**](../../models/PaginatedAssetWalletResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_max_spendable_amount**
<a id="get_max_spendable_amount"></a>
> get_max_spendable_amount(vault_account_idasset_id)

Get the maximum spendable amount in a single transaction.

Get the maximum amount of a particular asset that can be spent in a single transaction from a specified vault account (UTXO assets only, with a limitation on number of inputs embedded). Send several transactions if you want to spend more than the maximum spendable amount.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    query_params = {
    }
    try:
        # Get the maximum spendable amount in a single transaction.
        api_response = api_instance.get_max_spendable_amount(
            path_params=path_params,
            query_params=query_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_max_spendable_amount: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    query_params = {
        'manualSignging': True,
    }
    try:
        # Get the maximum spendable amount in a single transaction.
        api_response = api_instance.get_max_spendable_amount(
            path_params=path_params,
            query_params=query_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_max_spendable_amount: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
manualSignging | ManualSigngingSchema | | optional


# ManualSigngingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_max_spendable_amount.ApiResponseFor200) | OK
default | [ApiResponseForDefault](#get_max_spendable_amount.ApiResponseForDefault) | Error Response

#### get_max_spendable_amount.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor200 |  |
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_max_spendable_amount.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_paged_vault_accounts**
<a id="get_paged_vault_accounts"></a>
> VaultAccountsPagedResponse get_paged_vault_accounts()

List vault acounts (Paginated)

Gets all vault accounts in your workspace. This endpoint returns a limited amount of results with a quick response time.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_accounts_paged_response import VaultAccountsPagedResponse
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()

    # example passing only optional values
    query_params = {
        'namePrefix': "namePrefix_example",
        'nameSuffix': "nameSuffix_example",
        'minAmountThreshold': 3.14,
        'assetId': "assetId_example",
        'orderBy': "DESC",
        'before': "before_example",
        'after': "after_example",
        'limit': 200,
    }
    try:
        # List vault acounts (Paginated)
        api_response = api_instance.get_paged_vault_accounts(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_paged_vault_accounts: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namePrefix | NamePrefixSchema | | optional
nameSuffix | NameSuffixSchema | | optional
minAmountThreshold | MinAmountThresholdSchema | | optional
assetId | AssetIdSchema | | optional
orderBy | OrderBySchema | | optional
before | BeforeSchema | | optional
after | AfterSchema | | optional
limit | LimitSchema | | optional


# NamePrefixSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSuffixSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MinAmountThresholdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "DESC"

# BeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | if omitted the server will use the default value of 200

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_paged_vault_accounts.ApiResponseFor200) | A VaultAccountsPagedResponse object

#### get_paged_vault_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultAccountsPagedResponse**](../../models/VaultAccountsPagedResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_public_key_info**
<a id="get_public_key_info"></a>
> PublicKeyInformation get_public_key_info(derivation_pathalgorithm)

Get the public key information

Gets the public key information based on derivation path and signing algorithm.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.public_key_information import PublicKeyInformation
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    query_params = {
        'derivationPath': "derivationPath_example",
        'algorithm': "algorithm_example",
    }
    try:
        # Get the public key information
        api_response = api_instance.get_public_key_info(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_public_key_info: %s\n" % e)

    # example passing only optional values
    query_params = {
        'derivationPath': "derivationPath_example",
        'algorithm': "algorithm_example",
        'compressed': True,
    }
    try:
        # Get the public key information
        api_response = api_instance.get_public_key_info(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_public_key_info: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
derivationPath | DerivationPathSchema | | 
algorithm | AlgorithmSchema | | 
compressed | CompressedSchema | | optional


# DerivationPathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AlgorithmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CompressedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_public_key_info.ApiResponseFor200) | Public key information
default | [ApiResponseForDefault](#get_public_key_info.ApiResponseForDefault) | Error Response

#### get_public_key_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**PublicKeyInformation**](../../models/PublicKeyInformation.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_public_key_info.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_public_key_info_for_address**
<a id="get_public_key_info_for_address"></a>
> PublicKeyInformation get_public_key_info_for_address(vault_account_idasset_idchangeaddress_index)

Get the public key for a vault account

Gets the public key information for the vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.public_key_information import PublicKeyInformation
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
        'change': 3.14,
        'addressIndex': 3.14,
    }
    query_params = {
    }
    try:
        # Get the public key for a vault account
        api_response = api_instance.get_public_key_info_for_address(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_public_key_info_for_address: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
        'change': 3.14,
        'addressIndex': 3.14,
    }
    query_params = {
        'compressed': True,
    }
    try:
        # Get the public key for a vault account
        api_response = api_instance.get_public_key_info_for_address(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_public_key_info_for_address: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
compressed | CompressedSchema | | optional


# CompressedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 
change | ChangeSchema | | 
addressIndex | AddressIndexSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ChangeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# AddressIndexSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_public_key_info_for_address.ApiResponseFor200) | Public Key Information
default | [ApiResponseForDefault](#get_public_key_info_for_address.ApiResponseForDefault) | Error Response

#### get_public_key_info_for_address.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**PublicKeyInformation**](../../models/PublicKeyInformation.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_public_key_info_for_address.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault_account_asset**
<a id="get_vault_account_asset"></a>
> VaultAsset get_vault_account_asset(vault_account_idasset_id)

Get the asset balance for a vault account

Returns a wallet for a specific asset of a vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_asset import VaultAsset
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Get the asset balance for a vault account
        api_response = api_instance.get_vault_account_asset(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_vault_account_asset: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault_account_asset.ApiResponseFor200) | A VaultAsset object
default | [ApiResponseForDefault](#get_vault_account_asset.ApiResponseForDefault) | Error Response

#### get_vault_account_asset.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultAsset**](../../models/VaultAsset.md) |  | 


#### get_vault_account_asset.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault_account_asset_addresses**
<a id="get_vault_account_asset_addresses"></a>
> [VaultWalletAddress] get_vault_account_asset_addresses(vault_account_idasset_id)

Get asset addresses

Lists all addresses for specific asset of vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_wallet_address import VaultWalletAddress
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Get asset addresses
        api_response = api_instance.get_vault_account_asset_addresses(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_vault_account_asset_addresses: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault_account_asset_addresses.ApiResponseFor200) | A list of deposit addresses
default | [ApiResponseForDefault](#get_vault_account_asset_addresses.ApiResponseForDefault) | Error Response

#### get_vault_account_asset_addresses.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VaultWalletAddress**]({{complexTypePrefix}}VaultWalletAddress.md) | [**VaultWalletAddress**]({{complexTypePrefix}}VaultWalletAddress.md) | [**VaultWalletAddress**]({{complexTypePrefix}}VaultWalletAddress.md) |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_vault_account_asset_addresses.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault_account_asset_unspent_inputs**
<a id="get_vault_account_asset_unspent_inputs"></a>
> [UnspentInputsResponse] get_vault_account_asset_unspent_inputs(vault_account_idasset_id)

Get UTXO unspent inputs information

Returns unspent inputs information of an asset in a vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.unspent_inputs_response import UnspentInputsResponse
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Get UTXO unspent inputs information
        api_response = api_instance.get_vault_account_asset_unspent_inputs(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_vault_account_asset_unspent_inputs: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault_account_asset_unspent_inputs.ApiResponseFor200) | List of Unspent information per input
default | [ApiResponseForDefault](#get_vault_account_asset_unspent_inputs.ApiResponseForDefault) | Error Response

#### get_vault_account_asset_unspent_inputs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UnspentInputsResponse**]({{complexTypePrefix}}UnspentInputsResponse.md) | [**UnspentInputsResponse**]({{complexTypePrefix}}UnspentInputsResponse.md) | [**UnspentInputsResponse**]({{complexTypePrefix}}UnspentInputsResponse.md) |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_vault_account_asset_unspent_inputs.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault_account_by_id**
<a id="get_vault_account_by_id"></a>
> VaultAccount get_vault_account_by_id(vault_account_id)

Find a vault account by ID

Returns the requested vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_account import VaultAccount
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
    }
    try:
        # Find a vault account by ID
        api_response = api_instance.get_vault_account_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_vault_account_by_id: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault_account_by_id.ApiResponseFor200) | A Vault Account object
default | [ApiResponseForDefault](#get_vault_account_by_id.ApiResponseForDefault) | Error Response

#### get_vault_account_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultAccount**](../../models/VaultAccount.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_vault_account_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault_accounts**
<a id="get_vault_accounts"></a>
> [VaultAccount] get_vault_accounts()

List vault accounts

Gets all vault accounts in your workspace.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_account import VaultAccount
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()

    # example passing only optional values
    query_params = {
        'namePrefix': "namePrefix_example",
        'nameSuffix': "nameSuffix_example",
        'minAmountThreshold': 3.14,
        'assetId': "assetId_example",
    }
    try:
        # List vault accounts
        api_response = api_instance.get_vault_accounts(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_vault_accounts: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namePrefix | NamePrefixSchema | | optional
nameSuffix | NameSuffixSchema | | optional
minAmountThreshold | MinAmountThresholdSchema | | optional
assetId | AssetIdSchema | | optional


# NamePrefixSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSuffixSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MinAmountThresholdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault_accounts.ApiResponseFor200) | A list of vault accounts
default | [ApiResponseForDefault](#get_vault_accounts.ApiResponseForDefault) | Error Response

#### get_vault_accounts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VaultAccount**]({{complexTypePrefix}}VaultAccount.md) | [**VaultAccount**]({{complexTypePrefix}}VaultAccount.md) | [**VaultAccount**]({{complexTypePrefix}}VaultAccount.md) |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_vault_accounts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault_asset_by_id**
<a id="get_vault_asset_by_id"></a>
> VaultAsset get_vault_asset_by_id(asset_id)

Get vault balance by asset

Gets the vault balance summary for an asset.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_asset import VaultAsset
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'assetId': "assetId_example",
    }
    try:
        # Get vault balance by asset
        api_response = api_instance.get_vault_asset_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_vault_asset_by_id: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
assetId | AssetIdSchema | | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault_asset_by_id.ApiResponseFor200) | Vault amount by asset
default | [ApiResponseForDefault](#get_vault_asset_by_id.ApiResponseForDefault) | Error Response

#### get_vault_asset_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultAsset**](../../models/VaultAsset.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_vault_asset_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_vault_assets**
<a id="get_vault_assets"></a>
> [VaultAsset] get_vault_assets()

Get asset balance for chosen assets

Gets the assets amount summary for all accounts or filtered accounts.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_asset import VaultAsset
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()

    # example passing only optional values
    query_params = {
        'accountNamePrefix': "accountNamePrefix_example",
        'accountNameSuffix': "accountNameSuffix_example",
    }
    try:
        # Get asset balance for chosen assets
        api_response = api_instance.get_vault_assets(
            query_params=query_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->get_vault_assets: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
accountNamePrefix | AccountNamePrefixSchema | | optional
accountNameSuffix | AccountNameSuffixSchema | | optional


# AccountNamePrefixSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountNameSuffixSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vault_assets.ApiResponseFor200) | Amount by asset
default | [ApiResponseForDefault](#get_vault_assets.ApiResponseForDefault) | Error Response

#### get_vault_assets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VaultAsset**]({{complexTypePrefix}}VaultAsset.md) | [**VaultAsset**]({{complexTypePrefix}}VaultAsset.md) | [**VaultAsset**]({{complexTypePrefix}}VaultAsset.md) |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_vault_assets.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **hide_vault_account**
<a id="hide_vault_account"></a>
> hide_vault_account(vault_account_id)

Hide a vault account in the console

Hides the requested vault account from the web console view.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
    }
    try:
        # Hide a vault account in the console
        api_response = api_instance.hide_vault_account(
            path_params=path_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->hide_vault_account: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#hide_vault_account.ApiResponseFor201) | OK
default | [ApiResponseForDefault](#hide_vault_account.ApiResponseForDefault) | Error Response

#### hide_vault_account.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### hide_vault_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_auto_fuel_for_vault_account**
<a id="set_auto_fuel_for_vault_account"></a>
> set_auto_fuel_for_vault_account(vault_account_idany_type)

Turn autofueling on or off

Sets the autofueling property of the vault account to enabled or disabled.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
    }
    body = None
    try:
        # Turn autofueling on or off
        api_response = api_instance.set_auto_fuel_for_vault_account(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->set_auto_fuel_for_vault_account: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**autoFuel** | bool,  | BoolClass,  | Auto Fuel | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#set_auto_fuel_for_vault_account.ApiResponseFor201) | OK
default | [ApiResponseForDefault](#set_auto_fuel_for_vault_account.ApiResponseForDefault) | Error Response

#### set_auto_fuel_for_vault_account.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### set_auto_fuel_for_vault_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_customer_ref_id_for_vault_account**
<a id="set_customer_ref_id_for_vault_account"></a>
> set_customer_ref_id_for_vault_account(vault_account_idany_type)

Set an AML/KYT customer reference ID for a vault account

Assigns an AML/KYT customer reference ID for the vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
    }
    body = None
    try:
        # Set an AML/KYT customer reference ID for a vault account
        api_response = api_instance.set_customer_ref_id_for_vault_account(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->set_customer_ref_id_for_vault_account: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customerRefId** | str,  | str,  | Customer reference ID | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#set_customer_ref_id_for_vault_account.ApiResponseFor201) | OK
default | [ApiResponseForDefault](#set_customer_ref_id_for_vault_account.ApiResponseForDefault) | Error Response

#### set_customer_ref_id_for_vault_account.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### set_customer_ref_id_for_vault_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_customer_ref_id_for_vault_account_asset_address**
<a id="set_customer_ref_id_for_vault_account_asset_address"></a>
> set_customer_ref_id_for_vault_account_asset_address(vault_account_idasset_idaddress_idany_type)

Assign AML customer reference ID

Sets an AML/KYT customer reference ID for a specific address.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
        'addressId': "addressId_example",
    }
    body = None
    try:
        # Assign AML customer reference ID
        api_response = api_instance.set_customer_ref_id_for_vault_account_asset_address(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->set_customer_ref_id_for_vault_account_asset_address: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**customerRefId** | str,  | str,  | Customer reference ID | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 
addressId | AddressIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AddressIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#set_customer_ref_id_for_vault_account_asset_address.ApiResponseFor201) | OK
default | [ApiResponseForDefault](#set_customer_ref_id_for_vault_account_asset_address.ApiResponseForDefault) | Error Response

#### set_customer_ref_id_for_vault_account_asset_address.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### set_customer_ref_id_for_vault_account_asset_address.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **unhide_vault_account**
<a id="unhide_vault_account"></a>
> unhide_vault_account(vault_account_id)

Unhide a vault account in the console

Makes a hidden vault account visible in web console view.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
    }
    try:
        # Unhide a vault account in the console
        api_response = api_instance.unhide_vault_account(
            path_params=path_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->unhide_vault_account: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#unhide_vault_account.ApiResponseFor201) | OK
default | [ApiResponseForDefault](#unhide_vault_account.ApiResponseForDefault) | Error Response

#### unhide_vault_account.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### unhide_vault_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_vault_account**
<a id="update_vault_account"></a>
> update_vault_account(vault_account_idany_type)

Rename a vault account

Renames the requested vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
    }
    body = None
    try:
        # Rename a vault account
        api_response = api_instance.update_vault_account(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->update_vault_account: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Account Name | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#update_vault_account.ApiResponseFor201) | OK
default | [ApiResponseForDefault](#update_vault_account.ApiResponseForDefault) | Error Response

#### update_vault_account.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### update_vault_account.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_vault_account_asset_address**
<a id="update_vault_account_asset_address"></a>
> update_vault_account_asset_address(vault_account_idasset_idaddress_id)

Update address description

Updates the description of an existing address of an asset in a vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
        'addressId': "addressId_example",
    }
    try:
        # Update address description
        api_response = api_instance.update_vault_account_asset_address(
            path_params=path_params,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->update_vault_account_asset_address: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
        'addressId': "addressId_example",
    }
    body = None
    try:
        # Update address description
        api_response = api_instance.update_vault_account_asset_address(
            path_params=path_params,
            body=body,
        )
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->update_vault_account_asset_address: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  | The address description | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 
addressId | AddressIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AddressIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#update_vault_account_asset_address.ApiResponseFor201) | OK
default | [ApiResponseForDefault](#update_vault_account_asset_address.ApiResponseForDefault) | Error Response

#### update_vault_account_asset_address.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### update_vault_account_asset_address.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_vault_account_asset_balance**
<a id="update_vault_account_asset_balance"></a>
> VaultAsset update_vault_account_asset_balance(vault_account_idasset_id)

Refresh asset balance data

Updates the balance of a specific asset in a vault account.

### Example

```python
import fireblocks_client
from fireblocks_client.apis.tags import vaults_api
from fireblocks_client.model.vault_asset import VaultAsset
from fireblocks_client.model.error import Error
from pprint import pprint

# Set Fireblocks Parameters
os.environ["FIREBLOCKS_BASE_PATH"] = "https://sandbox-api.fireblocks.io/v1" # If left unset, default path is api.fireblocks.com
os.environ["FIREBLOCKS_API_KEY"] = "api-key"
os.environ["FIREBLOCKS_SECRET_KEY"] = open("./fireblocks_secret.key", "r").read()

    # Create an instance of the API class
    api_instance = vaults_api.VaultsApi()
    # example passing only required values which don't have defaults set
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    try:
        # Refresh asset balance data
        api_response = api_instance.update_vault_account_asset_balance(
            path_params=path_params,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->update_vault_account_asset_balance: %s\n" % e)

    # example passing only optional values
    path_params = {
        'vaultAccountId': "vaultAccountId_example",
        'assetId': "assetId_example",
    }
    body = dict()
    try:
        # Refresh asset balance data
        api_response = api_instance.update_vault_account_asset_balance(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except fireblocks_client.ApiException as e:
        print("Exception when calling VaultsApi->update_vault_account_asset_balance: %s\n" % e)
```### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('*/*', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
vaultAccountId | VaultAccountIdSchema | | 
assetId | AssetIdSchema | | 

# VaultAccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AssetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_vault_account_asset_balance.ApiResponseFor200) | A VaultAsset object
default | [ApiResponseForDefault](#update_vault_account_asset_balance.ApiResponseForDefault) | Error Response

#### update_vault_account_asset_balance.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBody, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBody
Type | Description  | Notes
------------- | ------------- | -------------
[**VaultAsset**](../../models/VaultAsset.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### update_vault_account_asset_balance.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor0 |  |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor0

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Request-ID | XRequestIDSchema | | optional

# XRequestIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

