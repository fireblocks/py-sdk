# BlockInfo

The block hash and height of the block that this transaction was mined in.      **Note**: If an outgoing transaction uses the destinations object with more than one value in the array, blockHash is set to null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_height** | **str** |  | [optional] 
**block_hash** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.block_info import BlockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BlockInfo from a JSON string
block_info_instance = BlockInfo.from_json(json)
# print the JSON string representation of the object
print(BlockInfo.to_json())

# convert the object into a dict
block_info_dict = block_info_instance.to_dict()
# create an instance of BlockInfo from a dict
block_info_from_dict = BlockInfo.from_dict(block_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


