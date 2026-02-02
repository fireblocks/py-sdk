# TRLinkPublicAssetInfo

Public asset information with limited properties for API consumption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the asset (e.g., Fireblocks asset ID) | 
**name** | **str** | The name of the asset | 
**type** | **str** | The type of the asset (e.g., BASE_ASSET, ERC20) | 
**contract_address** | **str** | The contract address of the asset (for tokenized assets) | 
**native_asset** | **str** | The native asset of the network (e.g., ETH for ERC20 tokens) | 
**decimals** | **float** | The number of decimal places for the asset | 
**issuer_address** | **str** | The issuer address of the asset (optional) | [optional] 

## Example

```python
from fireblocks.models.tr_link_public_asset_info import TRLinkPublicAssetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkPublicAssetInfo from a JSON string
tr_link_public_asset_info_instance = TRLinkPublicAssetInfo.from_json(json)
# print the JSON string representation of the object
print(TRLinkPublicAssetInfo.to_json())

# convert the object into a dict
tr_link_public_asset_info_dict = tr_link_public_asset_info_instance.to_dict()
# create an instance of TRLinkPublicAssetInfo from a dict
tr_link_public_asset_info_from_dict = TRLinkPublicAssetInfo.from_dict(tr_link_public_asset_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


