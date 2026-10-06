# TempoTransferSource

The transfer's source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The kind of source. | 
**id** | **str** | Required when type is VAULT_ACCOUNT — the vault account ID. | [optional] 
**wallet_id** | **str** | Required when type is EMBEDDED_WALLET. | [optional] 

## Example

```python
from fireblocks.models.tempo_transfer_source import TempoTransferSource

# TODO update the JSON string below
json = "{}"
# create an instance of TempoTransferSource from a JSON string
tempo_transfer_source_instance = TempoTransferSource.from_json(json)
# print the JSON string representation of the object
print(TempoTransferSource.to_json())

# convert the object into a dict
tempo_transfer_source_dict = tempo_transfer_source_instance.to_dict()
# create an instance of TempoTransferSource from a dict
tempo_transfer_source_from_dict = TempoTransferSource.from_dict(tempo_transfer_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


