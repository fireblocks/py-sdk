# TRLinkAssetsListPagedResponse

Paginated list of supported assets with partner capability flag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TRLinkPublicAssetInfo]**](TRLinkPublicAssetInfo.md) | List of supported assets | 
**paging** | [**TRLinkPaging**](TRLinkPaging.md) |  | [optional] 
**partner_can_handle_any_asset** | **bool** | Whether partner can handle any asset (not just explicitly listed ones) | 
**note** | **str** | Note about asset support capabilities | 

## Example

```python
from fireblocks.models.tr_link_assets_list_paged_response import TRLinkAssetsListPagedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAssetsListPagedResponse from a JSON string
tr_link_assets_list_paged_response_instance = TRLinkAssetsListPagedResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkAssetsListPagedResponse.to_json())

# convert the object into a dict
tr_link_assets_list_paged_response_dict = tr_link_assets_list_paged_response_instance.to_dict()
# create an instance of TRLinkAssetsListPagedResponse from a dict
tr_link_assets_list_paged_response_from_dict = TRLinkAssetsListPagedResponse.from_dict(tr_link_assets_list_paged_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


