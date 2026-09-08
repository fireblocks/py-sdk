# QuorumStatus

The approval quorum's structure and progress for this request.  `null` when `quorumStatusMode` is omitted or `NONE`. Also `null` on an otherwise successful response when the quorum cannot be reported faithfully — a multi-tier request in a workspace that does not maintain per-tier approval counts — so absence here does not imply the request has no quorum.  The object may carry additional backend-defined fields beyond those documented.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_status** | [**QuorumRequestState**](QuorumRequestState.md) |  | 
**users** | [**List[QuorumUser]**](QuorumUser.md) | Every user participating in this request&#39;s quorum. Returned only for &#x60;quorumStatusMode&#x3D;FULL&#x60;; omitted otherwise. | [optional] 
**quorum** | [**QuorumStatusQuorum**](QuorumStatusQuorum.md) |  | 

## Example

```python
from fireblocks.models.quorum_status import QuorumStatus

# TODO update the JSON string below
json = "{}"
# create an instance of QuorumStatus from a JSON string
quorum_status_instance = QuorumStatus.from_json(json)
# print the JSON string representation of the object
print(QuorumStatus.to_json())

# convert the object into a dict
quorum_status_dict = quorum_status_instance.to_dict()
# create an instance of QuorumStatus from a dict
quorum_status_from_dict = QuorumStatus.from_dict(quorum_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


