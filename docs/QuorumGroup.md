# QuorumGroup

A single tier of a ruleset: a threshold and the approvals collected toward it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **int** | Number of approvals this tier requires. | 
**current_approval_count** | **int** | Approvals collected so far toward &#x60;threshold&#x60;. | 
**status** | [**QuorumApprovalState**](QuorumApprovalState.md) |  | 
**members** | **List[int]** | Indexes into the top-level &#x60;users&#x60; array identifying the users who belong to this tier. Returned only for &#x60;quorumStatusMode&#x3D;FULL&#x60;; omitted otherwise. | [optional] 

## Example

```python
from fireblocks.models.quorum_group import QuorumGroup

# TODO update the JSON string below
json = "{}"
# create an instance of QuorumGroup from a JSON string
quorum_group_instance = QuorumGroup.from_json(json)
# print the JSON string representation of the object
print(QuorumGroup.to_json())

# convert the object into a dict
quorum_group_dict = quorum_group_instance.to_dict()
# create an instance of QuorumGroup from a dict
quorum_group_from_dict = QuorumGroup.from_dict(quorum_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


