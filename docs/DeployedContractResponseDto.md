# DeployedContractResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The deployed contract data identifier | 
**contract_address** | **str** | The contract&#39;s onchain address | 
**contract_template_id** | **str** | The contract template identifier | 
**vault_account_id** | **str** | The vault account id this contract was deploy from | [optional] 
**blockchain_id** | **str** |  | 

## Example

```python
from fireblocks_client.models.deployed_contract_response_dto import DeployedContractResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeployedContractResponseDto from a JSON string
deployed_contract_response_dto_instance = DeployedContractResponseDto.from_json(json)
# print the JSON string representation of the object
print(DeployedContractResponseDto.to_json())

# convert the object into a dict
deployed_contract_response_dto_dict = deployed_contract_response_dto_instance.to_dict()
# create an instance of DeployedContractResponseDto from a dict
deployed_contract_response_dto_from_dict = DeployedContractResponseDto.from_dict(deployed_contract_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


