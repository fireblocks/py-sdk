# RulesetQuorum

The general shape, used when the request has more than one sub-request or a sub-request with more than one tier. Each entry in `rulesets` is a sub-request; each of its `groups` is a tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator identifying the multi-tier shape. | 
**ruleset_match** | **str** | Whether every sub-request in &#x60;rulesets&#x60; must be satisfied (&#x60;ALL&#x60;) or any single one of them (&#x60;ANY&#x60;). | 
**status** | [**QuorumApprovalState**](QuorumApprovalState.md) |  | 
**is_mandatory_owner_approved** | **bool** | Present only when this request additionally requires the workspace owner&#39;s approval. &#x60;false&#x60; means the owner has not approved yet. Absent when no owner approval is required. | [optional] 
**rulesets** | [**List[QuorumRuleset]**](QuorumRuleset.md) | The sub-requests of the approval criteria, evaluated according to &#x60;rulesetMatch&#x60;. | 

## Example

```python
from fireblocks.models.ruleset_quorum import RulesetQuorum

# TODO update the JSON string below
json = "{}"
# create an instance of RulesetQuorum from a JSON string
ruleset_quorum_instance = RulesetQuorum.from_json(json)
# print the JSON string representation of the object
print(RulesetQuorum.to_json())

# convert the object into a dict
ruleset_quorum_dict = ruleset_quorum_instance.to_dict()
# create an instance of RulesetQuorum from a dict
ruleset_quorum_from_dict = RulesetQuorum.from_dict(ruleset_quorum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


