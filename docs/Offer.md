# Offer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**via** | [**AccessType**](AccessType.md) |  | 
**base_asset_id** | **str** | The source asset identifier. | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | The target asset identifier. | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**rate** | **str** | The indicative exchange rate — the number of units of the quote asset that equal 1 unit of the base asset. For example, if base is BTC and quote is USD, a rate of 75000 means 1 BTC &#x3D; 75,000 USD. | 
**offer_type** | **str** | The type of offer — QUOTE for executable committed quotes. | 
**id** | **str** | The unique identifier of the quote. | 
**base_amount** | **str** | The amount of the base asset. | 
**quote_amount** | **str** | The amount of the quote asset. | 
**price_impact** | **float** | The estimated price impact as a decimal fraction. | [optional] 
**quote_min_amount** | **str** | The minimum guaranteed amount of the quote asset. | [optional] 
**is_slippage_applied** | **bool** | Indicates if slippage was applied to the quote. | [optional] [default to False]
**execution_steps** | [**List[QuoteExecutionStep]**](QuoteExecutionStep.md) | Ordered list of execution steps for the quote. | [optional] 
**general_fees** | [**List[Fee]**](Fee.md) | General fees associated with the quote. | [optional] 
**side** | [**Side**](Side.md) |  | 
**expires_at** | **str** | The expiration time of the quote in ISO 8601 format. | 
**required_participants_identification_on_order** | **str** | A JSON Schema Draft-7 document in string format describing the fields required when creating an order so clients can validate their order payload before sending.  | [optional] 
**type** | **str** | The type of the quote. | 

## Example

```python
from fireblocks.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print(Offer.to_json())

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_from_dict = Offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


