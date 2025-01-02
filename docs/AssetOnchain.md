# AssetOnchain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The asset symbol | 
**name** | **str** | The asset name | 
**address** | **str** | The asset address | [optional] 
**decimals** | **float** | Number of decimals | 
**standard** | **str** | The asset standard | [optional] 

## Example

```python
from fireblocks.models.asset_onchain import AssetOnchain

# TODO update the JSON string below
json = "{}"
# create an instance of AssetOnchain from a JSON string
asset_onchain_instance = AssetOnchain.from_json(json)
# print the JSON string representation of the object
print(AssetOnchain.to_json())

# convert the object into a dict
asset_onchain_dict = asset_onchain_instance.to_dict()
# create an instance of AssetOnchain from a dict
asset_onchain_from_dict = AssetOnchain.from_dict(asset_onchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


