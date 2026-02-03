# EthereumBlockchainData

Additional fields per blockchain for Ethereum (ETH) - can be empty or missing if not initialized or no specific data is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_compounding_validator** | **bool** | Is the validator compounding (i.e it was created with compounding validator type). | 

## Example

```python
from fireblocks.models.ethereum_blockchain_data import EthereumBlockchainData

# TODO update the JSON string below
json = "{}"
# create an instance of EthereumBlockchainData from a JSON string
ethereum_blockchain_data_instance = EthereumBlockchainData.from_json(json)
# print the JSON string representation of the object
print(EthereumBlockchainData.to_json())

# convert the object into a dict
ethereum_blockchain_data_dict = ethereum_blockchain_data_instance.to_dict()
# create an instance of EthereumBlockchainData from a dict
ethereum_blockchain_data_from_dict = EthereumBlockchainData.from_dict(ethereum_blockchain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


