# MultichainDeploymentMetadata

The multichain deployment metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the deployment metadata | [optional] 
**address** | **str** | The address of the deployed contract | [optional] 
**template_id** | **str** | The unique identifier of the contract template | [optional] 
**deployment_salt** | **str** | The salt used for the deployment | [optional] 
**init_params** | [**List[ParameterWithValue]**](ParameterWithValue.md) |  | [optional] 
**encoded_init_params** | **str** | The encoded init params | [optional] 

## Example

```python
from fireblocks.models.multichain_deployment_metadata import MultichainDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MultichainDeploymentMetadata from a JSON string
multichain_deployment_metadata_instance = MultichainDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(MultichainDeploymentMetadata.to_json())

# convert the object into a dict
multichain_deployment_metadata_dict = multichain_deployment_metadata_instance.to_dict()
# create an instance of MultichainDeploymentMetadata from a dict
multichain_deployment_metadata_from_dict = MultichainDeploymentMetadata.from_dict(multichain_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


