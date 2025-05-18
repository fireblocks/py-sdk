# ContractAbiResponseDtoAbiInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the instruction | 
**state_mutability** | **str** | The state mutability of the contract function as it appears in the ABI | [optional] 
**type** | **str** | The type of the function | 
**inputs** | [**List[Parameter]**](Parameter.md) | The parameters that this function/constructor posses | [optional] 
**outputs** | [**List[Parameter]**](Parameter.md) | The parameters that this &#39;read&#39; function returns | [optional] 
**description** | **str** | The documentation of this function (if has any) | [optional] 
**discriminator** | **List[float]** | The discriminator for the instruction. Acts as a function selector | 
**accounts** | [**List[SOLAccount]**](SOLAccount.md) |  | 
**args** | [**List[SolParameter]**](SolParameter.md) |  | 

## Example

```python
from fireblocks.models.contract_abi_response_dto_abi_inner import ContractAbiResponseDtoAbiInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContractAbiResponseDtoAbiInner from a JSON string
contract_abi_response_dto_abi_inner_instance = ContractAbiResponseDtoAbiInner.from_json(json)
# print the JSON string representation of the object
print(ContractAbiResponseDtoAbiInner.to_json())

# convert the object into a dict
contract_abi_response_dto_abi_inner_dict = contract_abi_response_dto_abi_inner_instance.to_dict()
# create an instance of ContractAbiResponseDtoAbiInner from a dict
contract_abi_response_dto_abi_inner_from_dict = ContractAbiResponseDtoAbiInner.from_dict(contract_abi_response_dto_abi_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


