# AssetResponseOnchain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | The asset symbol | 
**name** | **str** | The asset name | 
**address** | **str** | The asset address | [optional] 
**decimals** | **float** | Number of decimals | 
**standard** | **str** | The asset standard | 

## Example

```python
from fireblocks_client.models.asset_response_onchain import AssetResponseOnchain

# TODO update the JSON string below
json = "{}"
# create an instance of AssetResponseOnchain from a JSON string
asset_response_onchain_instance = AssetResponseOnchain.from_json(json)
# print the JSON string representation of the object
print AssetResponseOnchain.to_json()

# convert the object into a dict
asset_response_onchain_dict = asset_response_onchain_instance.to_dict()
# create an instance of AssetResponseOnchain from a dict
asset_response_onchain_form_dict = asset_response_onchain.from_dict(asset_response_onchain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


