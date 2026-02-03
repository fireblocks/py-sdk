# TRLinkGetSupportedAssetResponse

Response for getting a single supported asset by ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fireblocks_asset** | [**TRLinkPublicAssetInfo**](TRLinkPublicAssetInfo.md) |  | 
**partner_response** | **Dict[str, object]** | Raw partner response data | 
**partner_can_handle_any_asset** | **bool** | Whether partner can handle any asset (not just explicitly listed ones) | 
**note** | **str** | Note about asset support capabilities | 
**supported** | **bool** | Whether the asset is supported by the partner | 

## Example

```python
from fireblocks.models.tr_link_get_supported_asset_response import TRLinkGetSupportedAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkGetSupportedAssetResponse from a JSON string
tr_link_get_supported_asset_response_instance = TRLinkGetSupportedAssetResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkGetSupportedAssetResponse.to_json())

# convert the object into a dict
tr_link_get_supported_asset_response_dict = tr_link_get_supported_asset_response_instance.to_dict()
# create an instance of TRLinkGetSupportedAssetResponse from a dict
tr_link_get_supported_asset_response_from_dict = TRLinkGetSupportedAssetResponse.from_dict(tr_link_get_supported_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


