# NetworkFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_per_byte** | **str** |  | [optional] 
**gas_price** | **str** |  | [optional] 
**network_fee** | **str** |  | [optional] 
**base_fee** | **str** | (optional) Base Fee according to EIP-1559 (ETH assets) | [optional] 
**priority_fee** | **str** | (optional) Priority Fee according to EIP-1559 (ETH assets) | [optional] 

## Example

```python
from fireblocks_client.models.network_fee import NetworkFee

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkFee from a JSON string
network_fee_instance = NetworkFee.from_json(json)
# print the JSON string representation of the object
print(NetworkFee.to_json())

# convert the object into a dict
network_fee_dict = network_fee_instance.to_dict()
# create an instance of NetworkFee from a dict
network_fee_from_dict = NetworkFee.from_dict(network_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


