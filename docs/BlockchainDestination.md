# BlockchainDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of destination. Use \&quot;BLOCKCHAIN\&quot; for blockchain address destinations. | 
**address** | [**BlockchainAddress**](BlockchainAddress.md) |  | 

## Example

```python
from fireblocks.models.blockchain_destination import BlockchainDestination

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainDestination from a JSON string
blockchain_destination_instance = BlockchainDestination.from_json(json)
# print the JSON string representation of the object
print(BlockchainDestination.to_json())

# convert the object into a dict
blockchain_destination_dict = blockchain_destination_instance.to_dict()
# create an instance of BlockchainDestination from a dict
blockchain_destination_from_dict = BlockchainDestination.from_dict(blockchain_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


