# TriggerScreeningResponse

Acknowledgement that a screening was accepted and is now running.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screening_id** | **str** | Identifier of the screening that was created. Poll &#x60;GET /v1/compliance/orchestrator/screenings/{screeningId}&#x60; with it for the verdict. | 
**screening_status** | [**ComplianceScreeningStatusEnum**](ComplianceScreeningStatusEnum.md) |  | 

## Example

```python
from fireblocks.models.trigger_screening_response import TriggerScreeningResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerScreeningResponse from a JSON string
trigger_screening_response_instance = TriggerScreeningResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerScreeningResponse.to_json())

# convert the object into a dict
trigger_screening_response_dict = trigger_screening_response_instance.to_dict()
# create an instance of TriggerScreeningResponse from a dict
trigger_screening_response_from_dict = TriggerScreeningResponse.from_dict(trigger_screening_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


