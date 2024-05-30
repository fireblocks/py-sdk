# fireblocks.StakingBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_terms_of_service_by_provider_id**](StakingBetaApi.md#approve_terms_of_service_by_provider_id) | **POST** /staking/providers/{providerId}/approveTermsOfService | 
[**execute_action**](StakingBetaApi.md#execute_action) | **POST** /staking/chains/{chainDescriptor}/{actionId} | 
[**get_all_delegations**](StakingBetaApi.md#get_all_delegations) | **GET** /staking/positions | 
[**get_chain_info**](StakingBetaApi.md#get_chain_info) | **GET** /staking/chains/{chainDescriptor}/chainInfo | 
[**get_chains**](StakingBetaApi.md#get_chains) | **GET** /staking/chains | 
[**get_delegation_by_id**](StakingBetaApi.md#get_delegation_by_id) | **GET** /staking/positions/{id} | 
[**get_providers**](StakingBetaApi.md#get_providers) | **GET** /staking/providers | 
[**get_summary**](StakingBetaApi.md#get_summary) | **GET** /staking/positions/summary | 
[**get_summary_by_vault**](StakingBetaApi.md#get_summary_by_vault) | **GET** /staking/positions/summary/vaults | 


# **approve_terms_of_service_by_provider_id**
> object approve_terms_of_service_by_provider_id(provider_id, idempotency_key=idempotency_key)



Approve the terms of service of the staking provider. This must be called before performing a staking action for the first time with this provider.

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
    provider_id = 'provider_id_example' # str | The unique identifier of the staking provider
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # 
        api_response = fireblocks.staking_beta.approve_terms_of_service_by_provider_id(provider_id, idempotency_key=idempotency_key).result()
        print("The response of StakingBetaApi->approve_terms_of_service_by_provider_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->approve_terms_of_service_by_provider_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **str**| The unique identifier of the staking provider | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The terms of service have been successfully approved and is associated with 201 status code. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_action**
> ExecuteActionResponse execute_action(chain_descriptor, action_id, execute_action_request, idempotency_key=idempotency_key)



Perform a chain-specific staking action (e.g. stake, unstake, withdraw).

### Example


```python
from fireblocks.models.execute_action_request import ExecuteActionRequest
from fireblocks.models.execute_action_response import ExecuteActionResponse
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
    chain_descriptor = 'chain_descriptor_example' # str | The protocol identifier (e.g. \"ETH\"/\"SOL\") to use
    action_id = 'action_id_example' # str | The operation that can be executed on a vault/position
    execute_action_request = {"vaultAccountId":"22","providerId":"kiln","stakeAmount":"32","chainDescriptor":"ETH","txNote":"stake request id CcaHc2L43ZWjwCHART3oZoJvHLAe9hzT2DJNUpBzoTN1 of 32ETH created on 02.04.23","feeLevel":"MEDIUM"} # ExecuteActionRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # 
        api_response = fireblocks.staking_beta.execute_action(chain_descriptor, action_id, execute_action_request, idempotency_key=idempotency_key).result()
        print("The response of StakingBetaApi->execute_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->execute_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;) to use | 
 **action_id** | **str**| The operation that can be executed on a vault/position | 
 **execute_action_request** | [**ExecuteActionRequest**](ExecuteActionRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ExecuteActionResponse**](ExecuteActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A chain-specific action has been executed successfully on vault/position and is associated with 201 status code. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_delegations**
> List[DelegationDto] get_all_delegations(chain_descriptor=chain_descriptor)



Return detailed information on all staking positions, including the staked amount, rewards, status and more.

### Example


```python
from fireblocks.models.delegation_dto import DelegationDto
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
    chain_descriptor = 'chain_descriptor_example' # str | Use \"ETH\" / \"SOL\" in order to obtain information related to the specific blockchain network or retrieve information about all chains that have data available by providing no argument. (optional)

    try:
        # 
        api_response = fireblocks.staking_beta.get_all_delegations(chain_descriptor=chain_descriptor).result()
        print("The response of StakingBetaApi->get_all_delegations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->get_all_delegations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| Use \&quot;ETH\&quot; / \&quot;SOL\&quot; in order to obtain information related to the specific blockchain network or retrieve information about all chains that have data available by providing no argument. | [optional] 

### Return type

[**List[DelegationDto]**](DelegationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of position data was returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chain_info**
> ChainInfoResponseDto get_chain_info(chain_descriptor)



Return chain-specific, staking-related information summary (e.g. epoch details, lockup durations, estimated rewards, etc.)

### Example


```python
from fireblocks.models.chain_info_response_dto import ChainInfoResponseDto
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
    chain_descriptor = 'chain_descriptor_example' # str | The protocol identifier (e.g. \"ETH\"/\"SOL\") to use

    try:
        # 
        api_response = fireblocks.staking_beta.get_chain_info(chain_descriptor).result()
        print("The response of StakingBetaApi->get_chain_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->get_chain_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;) to use | 

### Return type

[**ChainInfoResponseDto**](ChainInfoResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chain specific info summary was returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chains**
> List[str] get_chains()



Return an alphabetical list of supported chains.

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
        # 
        api_response = fireblocks.staking_beta.get_chains().result()
        print("The response of StakingBetaApi->get_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->get_chains: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegation_by_id**
> DelegationDto get_delegation_by_id(id)



Return detailed information on a staking position, including the staked amount, rewards, status and more.

### Example


```python
from fireblocks.models.delegation_dto import DelegationDto
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
    id = 'id_example' # str | The unique identifier of the staking position

    try:
        # 
        api_response = fireblocks.staking_beta.get_delegation_by_id(id).result()
        print("The response of StakingBetaApi->get_delegation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->get_delegation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the staking position | 

### Return type

[**DelegationDto**](DelegationDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position data was returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> List[ProviderDto] get_providers()



Return information on all the available staking providers.

### Example


```python
from fireblocks.models.provider_dto import ProviderDto
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
        # 
        api_response = fireblocks.staking_beta.get_providers().result()
        print("The response of StakingBetaApi->get_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->get_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ProviderDto]**](ProviderDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of supported providers was returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary**
> DelegationSummaryDto get_summary()



Return a summary of all vaults, categorized by their status (active, inactive), the total amounts staked and total rewards per-chain.

### Example


```python
from fireblocks.models.delegation_summary_dto import DelegationSummaryDto
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
        # 
        api_response = fireblocks.staking_beta.get_summary().result()
        print("The response of StakingBetaApi->get_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->get_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DelegationSummaryDto**](DelegationSummaryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A summary for all vaults were returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_by_vault**
> Dict[str, DelegationSummaryDto] get_summary_by_vault()



Return a summary for each vault, categorized by their status (active, inactive), the total amounts staked and total rewards per-chain.

### Example


```python
from fireblocks.models.delegation_summary_dto import DelegationSummaryDto
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
        # 
        api_response = fireblocks.staking_beta.get_summary_by_vault().result()
        print("The response of StakingBetaApi->get_summary_by_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingBetaApi->get_summary_by_vault: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, DelegationSummaryDto]**](DelegationSummaryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A summary for each vault were returned successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

