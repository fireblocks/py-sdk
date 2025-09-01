# ApproversConfig

Approvers configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_initiator_approve** | **bool** | Whether initiator can approve | [optional] 
**operator** | **str** | Operator for approval groups | [optional] 
**allow_operator_as_authorizer** | **bool** | Whether operator can be authorizer | [optional] 
**approval_groups** | [**List[ApproversConfigApprovalGroupsInner]**](ApproversConfigApprovalGroupsInner.md) | List of approval groups | [optional] 

## Example

```python
from fireblocks.models.approvers_config import ApproversConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ApproversConfig from a JSON string
approvers_config_instance = ApproversConfig.from_json(json)
# print the JSON string representation of the object
print(ApproversConfig.to_json())

# convert the object into a dict
approvers_config_dict = approvers_config_instance.to_dict()
# create an instance of ApproversConfig from a dict
approvers_config_from_dict = ApproversConfig.from_dict(approvers_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


