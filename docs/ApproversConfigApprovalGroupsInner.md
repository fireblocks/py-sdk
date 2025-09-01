# ApproversConfigApprovalGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **float** | Approval threshold | 
**users** | **List[str]** | List of user IDs | [optional] 
**groups** | **List[str]** | List of policy group IDs | [optional] 

## Example

```python
from fireblocks.models.approvers_config_approval_groups_inner import ApproversConfigApprovalGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApproversConfigApprovalGroupsInner from a JSON string
approvers_config_approval_groups_inner_instance = ApproversConfigApprovalGroupsInner.from_json(json)
# print the JSON string representation of the object
print(ApproversConfigApprovalGroupsInner.to_json())

# convert the object into a dict
approvers_config_approval_groups_inner_dict = approvers_config_approval_groups_inner_instance.to_dict()
# create an instance of ApproversConfigApprovalGroupsInner from a dict
approvers_config_approval_groups_inner_from_dict = ApproversConfigApprovalGroupsInner.from_dict(approvers_config_approval_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


