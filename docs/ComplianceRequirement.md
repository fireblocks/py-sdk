# ComplianceRequirement

A compliance requirement associated with a finding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the compliance requirement | 
**standard** | **str** | The compliance standard this requirement belongs to | 
**criteria** | **str** | The specific criteria within the compliance standard | 
**description** | **str** | Human-readable description of the requirement, omitted if not available | [optional] 

## Example

```python
from fireblocks.models.compliance_requirement import ComplianceRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceRequirement from a JSON string
compliance_requirement_instance = ComplianceRequirement.from_json(json)
# print the JSON string representation of the object
print(ComplianceRequirement.to_json())

# convert the object into a dict
compliance_requirement_dict = compliance_requirement_instance.to_dict()
# create an instance of ComplianceRequirement from a dict
compliance_requirement_from_dict = ComplianceRequirement.from_dict(compliance_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


