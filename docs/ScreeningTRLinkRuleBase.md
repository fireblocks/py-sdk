# ScreeningTRLinkRuleBase

Base interface for TRLink policy rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Reference to TRLinkCustomer.id | [optional] 
**direction** | [**TravelRuleDirectionEnum**](TravelRuleDirectionEnum.md) |  | [optional] 
**source_type** | [**TransferPeerTypeEnum**](TransferPeerTypeEnum.md) |  | [optional] 
**source_sub_type** | [**TransferPeerSubTypeEnum**](TransferPeerSubTypeEnum.md) |  | [optional] 
**source_address** | **str** | Source address | [optional] 
**dest_type** | [**TransferPeerTypeEnum**](TransferPeerTypeEnum.md) |  | [optional] 
**dest_sub_type** | [**TransferPeerSubTypeEnum**](TransferPeerSubTypeEnum.md) |  | [optional] 
**dest_address** | **str** | Destination address | [optional] 
**source_id** | **str** | Source ID | [optional] 
**dest_id** | **str** | Destination ID | [optional] 
**asset** | **str** | Asset symbol | [optional] 
**base_asset** | **str** | Base asset symbol | [optional] 
**amount** | [**ScreeningTRLinkAmount**](ScreeningTRLinkAmount.md) |  | [optional] 
**network_protocol** | **str** | Network protocol | [optional] 
**operation** | [**TransactionOperationEnum**](TransactionOperationEnum.md) |  | [optional] 
**description** | **str** | Rule description | [optional] 
**is_default** | **bool** | Whether this is a default rule | [optional] [default to False]

## Example

```python
from fireblocks.models.screening_tr_link_rule_base import ScreeningTRLinkRuleBase

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningTRLinkRuleBase from a JSON string
screening_tr_link_rule_base_instance = ScreeningTRLinkRuleBase.from_json(json)
# print the JSON string representation of the object
print(ScreeningTRLinkRuleBase.to_json())

# convert the object into a dict
screening_tr_link_rule_base_dict = screening_tr_link_rule_base_instance.to_dict()
# create an instance of ScreeningTRLinkRuleBase from a dict
screening_tr_link_rule_base_from_dict = ScreeningTRLinkRuleBase.from_dict(screening_tr_link_rule_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


