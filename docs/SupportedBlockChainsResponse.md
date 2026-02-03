# SupportedBlockChainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_all_blockchains** | **bool** | Boolean representing if all blockchains are supported | 
**supported_blockchains** | [**List[SupportedBlockchain]**](SupportedBlockchain.md) | List of supported blockchains | [optional] 

## Example

```python
from fireblocks.models.supported_block_chains_response import SupportedBlockChainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedBlockChainsResponse from a JSON string
supported_block_chains_response_instance = SupportedBlockChainsResponse.from_json(json)
# print the JSON string representation of the object
print(SupportedBlockChainsResponse.to_json())

# convert the object into a dict
supported_block_chains_response_dict = supported_block_chains_response_instance.to_dict()
# create an instance of SupportedBlockChainsResponse from a dict
supported_block_chains_response_from_dict = SupportedBlockChainsResponse.from_dict(supported_block_chains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


