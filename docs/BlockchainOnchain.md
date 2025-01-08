# BlockchainOnchain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The protocol of the blockchain | 
**chain_id** | **str** | Network/chain ID | [optional] 
**test** | **bool** | Is test blockchain | 
**signing_algo** | **str** | Signing alghorithm | 

## Example

```python
from fireblocks.models.blockchain_onchain import BlockchainOnchain

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainOnchain from a JSON string
blockchain_onchain_instance = BlockchainOnchain.from_json(json)
# print the JSON string representation of the object
print(BlockchainOnchain.to_json())

# convert the object into a dict
blockchain_onchain_dict = blockchain_onchain_instance.to_dict()
# create an instance of BlockchainOnchain from a dict
blockchain_onchain_from_dict = BlockchainOnchain.from_dict(blockchain_onchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


