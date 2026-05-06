# TRLinkManualDecisionResponse

Response containing the result of the manual decision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TRLinkManualDecisionAction**](TRLinkManualDecisionAction.md) |  | 
**source** | [**TRLinkManualDecisionSource**](TRLinkManualDecisionSource.md) |  | 
**tx_id** | **str** | Transaction ID | 
**destinations_affected** | **int** | Number of destinations where the decision was applied | 
**destinations_skipped** | **int** | Number of destinations that were skipped | 
**details** | [**List[TRLinkManualDecisionDestinationDetail]**](TRLinkManualDecisionDestinationDetail.md) | Per-destination details | 

## Example

```python
from fireblocks.models.tr_link_manual_decision_response import TRLinkManualDecisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkManualDecisionResponse from a JSON string
tr_link_manual_decision_response_instance = TRLinkManualDecisionResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkManualDecisionResponse.to_json())

# convert the object into a dict
tr_link_manual_decision_response_dict = tr_link_manual_decision_response_instance.to_dict()
# create an instance of TRLinkManualDecisionResponse from a dict
tr_link_manual_decision_response_from_dict = TRLinkManualDecisionResponse.from_dict(tr_link_manual_decision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


