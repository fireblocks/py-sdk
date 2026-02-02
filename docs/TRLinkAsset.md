# TRLinkAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**TRLinkAssetFormat**](TRLinkAssetFormat.md) |  | 
**data** | [**TRLinkAssetData**](TRLinkAssetData.md) |  | 

## Example

```python
from fireblocks.models.tr_link_asset import TRLinkAsset

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAsset from a JSON string
tr_link_asset_instance = TRLinkAsset.from_json(json)
# print the JSON string representation of the object
print(TRLinkAsset.to_json())

# convert the object into a dict
tr_link_asset_dict = tr_link_asset_instance.to_dict()
# create an instance of TRLinkAsset from a dict
tr_link_asset_from_dict = TRLinkAsset.from_dict(tr_link_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


