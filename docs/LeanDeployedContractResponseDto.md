# LeanDeployedContractResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deployed contract data identifier | 
**contract_address** | **str** | The contract&#39;s onchain address | 
**contract_template_id** | **str** | The contract template identifier | 
**blockchain_id** | **str** |  | 

## Example

```python
from fireblocks.models.lean_deployed_contract_response_dto import LeanDeployedContractResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of LeanDeployedContractResponseDto from a JSON string
lean_deployed_contract_response_dto_instance = LeanDeployedContractResponseDto.from_json(json)
# print the JSON string representation of the object
print(LeanDeployedContractResponseDto.to_json())

# convert the object into a dict
lean_deployed_contract_response_dto_dict = lean_deployed_contract_response_dto_instance.to_dict()
# create an instance of LeanDeployedContractResponseDto from a dict
lean_deployed_contract_response_dto_from_dict = LeanDeployedContractResponseDto.from_dict(lean_deployed_contract_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


