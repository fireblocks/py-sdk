# ContractMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deployed contract ID | 
**blockchain_id** | **str** | The blockchain ID | 
**contract_address** | **str** | The address of the token contract | 
**contract_template_id** | **str** | The contract template ID | 
**vault_account_id** | **str** | The vault account ID that initiated the request to issue the token | [optional] 

## Example

```python
from fireblocks_client.models.contract_metadata_dto import ContractMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of ContractMetadataDto from a JSON string
contract_metadata_dto_instance = ContractMetadataDto.from_json(json)
# print the JSON string representation of the object
print ContractMetadataDto.to_json()

# convert the object into a dict
contract_metadata_dto_dict = contract_metadata_dto_instance.to_dict()
# create an instance of ContractMetadataDto from a dict
contract_metadata_dto_form_dict = contract_metadata_dto.from_dict(contract_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


