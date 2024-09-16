# RescanTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_hash** | **str** | Blockchain TX hash | [optional] 
**asset_id** | **str** | Asset symbol BTC,ETH) | [optional] 

## Example

```python
from fireblocks.models.rescan_transaction import RescanTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of RescanTransaction from a JSON string
rescan_transaction_instance = RescanTransaction.from_json(json)
# print the JSON string representation of the object
print(RescanTransaction.to_json())

# convert the object into a dict
rescan_transaction_dict = rescan_transaction_instance.to_dict()
# create an instance of RescanTransaction from a dict
rescan_transaction_from_dict = RescanTransaction.from_dict(rescan_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


