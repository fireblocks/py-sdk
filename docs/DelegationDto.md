# DelegationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the staking position | 
**vault_account_id** | **str** | The source vault account to stake from | 
**validator_name** | **str** | The destination validator address name | 
**provider_name** | **str** | The destination validator provider name | 
**chain_descriptor** | **str** | The protocol identifier (e.g. \&quot;ETH\&quot;/ \&quot;SOL\&quot;) to use | 
**amount** | **str** | Amount of tokens to stake, measured in the staked asset unit. | 
**rewards_amount** | **str** | The amount staked in the position, measured in the staked asset unit. | 
**date_created** | **str** | When was the request made (ISO Date). | 
**status** | **str** | The current status. | 
**related_transactions** | [**List[RelatedTransactionDto]**](RelatedTransactionDto.md) | An array of transaction objects related to this position. Each object includes a &#39;txId&#39; representing the transaction ID and a &#39;completed&#39; boolean indicating if the transaction was completed. | 
**validator_address** | **str** | The destination address of the staking transaction. | 
**provider_id** | **str** | The unique identifier of the staking provider | 
**available_actions** | **List[str]** | An array of available actions that can be performed. for example, actions like \&quot;unstake\&quot; or \&quot;withdraw\&quot;. | 
**in_progress** | **bool** | Indicates whether there is an ongoing action for this position (true if ongoing, false if not). | 
**in_progress_tx_id** | **str** | The transaction ID of the ongoing request | [optional] 
**blockchain_position_info** | [**SolanaBlockchainDataDto**](SolanaBlockchainDataDto.md) | Additional fields per blockchain - can be empty or missing if not initialized or no additional info exists. The type depends on the chainDescriptor value. For Solana (SOL), stake account address. For Ethereum (ETH), an empty object is returned as no specific data is available. | 

## Example

```python
from fireblocks_client.models.delegation_dto import DelegationDto

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationDto from a JSON string
delegation_dto_instance = DelegationDto.from_json(json)
# print the JSON string representation of the object
print(DelegationDto.to_json())

# convert the object into a dict
delegation_dto_dict = delegation_dto_instance.to_dict()
# create an instance of DelegationDto from a dict
delegation_dto_from_dict = DelegationDto.from_dict(delegation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


