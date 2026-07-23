# CreateBlockchainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain** | [**Blockchain**](Blockchain.md) |  | 
**message** | **str** | Human-readable result message. | 

## Example

```python
from fireblocks.models.create_blockchain_response import CreateBlockchainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlockchainResponse from a JSON string
create_blockchain_response_instance = CreateBlockchainResponse.from_json(json)
# print the JSON string representation of the object
print(CreateBlockchainResponse.to_json())

# convert the object into a dict
create_blockchain_response_dict = create_blockchain_response_instance.to_dict()
# create an instance of CreateBlockchainResponse from a dict
create_blockchain_response_from_dict = CreateBlockchainResponse.from_dict(create_blockchain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


