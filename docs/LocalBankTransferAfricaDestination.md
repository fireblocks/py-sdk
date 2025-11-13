# LocalBankTransferAfricaDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**LocalBankTransferAfricaAddress**](LocalBankTransferAfricaAddress.md) |  | 

## Example

```python
from fireblocks.models.local_bank_transfer_africa_destination import LocalBankTransferAfricaDestination

# TODO update the JSON string below
json = "{}"
# create an instance of LocalBankTransferAfricaDestination from a JSON string
local_bank_transfer_africa_destination_instance = LocalBankTransferAfricaDestination.from_json(json)
# print the JSON string representation of the object
print(LocalBankTransferAfricaDestination.to_json())

# convert the object into a dict
local_bank_transfer_africa_destination_dict = local_bank_transfer_africa_destination_instance.to_dict()
# create an instance of LocalBankTransferAfricaDestination from a dict
local_bank_transfer_africa_destination_from_dict = LocalBankTransferAfricaDestination.from_dict(local_bank_transfer_africa_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


