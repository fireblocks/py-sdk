# PostTradeSettlement

Nothing moves on-platform; settlement happens bilaterally, provider-side, after execution. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PostTradeSettlementType**](PostTradeSettlementType.md) |  | 

## Example

```python
from fireblocks.models.post_trade_settlement import PostTradeSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of PostTradeSettlement from a JSON string
post_trade_settlement_instance = PostTradeSettlement.from_json(json)
# print the JSON string representation of the object
print(PostTradeSettlement.to_json())

# convert the object into a dict
post_trade_settlement_dict = post_trade_settlement_instance.to_dict()
# create an instance of PostTradeSettlement from a dict
post_trade_settlement_from_dict = PostTradeSettlement.from_dict(post_trade_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


