# RateOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**via** | [**AccessType**](AccessType.md) |  | 
**base_asset_id** | **str** | The source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | The target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**rate** | **str** | The indicative exchange rate — the number of units of the quote asset that equal 1 unit of the base asset. For example, if base is BTC and quote is USD, a rate of 75000 means 1 BTC &#x3D; 75,000 USD. | 
**offer_type** | **str** | The type of offer — RATE for indicative pricing. | 

## Example

```python
from fireblocks.models.rate_offer import RateOffer

# TODO update the JSON string below
json = "{}"
# create an instance of RateOffer from a JSON string
rate_offer_instance = RateOffer.from_json(json)
# print the JSON string representation of the object
print(RateOffer.to_json())

# convert the object into a dict
rate_offer_dict = rate_offer_instance.to_dict()
# create an instance of RateOffer from a dict
rate_offer_from_dict = RateOffer.from_dict(rate_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


