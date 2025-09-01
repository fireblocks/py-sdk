# DerivationPathConfig

Derivation path configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[float]** | Derivation path as array of numbers | 
**partial** | **bool** | Whether this is a partial path | [optional] 

## Example

```python
from fireblocks.models.derivation_path_config import DerivationPathConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DerivationPathConfig from a JSON string
derivation_path_config_instance = DerivationPathConfig.from_json(json)
# print the JSON string representation of the object
print(DerivationPathConfig.to_json())

# convert the object into a dict
derivation_path_config_dict = derivation_path_config_instance.to_dict()
# create an instance of DerivationPathConfig from a dict
derivation_path_config_from_dict = DerivationPathConfig.from_dict(derivation_path_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


