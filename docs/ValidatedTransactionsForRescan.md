# ValidatedTransactionsForRescan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset** | **str** | Base asset symbol BTC_TEST, ETH_TEST5) | [optional] 
**network_protocol** | **str** | Netowrk protocol of the blockchain (BTC, ETH) | [optional] 
**tx_hashes** | **List[str]** | Blockchain TX hashes | [optional] 

## Example

```python
from fireblocks.models.validated_transactions_for_rescan import ValidatedTransactionsForRescan

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatedTransactionsForRescan from a JSON string
validated_transactions_for_rescan_instance = ValidatedTransactionsForRescan.from_json(json)
# print the JSON string representation of the object
print(ValidatedTransactionsForRescan.to_json())

# convert the object into a dict
validated_transactions_for_rescan_dict = validated_transactions_for_rescan_instance.to_dict()
# create an instance of ValidatedTransactionsForRescan from a dict
validated_transactions_for_rescan_from_dict = ValidatedTransactionsForRescan.from_dict(validated_transactions_for_rescan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


