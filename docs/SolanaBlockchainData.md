# SolanaBlockchainData

Additional fields per blockchain - can be empty or missing if not initialized or no additional info exists. The type depends on the chainDescriptor value. For Solana (SOL), stake account address. For Ethereum (ETH), an empty object is returned as no specific data is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stake_account_address** | **str** | The stake account address matching the stakeAccountId. | 
**stake_account_derivation_change_value** | **float** | The value of the change level in the BIP32 path which was used to derive the stake account address | 

## Example

```python
from fireblocks.models.solana_blockchain_data import SolanaBlockchainData

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaBlockchainData from a JSON string
solana_blockchain_data_instance = SolanaBlockchainData.from_json(json)
# print the JSON string representation of the object
print(SolanaBlockchainData.to_json())

# convert the object into a dict
solana_blockchain_data_dict = solana_blockchain_data_instance.to_dict()
# create an instance of SolanaBlockchainData from a dict
solana_blockchain_data_from_dict = SolanaBlockchainData.from_dict(solana_blockchain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


