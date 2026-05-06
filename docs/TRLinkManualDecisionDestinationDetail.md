# TRLinkManualDecisionDestinationDetail

Per-destination result of the manual decision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_screening_id** | **str** | Destination screening record ID | 
**applied** | **bool** | Whether the decision was applied to this destination | 
**skip_reason** | **str** | Reason if the destination was skipped | [optional] 

## Example

```python
from fireblocks.models.tr_link_manual_decision_destination_detail import TRLinkManualDecisionDestinationDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkManualDecisionDestinationDetail from a JSON string
tr_link_manual_decision_destination_detail_instance = TRLinkManualDecisionDestinationDetail.from_json(json)
# print the JSON string representation of the object
print(TRLinkManualDecisionDestinationDetail.to_json())

# convert the object into a dict
tr_link_manual_decision_destination_detail_dict = tr_link_manual_decision_destination_detail_instance.to_dict()
# create an instance of TRLinkManualDecisionDestinationDetail from a dict
tr_link_manual_decision_destination_detail_from_dict = TRLinkManualDecisionDestinationDetail.from_dict(tr_link_manual_decision_destination_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


