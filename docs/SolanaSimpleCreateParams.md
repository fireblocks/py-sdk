# SolanaSimpleCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the token or asset being created. | 
**symbol** | **str** | The symbol for the token, typically an abbreviated representation. | 
**decimals** | **int** | The number of decimal places the token supports (e.g., 9 for typical Solana tokens). | 

## Example

```python
from fireblocks.models.solana_simple_create_params import SolanaSimpleCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SolanaSimpleCreateParams from a JSON string
solana_simple_create_params_instance = SolanaSimpleCreateParams.from_json(json)
# print the JSON string representation of the object
print(SolanaSimpleCreateParams.to_json())

# convert the object into a dict
solana_simple_create_params_dict = solana_simple_create_params_instance.to_dict()
# create an instance of SolanaSimpleCreateParams from a dict
solana_simple_create_params_from_dict = SolanaSimpleCreateParams.from_dict(solana_simple_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


