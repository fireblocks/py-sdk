# TempoTransferDestinationItem

One destination in a multi-destination transfer. `destination.type` is narrowed the same way as the top-level `destination` field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount to transfer to this destination, as a numeric string. | [optional] 
**destination** | [**TempoTransferDestination**](TempoTransferDestination.md) |  | [optional] 
**travel_rule_message_id** | **str** | Beta. An identifier of a TravelRule message, already sent to the TravelRule provider. | [optional] 
**customer_ref_id** | **str** | The ID for AML providers to associate the owner of funds with transactions. | [optional] 

## Example

```python
from fireblocks.models.tempo_transfer_destination_item import TempoTransferDestinationItem

# TODO update the JSON string below
json = "{}"
# create an instance of TempoTransferDestinationItem from a JSON string
tempo_transfer_destination_item_instance = TempoTransferDestinationItem.from_json(json)
# print the JSON string representation of the object
print(TempoTransferDestinationItem.to_json())

# convert the object into a dict
tempo_transfer_destination_item_dict = tempo_transfer_destination_item_instance.to_dict()
# create an instance of TempoTransferDestinationItem from a dict
tempo_transfer_destination_item_from_dict = TempoTransferDestinationItem.from_dict(tempo_transfer_destination_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


