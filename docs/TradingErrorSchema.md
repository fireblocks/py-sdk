# TradingErrorSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**code** | **float** |  | 
**descriptor** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.trading_error_schema import TradingErrorSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TradingErrorSchema from a JSON string
trading_error_schema_instance = TradingErrorSchema.from_json(json)
# print the JSON string representation of the object
print(TradingErrorSchema.to_json())

# convert the object into a dict
trading_error_schema_dict = trading_error_schema_instance.to_dict()
# create an instance of TradingErrorSchema from a dict
trading_error_schema_from_dict = TradingErrorSchema.from_dict(trading_error_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


