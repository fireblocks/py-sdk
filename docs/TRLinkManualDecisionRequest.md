# TRLinkManualDecisionRequest

Request to manually accept or reject destinations stuck in NoTRM status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TRLinkManualDecisionAction**](TRLinkManualDecisionAction.md) |  | 
**reason** | **str** | Optional reason for the manual decision (e.g. &#39;Internal KYC approved&#39;). Do not include PII. | [optional] 

## Example

```python
from fireblocks.models.tr_link_manual_decision_request import TRLinkManualDecisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkManualDecisionRequest from a JSON string
tr_link_manual_decision_request_instance = TRLinkManualDecisionRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkManualDecisionRequest.to_json())

# convert the object into a dict
tr_link_manual_decision_request_dict = tr_link_manual_decision_request_instance.to_dict()
# create an instance of TRLinkManualDecisionRequest from a dict
tr_link_manual_decision_request_from_dict = TRLinkManualDecisionRequest.from_dict(tr_link_manual_decision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


