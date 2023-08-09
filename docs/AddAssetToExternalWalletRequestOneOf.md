# AddAssetToExternalWalletRequestOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet&#39;s address (or xpub) of the wallet | 
**tag** | **str** | For XRP wallets, the destination tag; for EOS/XLM, the memo; for the fiat providers (BLINC by BCB Group), the Bank Transfer Description | [optional] 

## Example

```python
from fireblocks_client.models.add_asset_to_external_wallet_request_one_of import AddAssetToExternalWalletRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AddAssetToExternalWalletRequestOneOf from a JSON string
add_asset_to_external_wallet_request_one_of_instance = AddAssetToExternalWalletRequestOneOf.from_json(json)
# print the JSON string representation of the object
print AddAssetToExternalWalletRequestOneOf.to_json()

# convert the object into a dict
add_asset_to_external_wallet_request_one_of_dict = add_asset_to_external_wallet_request_one_of_instance.to_dict()
# create an instance of AddAssetToExternalWalletRequestOneOf from a dict
add_asset_to_external_wallet_request_one_of_form_dict = add_asset_to_external_wallet_request_one_of.from_dict(add_asset_to_external_wallet_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


