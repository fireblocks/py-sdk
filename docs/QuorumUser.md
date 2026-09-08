# QuorumUser

A user who participates in this request's approval quorum, and their approval state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Zero-based position of this user within the &#x60;users&#x60; array. The &#x60;members&#x60; arrays elsewhere in the document reference users by this index rather than repeating the user ID. | 
**user_id** | **str** | The participating user&#39;s ID. | 
**status** | [**QuorumApprovalState**](QuorumApprovalState.md) |  | 
**is_mandatory_owner** | **bool** | Present and &#x60;true&#x60; only for the workspace owner, when this request additionally requires the owner&#39;s approval. Absent for every other participant. | [optional] 

## Example

```python
from fireblocks.models.quorum_user import QuorumUser

# TODO update the JSON string below
json = "{}"
# create an instance of QuorumUser from a JSON string
quorum_user_instance = QuorumUser.from_json(json)
# print the JSON string representation of the object
print(QuorumUser.to_json())

# convert the object into a dict
quorum_user_dict = quorum_user_instance.to_dict()
# create an instance of QuorumUser from a dict
quorum_user_from_dict = QuorumUser.from_dict(quorum_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


