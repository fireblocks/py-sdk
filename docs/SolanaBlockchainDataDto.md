# SolanaBlockchainDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stake_account_address** | **str** | The stake account address matching the stakeAccountId. | 

## Example

```python
from fireblocks.models.solana_blockchain_data_dto import SolanaBlockchainDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaBlockchainDataDto from a JSON string
solana_blockchain_data_dto_instance = SolanaBlockchainDataDto.from_json(json)
# print the JSON string representation of the object
print(SolanaBlockchainDataDto.to_json())

# convert the object into a dict
solana_blockchain_data_dto_dict = solana_blockchain_data_dto_instance.to_dict()
# create an instance of SolanaBlockchainDataDto from a dict
solana_blockchain_data_dto_from_dict = SolanaBlockchainDataDto.from_dict(solana_blockchain_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


