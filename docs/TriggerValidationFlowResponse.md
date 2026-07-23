# TriggerValidationFlowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable result message. | 

## Example

```python
from fireblocks.models.trigger_validation_flow_response import TriggerValidationFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerValidationFlowResponse from a JSON string
trigger_validation_flow_response_instance = TriggerValidationFlowResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerValidationFlowResponse.to_json())

# convert the object into a dict
trigger_validation_flow_response_dict = trigger_validation_flow_response_instance.to_dict()
# create an instance of TriggerValidationFlowResponse from a dict
trigger_validation_flow_response_from_dict = TriggerValidationFlowResponse.from_dict(trigger_validation_flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


