# CreateTokenRequestDtoCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_id** | **str** | The id of the contract template that will be used to create the token | 
**deploy_function_params** | [**List[ParameterWithValue]**](ParameterWithValue.md) | The deploy function parameters and values of the contract template | [optional] 
**symbol** | **str** | The symbol for the token, typically an abbreviated representation. | 
**name** | **str** | The name of the token or asset being created. | 
**issuer_address** | **str** | The address of the issuer of this token. Will be part of the identifier of this token on chain. | 
**decimals** | **int** | The number of decimal places the token supports (e.g., 9 for typical Solana tokens). | 

## Example

```python
from fireblocks.models.create_token_request_dto_create_params import CreateTokenRequestDtoCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTokenRequestDtoCreateParams from a JSON string
create_token_request_dto_create_params_instance = CreateTokenRequestDtoCreateParams.from_json(json)
# print the JSON string representation of the object
print(CreateTokenRequestDtoCreateParams.to_json())

# convert the object into a dict
create_token_request_dto_create_params_dict = create_token_request_dto_create_params_instance.to_dict()
# create an instance of CreateTokenRequestDtoCreateParams from a dict
create_token_request_dto_create_params_from_dict = CreateTokenRequestDtoCreateParams.from_dict(create_token_request_dto_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


