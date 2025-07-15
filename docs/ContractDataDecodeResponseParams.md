# ContractDataDecodeResponseParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the contract function. | 
**signature** | **str** | The signature of the contract function. | 
**args** | [**List[ParameterWithValue]**](ParameterWithValue.md) |  | 

## Example

```python
from fireblocks.models.contract_data_decode_response_params import ContractDataDecodeResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDataDecodeResponseParams from a JSON string
contract_data_decode_response_params_instance = ContractDataDecodeResponseParams.from_json(json)
# print the JSON string representation of the object
print(ContractDataDecodeResponseParams.to_json())

# convert the object into a dict
contract_data_decode_response_params_dict = contract_data_decode_response_params_instance.to_dict()
# create an instance of ContractDataDecodeResponseParams from a dict
contract_data_decode_response_params_from_dict = ContractDataDecodeResponseParams.from_dict(contract_data_decode_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


