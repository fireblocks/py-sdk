# AssetDetailsOnchain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The asset symbol | 
**name** | **str** | The asset name | 
**address** | **str** | The asset address | [optional] 
**decimals** | **float** | Number of decimals | 
**standards** | **List[str]** | Supported standards | [optional] 

## Example

```python
from fireblocks.models.asset_details_onchain import AssetDetailsOnchain

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDetailsOnchain from a JSON string
asset_details_onchain_instance = AssetDetailsOnchain.from_json(json)
# print the JSON string representation of the object
print(AssetDetailsOnchain.to_json())

# convert the object into a dict
asset_details_onchain_dict = asset_details_onchain_instance.to_dict()
# create an instance of AssetDetailsOnchain from a dict
asset_details_onchain_from_dict = AssetDetailsOnchain.from_dict(asset_details_onchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


