# SecurityFindingDetailed

A single FSPM finding, redacted to the public field set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the finding | 
**type** | **str** | The finding type identifier | 
**status** | **str** | Current status of the finding | 
**severity** | **str** | Severity level of the finding | 
**category** | **str** | Category of the finding | 
**created_at** | **datetime** | When the finding was first detected | 
**title** | **str** | Human-readable title of the finding | 
**status_updated_at** | **datetime** | When the finding status was last updated, omitted if the status was never updated | [optional] 
**status_updated_by_user_id** | **str** | The user who last updated the finding status, omitted if the status was never updated | [optional] 
**status_updated_reason** | **str** | The reason provided for the last status update, omitted if none was provided | [optional] 
**info** | **Dict[str, object]** | Additional structured context about the finding. Shape varies by finding type. | 
**compliance_reqs** | [**List[ComplianceRequirement]**](ComplianceRequirement.md) | Compliance requirements this finding relates to | 
**risk_explanation** | **str** | Explanation of the risk this finding represents | 
**mitigation_guidance** | **str** | Guidance on how to mitigate this finding | 

## Example

```python
from fireblocks.models.security_finding_detailed import SecurityFindingDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityFindingDetailed from a JSON string
security_finding_detailed_instance = SecurityFindingDetailed.from_json(json)
# print the JSON string representation of the object
print(SecurityFindingDetailed.to_json())

# convert the object into a dict
security_finding_detailed_dict = security_finding_detailed_instance.to_dict()
# create an instance of SecurityFindingDetailed from a dict
security_finding_detailed_from_dict = SecurityFindingDetailed.from_dict(security_finding_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


