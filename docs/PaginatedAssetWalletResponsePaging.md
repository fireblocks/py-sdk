# PaginatedAssetWalletResponsePaging


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** | A string representing a cursor. Users can use this with a new request to this API endpoint as the “before” request parameter to fetch the previous page of results. | [optional] 
**after** | **str** | A string representing a cursor. Users can use this with a new request to this API endpoint as the “before” request parameter to fetch the next page of results. | [optional] 

## Example

```python
from fireblocks_client.models.paginated_asset_wallet_response_paging import PaginatedAssetWalletResponsePaging

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssetWalletResponsePaging from a JSON string
paginated_asset_wallet_response_paging_instance = PaginatedAssetWalletResponsePaging.from_json(json)
# print the JSON string representation of the object
print PaginatedAssetWalletResponsePaging.to_json()

# convert the object into a dict
paginated_asset_wallet_response_paging_dict = paginated_asset_wallet_response_paging_instance.to_dict()
# create an instance of PaginatedAssetWalletResponsePaging from a dict
paginated_asset_wallet_response_paging_form_dict = paginated_asset_wallet_response_paging.from_dict(paginated_asset_wallet_response_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


