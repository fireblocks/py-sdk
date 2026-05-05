# CounterpartyGroup

A counterparty group used to classify counterparties for compliance and routing purposes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Unique identifier of the counterparty group | 
**name** | **str** | Human-readable name of the group | 
**description** | **str** | Optional description of the group | [optional] 
**jurisdiction_codes** | **List[str]** | List of jurisdiction codes associated with the group | [optional] 
**is_active** | **bool** | Whether the counterparty group is currently active | 
**created_at** | **datetime** | ISO 8601 timestamp when the group was created | 
**updated_at** | **datetime** | ISO 8601 timestamp when the group was last updated | 

## Example

```python
from fireblocks.models.counterparty_group import CounterpartyGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CounterpartyGroup from a JSON string
counterparty_group_instance = CounterpartyGroup.from_json(json)
# print the JSON string representation of the object
print(CounterpartyGroup.to_json())

# convert the object into a dict
counterparty_group_dict = counterparty_group_instance.to_dict()
# create an instance of CounterpartyGroup from a dict
counterparty_group_from_dict = CounterpartyGroup.from_dict(counterparty_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


