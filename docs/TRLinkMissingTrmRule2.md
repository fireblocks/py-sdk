# TRLinkMissingTrmRule2

Rule for handling transactions when TRM screening data is missing or unavailable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer identifier | [optional] 
**direction** | [**TRLinkTransactionDirection**](TRLinkTransactionDirection.md) |  | [optional] 
**source_type** | **str** | Source entity type | [optional] 
**source_sub_type** | **str** | Source entity subtype | [optional] 
**source_address** | **str** | Source blockchain address | [optional] 
**dest_type** | **str** | Destination entity type | [optional] 
**dest_sub_type** | **str** | Destination entity subtype | [optional] 
**dest_address** | **str** | Destination blockchain address | [optional] 
**source_id** | **str** | Source identifier | [optional] 
**dest_id** | **str** | Destination identifier | [optional] 
**asset** | **str** | Asset or cryptocurrency type | [optional] 
**base_asset** | **str** | Base asset for derivatives | [optional] 
**amount** | [**TRLinkAmount2**](TRLinkAmount2.md) |  | [optional] 
**network_protocol** | **str** | Network protocol identifier | [optional] 
**operation** | **str** | Operation type | [optional] 
**description** | **str** | Rule description | [optional] 
**is_default** | **bool** | Whether this is a default rule | [optional] 
**valid_before** | **int** | Rule is valid before this timestamp (milliseconds) | [optional] 
**valid_after** | **int** | Rule is valid after this timestamp (milliseconds) | [optional] 
**action** | [**TRLinkMissingTrmAction2**](TRLinkMissingTrmAction2.md) |  | 

## Example

```python
from fireblocks.models.tr_link_missing_trm_rule2 import TRLinkMissingTrmRule2

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkMissingTrmRule2 from a JSON string
tr_link_missing_trm_rule2_instance = TRLinkMissingTrmRule2.from_json(json)
# print the JSON string representation of the object
print(TRLinkMissingTrmRule2.to_json())

# convert the object into a dict
tr_link_missing_trm_rule2_dict = tr_link_missing_trm_rule2_instance.to_dict()
# create an instance of TRLinkMissingTrmRule2 from a dict
tr_link_missing_trm_rule2_from_dict = TRLinkMissingTrmRule2.from_dict(tr_link_missing_trm_rule2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


