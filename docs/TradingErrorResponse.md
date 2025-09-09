# TradingErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**TradingErrorResponseError**](TradingErrorResponseError.md) |  | 

## Example

```python
from fireblocks.models.trading_error_response import TradingErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TradingErrorResponse from a JSON string
trading_error_response_instance = TradingErrorResponse.from_json(json)
# print the JSON string representation of the object
print(TradingErrorResponse.to_json())

# convert the object into a dict
trading_error_response_dict = trading_error_response_instance.to_dict()
# create an instance of TradingErrorResponse from a dict
trading_error_response_from_dict = TradingErrorResponse.from_dict(trading_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


