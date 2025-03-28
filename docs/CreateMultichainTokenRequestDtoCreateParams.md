# CreateMultichainTokenRequestDtoCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | The id of the contract template that will be used to create the token | 
**deploy_function_params** | [**List[ParameterWithValue]**](ParameterWithValue.md) | The deploy function parameters and values of the contract template | [optional] 

## Example

```python
from fireblocks.models.create_multichain_token_request_dto_create_params import CreateMultichainTokenRequestDtoCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultichainTokenRequestDtoCreateParams from a JSON string
create_multichain_token_request_dto_create_params_instance = CreateMultichainTokenRequestDtoCreateParams.from_json(json)
# print the JSON string representation of the object
print(CreateMultichainTokenRequestDtoCreateParams.to_json())

# convert the object into a dict
create_multichain_token_request_dto_create_params_dict = create_multichain_token_request_dto_create_params_instance.to_dict()
# create an instance of CreateMultichainTokenRequestDtoCreateParams from a dict
create_multichain_token_request_dto_create_params_from_dict = CreateMultichainTokenRequestDtoCreateParams.from_dict(create_multichain_token_request_dto_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


