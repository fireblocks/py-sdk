# ActivateBlockchainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable result message. | 

## Example

```python
from fireblocks.models.activate_blockchain_response import ActivateBlockchainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateBlockchainResponse from a JSON string
activate_blockchain_response_instance = ActivateBlockchainResponse.from_json(json)
# print the JSON string representation of the object
print(ActivateBlockchainResponse.to_json())

# convert the object into a dict
activate_blockchain_response_dict = activate_blockchain_response_instance.to_dict()
# create an instance of ActivateBlockchainResponse from a dict
activate_blockchain_response_from_dict = ActivateBlockchainResponse.from_dict(activate_blockchain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


