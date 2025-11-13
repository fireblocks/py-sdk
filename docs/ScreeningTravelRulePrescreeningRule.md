# ScreeningTravelRulePrescreeningRule

Matched prescreening rule details. Prescreening rules are evaluated before the main screening to determine if screening is necessary or should be bypassed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_reason** | **str** | Reason for bypass if prescreening rule triggered a bypass | [optional] 
**source_type** | [**TransferPeerTypeEnum**](TransferPeerTypeEnum.md) |  | [optional] 
**source_sub_type** | [**TransferPeerSubTypeEnum**](TransferPeerSubTypeEnum.md) |  | [optional] 
**dest_type** | [**TransferPeerTypeEnum**](TransferPeerTypeEnum.md) |  | [optional] 
**dest_sub_type** | [**TransferPeerSubTypeEnum**](TransferPeerSubTypeEnum.md) |  | [optional] 
**transfer_peer_type** | [**TransferPeerTypeEnum**](TransferPeerTypeEnum.md) |  | [optional] 
**transfer_peer_sub_type** | [**TransferPeerSubTypeEnum**](TransferPeerSubTypeEnum.md) |  | [optional] 
**dest_address** | **str** | Destination address | [optional] 
**source_id** | **str** | Source ID | [optional] 
**dest_id** | **str** | Destination ID | [optional] 
**asset** | **str** | Asset identifier | [optional] 
**base_asset** | **str** | Base asset | [optional] 
**amount** | **float** | Amount | [optional] 
**amount_usd** | **float** | Amount in USD | [optional] 
**network_protocol** | **str** | Network protocol | [optional] 
**operation** | [**TransactionOperationEnum**](TransactionOperationEnum.md) |  | [optional] 
**action** | [**TravelRuleActionEnum**](TravelRuleActionEnum.md) |  | [optional] 

## Example

```python
from fireblocks.models.screening_travel_rule_prescreening_rule import ScreeningTravelRulePrescreeningRule

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningTravelRulePrescreeningRule from a JSON string
screening_travel_rule_prescreening_rule_instance = ScreeningTravelRulePrescreeningRule.from_json(json)
# print the JSON string representation of the object
print(ScreeningTravelRulePrescreeningRule.to_json())

# convert the object into a dict
screening_travel_rule_prescreening_rule_dict = screening_travel_rule_prescreening_rule_instance.to_dict()
# create an instance of ScreeningTravelRulePrescreeningRule from a dict
screening_travel_rule_prescreening_rule_from_dict = ScreeningTravelRulePrescreeningRule.from_dict(screening_travel_rule_prescreening_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


