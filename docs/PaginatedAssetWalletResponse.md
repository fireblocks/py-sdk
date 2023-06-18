# PaginatedAssetWalletResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_wallets** | [**List[AssetWallet]**](AssetWallet.md) |  | [optional] 
**paging** | [**PaginatedAssetWalletResponsePaging**](PaginatedAssetWalletResponsePaging.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.paginated_asset_wallet_response import PaginatedAssetWalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAssetWalletResponse from a JSON string
paginated_asset_wallet_response_instance = PaginatedAssetWalletResponse.from_json(json)
# print the JSON string representation of the object
print PaginatedAssetWalletResponse.to_json()

# convert the object into a dict
paginated_asset_wallet_response_dict = paginated_asset_wallet_response_instance.to_dict()
# create an instance of PaginatedAssetWalletResponse from a dict
paginated_asset_wallet_response_form_dict = paginated_asset_wallet_response.from_dict(paginated_asset_wallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


