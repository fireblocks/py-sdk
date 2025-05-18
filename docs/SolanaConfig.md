# SolanaConfig

The Solana configuration of the contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensions** | **List[str]** | The extensions that the contract implements. | [optional] 
**type** | **str** | The type of the contract. | [optional] 

## Example

```python
from fireblocks.models.solana_config import SolanaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaConfig from a JSON string
solana_config_instance = SolanaConfig.from_json(json)
# print the JSON string representation of the object
print(SolanaConfig.to_json())

# convert the object into a dict
solana_config_dict = solana_config_instance.to_dict()
# create an instance of SolanaConfig from a dict
solana_config_from_dict = SolanaConfig.from_dict(solana_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


