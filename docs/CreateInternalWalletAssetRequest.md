# CreateInternalWalletAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet&#39;s address or, for EOS wallets, the account name | 
**tag** | **str** | for XRP wallets, the destination tag; for EOS, the memo; for the fiat providers (BLINC by BCB Group), the Bank Transfer Description | [optional] 

## Example

```python
from fireblocks_client.models.create_internal_wallet_asset_request import CreateInternalWalletAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInternalWalletAssetRequest from a JSON string
create_internal_wallet_asset_request_instance = CreateInternalWalletAssetRequest.from_json(json)
# print the JSON string representation of the object
print CreateInternalWalletAssetRequest.to_json()

# convert the object into a dict
create_internal_wallet_asset_request_dict = create_internal_wallet_asset_request_instance.to_dict()
# create an instance of CreateInternalWalletAssetRequest from a dict
create_internal_wallet_asset_request_form_dict = create_internal_wallet_asset_request.from_dict(create_internal_wallet_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


