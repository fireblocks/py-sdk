# UpdateBlockchainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | [**Blockchain**](Blockchain.md) |  | 
**message** | **str** | Human-readable result message. | 

## Example

```python
from fireblocks.models.update_blockchain_response import UpdateBlockchainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBlockchainResponse from a JSON string
update_blockchain_response_instance = UpdateBlockchainResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateBlockchainResponse.to_json())

# convert the object into a dict
update_blockchain_response_dict = update_blockchain_response_instance.to_dict()
# create an instance of UpdateBlockchainResponse from a dict
update_blockchain_response_from_dict = UpdateBlockchainResponse.from_dict(update_blockchain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


