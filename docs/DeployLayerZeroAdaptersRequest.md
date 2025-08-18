# DeployLayerZeroAdaptersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The id of the vault account that initiated the request to deploy adapter for the token | 
**create_params** | [**List[LayerZeroAdapterCreateParams]**](LayerZeroAdapterCreateParams.md) | Array of creation parameters for LayerZero adapters, one per tokenLink. | 
**display_name** | **str** | The display name of the contract | [optional] 
**use_gasless** | **bool** | Whether to use gasless deployment or not | [optional] 
**fee_level** | **str** | Fee level for the write function transaction. interchangeable with the &#39;fee&#39; field | [optional] 
**fee** | **str** | Max fee amount for the write function transaction. interchangeable with the &#39;feeLevel&#39; field | [optional] 
**salt** | **str** | The salt to calculate the deterministic address. Must be a number between 0 and 2^256 -1, for it to fit in the bytes32 parameter | [optional] 

## Example

```python
from fireblocks.models.deploy_layer_zero_adapters_request import DeployLayerZeroAdaptersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeployLayerZeroAdaptersRequest from a JSON string
deploy_layer_zero_adapters_request_instance = DeployLayerZeroAdaptersRequest.from_json(json)
# print the JSON string representation of the object
print(DeployLayerZeroAdaptersRequest.to_json())

# convert the object into a dict
deploy_layer_zero_adapters_request_dict = deploy_layer_zero_adapters_request_instance.to_dict()
# create an instance of DeployLayerZeroAdaptersRequest from a dict
deploy_layer_zero_adapters_request_from_dict = DeployLayerZeroAdaptersRequest.from_dict(deploy_layer_zero_adapters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


