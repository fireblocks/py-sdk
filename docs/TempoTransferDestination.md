# TempoTransferDestination

The transfer's destination. Mutually exclusive with `destinations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The kind of destination. | 
**id** | **str** | Required when type is VAULT_ACCOUNT or UNMANAGED_WALLET. | [optional] 
**one_time_address** | [**OneTimeAddress**](OneTimeAddress.md) |  | [optional] 

## Example

```python
from fireblocks.models.tempo_transfer_destination import TempoTransferDestination

# TODO update the JSON string below
json = "{}"
# create an instance of TempoTransferDestination from a JSON string
tempo_transfer_destination_instance = TempoTransferDestination.from_json(json)
# print the JSON string representation of the object
print(TempoTransferDestination.to_json())

# convert the object into a dict
tempo_transfer_destination_dict = tempo_transfer_destination_instance.to_dict()
# create an instance of TempoTransferDestination from a dict
tempo_transfer_destination_from_dict = TempoTransferDestination.from_dict(tempo_transfer_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


