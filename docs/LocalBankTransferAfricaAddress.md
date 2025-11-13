# LocalBankTransferAfricaAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**account_number** | **str** |  | 
**bank_name** | **str** | Name of the bank | 
**bank_code** | **str** | Internal bank identifier | 

## Example

```python
from fireblocks.models.local_bank_transfer_africa_address import LocalBankTransferAfricaAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LocalBankTransferAfricaAddress from a JSON string
local_bank_transfer_africa_address_instance = LocalBankTransferAfricaAddress.from_json(json)
# print the JSON string representation of the object
print(LocalBankTransferAfricaAddress.to_json())

# convert the object into a dict
local_bank_transfer_africa_address_dict = local_bank_transfer_africa_address_instance.to_dict()
# create an instance of LocalBankTransferAfricaAddress from a dict
local_bank_transfer_africa_address_from_dict = LocalBankTransferAfricaAddress.from_dict(local_bank_transfer_africa_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


