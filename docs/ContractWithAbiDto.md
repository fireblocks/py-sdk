# ContractWithAbiDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | The address of the contract | 
**base_asset_id** | **str** | The blockchain base assetId | 
**name** | **str** | The name of the contract | 
**abi** | [**List[AbiFunction]**](AbiFunction.md) | The ABI of the contract | 
**is_proxy** | **bool** | Whether the contract is a proxy contract | [optional] 
**implementation** | **str** | The implementation contract address | [optional] 
**is_public** | **bool** | Whether the contract ABI is public | 

## Example

```python
from fireblocks.models.contract_with_abi_dto import ContractWithAbiDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractWithAbiDto from a JSON string
contract_with_abi_dto_instance = ContractWithAbiDto.from_json(json)
# print the JSON string representation of the object
print(ContractWithAbiDto.to_json())

# convert the object into a dict
contract_with_abi_dto_dict = contract_with_abi_dto_instance.to_dict()
# create an instance of ContractWithAbiDto from a dict
contract_with_abi_dto_from_dict = ContractWithAbiDto.from_dict(contract_with_abi_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


