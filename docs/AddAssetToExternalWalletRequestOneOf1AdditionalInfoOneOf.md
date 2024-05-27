# AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder_given_name** | **str** |  | 
**account_holder_surname** | **str** |  | [optional] 
**account_holder_city** | **str** |  | 
**account_holder_country** | **str** |  | 
**account_holder_address1** | **str** |  | 
**account_holder_address2** | **str** |  | [optional] 
**account_holder_district** | **str** |  | [optional] 
**account_holder_postal_code** | **str** |  | 
**iban** | **str** |  | 
**iban_city** | **str** |  | 
**iban_country** | **str** |  | 

## Example

```python
from fireblocks_client.models.add_asset_to_external_wallet_request_one_of1_additional_info_one_of import AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf from a JSON string
add_asset_to_external_wallet_request_one_of1_additional_info_one_of_instance = AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf.from_json(json)
# print the JSON string representation of the object
print AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf.to_json()

# convert the object into a dict
add_asset_to_external_wallet_request_one_of1_additional_info_one_of_dict = add_asset_to_external_wallet_request_one_of1_additional_info_one_of_instance.to_dict()
# create an instance of AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf from a dict
add_asset_to_external_wallet_request_one_of1_additional_info_one_of_form_dict = add_asset_to_external_wallet_request_one_of1_additional_info_one_of.from_dict(add_asset_to_external_wallet_request_one_of1_additional_info_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


