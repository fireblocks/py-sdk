# AssetOnchainBeta


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
from fireblocks.models.asset_onchain_beta import AssetOnchainBeta

# TODO update the JSON string below
json = "{}"
# create an instance of AssetOnchainBeta from a JSON string
asset_onchain_beta_instance = AssetOnchainBeta.from_json(json)
# print the JSON string representation of the object
print(AssetOnchainBeta.to_json())

# convert the object into a dict
asset_onchain_beta_dict = asset_onchain_beta_instance.to_dict()
# create an instance of AssetOnchainBeta from a dict
asset_onchain_beta_from_dict = AssetOnchainBeta.from_dict(asset_onchain_beta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


