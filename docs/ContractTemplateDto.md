# ContractTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the contract template | 
**name** | **str** | The name of the contract template | 
**description** | **str** | A short description of the contract template | 
**long_description** | **str** | A full description of the contract template. May contain   to break the lines | [optional] 
**abi** | **List[List[AbiFunction]]** |  | 
**attributes** | [**ContractAttributes**](ContractAttributes.md) | The attributes related to this contract template. It will be displayed in the tokenization page | [optional] 
**docs** | [**ContractDoc**](ContractDoc.md) | A &#x60;natspec&#x60; compliant documentation json. Can be retrieved from the output json after compilation | [optional] 
**owner** | **str** | The workspace id of the owner of this contract template. If it&#39;s a private contract, only this workspace will be allowed to deploy it | [optional] 
**vendor** | [**VendorDto**](VendorDto.md) | The details of the vendor of this contract template. Applicable only for public contract templates | [optional] 
**is_public** | **bool** | Is this a contract that is viewable by all fireblocks&#39;s users or is it visible only for this workspace | 
**can_deploy** | **bool** | True if the workspace allowed to deploy this contract, false otherwise | [optional] 
**type** | **str** | The type of the contract template | [optional] 
**implementation_contract_id** | **str** |  | [optional] 
**initialization_phase** | **str** |  | 

## Example

```python
from fireblocks_client.models.contract_template_dto import ContractTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractTemplateDto from a JSON string
contract_template_dto_instance = ContractTemplateDto.from_json(json)
# print the JSON string representation of the object
print ContractTemplateDto.to_json()

# convert the object into a dict
contract_template_dto_dict = contract_template_dto_instance.to_dict()
# create an instance of ContractTemplateDto from a dict
contract_template_dto_form_dict = contract_template_dto.from_dict(contract_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


