# ContractAbiResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abi** | [**List[ContractAbiResponseDtoAbiInner]**](ContractAbiResponseDtoAbiInner.md) | The abi of the contract | 
**implementation_abi** | [**List[AbiFunction]**](AbiFunction.md) | The abi of the implementation contract if exists. Relevant only for proxy patterns | [optional] 

## Example

```python
from fireblocks.models.contract_abi_response_dto import ContractAbiResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAbiResponseDto from a JSON string
contract_abi_response_dto_instance = ContractAbiResponseDto.from_json(json)
# print the JSON string representation of the object
print(ContractAbiResponseDto.to_json())

# convert the object into a dict
contract_abi_response_dto_dict = contract_abi_response_dto_instance.to_dict()
# create an instance of ContractAbiResponseDto from a dict
contract_abi_response_dto_from_dict = ContractAbiResponseDto.from_dict(contract_abi_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


