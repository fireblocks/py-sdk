# RemoveLayerZeroAdaptersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The vault account ID to use for signing the role revocation transactions. | 
**adapter_token_link_ids** | **List[str]** | A list of adapter token link IDs to be deactivated and unlinked. | 

## Example

```python
from fireblocks.models.remove_layer_zero_adapters_request import RemoveLayerZeroAdaptersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveLayerZeroAdaptersRequest from a JSON string
remove_layer_zero_adapters_request_instance = RemoveLayerZeroAdaptersRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveLayerZeroAdaptersRequest.to_json())

# convert the object into a dict
remove_layer_zero_adapters_request_dict = remove_layer_zero_adapters_request_instance.to_dict()
# create an instance of RemoveLayerZeroAdaptersRequest from a dict
remove_layer_zero_adapters_request_from_dict = RemoveLayerZeroAdaptersRequest.from_dict(remove_layer_zero_adapters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


