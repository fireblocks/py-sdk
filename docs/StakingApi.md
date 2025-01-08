# fireblocks.StakingApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_terms_of_service_by_provider_id**](StakingApi.md#approve_terms_of_service_by_provider_id) | **POST** /staking/providers/{providerId}/approveTermsOfService | Approve staking terms of service
[**claim_rewards**](StakingApi.md#claim_rewards) | **POST** /staking/chains/{chainDescriptor}/claim_rewards | Execute a Claim Rewards operation
[**get_all_delegations**](StakingApi.md#get_all_delegations) | **GET** /staking/positions | List staking positions details
[**get_chain_info**](StakingApi.md#get_chain_info) | **GET** /staking/chains/{chainDescriptor}/chainInfo | Get chain-specific staking summary
[**get_chains**](StakingApi.md#get_chains) | **GET** /staking/chains | List staking supported chains
[**get_delegation_by_id**](StakingApi.md#get_delegation_by_id) | **GET** /staking/positions/{id} | Get staking position details
[**get_providers**](StakingApi.md#get_providers) | **GET** /staking/providers | List staking providers details
[**get_summary**](StakingApi.md#get_summary) | **GET** /staking/positions/summary | Get staking summary details
[**get_summary_by_vault**](StakingApi.md#get_summary_by_vault) | **GET** /staking/positions/summary/vaults | Get staking summary details by vault
[**split**](StakingApi.md#split) | **POST** /staking/chains/{chainDescriptor}/split | Execute a Split operation on SOL/SOL_TEST stake account
[**stake**](StakingApi.md#stake) | **POST** /staking/chains/{chainDescriptor}/stake | Initiate Stake Operation
[**unstake**](StakingApi.md#unstake) | **POST** /staking/chains/{chainDescriptor}/unstake | Execute an Unstake operation
[**withdraw**](StakingApi.md#withdraw) | **POST** /staking/chains/{chainDescriptor}/withdraw | Execute a Withdraw operation


# **approve_terms_of_service_by_provider_id**
> approve_terms_of_service_by_provider_id(provider_id, idempotency_key=idempotency_key)

Approve staking terms of service

Approve the terms of service of the staking provider. This must be called before performing a staking action for the first time with this provider.

### Example


```python
from fireblocks.models.staking_provider import StakingProvider
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
    provider_id = fireblocks.StakingProvider() # StakingProvider | The unique identifier of the staking provider
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Approve staking terms of service
        fireblocks.staking.approve_terms_of_service_by_provider_id(provider_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->approve_terms_of_service_by_provider_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | [**StakingProvider**](.md)| The unique identifier of the staking provider | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**201** | The terms of service have been successfully approved and is associated with 201 status code. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_rewards**
> claim_rewards(chain_descriptor, claim_rewards_request, idempotency_key=idempotency_key)

Execute a Claim Rewards operation

Perform a chain-specific Claim Rewards.

### Example


```python
from fireblocks.models.claim_rewards_request import ClaimRewardsRequest
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
    chain_descriptor = 'MATIC' # str | The protocol identifier (e.g. \"MATIC\"/\"SOL\") to use
    claim_rewards_request = fireblocks.ClaimRewardsRequest() # ClaimRewardsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Execute a Claim Rewards operation
        fireblocks.staking.claim_rewards(chain_descriptor, claim_rewards_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->claim_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| The protocol identifier (e.g. \&quot;MATIC\&quot;/\&quot;SOL\&quot;) to use | 
 **claim_rewards_request** | [**ClaimRewardsRequest**](ClaimRewardsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**201** | Claim Rewards action has been executed successfully on vault and is associated with 201 status code. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_delegations**
> List[Delegation] get_all_delegations(chain_descriptor=chain_descriptor)

List staking positions details

Return detailed information on all staking positions, including the staked amount, rewards, status and more.

### Example


```python
from fireblocks.models.chain_descriptor import ChainDescriptor
from fireblocks.models.delegation import Delegation
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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | Use \"ETH\" / \"SOL\" / \"MATIC\" / \"STETH_ETH\" in order to obtain information related to the specific blockchain network or retrieve information about all chains that have data available by providing no argument. (optional)

    try:
        # List staking positions details
        api_response = fireblocks.staking.get_all_delegations(chain_descriptor=chain_descriptor).result()
        print("The response of StakingApi->get_all_delegations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_all_delegations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| Use \&quot;ETH\&quot; / \&quot;SOL\&quot; / \&quot;MATIC\&quot; / \&quot;STETH_ETH\&quot; in order to obtain information related to the specific blockchain network or retrieve information about all chains that have data available by providing no argument. | [optional] 

### Return type

[**List[Delegation]**](Delegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of position data was returned successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chain_info**
> ChainInfoResponse get_chain_info(chain_descriptor)

Get chain-specific staking summary

Return chain-specific, staking-related information summary (e.g. epoch details, lockup durations, estimated rewards, etc.)

### Example


```python
from fireblocks.models.chain_descriptor import ChainDescriptor
from fireblocks.models.chain_info_response import ChainInfoResponse
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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | The protocol identifier (e.g. \"ETH\"/\"SOL\"/\"MATIC\"/\"STETH_ETH\") to use

    try:
        # Get chain-specific staking summary
        api_response = fireblocks.staking.get_chain_info(chain_descriptor).result()
        print("The response of StakingApi->get_chain_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_chain_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;/\&quot;MATIC\&quot;/\&quot;STETH_ETH\&quot;) to use | 

### Return type

[**ChainInfoResponse**](ChainInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chain specific info summary was returned successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chains**
> List[ChainDescriptor] get_chains()

List staking supported chains

Return an alphabetical list of supported chains.

### Example


```python
from fireblocks.models.chain_descriptor import ChainDescriptor
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
        # List staking supported chains
        api_response = fireblocks.staking.get_chains().result()
        print("The response of StakingApi->get_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_chains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChainDescriptor]**](ChainDescriptor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of supported chains was returned successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegation_by_id**
> Delegation get_delegation_by_id(id)

Get staking position details

Return detailed information on a staking position, including the staked amount, rewards, status and more.

### Example


```python
from fireblocks.models.delegation import Delegation
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
    id = '1fe3b61f-7e1f-4a19-aff0-4f0a524d44d7' # str | The unique identifier of the staking position

    try:
        # Get staking position details
        api_response = fireblocks.staking.get_delegation_by_id(id).result()
        print("The response of StakingApi->get_delegation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_delegation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the staking position | 

### Return type

[**Delegation**](Delegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position data was returned successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> List[Provider] get_providers()

List staking providers details

Return information on all the available staking providers.

### Example


```python
from fireblocks.models.provider import Provider
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
        # List staking providers details
        api_response = fireblocks.staking.get_providers().result()
        print("The response of StakingApi->get_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of supported providers was returned successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary**
> DelegationSummary get_summary()

Get staking summary details

Return a summary of all vaults, categorized by their status (active, inactive), the total amounts staked and total rewards per-chain.

### Example


```python
from fireblocks.models.delegation_summary import DelegationSummary
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
        # Get staking summary details
        api_response = fireblocks.staking.get_summary().result()
        print("The response of StakingApi->get_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DelegationSummary**](DelegationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A summary for all vaults were returned successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_by_vault**
> Dict[str, DelegationSummary] get_summary_by_vault()

Get staking summary details by vault

Return a summary for each vault, categorized by their status (active, inactive), the total amounts staked and total rewards per-chain.

### Example


```python
from fireblocks.models.delegation_summary import DelegationSummary
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
        # Get staking summary details by vault
        api_response = fireblocks.staking.get_summary_by_vault().result()
        print("The response of StakingApi->get_summary_by_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_summary_by_vault: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dict[str, DelegationSummary]**](DelegationSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A summary for each vault were returned successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split**
> SplitResponse split(chain_descriptor, split_request, idempotency_key=idempotency_key)

Execute a Split operation on SOL/SOL_TEST stake account

Perform a Solana Split stake account.

### Example


```python
from fireblocks.models.split_request import SplitRequest
from fireblocks.models.split_response import SplitResponse
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
    chain_descriptor = 'SOL' # str | The protocol identifier (e.g. \"SOL\"/\"SOL_TEST\") to use
    split_request = fireblocks.SplitRequest() # SplitRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Execute a Split operation on SOL/SOL_TEST stake account
        api_response = fireblocks.staking.split(chain_descriptor, split_request, idempotency_key=idempotency_key).result()
        print("The response of StakingApi->split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->split: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| The protocol identifier (e.g. \&quot;SOL\&quot;/\&quot;SOL_TEST\&quot;) to use | 
 **split_request** | [**SplitRequest**](SplitRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SplitResponse**](SplitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Split action has been executed successfully on vault and is associated with 201 status code. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stake**
> StakeResponse stake(chain_descriptor, stake_request, idempotency_key=idempotency_key)

Initiate Stake Operation

Perform a chain-specific Stake.

### Example


```python
from fireblocks.models.chain_descriptor import ChainDescriptor
from fireblocks.models.stake_request import StakeRequest
from fireblocks.models.stake_response import StakeResponse
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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | The protocol identifier (e.g. \"ETH\"/\"SOL\"/\"MATIC\") to use
    stake_request = fireblocks.StakeRequest() # StakeRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Initiate Stake Operation
        api_response = fireblocks.staking.stake(chain_descriptor, stake_request, idempotency_key=idempotency_key).result()
        print("The response of StakingApi->stake:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->stake: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;/\&quot;MATIC\&quot;) to use | 
 **stake_request** | [**StakeRequest**](StakeRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**StakeResponse**](StakeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Stake action has been executed successfully on vault and is associated with 201 status code. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unstake**
> unstake(chain_descriptor, unstake_request, idempotency_key=idempotency_key)

Execute an Unstake operation

Execute an Unstake operation

### Example


```python
from fireblocks.models.chain_descriptor import ChainDescriptor
from fireblocks.models.unstake_request import UnstakeRequest
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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | The protocol identifier (e.g. \"ETH\"/\"SOL\"/\"MATIC\") to use
    unstake_request = fireblocks.UnstakeRequest() # UnstakeRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Execute an Unstake operation
        fireblocks.staking.unstake(chain_descriptor, unstake_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->unstake: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;/\&quot;MATIC\&quot;) to use | 
 **unstake_request** | [**UnstakeRequest**](UnstakeRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**201** | Unstake action has been executed successfully on vault and is associated with 201 status code. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw**
> withdraw(chain_descriptor, withdraw_request, idempotency_key=idempotency_key)

Execute a Withdraw operation

Perform a chain-specific Withdraw.

### Example


```python
from fireblocks.models.chain_descriptor import ChainDescriptor
from fireblocks.models.withdraw_request import WithdrawRequest
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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | The protocol identifier (e.g. \"ETH\"/\"SOL\"/\"MATIC\") to use
    withdraw_request = fireblocks.WithdrawRequest() # WithdrawRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Execute a Withdraw operation
        fireblocks.staking.withdraw(chain_descriptor, withdraw_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;/\&quot;MATIC\&quot;) to use | 
 **withdraw_request** | [**WithdrawRequest**](WithdrawRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**201** | Withdraw action has been executed successfully on vault and is associated with 201 status code. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

