# TRLinkPostScreeningRule2

Post-screening rule that determines the verdict based on screening results

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
**provider_ident** | **str** | TRP provider identifier | [optional] 
**trm_status** | [**TRLinkTrmStatus**](TRLinkTrmStatus.md) |  | [optional] 
**valid_before** | **int** | Rule is valid before this timestamp (milliseconds) | [optional] 
**valid_after** | **int** | Rule is valid after this timestamp (milliseconds) | [optional] 
**action** | [**TRLinkPostScreeningAction**](TRLinkPostScreeningAction.md) |  | 

## Example

```python
from fireblocks.models.tr_link_post_screening_rule2 import TRLinkPostScreeningRule2

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkPostScreeningRule2 from a JSON string
tr_link_post_screening_rule2_instance = TRLinkPostScreeningRule2.from_json(json)
# print the JSON string representation of the object
print(TRLinkPostScreeningRule2.to_json())

# convert the object into a dict
tr_link_post_screening_rule2_dict = tr_link_post_screening_rule2_instance.to_dict()
# create an instance of TRLinkPostScreeningRule2 from a dict
tr_link_post_screening_rule2_from_dict = TRLinkPostScreeningRule2.from_dict(tr_link_post_screening_rule2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


