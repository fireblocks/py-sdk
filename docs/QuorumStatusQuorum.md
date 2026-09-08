# QuorumStatusQuorum

The approval criteria and how far they have been met. `type` discriminates the two shapes: `SIMPLE` flattens the common single-tier case, `RULESET` is the general multi-tier form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator identifying the flattened single-tier shape. | 
**threshold** | **int** | Number of approvals this request requires. | 
**current_approval_count** | **int** | Approvals collected so far toward &#x60;threshold&#x60;. | 
**status** | [**QuorumApprovalState**](QuorumApprovalState.md) |  | 
**is_mandatory_owner_approved** | **bool** | Present only when this request additionally requires the workspace owner&#39;s approval. &#x60;false&#x60; means the owner has not approved yet. Absent when no owner approval is required. | [optional] 
**members** | **List[int]** | Indexes into the top-level &#x60;users&#x60; array identifying the users who may approve. Returned only for &#x60;quorumStatusMode&#x3D;FULL&#x60;; omitted otherwise. | [optional] 
**ruleset_match** | **str** | Whether every sub-request in &#x60;rulesets&#x60; must be satisfied (&#x60;ALL&#x60;) or any single one of them (&#x60;ANY&#x60;). | 
**rulesets** | [**List[QuorumRuleset]**](QuorumRuleset.md) | The sub-requests of the approval criteria, evaluated according to &#x60;rulesetMatch&#x60;. | 

## Example

```python
from fireblocks.models.quorum_status_quorum import QuorumStatusQuorum

# TODO update the JSON string below
json = "{}"
# create an instance of QuorumStatusQuorum from a JSON string
quorum_status_quorum_instance = QuorumStatusQuorum.from_json(json)
# print the JSON string representation of the object
print(QuorumStatusQuorum.to_json())

# convert the object into a dict
quorum_status_quorum_dict = quorum_status_quorum_instance.to_dict()
# create an instance of QuorumStatusQuorum from a dict
quorum_status_quorum_from_dict = QuorumStatusQuorum.from_dict(quorum_status_quorum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


