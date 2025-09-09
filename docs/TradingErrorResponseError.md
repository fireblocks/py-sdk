# TradingErrorResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**message** | **str** |  | 
**error_code** | [**ErrorCodes**](ErrorCodes.md) |  | [optional] 

## Example

```python
from fireblocks.models.trading_error_response_error import TradingErrorResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of TradingErrorResponseError from a JSON string
trading_error_response_error_instance = TradingErrorResponseError.from_json(json)
# print the JSON string representation of the object
print(TradingErrorResponseError.to_json())

# convert the object into a dict
trading_error_response_error_dict = trading_error_response_error_instance.to_dict()
# create an instance of TradingErrorResponseError from a dict
trading_error_response_error_from_dict = TradingErrorResponseError.from_dict(trading_error_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


