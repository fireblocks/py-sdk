# BlockchainAddress

The blockchain address information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain_address** | **str** | The blockchain address. | 
**tag** | **str** | The tag of the blockchain address. It is used to identify the address in the blockchain. It is optional. | [optional] 

## Example

```python
from fireblocks.models.blockchain_address import BlockchainAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainAddress from a JSON string
blockchain_address_instance = BlockchainAddress.from_json(json)
# print the JSON string representation of the object
print(BlockchainAddress.to_json())

# convert the object into a dict
blockchain_address_dict = blockchain_address_instance.to_dict()
# create an instance of BlockchainAddress from a dict
blockchain_address_from_dict = BlockchainAddress.from_dict(blockchain_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


