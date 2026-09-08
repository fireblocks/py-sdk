# SimpleQuorum

The flattened shape used when the request has a single sub-request with a single tier, which is the common case. The threshold and approval count sit directly on the quorum object instead of inside `rulesets`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator identifying the flattened single-tier shape. | 
**threshold** | **int** | Number of approvals this request requires. | 
**current_approval_count** | **int** | Approvals collected so far toward &#x60;threshold&#x60;. | 
**status** | [**QuorumApprovalState**](QuorumApprovalState.md) |  | 
**is_mandatory_owner_approved** | **bool** | Present only when this request additionally requires the workspace owner&#39;s approval. &#x60;false&#x60; means the owner has not approved yet, which is why &#x60;status&#x60; can remain &#x60;PENDING&#x60; even once &#x60;currentApprovalCount&#x60; reaches &#x60;threshold&#x60;. Absent when no owner approval is required. | [optional] 
**members** | **List[int]** | Indexes into the top-level &#x60;users&#x60; array identifying the users who may approve. Returned only for &#x60;quorumStatusMode&#x3D;FULL&#x60;; omitted otherwise. | [optional] 

## Example

```python
from fireblocks.models.simple_quorum import SimpleQuorum

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleQuorum from a JSON string
simple_quorum_instance = SimpleQuorum.from_json(json)
# print the JSON string representation of the object
print(SimpleQuorum.to_json())

# convert the object into a dict
simple_quorum_dict = simple_quorum_instance.to_dict()
# create an instance of SimpleQuorum from a dict
simple_quorum_from_dict = SimpleQuorum.from_dict(simple_quorum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


