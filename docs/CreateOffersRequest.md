# CreateOffersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset_id** | **str** | The source asset identifier. | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | The target asset identifier. | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**base_amount** | **str** | The amount to get offers for | 
**slippage_bps** | **int** | Slippage tolerance in basis points (bps) for defi quotes - 1 is 0.01% and 10000 is 100%. If not set, defaults to 50 bps (0.5%). | [optional] [default to 50]
**settlement** | [**DVPSettlement**](DVPSettlement.md) |  | [optional] 
**side** | [**Side**](Side.md) |  | 

## Example

```python
from fireblocks.models.create_offers_request import CreateOffersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOffersRequest from a JSON string
create_offers_request_instance = CreateOffersRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOffersRequest.to_json())

# convert the object into a dict
create_offers_request_dict = create_offers_request_instance.to_dict()
# create an instance of CreateOffersRequest from a dict
create_offers_request_from_dict = CreateOffersRequest.from_dict(create_offers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


