# Rate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**via** | [**AccessType**](AccessType.md) |  | 
**base_asset_id** | **str** | The source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | The target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**rate** | **str** | The indicative exchange rate — the number of units of the quote asset that equal 1 unit of the base asset. For example, if base is BTC and quote is USD, a rate of 75000 means 1 BTC &#x3D; 75,000 USD. | 

## Example

```python
from fireblocks.models.rate import Rate

# TODO update the JSON string below
json = "{}"
# create an instance of Rate from a JSON string
rate_instance = Rate.from_json(json)
# print the JSON string representation of the object
print(Rate.to_json())

# convert the object into a dict
rate_dict = rate_instance.to_dict()
# create an instance of Rate from a dict
rate_from_dict = Rate.from_dict(rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


