# AllocationWithdrawPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **str** | The vault account whose Canton wallet acts here. | 
**asset** | **str** | Chain asset — &#x60;CANTON&#x60; or &#x60;CANTON_TEST&#x60;. | 
**allocation_transaction_id** | **str** | The Fireblocks transaction id of the outgoing response that created the allocation. The allocation is resolved from it — Canton contract ids are never accepted here. | 

## Example

```python
from fireblocks.models.allocation_withdraw_payload import AllocationWithdrawPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AllocationWithdrawPayload from a JSON string
allocation_withdraw_payload_instance = AllocationWithdrawPayload.from_json(json)
# print the JSON string representation of the object
print(AllocationWithdrawPayload.to_json())

# convert the object into a dict
allocation_withdraw_payload_dict = allocation_withdraw_payload_instance.to_dict()
# create an instance of AllocationWithdrawPayload from a dict
allocation_withdraw_payload_from_dict = AllocationWithdrawPayload.from_dict(allocation_withdraw_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


