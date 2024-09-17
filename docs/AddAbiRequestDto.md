# AddAbiRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_address** | **str** | The address of deployed contract | 
**base_asset_id** | **str** | The blockchain base assetId | 
**abi** | [**List[AbiFunction]**](AbiFunction.md) | The ABI of the contract | 
**name** | **str** | The name of the contract | [optional] 

## Example

```python
from fireblocks.models.add_abi_request_dto import AddAbiRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AddAbiRequestDto from a JSON string
add_abi_request_dto_instance = AddAbiRequestDto.from_json(json)
# print the JSON string representation of the object
print(AddAbiRequestDto.to_json())

# convert the object into a dict
add_abi_request_dto_dict = add_abi_request_dto_instance.to_dict()
# create an instance of AddAbiRequestDto from a dict
add_abi_request_dto_from_dict = AddAbiRequestDto.from_dict(add_abi_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


