# SecurityFinding

A single FSPM finding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the finding | [optional] 
**type** | **str** | The finding type identifier | [optional] 
**status** | **str** | Current status of the finding | [optional] 
**severity** | **str** | Severity level of the finding | [optional] 
**category** | **str** | Category of the finding | [optional] 
**created_at** | **datetime** | When the finding was first detected | [optional] 
**title** | **str** | Human-readable title of the finding | [optional] 

## Example

```python
from fireblocks.models.security_finding import SecurityFinding

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityFinding from a JSON string
security_finding_instance = SecurityFinding.from_json(json)
# print the JSON string representation of the object
print(SecurityFinding.to_json())

# convert the object into a dict
security_finding_dict = security_finding_instance.to_dict()
# create an instance of SecurityFinding from a dict
security_finding_from_dict = SecurityFinding.from_dict(security_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


