# TRLinkResult

TRLink screening result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | The TRLink provider name | 
**timestamp** | **float** | Unix timestamp of the screening result | 
**status** | **str** | Status of the TRLink screening | 
**verdict** | [**TRLinkVerdict**](TRLinkVerdict.md) |  | [optional] 
**dest_address** | **str** | The destination address associated with the TRLink screening | [optional] 
**dest_tag** | **str** | Destination tag for the screening | [optional] 
**bypass_reason** | **str** | Reason for bypassing the TRLink screening | [optional] 
**details_message** | **str** | Additional details message about the screening result | [optional] 
**customer_integration_id** | **str** | Customer integration identifier | [optional] 
**customer_short_name** | **str** | Customer short name | [optional] 
**travel_rule_message_id** | **str** | Travel rule message identifier for linking | [optional] 
**result** | [**TRLinkProviderResultWithRule**](TRLinkProviderResultWithRule.md) |  | [optional] 
**matched_prescreening_rule** | [**TRLinkPreScreeningRule**](TRLinkPreScreeningRule.md) |  | [optional] 
**matched_no_trm_screening_rule** | [**TRLinkMissingTrmDecision**](TRLinkMissingTrmDecision.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_result import TRLinkResult

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkResult from a JSON string
tr_link_result_instance = TRLinkResult.from_json(json)
# print the JSON string representation of the object
print(TRLinkResult.to_json())

# convert the object into a dict
tr_link_result_dict = tr_link_result_instance.to_dict()
# create an instance of TRLinkResult from a dict
tr_link_result_from_dict = TRLinkResult.from_dict(tr_link_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


