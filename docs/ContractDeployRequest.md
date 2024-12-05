# ContractDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The base asset identifier of the blockchain you want to deploy to | 
**vault_account_id** | **str** | The vault account id you wish to deploy from | 
**constructor_parameters** | [**List[ParameterWithValue]**](ParameterWithValue.md) | The constructor parameters of this contract | [optional] 
**use_gasless** | **bool** | Indicates whether the token should be created in a gasless manner, utilizing the ERC-2771 standard. When set to true, the transaction will be relayed by a designated relayer. The workspace must be configured to use Fireblocks gasless relay. | [optional] 
**fee** | **str** | Max fee amount for the write function transaction. interchangeable with the &#39;feeLevel&#39; field | [optional] 
**fee_level** | **str** | Fee level for the write function transaction. interchangeable with the &#39;fee&#39; field | [optional] 

## Example

```python
from fireblocks.models.contract_deploy_request import ContractDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContractDeployRequest from a JSON string
contract_deploy_request_instance = ContractDeployRequest.from_json(json)
# print the JSON string representation of the object
print(ContractDeployRequest.to_json())

# convert the object into a dict
contract_deploy_request_dict = contract_deploy_request_instance.to_dict()
# create an instance of ContractDeployRequest from a dict
contract_deploy_request_from_dict = ContractDeployRequest.from_dict(contract_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


