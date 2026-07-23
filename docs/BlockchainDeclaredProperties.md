# BlockchainDeclaredProperties

Declared properties for blockchain configuration (create/update API and response) Only the fields sent by the API and returned in list/create/update responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_name** | **str** | Human-readable name of the blockchain. | 
**chain_id** | **float** | EVM chain ID of the blockchain. | 
**symbol_name** | **str** | Native asset symbol of the blockchain. | 
**decimals** | **float** | Number of decimals for the native asset. | [optional] 
**rpc_urls** | **List[str]** | RPC endpoint URLs for the blockchain. | 
**environment_type** | **str** | Network environment (mainnet or testnet). | 
**block_explorer_url** | **str** | Base URL of the block explorer. | [optional] 
**block_explorer_transaction_path** | **str** | Path template for a transaction on the block explorer. | [optional] 
**block_explorer_address_path** | **str** | Path template for an address on the block explorer. | [optional] 
**network_id** | **float** | EVM network ID of the blockchain. | [optional] 
**has_fee** | **bool** | Whether the blockchain charges transaction fees. | [optional] 
**is_poa** | **bool** | Whether the blockchain uses proof-of-authority consensus. | [optional] 
**has_layered_fee** | **bool** | Whether the blockchain uses a layered fee model. | [optional] 
**node_type** | **str** | Node client type for the blockchain. | [optional] 
**transaction_format** | **float** | Transaction format identifier. | [optional] 
**base_asset_tenant_ids** | **List[str]** | Tenant IDs that share this base asset. | [optional] 
**explorer_api_url** | **str** | Block explorer API base URL. | [optional] 
**explorer_api_key** | **str** | API key for the block explorer API. | [optional] 
**is_trace_enabled** | **bool** | Whether trace/debug RPC methods are enabled. | [optional] 
**rpc_auth** | [**BlockchainRpcAuth**](BlockchainRpcAuth.md) |  | [optional] 

## Example

```python
from fireblocks.models.blockchain_declared_properties import BlockchainDeclaredProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainDeclaredProperties from a JSON string
blockchain_declared_properties_instance = BlockchainDeclaredProperties.from_json(json)
# print the JSON string representation of the object
print(BlockchainDeclaredProperties.to_json())

# convert the object into a dict
blockchain_declared_properties_dict = blockchain_declared_properties_instance.to_dict()
# create an instance of BlockchainDeclaredProperties from a dict
blockchain_declared_properties_from_dict = BlockchainDeclaredProperties.from_dict(blockchain_declared_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


