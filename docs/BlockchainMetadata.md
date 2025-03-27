# BlockchainMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**AssetScope**](AssetScope.md) |  | 
**deprecated** | **bool** | Is blockchain deprecated | 
**media** | [**List[BlockchainMedia]**](BlockchainMedia.md) | Blockchain’s media | [optional] 
**explorer** | [**BlockchainExplorer**](BlockchainExplorer.md) |  | [optional] 

## Example

```python
from fireblocks.models.blockchain_metadata import BlockchainMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainMetadata from a JSON string
blockchain_metadata_instance = BlockchainMetadata.from_json(json)
# print the JSON string representation of the object
print(BlockchainMetadata.to_json())

# convert the object into a dict
blockchain_metadata_dict = blockchain_metadata_instance.to_dict()
# create an instance of BlockchainMetadata from a dict
blockchain_metadata_from_dict = BlockchainMetadata.from_dict(blockchain_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


