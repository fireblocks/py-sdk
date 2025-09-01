# AddAssetToExternalWalletRequest

Request schema for adding an asset to an external wallet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet&#39;s address (or xpub) of the external wallet | 
**tag** | **str** | For XRP wallets, the destination tag; for EOS/XLM, the memo; for the fiat providers (BLINC by BCB Group), the Bank Transfer Description | [optional] 
**additional_info** | [**AdditionalInfoRequestAdditionalInfo**](AdditionalInfoRequestAdditionalInfo.md) |  | 

## Example

```python
from fireblocks.models.add_asset_to_external_wallet_request import AddAssetToExternalWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAssetToExternalWalletRequest from a JSON string
add_asset_to_external_wallet_request_instance = AddAssetToExternalWalletRequest.from_json(json)
# print the JSON string representation of the object
print(AddAssetToExternalWalletRequest.to_json())

# convert the object into a dict
add_asset_to_external_wallet_request_dict = add_asset_to_external_wallet_request_instance.to_dict()
# create an instance of AddAssetToExternalWalletRequest from a dict
add_asset_to_external_wallet_request_from_dict = AddAssetToExternalWalletRequest.from_dict(add_asset_to_external_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


