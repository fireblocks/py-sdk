# SupportedBlockchain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the blockchain | 
**legacy_id** | **str** | The old blockchain ID representation of the blockchain | 
**display_name** | **str** | The name of the blockchain | 
**native_asset_id** | **str** | Native asset ID of this blockchain | 

## Example

```python
from fireblocks.models.supported_blockchain import SupportedBlockchain

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedBlockchain from a JSON string
supported_blockchain_instance = SupportedBlockchain.from_json(json)
# print the JSON string representation of the object
print(SupportedBlockchain.to_json())

# convert the object into a dict
supported_blockchain_dict = supported_blockchain_instance.to_dict()
# create an instance of SupportedBlockchain from a dict
supported_blockchain_from_dict = SupportedBlockchain.from_dict(supported_blockchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


