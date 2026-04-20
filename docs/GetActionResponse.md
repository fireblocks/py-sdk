# GetActionResponse

Single lending action (intent plus per-step execution rows).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Action sequence id (UUID). | 
**status** | **str** | Intent status (e.g. CREATED, IN_PROGRESS, COMPLETED). | 
**provider_id** | **str** | Lending protocol identifier. | 
**action_type** | **str** | Whether this action is a deposit or withdraw flow. | 
**opportunity_id** | **str** | Target lending opportunity identifier. | 
**position_id** | **str** | Position id in the system when applicable. | [optional] 
**amount** | **str** | Human-readable amount for the action. | 
**created_at** | **str** | Creation time (ISO-8601). | 
**updated_at** | **str** | Last update time (ISO-8601). | 
**records** | [**List[ActionRecord]**](ActionRecord.md) | Ordered execution steps for this action. | 

## Example

```python
from fireblocks.models.get_action_response import GetActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionResponse from a JSON string
get_action_response_instance = GetActionResponse.from_json(json)
# print the JSON string representation of the object
print(GetActionResponse.to_json())

# convert the object into a dict
get_action_response_dict = get_action_response_instance.to_dict()
# create an instance of GetActionResponse from a dict
get_action_response_from_dict = GetActionResponse.from_dict(get_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


