# WalletAssetAdditionalInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder_given_name** | **str** |  | [optional] 
**account_holder_surname** | **str** |  | [optional] 
**account_holder_city** | **str** |  | [optional] 
**account_holder_country** | **str** |  | [optional] 
**account_holder_address1** | **str** |  | [optional] 
**account_holder_address2** | **str** |  | [optional] 
**account_holder_district** | **str** |  | [optional] 
**account_holder_postal_code** | **str** |  | [optional] 
**aba_routing_number** | **str** |  | [optional] 
**aba_account_number** | **str** |  | [optional] 
**aba_country** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**iban_city** | **str** |  | [optional] 
**iban_country** | **str** |  | [optional] 
**spei_clabe** | **str** |  | [optional] 
**spei_name** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.wallet_asset_additional_info import WalletAssetAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WalletAssetAdditionalInfo from a JSON string
wallet_asset_additional_info_instance = WalletAssetAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print WalletAssetAdditionalInfo.to_json()

# convert the object into a dict
wallet_asset_additional_info_dict = wallet_asset_additional_info_instance.to_dict()
# create an instance of WalletAssetAdditionalInfo from a dict
wallet_asset_additional_info_form_dict = wallet_asset_additional_info.from_dict(wallet_asset_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


