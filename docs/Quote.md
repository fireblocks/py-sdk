# Quote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**via** | [**AccessType**](AccessType.md) |  | 
**id** | **str** |  | 
**quote_asset_id** | **str** |  | 
**base_asset_id** | **str** |  | 
**base_amount** | **str** |  | 
**quote_amount** | **str** |  | 
**price_impact** | **float** |  | [optional] 
**quote_min_amount** | **str** |  | [optional] 
**execution_steps** | [**List[QuoteExecutionStep]**](QuoteExecutionStep.md) |  | [optional] 
**general_fees** | [**List[Fee]**](Fee.md) |  | [optional] 
**side** | [**Side**](Side.md) |  | 
**expires_at** | **str** | The expiration time of the quote in ISO format. | 
**type** | [**IndicativeQuoteEnum**](IndicativeQuoteEnum.md) |  | 

## Example

```python
from fireblocks.models.quote import Quote

# TODO update the JSON string below
json = "{}"
# create an instance of Quote from a JSON string
quote_instance = Quote.from_json(json)
# print the JSON string representation of the object
print(Quote.to_json())

# convert the object into a dict
quote_dict = quote_instance.to_dict()
# create an instance of Quote from a dict
quote_from_dict = Quote.from_dict(quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


