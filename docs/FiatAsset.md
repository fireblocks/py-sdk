# FiatAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**balance** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.fiat_asset import FiatAsset

# TODO update the JSON string below
json = "{}"
# create an instance of FiatAsset from a JSON string
fiat_asset_instance = FiatAsset.from_json(json)
# print the JSON string representation of the object
print(FiatAsset.to_json())

# convert the object into a dict
fiat_asset_dict = fiat_asset_instance.to_dict()
# create an instance of FiatAsset from a dict
fiat_asset_from_dict = FiatAsset.from_dict(fiat_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


