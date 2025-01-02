# BlockchainMedia


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Media URL | 
**type** | **str** | Media type | 

## Example

```python
from fireblocks.models.blockchain_media import BlockchainMedia

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainMedia from a JSON string
blockchain_media_instance = BlockchainMedia.from_json(json)
# print the JSON string representation of the object
print(BlockchainMedia.to_json())

# convert the object into a dict
blockchain_media_dict = blockchain_media_instance.to_dict()
# create an instance of BlockchainMedia from a dict
blockchain_media_from_dict = BlockchainMedia.from_dict(blockchain_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


