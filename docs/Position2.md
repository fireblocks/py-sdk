# Position2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Position UUID. | [optional] 
**status** | **str** | Lifecycle status of the position. | [optional] 
**in_flight** | **bool** | True while an action is in progress for this position. | [optional] 
**position_type** | **str** | Whether the position is lend- or borrow-side. | [optional] 
**vault_account_id** | **str** | Fireblocks vault account holding the position. | [optional] 
**opportunity_id** | **str** | Opportunity / vault or market identifier. | [optional] 
**chain_id** | **str** | Chain identifier as a string (e.g. \&quot;1\&quot;). | [optional] 
**provider_id** | **str** | Lending protocol. | [optional] 
**origin** | **str** | Whether the position was opened natively in Fireblocks or imported externally. | [optional] 
**principal_asset_id** | **str** | Fireblocks asset id for the principal (underlying) asset. | [optional] 
**position_asset_id** | **str** | Fireblocks asset id for the position / share token. | [optional] 
**principal_balance** | **str** | Human-readable principal balance. | [optional] 
**position_balance** | **str** | Human-readable position token balance. | [optional] 
**created_at** | **str** | Creation time (ISO-8601). | [optional] 
**updated_at** | **str** | Last update time (ISO-8601). | [optional] 
**last_synced_at** | **str** | Last successful on-chain sync time (ISO-8601). | [optional] 
**available_actions** | **List[str]** | Actions the API allows next for this position. | [optional] 

## Example

```python
from fireblocks.models.position2 import Position2

# TODO update the JSON string below
json = "{}"
# create an instance of Position2 from a JSON string
position2_instance = Position2.from_json(json)
# print the JSON string representation of the object
print(Position2.to_json())

# convert the object into a dict
position2_dict = position2_instance.to_dict()
# create an instance of Position2 from a dict
position2_from_dict = Position2.from_dict(position2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


