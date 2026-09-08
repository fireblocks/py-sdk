# TransferWithdrawPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The vault account whose Canton wallet acts here. | 
**asset** | **str** | Chain asset — &#x60;CANTON&#x60; or &#x60;CANTON_TEST&#x60;. | 
**offer_transaction_id** | **str** | The Fireblocks transaction id of the OUTGOING transfer offer being withdrawn. | 

## Example

```python
from fireblocks.models.transfer_withdraw_payload import TransferWithdrawPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TransferWithdrawPayload from a JSON string
transfer_withdraw_payload_instance = TransferWithdrawPayload.from_json(json)
# print the JSON string representation of the object
print(TransferWithdrawPayload.to_json())

# convert the object into a dict
transfer_withdraw_payload_dict = transfer_withdraw_payload_instance.to_dict()
# create an instance of TransferWithdrawPayload from a dict
transfer_withdraw_payload_from_dict = TransferWithdrawPayload.from_dict(transfer_withdraw_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


