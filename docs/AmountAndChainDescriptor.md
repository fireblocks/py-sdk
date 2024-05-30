# AmountAndChainDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_descriptor** | **str** | The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;) for summary | 
**amount** | **str** | Cryptocurrency quantity | 

## Example

```python
from fireblocks_client.models.amount_and_chain_descriptor import AmountAndChainDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of AmountAndChainDescriptor from a JSON string
amount_and_chain_descriptor_instance = AmountAndChainDescriptor.from_json(json)
# print the JSON string representation of the object
print(AmountAndChainDescriptor.to_json())

# convert the object into a dict
amount_and_chain_descriptor_dict = amount_and_chain_descriptor_instance.to_dict()
# create an instance of AmountAndChainDescriptor from a dict
amount_and_chain_descriptor_from_dict = AmountAndChainDescriptor.from_dict(amount_and_chain_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


