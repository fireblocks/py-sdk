# BlockchainRpcAuth

Discriminated RPC auth payload. Sent on create/update so backend can distinguish \"no auth\" from \"field unchanged\" on PUT updates. Credential values are stored inside declaredProperties and fetched at activation time; they are deliberately not carried through workflow context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Authentication scheme used when calling the RPC endpoint. | 
**username** | **str** | Username for RPC_AUTH_BASIC authentication. | [optional] 
**password** | **str** | Password for RPC_AUTH_BASIC authentication. | [optional] 
**token** | **str** | Bearer token for RPC_AUTH_BEARER authentication. | [optional] 
**header_name** | **str** | Header name for RPC_AUTH_CUSTOM_HEADER authentication. | [optional] 
**header_value** | **str** | Header value for RPC_AUTH_CUSTOM_HEADER authentication. | [optional] 

## Example

```python
from fireblocks.models.blockchain_rpc_auth import BlockchainRpcAuth

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainRpcAuth from a JSON string
blockchain_rpc_auth_instance = BlockchainRpcAuth.from_json(json)
# print the JSON string representation of the object
print(BlockchainRpcAuth.to_json())

# convert the object into a dict
blockchain_rpc_auth_dict = blockchain_rpc_auth_instance.to_dict()
# create an instance of BlockchainRpcAuth from a dict
blockchain_rpc_auth_from_dict = BlockchainRpcAuth.from_dict(blockchain_rpc_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


