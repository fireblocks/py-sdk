# StEthBlockchainData

Additional fields per blockchain for Staked Ethereum (STETH_ETH) - can be empty or missing if not initialized or no additional info exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_withdrawable_amount** | **str** | The total amount available for withdrawal. | 
**total_inactive_amount** | **str** | The total inactive amount. | 

## Example

```python
from fireblocks.models.st_eth_blockchain_data import StEthBlockchainData

# TODO update the JSON string below
json = "{}"
# create an instance of StEthBlockchainData from a JSON string
st_eth_blockchain_data_instance = StEthBlockchainData.from_json(json)
# print the JSON string representation of the object
print(StEthBlockchainData.to_json())

# convert the object into a dict
st_eth_blockchain_data_dict = st_eth_blockchain_data_instance.to_dict()
# create an instance of StEthBlockchainData from a dict
st_eth_blockchain_data_from_dict = StEthBlockchainData.from_dict(st_eth_blockchain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


