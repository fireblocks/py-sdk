# LeanContractDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the contract template | 
**name** | **str** | The name of the contract template | 
**description** | **str** | A short description of the contract template | 
**attributes** | [**ContractAttributes**](ContractAttributes.md) | The attributes related to this contract template. It will be displayed in the tokenization page | [optional] 
**is_public** | **bool** | Is this a contract that is viewable by all fireblocks&#39;s users or is it visible only for this workspace | 
**can_deploy** | **bool** | True if the workspace allowed to deploy this contract, false otherwise | [optional] 
**owner** | **str** | The workspace id of the owner of this contract template. If it&#39;s a private contract, only this workspace will be allowed to deploy it | [optional] 
**vendor** | [**VendorDto**](VendorDto.md) | The details of the vendor of this contract template. Applicable only for public contract templates | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.lean_contract_dto import LeanContractDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeanContractDto from a JSON string
lean_contract_dto_instance = LeanContractDto.from_json(json)
# print the JSON string representation of the object
print LeanContractDto.to_json()

# convert the object into a dict
lean_contract_dto_dict = lean_contract_dto_instance.to_dict()
# create an instance of LeanContractDto from a dict
lean_contract_dto_form_dict = lean_contract_dto.from_dict(lean_contract_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


