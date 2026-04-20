# ActionRecord

One row in the lending action execution sequence.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Kind of step in the lending sequence. | 
**status** | **str** | Step lifecycle status. | 
**tx_id** | **str** | Fireblocks transaction id when applicable (unset when NOT_STARTED). | [optional] 
**tx_hash** | **str** | On-chain transaction hash when applicable (unset when NOT_STARTED). | [optional] 
**error_message** | **str** | Error detail when the step failed. | [optional] 
**updated_at** | **str** | Last update time (ISO-8601); may be empty when status is NOT_STARTED. | 

## Example

```python
from fireblocks.models.action_record import ActionRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRecord from a JSON string
action_record_instance = ActionRecord.from_json(json)
# print the JSON string representation of the object
print(ActionRecord.to_json())

# convert the object into a dict
action_record_dict = action_record_instance.to_dict()
# create an instance of ActionRecord from a dict
action_record_from_dict = ActionRecord.from_dict(action_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


