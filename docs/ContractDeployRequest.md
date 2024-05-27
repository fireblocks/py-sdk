# ContractDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The base asset identifier of the blockchain you want to deploy to | 
**vault_account_id** | **str** | The vault account id you wish to deploy from | 
**constructor_parameters** | [**List[ParameterWithValue]**](ParameterWithValue.md) | The constructor parameters of this contract | [optional] 

## Example

```python
from fireblocks_client.models.contract_deploy_request import ContractDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDeployRequest from a JSON string
contract_deploy_request_instance = ContractDeployRequest.from_json(json)
# print the JSON string representation of the object
print ContractDeployRequest.to_json()

# convert the object into a dict
contract_deploy_request_dict = contract_deploy_request_instance.to_dict()
# create an instance of ContractDeployRequest from a dict
contract_deploy_request_form_dict = contract_deploy_request.from_dict(contract_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


