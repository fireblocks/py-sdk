# fireblocks.KeyLinkBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_signing_key**](KeyLinkBetaApi.md#create_signing_key) | **POST** /key_link/signing_keys | Add a new signing key
[**create_validation_key**](KeyLinkBetaApi.md#create_validation_key) | **POST** /key_link/validation_keys | Add a new validation key
[**disable_validation_key**](KeyLinkBetaApi.md#disable_validation_key) | **PATCH** /key_link/validation_keys/{keyId} | Disables a validation key
[**get_signing_key**](KeyLinkBetaApi.md#get_signing_key) | **GET** /key_link/signing_keys/{keyId} | Get a signing key by &#x60;keyId&#x60;
[**get_signing_keys_list**](KeyLinkBetaApi.md#get_signing_keys_list) | **GET** /key_link/signing_keys | Get list of signing keys
[**get_validation_key**](KeyLinkBetaApi.md#get_validation_key) | **GET** /key_link/validation_keys/{keyId} | Get a validation key by &#x60;keyId&#x60;
[**get_validation_keys_list**](KeyLinkBetaApi.md#get_validation_keys_list) | **GET** /key_link/validation_keys | Get list of registered validation keys
[**set_agent_id**](KeyLinkBetaApi.md#set_agent_id) | **PATCH** /key_link/signing_keys/{keyId}/agent_user_id | Set agent user id that can sign with the signing key identified by the Fireblocks provided &#x60;keyId&#x60;
[**update_signing_key**](KeyLinkBetaApi.md#update_signing_key) | **PATCH** /key_link/signing_keys/{keyId} | Modify the signing by Fireblocks provided &#x60;keyId&#x60;


# **create_signing_key**
> SigningKeyDto create_signing_key(create_signing_key_dto, idempotency_key=idempotency_key)

Add a new signing key

Adds a new signing key to the workspace. The added key will be linked to the specific Fireblocks agent user ID. The same user will receive the proof of ownership message to be signed, and upon successful proof, the key will become enabled.
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.create_signing_key_dto import CreateSigningKeyDto
from fireblocks.models.signing_key_dto import SigningKeyDto
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
    create_signing_key_dto = fireblocks.CreateSigningKeyDto() # CreateSigningKeyDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add a new signing key
        api_response = fireblocks.key_link_beta.create_signing_key(create_signing_key_dto, idempotency_key=idempotency_key).result()
        print("The response of KeyLinkBetaApi->create_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->create_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_signing_key_dto** | [**CreateSigningKeyDto**](CreateSigningKeyDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SigningKeyDto**](SigningKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Newly created signing key |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_validation_key**
> CreateValidationKeyResponseDto create_validation_key(create_validation_key_dto, idempotency_key=idempotency_key)

Add a new validation key

Adds a new validation key used to validate signing keys. The new validation key will undergo an approval process by the workspace quorum.
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.create_validation_key_dto import CreateValidationKeyDto
from fireblocks.models.create_validation_key_response_dto import CreateValidationKeyResponseDto
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
    create_validation_key_dto = fireblocks.CreateValidationKeyDto() # CreateValidationKeyDto | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add a new validation key
        api_response = fireblocks.key_link_beta.create_validation_key(create_validation_key_dto, idempotency_key=idempotency_key).result()
        print("The response of KeyLinkBetaApi->create_validation_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->create_validation_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_validation_key_dto** | [**CreateValidationKeyDto**](CreateValidationKeyDto.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateValidationKeyResponseDto**](CreateValidationKeyResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The validation key that was added and is pending approval. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_validation_key**
> ValidationKeyDto disable_validation_key(key_id, modify_validation_key_dto)

Disables a validation key

Allows disabling validation key even if it has not expired yet. It is not allowed to enable the validation key back. Another key has to be used for future validations.
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.modify_validation_key_dto import ModifyValidationKeyDto
from fireblocks.models.validation_key_dto import ValidationKeyDto
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
    key_id = '46a92767-5f93-4a46-9eed-f012196bb4fc' # str | The unique identifier for the validation key provided by Fireblocks
    modify_validation_key_dto = fireblocks.ModifyValidationKeyDto() # ModifyValidationKeyDto | 

    try:
        # Disables a validation key
        api_response = fireblocks.key_link_beta.disable_validation_key(key_id, modify_validation_key_dto).result()
        print("The response of KeyLinkBetaApi->disable_validation_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->disable_validation_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The unique identifier for the validation key provided by Fireblocks | 
 **modify_validation_key_dto** | [**ModifyValidationKeyDto**](ModifyValidationKeyDto.md)|  | 

### Return type

[**ValidationKeyDto**](ValidationKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modified validation key data |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_key**
> SigningKeyDto get_signing_key(key_id)

Get a signing key by `keyId`

Returns a signing key if it exists, identified by the specified Fireblocks provided `keyId`.
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.signing_key_dto import SigningKeyDto
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
    key_id = '46a92767-5f93-4a46-9eed-f012196bb4fc' # str | The unique identifier for the signing key provided by Fireblocks

    try:
        # Get a signing key by `keyId`
        api_response = fireblocks.key_link_beta.get_signing_key(key_id).result()
        print("The response of KeyLinkBetaApi->get_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->get_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The unique identifier for the signing key provided by Fireblocks | 

### Return type

[**SigningKeyDto**](SigningKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested signing key data |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signing_keys_list**
> GetSigningKeyResponseDto get_signing_keys_list(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order, vault_account_id=vault_account_id, agent_user_id=agent_user_id, algorithm=algorithm, enabled=enabled, available=available, is_assigned=is_assigned)

Get list of signing keys

Returns the list of signing keys in the workspace
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.get_signing_key_response_dto import GetSigningKeyResponseDto
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
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Cursor to the next page (optional)
    page_size = 10 # float | Amount of results to return in the next page (optional) (default to 10)
    sort_by = createdAt # str | Field(s) to use for sorting (optional) (default to createdAt)
    order = ASC # str | Is the order ascending or descending (optional) (default to ASC)
    vault_account_id = 4 # float | Return keys assigned to a specific vault (optional)
    agent_user_id = '12fed207-5bdf-4a0c-ab12-fcd2627f75d1' # str | Return keys associated with a specific agent user (optional)
    algorithm = 'ECDSA_SECP256K1' # str | Return only keys with a specific algorithm (optional)
    enabled = True # bool | Return keys that have been proof of ownership (optional)
    available = True # bool | Return keys that are proof of ownership but not assigned. Available filter can be used only when vaultAccountId and enabled filters are not set (optional)
    is_assigned = True # bool | Return keys that are assigned to a vault account (optional)

    try:
        # Get list of signing keys
        api_response = fireblocks.key_link_beta.get_signing_keys_list(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order, vault_account_id=vault_account_id, agent_user_id=agent_user_id, algorithm=algorithm, enabled=enabled, available=available, is_assigned=is_assigned).result()
        print("The response of KeyLinkBetaApi->get_signing_keys_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->get_signing_keys_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor to the next page | [optional] 
 **page_size** | **float**| Amount of results to return in the next page | [optional] [default to 10]
 **sort_by** | **str**| Field(s) to use for sorting | [optional] [default to createdAt]
 **order** | **str**| Is the order ascending or descending | [optional] [default to ASC]
 **vault_account_id** | **float**| Return keys assigned to a specific vault | [optional] 
 **agent_user_id** | **str**| Return keys associated with a specific agent user | [optional] 
 **algorithm** | **str**| Return only keys with a specific algorithm | [optional] 
 **enabled** | **bool**| Return keys that have been proof of ownership | [optional] 
 **available** | **bool**| Return keys that are proof of ownership but not assigned. Available filter can be used only when vaultAccountId and enabled filters are not set | [optional] 
 **is_assigned** | **bool**| Return keys that are assigned to a vault account | [optional] 

### Return type

[**GetSigningKeyResponseDto**](GetSigningKeyResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of signing keys and a data that allows requesting the next page if applicable |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_key**
> ValidationKeyDto get_validation_key(key_id)

Get a validation key by `keyId`

Returns a validation key if it exists, identified by the specified `keyId`.
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.validation_key_dto import ValidationKeyDto
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
    key_id = 'key_id_example' # str | 

    try:
        # Get a validation key by `keyId`
        api_response = fireblocks.key_link_beta.get_validation_key(key_id).result()
        print("The response of KeyLinkBetaApi->get_validation_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->get_validation_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

### Return type

[**ValidationKeyDto**](ValidationKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested validation key data |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_keys_list**
> GetValidationKeyResponseDto get_validation_keys_list(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order)

Get list of registered validation keys

Returns the list of validation keys in the workspace
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.get_validation_key_response_dto import GetValidationKeyResponseDto
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
    page_cursor = 'MjAyMy0xMi0xMyAyMDozNjowOC4zMDI=:MTEwMA==' # str | Cursor to the next page (optional)
    page_size = 10 # float | Amount of results to return in the next page (optional) (default to 10)
    sort_by = createdAt # str | Field(s) to use for sorting (optional) (default to createdAt)
    order = ASC # str | Is the order ascending or descending (optional) (default to ASC)

    try:
        # Get list of registered validation keys
        api_response = fireblocks.key_link_beta.get_validation_keys_list(page_cursor=page_cursor, page_size=page_size, sort_by=sort_by, order=order).result()
        print("The response of KeyLinkBetaApi->get_validation_keys_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->get_validation_keys_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor to the next page | [optional] 
 **page_size** | **float**| Amount of results to return in the next page | [optional] [default to 10]
 **sort_by** | **str**| Field(s) to use for sorting | [optional] [default to createdAt]
 **order** | **str**| Is the order ascending or descending | [optional] [default to ASC]

### Return type

[**GetValidationKeyResponseDto**](GetValidationKeyResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation keys list along with data required to request the next page if applicable |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_agent_id**
> set_agent_id(key_id, modify_signing_key_agent_id_dto)

Set agent user id that can sign with the signing key identified by the Fireblocks provided `keyId`

Can modify existing signing key id if the key is not enabled. The change done in background and will be visible once applied. If key is already enabled (after proof of ownership) the user cannot be changed.
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.modify_signing_key_agent_id_dto import ModifySigningKeyAgentIdDto
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
    key_id = '46a92767-5f93-4a46-9eed-f012196bb4fc' # str | The unique identifier for the signing key provided by Fireblocks
    modify_signing_key_agent_id_dto = fireblocks.ModifySigningKeyAgentIdDto() # ModifySigningKeyAgentIdDto | 

    try:
        # Set agent user id that can sign with the signing key identified by the Fireblocks provided `keyId`
        fireblocks.key_link_beta.set_agent_id(key_id, modify_signing_key_agent_id_dto).result()
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->set_agent_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The unique identifier for the signing key provided by Fireblocks | 
 **modify_signing_key_agent_id_dto** | [**ModifySigningKeyAgentIdDto**](ModifySigningKeyAgentIdDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Agent user id modification process has started in background. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_signing_key**
> SigningKeyDto update_signing_key(key_id, modify_signing_key_dto)

Modify the signing by Fireblocks provided `keyId`

Allows assigning the signing key to a vault account, if it hasn't been assigned to any other vault accounts yet.
Please note that this endpoint is available only for Key Link enabled workspaces.
**Note:** 
This endpoint is currently in beta and might be subject to changes.
If you want to participate and learn more about the Fireblocks Key Link, please contact your Fireblocks Customer Success Manager or send an email to CSM@fireblocks.com.

### Example


```python
from fireblocks.models.modify_signing_key_dto import ModifySigningKeyDto
from fireblocks.models.signing_key_dto import SigningKeyDto
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
    key_id = '46a92767-5f93-4a46-9eed-f012196bb4fc' # str | The unique identifier for the signing key provided by Fireblocks
    modify_signing_key_dto = fireblocks.ModifySigningKeyDto() # ModifySigningKeyDto | 

    try:
        # Modify the signing by Fireblocks provided `keyId`
        api_response = fireblocks.key_link_beta.update_signing_key(key_id, modify_signing_key_dto).result()
        print("The response of KeyLinkBetaApi->update_signing_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyLinkBetaApi->update_signing_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The unique identifier for the signing key provided by Fireblocks | 
 **modify_signing_key_dto** | [**ModifySigningKeyDto**](ModifySigningKeyDto.md)|  | 

### Return type

[**SigningKeyDto**](SigningKeyDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Modified signing key data |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

