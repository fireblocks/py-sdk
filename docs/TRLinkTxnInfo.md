# TRLinkTxnInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator_wallet_address** | **str** | Originator&#39;s blockchain wallet address | 
**beneficiary_wallet_address** | **str** | Beneficiary&#39;s blockchain wallet address | 
**tx_hash** | **str** | Blockchain transaction hash | 

## Example

```python
from fireblocks.models.tr_link_txn_info import TRLinkTxnInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkTxnInfo from a JSON string
tr_link_txn_info_instance = TRLinkTxnInfo.from_json(json)
# print the JSON string representation of the object
print(TRLinkTxnInfo.to_json())

# convert the object into a dict
tr_link_txn_info_dict = tr_link_txn_info_instance.to_dict()
# create an instance of TRLinkTxnInfo from a dict
tr_link_txn_info_from_dict = TRLinkTxnInfo.from_dict(tr_link_txn_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


