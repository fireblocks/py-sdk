# TransferReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**tx_hash** | **str** | The hash of the transaction on the blockchain. | [optional] 
**amount** | **str** | The amount of the fiat transfer. | 
**reference_id** | **str** | The reference ID for the fiat transfer. | [optional] 

## Example

```python
from fireblocks.models.transfer_receipt import TransferReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of TransferReceipt from a JSON string
transfer_receipt_instance = TransferReceipt.from_json(json)
# print the JSON string representation of the object
print(TransferReceipt.to_json())

# convert the object into a dict
transfer_receipt_dict = transfer_receipt_instance.to_dict()
# create an instance of TransferReceipt from a dict
transfer_receipt_from_dict = TransferReceipt.from_dict(transfer_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


