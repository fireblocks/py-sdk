# TRLinkMissingTrmDecision

Interface for reporting missing TRM screening decisions in ITRLinkResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Reference to TrlinkCustomer.id | [optional] 
**direction** | [**TransactionDirection**](TransactionDirection.md) |  | [optional] 
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
**amount** | [**TRLinkAmount**](TRLinkAmount.md) |  | [optional] 
**network_protocol** | **str** | Network protocol | [optional] 
**operation** | [**TransactionOperationEnum**](TransactionOperationEnum.md) |  | [optional] 
**description** | **str** | Rule description | [optional] 
**is_default** | **bool** | Whether this is a default rule | [optional] [default to False]
**valid_before** | **float** | Unix timestamp when rule expires | [optional] 
**valid_after** | **float** | Unix timestamp when rule becomes valid | [optional] 
**action** | [**TRLinkMissingTrmAction**](TRLinkMissingTrmAction.md) |  | 
**source** | **str** | TRLink missing TRM source | 
**timestamp** | **datetime** | Timestamp of the decision | [optional] 
**reason** | **str** | Reason for the decision | [optional] 

## Example

```python
from fireblocks.models.tr_link_missing_trm_decision import TRLinkMissingTrmDecision

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkMissingTrmDecision from a JSON string
tr_link_missing_trm_decision_instance = TRLinkMissingTrmDecision.from_json(json)
# print the JSON string representation of the object
print(TRLinkMissingTrmDecision.to_json())

# convert the object into a dict
tr_link_missing_trm_decision_dict = tr_link_missing_trm_decision_instance.to_dict()
# create an instance of TRLinkMissingTrmDecision from a dict
tr_link_missing_trm_decision_from_dict = TRLinkMissingTrmDecision.from_dict(tr_link_missing_trm_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


