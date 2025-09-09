# ExchangeAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 
**locked_amount** | **str** |  | [optional] 
**total** | **str** |  | [optional] 
**available** | **str** |  | [optional] 
**credit** | **str** |  | [optional] 
**asset_id** | **str** | The id of the asset | [optional] 
**provider_symbol** | **str** | The provider symbol of the asset | [optional] 
**asset_symbol** | **str** | The asset symbol of the asset | [optional] 
**asset_legacy_id** | **str** | The asset legacy id of the asset | [optional] 

## Example

```python
from fireblocks.models.exchange_asset import ExchangeAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAsset from a JSON string
exchange_asset_instance = ExchangeAsset.from_json(json)
# print the JSON string representation of the object
print(ExchangeAsset.to_json())

# convert the object into a dict
exchange_asset_dict = exchange_asset_instance.to_dict()
# create an instance of ExchangeAsset from a dict
exchange_asset_from_dict = ExchangeAsset.from_dict(exchange_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


