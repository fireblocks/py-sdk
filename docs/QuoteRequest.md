# QuoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The id of the vault account or account id | [optional] 
**input_amount** | **str** | The amount of tokens the swapper will provide, positive number, can be a decimal. | 
**input_asset** | **str** | The id of the asset the swapper will provide | 
**output_asset** | **str** | The id of the asset the swapper will receive | 
**slippage_tolerance** | **float** | The slippage tolerance is a percentage. The slippage tolerance is the maximum amount the price can change between the time the transaction is submitted and the time it is executed | 
**protocol** | [**SwapProviderProtocolsEnum**](SwapProviderProtocolsEnum.md) |  | 

## Example

```python
from fireblocks.models.quote_request import QuoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteRequest from a JSON string
quote_request_instance = QuoteRequest.from_json(json)
# print the JSON string representation of the object
print(QuoteRequest.to_json())

# convert the object into a dict
quote_request_dict = quote_request_instance.to_dict()
# create an instance of QuoteRequest from a dict
quote_request_from_dict = QuoteRequest.from_dict(quote_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


