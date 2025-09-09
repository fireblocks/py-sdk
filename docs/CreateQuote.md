# CreateQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**List[CreateQuoteScopeInner]**](CreateQuoteScopeInner.md) |  | 
**base_asset_id** | **str** |  | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** |  | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**base_amount** | **str** | The amount to convert from | 
**slippage_bps** | **float** | Slippage tolerance in basis points (bps) for defi quotes - 1 is 0.01% and 10000 is 100% | [optional] [default to 50]
**settlement** | [**DVPSettlement**](DVPSettlement.md) |  | [optional] 
**side** | **str** | Side of the order | 

## Example

```python
from fireblocks.models.create_quote import CreateQuote

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQuote from a JSON string
create_quote_instance = CreateQuote.from_json(json)
# print the JSON string representation of the object
print(CreateQuote.to_json())

# convert the object into a dict
create_quote_dict = create_quote_instance.to_dict()
# create an instance of CreateQuote from a dict
create_quote_from_dict = CreateQuote.from_dict(create_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


