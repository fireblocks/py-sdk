# fireblocks.StakingApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_terms_of_service_by_provider_id**](StakingApi.md#approve_terms_of_service_by_provider_id) | **POST** /staking/providers/{providerId}/approveTermsOfService | Approve provider terms of service
[**claim_rewards**](StakingApi.md#claim_rewards) | **POST** /staking/chains/{chainDescriptor}/claim_rewards | Claim accrued rewards
[**consolidate**](StakingApi.md#consolidate) | **POST** /staking/chains/{chainDescriptor}/consolidate | Consolidate staking positions (ETH validator consolidation)
[**get_all_delegations**](StakingApi.md#get_all_delegations) | **GET** /staking/positions | List staking positions
[**get_chain_info**](StakingApi.md#get_chain_info) | **GET** /staking/chains/{chainDescriptor}/chainInfo | Get chain-level staking parameters
[**get_chains**](StakingApi.md#get_chains) | **GET** /staking/chains | List supported staking chains
[**get_delegation_by_id**](StakingApi.md#get_delegation_by_id) | **GET** /staking/positions/{id} | Get position details
[**get_providers**](StakingApi.md#get_providers) | **GET** /staking/providers | List staking providers
[**get_summary**](StakingApi.md#get_summary) | **GET** /staking/positions/summary | Get positions summary
[**get_summary_by_vault**](StakingApi.md#get_summary_by_vault) | **GET** /staking/positions/summary/vaults | Get positions summary by vault
[**merge_stake_accounts**](StakingApi.md#merge_stake_accounts) | **POST** /staking/chains/{chainDescriptor}/merge | Merge staking positions
[**split**](StakingApi.md#split) | **POST** /staking/chains/{chainDescriptor}/split | Split a staking position
[**stake**](StakingApi.md#stake) | **POST** /staking/chains/{chainDescriptor}/stake | Initiate or add to existing stake
[**unstake**](StakingApi.md#unstake) | **POST** /staking/chains/{chainDescriptor}/unstake | Initiate unstake
[**withdraw**](StakingApi.md#withdraw) | **POST** /staking/chains/{chainDescriptor}/withdraw | Withdraw staked funds


# **approve_terms_of_service_by_provider_id**
> approve_terms_of_service_by_provider_id(provider_id, idempotency_key=idempotency_key)

Approve provider terms of service

Approves the provider's terms of service. Must be called once before performing any staking operation with this provider.

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
    provider_id = fireblocks.StakingProvider() # StakingProvider | Unique identifier of the staking provider.
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Approve provider terms of service
        fireblocks.staking.approve_terms_of_service_by_provider_id(provider_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->approve_terms_of_service_by_provider_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | [**StakingProvider**](.md)| Unique identifier of the staking provider. | 
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
**201** | Terms of service accepted. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_rewards**
> claim_rewards(chain_descriptor, claim_rewards_request, idempotency_key=idempotency_key)

Claim accrued rewards

Claims available staking rewards for the specified chain and vault. Supported chains: Solana and Polygon (Matic). Behavior depends on protocol reward distribution.

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
    chain_descriptor = 'SOL' # str | Protocol identifier for the claim rewards staking operation (e.g., MATIC/SOL).
    claim_rewards_request = fireblocks.ClaimRewardsRequest() # ClaimRewardsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Claim accrued rewards
        fireblocks.staking.claim_rewards(chain_descriptor, claim_rewards_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->claim_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| Protocol identifier for the claim rewards staking operation (e.g., MATIC/SOL). | 
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
**201** | Claim-rewards request accepted and created. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consolidate**
> MergeStakeAccountsResponse consolidate(chain_descriptor, merge_stake_accounts_request, idempotency_key=idempotency_key)

Consolidate staking positions (ETH validator consolidation)

Consolidates the source staking position into the destination, merging the balance into the destination and closing the source position once complete. Both positions must be from the same validator provider and same vault account. On chain, this translates into a consolidation transaction, where the source validator is consolidated into the destination validator. Supported chains: Ethereum (ETH) only.
</br>Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.merge_stake_accounts_request import MergeStakeAccountsRequest
from fireblocks.models.merge_stake_accounts_response import MergeStakeAccountsResponse
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
    chain_descriptor = 'ETH' # str | Protocol identifier for the staking operation (e.g., ETH).
    merge_stake_accounts_request = fireblocks.MergeStakeAccountsRequest() # MergeStakeAccountsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Consolidate staking positions (ETH validator consolidation)
        api_response = fireblocks.staking.consolidate(chain_descriptor, merge_stake_accounts_request, idempotency_key=idempotency_key).result()
        print("The response of StakingApi->consolidate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->consolidate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| Protocol identifier for the staking operation (e.g., ETH). | 
 **merge_stake_accounts_request** | [**MergeStakeAccountsRequest**](MergeStakeAccountsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**MergeStakeAccountsResponse**](MergeStakeAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Merge request accepted and created. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_delegations**
> List[Delegation] get_all_delegations(chain_descriptor=chain_descriptor)

List staking positions

Returns all staking positions with core details: amounts, rewards, status, chain, and vault.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | Protocol identifier to filter positions (e.g., ATOM_COS/AXL/CELESTIA}). If omitted, positions across all supported chains are returned. (optional)

    try:
        # List staking positions
        api_response = fireblocks.staking.get_all_delegations(chain_descriptor=chain_descriptor).result()
        print("The response of StakingApi->get_all_delegations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_all_delegations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| Protocol identifier to filter positions (e.g., ATOM_COS/AXL/CELESTIA}). If omitted, positions across all supported chains are returned. | [optional] 

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
**200** | Positions retrieved successfully. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chain_info**
> ChainInfoResponse get_chain_info(chain_descriptor)

Get chain-level staking parameters

Returns chain-specific staking information such as epoch/slot cadence, lockup or unbonding periods, fee/reward mechanics, and other operational constraints.

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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | Protocol identifier for the chain info staking operation (e.g., ETH/MATIC/SOL).

    try:
        # Get chain-level staking parameters
        api_response = fireblocks.staking.get_chain_info(chain_descriptor).result()
        print("The response of StakingApi->get_chain_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_chain_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| Protocol identifier for the chain info staking operation (e.g., ETH/MATIC/SOL). | 

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
**200** | Chain-specific staking information returned successfully. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chains**
> List[ChainDescriptor] get_chains()

List supported staking chains

Returns an alphabetical list of blockchains supported for staking by the current workspace context.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

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
        # List supported staking chains
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
**200** | An array of supported chains was returned successfully. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delegation_by_id**
> Delegation get_delegation_by_id(id)

Get position details

Returns full details for a single staking position: amounts, rewards, status, chain, and vault.

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
    id = 'id_example' # str | Unique identifier of the staking position.

    try:
        # Get position details
        api_response = fireblocks.staking.get_delegation_by_id(id).result()
        print("The response of StakingApi->get_delegation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->get_delegation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the staking position. | 

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
**200** | Position retrieved successfully. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers**
> List[Provider] get_providers()

List staking providers

Returns all available staking providers with metadata such as name, ID, and supported chains.
</br>Endpoint Permission: Admin, Non-Signing Admin, Signer, Approver, Editor.

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
        # List staking providers
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
**200** | Supported providers retrieved successfully. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary**
> DelegationSummary get_summary()

Get positions summary

Returns an aggregated cross-vault summary: active/inactive counts, total staked, and total rewards per chain.

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
        # Get positions summary
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
**200** | Summary across all vaults returned successfully. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_by_vault**
> Dict[str, DelegationSummary] get_summary_by_vault()

Get positions summary by vault

Returns per-vault aggregates: status breakdown, total staked, and total rewards per chain.

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
        # Get positions summary by vault
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
**200** | Per-vault summary returned successfully. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_stake_accounts**
> MergeStakeAccountsResponse merge_stake_accounts(chain_descriptor, merge_stake_accounts_request, idempotency_key=idempotency_key)

Merge staking positions

Merges the source stake account into the destination, consolidating the balance into the destination and closing the source account once complete. Both accounts must be from the same validator provider and of same vault account.. Supported chains: Solana (SOL).
</br>Endpoint Permission: Owner, Admin, Non-Signing Admin, Signer, Approver, Editor.

### Example


```python
from fireblocks.models.merge_stake_accounts_request import MergeStakeAccountsRequest
from fireblocks.models.merge_stake_accounts_response import MergeStakeAccountsResponse
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
    chain_descriptor = 'SOL' # str | Protocol identifier for the merge staking operation (e.g., SOL).
    merge_stake_accounts_request = fireblocks.MergeStakeAccountsRequest() # MergeStakeAccountsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Merge staking positions
        api_response = fireblocks.staking.merge_stake_accounts(chain_descriptor, merge_stake_accounts_request, idempotency_key=idempotency_key).result()
        print("The response of StakingApi->merge_stake_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->merge_stake_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| Protocol identifier for the merge staking operation (e.g., SOL). | 
 **merge_stake_accounts_request** | [**MergeStakeAccountsRequest**](MergeStakeAccountsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**MergeStakeAccountsResponse**](MergeStakeAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Merge request accepted and created. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split**
> SplitResponse split(chain_descriptor, split_request, idempotency_key=idempotency_key)

Split a staking position

Splits a staking position by creating a new stake account with the requested amount, while keeping the original account with the remaining balance. Supported chains: Solana (SOL).

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
    chain_descriptor = 'SOL' # str | Protocol identifier for the staking operation (e.g., SOL).
    split_request = fireblocks.SplitRequest() # SplitRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Split a staking position
        api_response = fireblocks.staking.split(chain_descriptor, split_request, idempotency_key=idempotency_key).result()
        print("The response of StakingApi->split:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->split: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | **str**| Protocol identifier for the staking operation (e.g., SOL). | 
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
**201** | Split request accepted and created. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stake**
> StakeResponse stake(chain_descriptor, stake_request, idempotency_key=idempotency_key)

Initiate or add to existing stake

Creates a new staking position and returns its unique ID. For Ethereum compounding validator (EIP-7251): when the 'id' of an existing compounding validator position is provided, adds to that position; otherwise creates a new position. For Ethereum legacy validator: creates a new position regardless of existing delegations. For Cosmos chains and Ethereum liquid staking (Lido): automatically add to existing positions for the same validator provider and same vault account if one exists, otherwise create a new position. For Solana and Polygon: always create new positions regardless of existing delegations.

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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | Protocol identifier for the stake staking operation (e.g., ATOM_COS/AXL/CELESTIA).
    stake_request = fireblocks.StakeRequest() # StakeRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Initiate or add to existing stake
        api_response = fireblocks.staking.stake(chain_descriptor, stake_request, idempotency_key=idempotency_key).result()
        print("The response of StakingApi->stake:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StakingApi->stake: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| Protocol identifier for the stake staking operation (e.g., ATOM_COS/AXL/CELESTIA). | 
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
**201** | Stake request accepted and created. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unstake**
> unstake(chain_descriptor, unstake_request, idempotency_key=idempotency_key)

Initiate unstake

Submits a chain-specific unstake request.

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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | Protocol identifier for the unstake staking operation (e.g., SOL/SOL_TEST/MATIC).
    unstake_request = fireblocks.UnstakeRequest() # UnstakeRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Initiate unstake
        fireblocks.staking.unstake(chain_descriptor, unstake_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->unstake: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| Protocol identifier for the unstake staking operation (e.g., SOL/SOL_TEST/MATIC). | 
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
**201** | Unstake request accepted and created. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw**
> withdraw(chain_descriptor, withdraw_request, idempotency_key=idempotency_key)

Withdraw staked funds

Withdraws funds that have completed the unbonding period. Typically requires the position to be deactivated first (unstake → unbond → withdraw). Amount and timing vary by chain protocol.

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
    chain_descriptor = fireblocks.ChainDescriptor() # ChainDescriptor | Protocol identifier for the withdraw staking operation (e.g., ATOM_COS/ETH/STETH_ETH).
    withdraw_request = fireblocks.WithdrawRequest() # WithdrawRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Withdraw staked funds
        fireblocks.staking.withdraw(chain_descriptor, withdraw_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling StakingApi->withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_descriptor** | [**ChainDescriptor**](.md)| Protocol identifier for the withdraw staking operation (e.g., ATOM_COS/ETH/STETH_ETH). | 
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
**201** | Withdraw request accepted and created. |  * X-Request-ID -  <br>  |
**400** | Bad request: missing/invalid fields, unsupported amount, or malformed payload. |  * X-Request-ID -  <br>  |
**403** | Forbidden: insufficient permissions, disabled feature, or restricted provider/validator. |  * X-Request-ID -  <br>  |
**404** | Not found: requested resource does not exist (e.g., position, validator, provider, or wallet). |  * X-Request-ID -  <br>  |
**429** | Rate limit exceeded: slow down and retry later. |  * X-Request-ID -  <br>  |
**500** | Internal error while processing the request. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

