# PolicyRuleAuthorizationGroups

Defines the transaction approval terms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | * AND - requires approval of all authorization groups * OR - requires approval of at least one of the authorization groups  | [optional] 
**allow_operator_as_authorizer** | **bool** | Defines whether the user who initiates a transaction can approve their own transaction and count toward the approval threshold for their transaction | [optional] 
**groups** | [**List[PolicyRuleAuthorizationGroupsGroupsInner]**](PolicyRuleAuthorizationGroupsGroupsInner.md) | Groups of entities which can approve the transaction | [optional] 

## Example

```python
from fireblocks_client.models.policy_rule_authorization_groups import PolicyRuleAuthorizationGroups

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleAuthorizationGroups from a JSON string
policy_rule_authorization_groups_instance = PolicyRuleAuthorizationGroups.from_json(json)
# print the JSON string representation of the object
print(PolicyRuleAuthorizationGroups.to_json())

# convert the object into a dict
policy_rule_authorization_groups_dict = policy_rule_authorization_groups_instance.to_dict()
# create an instance of PolicyRuleAuthorizationGroups from a dict
policy_rule_authorization_groups_from_dict = PolicyRuleAuthorizationGroups.from_dict(policy_rule_authorization_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


