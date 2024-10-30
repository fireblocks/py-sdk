# EVMTokenCreateParamsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | The id of the contract template that will be used to create the token | 
**deploy_function_params** | [**List[ParameterWithValue]**](ParameterWithValue.md) | The deploy function parameters and values of the contract template | [optional] 

## Example

```python
from fireblocks.models.evm_token_create_params_dto import EVMTokenCreateParamsDto

# TODO update the JSON string below
json = "{}"
# create an instance of EVMTokenCreateParamsDto from a JSON string
evm_token_create_params_dto_instance = EVMTokenCreateParamsDto.from_json(json)
# print the JSON string representation of the object
print(EVMTokenCreateParamsDto.to_json())

# convert the object into a dict
evm_token_create_params_dto_dict = evm_token_create_params_dto_instance.to_dict()
# create an instance of EVMTokenCreateParamsDto from a dict
evm_token_create_params_dto_from_dict = EVMTokenCreateParamsDto.from_dict(evm_token_create_params_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


