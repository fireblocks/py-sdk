# AssetConfig

Policy asset configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nft_transfer** | **bool** | Whether this is an NFT transfer | 
**asset_types** | [**List[AssetTypesConfigInner]**](AssetTypesConfigInner.md) | List of asset types | [optional] 
**operator** | [**PolicyOperator**](PolicyOperator.md) |  | [optional] 

## Example

```python
from fireblocks.models.asset_config import AssetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AssetConfig from a JSON string
asset_config_instance = AssetConfig.from_json(json)
# print the JSON string representation of the object
print(AssetConfig.to_json())

# convert the object into a dict
asset_config_dict = asset_config_instance.to_dict()
# create an instance of AssetConfig from a dict
asset_config_from_dict = AssetConfig.from_dict(asset_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


