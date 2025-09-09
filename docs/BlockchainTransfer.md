# BlockchainTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**tx_hash** | **str** | The hash of the transaction on the blockchain. | [optional] 
**amount** | **str** | The amount of the transaction. | 

## Example

```python
from fireblocks.models.blockchain_transfer import BlockchainTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainTransfer from a JSON string
blockchain_transfer_instance = BlockchainTransfer.from_json(json)
# print the JSON string representation of the object
print(BlockchainTransfer.to_json())

# convert the object into a dict
blockchain_transfer_dict = blockchain_transfer_instance.to_dict()
# create an instance of BlockchainTransfer from a dict
blockchain_transfer_from_dict = BlockchainTransfer.from_dict(blockchain_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


