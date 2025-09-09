# OrderSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**via** | [**AccessType**](AccessType.md) |  | 
**side** | **str** | Side of the order | 
**base_amount** | **str** |  | 
**quote_amount** | **str** |  | [optional] 
**base_asset_id** | **str** |  | 
**quote_asset_id** | **str** |  | 
**status** | [**OrderStatus**](OrderStatus.md) |  | 
**destination** | [**AccountReference**](AccountReference.md) |  | 
**source** | [**SettlementSourceAccount**](SettlementSourceAccount.md) |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from fireblocks.models.order_summary import OrderSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSummary from a JSON string
order_summary_instance = OrderSummary.from_json(json)
# print the JSON string representation of the object
print(OrderSummary.to_json())

# convert the object into a dict
order_summary_dict = order_summary_instance.to_dict()
# create an instance of OrderSummary from a dict
order_summary_from_dict = OrderSummary.from_dict(order_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


