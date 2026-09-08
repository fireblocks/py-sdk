# QuorumRuleset

One sub-request of the approval criteria, made up of one or more tiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_match** | **str** | Whether every tier in &#x60;groups&#x60; must be satisfied (&#x60;ALL&#x60;) or any single one of them (&#x60;ANY&#x60;). | 
**status** | [**QuorumApprovalState**](QuorumApprovalState.md) |  | 
**groups** | [**List[QuorumGroup]**](QuorumGroup.md) | The tiers of this sub-request, evaluated according to &#x60;groupMatch&#x60;. | 

## Example

```python
from fireblocks.models.quorum_ruleset import QuorumRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of QuorumRuleset from a JSON string
quorum_ruleset_instance = QuorumRuleset.from_json(json)
# print the JSON string representation of the object
print(QuorumRuleset.to_json())

# convert the object into a dict
quorum_ruleset_dict = quorum_ruleset_instance.to_dict()
# create an instance of QuorumRuleset from a dict
quorum_ruleset_from_dict = QuorumRuleset.from_dict(quorum_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


