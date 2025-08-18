# LayerZeroAdapterCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_link_id** | **str** | The token link id of the base token to deploy the adapters for | 
**delegate_address** | **str** | Address that will receive &#x60;CONTRACT_ADMIN_ROLE&#x60;. | 
**default_admin_address** | **str** | Address that will receive &#x60;DEFAULT_ADMIN_ROLE&#x60; on the adapter contract. | 
**pauser_address** | **str** | Address that will receive &#x60;PAUSER_ROLE&#x60;. | 

## Example

```python
from fireblocks.models.layer_zero_adapter_create_params import LayerZeroAdapterCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of LayerZeroAdapterCreateParams from a JSON string
layer_zero_adapter_create_params_instance = LayerZeroAdapterCreateParams.from_json(json)
# print the JSON string representation of the object
print(LayerZeroAdapterCreateParams.to_json())

# convert the object into a dict
layer_zero_adapter_create_params_dict = layer_zero_adapter_create_params_instance.to_dict()
# create an instance of LayerZeroAdapterCreateParams from a dict
layer_zero_adapter_create_params_from_dict = LayerZeroAdapterCreateParams.from_dict(layer_zero_adapter_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


