# InitiatorConfigPattern


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | List of user IDs | [optional] 
**groups** | **List[str]** | List of policy group IDs | [optional] 
**services** | **List[str]** |  | [optional] 
**fb_admin_groups** | **List[str]** |  | [optional] 
**exchange** | **List[str]** |  | [optional] 
**operator** | [**PolicyOperator**](PolicyOperator.md) |  | 

## Example

```python
from fireblocks.models.initiator_config_pattern import InitiatorConfigPattern

# TODO update the JSON string below
json = "{}"
# create an instance of InitiatorConfigPattern from a JSON string
initiator_config_pattern_instance = InitiatorConfigPattern.from_json(json)
# print the JSON string representation of the object
print(InitiatorConfigPattern.to_json())

# convert the object into a dict
initiator_config_pattern_dict = initiator_config_pattern_instance.to_dict()
# create an instance of InitiatorConfigPattern from a dict
initiator_config_pattern_from_dict = InitiatorConfigPattern.from_dict(initiator_config_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


