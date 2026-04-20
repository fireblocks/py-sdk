# EarnAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Contract address of the token on-chain. | [optional] 
**symbol** | **str** | Human-readable ticker (e.g. USDC). | [optional] 
**decimals** | **int** | Token decimals used when interpreting on-chain amounts. | [optional] 
**asset_id** | **str** | Fireblocks legacy asset identifier (e.g. USDC_ETH, PYUSD). | [optional] 

## Example

```python
from fireblocks.models.earn_asset import EarnAsset

# TODO update the JSON string below
json = "{}"
# create an instance of EarnAsset from a JSON string
earn_asset_instance = EarnAsset.from_json(json)
# print the JSON string representation of the object
print(EarnAsset.to_json())

# convert the object into a dict
earn_asset_dict = earn_asset_instance.to_dict()
# create an instance of EarnAsset from a dict
earn_asset_from_dict = EarnAsset.from_dict(earn_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


