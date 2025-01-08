# BlockchainResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the blockchain | 
**legacy_id** | **str** | The old blockchain ID representation of the blockchain | 
**display_name** | **str** | The name of the blockchain | 
**native_asset_id** | **str** | Native asset ID of this blockchain | 
**onchain** | [**BlockchainOnchain**](BlockchainOnchain.md) |  | 
**metadata** | [**BlockchainMetadata**](BlockchainMetadata.md) |  | 

## Example

```python
from fireblocks.models.blockchain_response import BlockchainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainResponse from a JSON string
blockchain_response_instance = BlockchainResponse.from_json(json)
# print the JSON string representation of the object
print(BlockchainResponse.to_json())

# convert the object into a dict
blockchain_response_dict = blockchain_response_instance.to_dict()
# create an instance of BlockchainResponse from a dict
blockchain_response_from_dict = BlockchainResponse.from_dict(blockchain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


