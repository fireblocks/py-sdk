# XBSettlementAsset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**asset_id** | [**XBSettlementAssetID**](XBSettlementAssetID.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.xb_settlement_asset import XBSettlementAsset

# TODO update the JSON string below
json = "{}"
# create an instance of XBSettlementAsset from a JSON string
xb_settlement_asset_instance = XBSettlementAsset.from_json(json)
# print the JSON string representation of the object
print XBSettlementAsset.to_json()

# convert the object into a dict
xb_settlement_asset_dict = xb_settlement_asset_instance.to_dict()
# create an instance of XBSettlementAsset from a dict
xb_settlement_asset_form_dict = xb_settlement_asset.from_dict(xb_settlement_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


