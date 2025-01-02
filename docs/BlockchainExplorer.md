# BlockchainExplorer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | Explorer base url | 
**address** | **str** | Explorer address url | [optional] 
**tx** | **str** | Explorer transaction url | [optional] 
**token** | **str** | Explorer token url | [optional] 

## Example

```python
from fireblocks.models.blockchain_explorer import BlockchainExplorer

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainExplorer from a JSON string
blockchain_explorer_instance = BlockchainExplorer.from_json(json)
# print the JSON string representation of the object
print(BlockchainExplorer.to_json())

# convert the object into a dict
blockchain_explorer_dict = blockchain_explorer_instance.to_dict()
# create an instance of BlockchainExplorer from a dict
blockchain_explorer_from_dict = BlockchainExplorer.from_dict(blockchain_explorer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


