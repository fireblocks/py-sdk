# CreateBlockchainRequest

Create blockchain request. tenant_id is derived from the JWT token context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**declared_properties** | [**BlockchainDeclaredProperties**](BlockchainDeclaredProperties.md) |  | 

## Example

```python
from fireblocks.models.create_blockchain_request import CreateBlockchainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlockchainRequest from a JSON string
create_blockchain_request_instance = CreateBlockchainRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBlockchainRequest.to_json())

# convert the object into a dict
create_blockchain_request_dict = create_blockchain_request_instance.to_dict()
# create an instance of CreateBlockchainRequest from a dict
create_blockchain_request_from_dict = CreateBlockchainRequest.from_dict(create_blockchain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


