# TriggerScreeningRequest

Request to trigger a screening against an active workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** | The workflow to screen against. Must be in &#x60;ACTIVE&#x60; status. | 
**input** | [**ScreeningInput**](ScreeningInput.md) |  | 

## Example

```python
from fireblocks.models.trigger_screening_request import TriggerScreeningRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerScreeningRequest from a JSON string
trigger_screening_request_instance = TriggerScreeningRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerScreeningRequest.to_json())

# convert the object into a dict
trigger_screening_request_dict = trigger_screening_request_instance.to_dict()
# create an instance of TriggerScreeningRequest from a dict
trigger_screening_request_from_dict = TriggerScreeningRequest.from_dict(trigger_screening_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


