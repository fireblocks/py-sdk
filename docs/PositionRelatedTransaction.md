# PositionRelatedTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | The transaction ID. | 
**tx_hash** | **str** | On-chain transaction hash. Absent while the transaction is pending. | [optional] 
**staking_operation** | **str** | Staking operation type. One of APPROVE, STAKE, UNSTAKE, WITHDRAW, CLAIM_REWARDS, SPLIT, CONSOLIDATE, MERGE, TRANSFER, AUTHORIZE, ADD_TO_STAKE. Absent on legacy persisted rows. | [optional] 
**timestamp** | **datetime** | ISO timestamp when the transaction was initiated (send time). | 
**status** | **str** | Transaction outcome. | 
**amount** | **str** | Portion of position amount this transaction moved (native units). Absent on legacy rows. | [optional] 
**tx_note** | **str** | User-provided note from the transfer request. Omitted when not set. | [optional] 

## Example

```python
from fireblocks.models.position_related_transaction import PositionRelatedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PositionRelatedTransaction from a JSON string
position_related_transaction_instance = PositionRelatedTransaction.from_json(json)
# print the JSON string representation of the object
print(PositionRelatedTransaction.to_json())

# convert the object into a dict
position_related_transaction_dict = position_related_transaction_instance.to_dict()
# create an instance of PositionRelatedTransaction from a dict
position_related_transaction_from_dict = PositionRelatedTransaction.from_dict(position_related_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


