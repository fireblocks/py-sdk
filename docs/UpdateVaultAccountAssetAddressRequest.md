# UpdateVaultAccountAssetAddressRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The address description | [optional] 

## Example

```python
from fireblocks_client.models.update_vault_account_asset_address_request import UpdateVaultAccountAssetAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVaultAccountAssetAddressRequest from a JSON string
update_vault_account_asset_address_request_instance = UpdateVaultAccountAssetAddressRequest.from_json(json)
# print the JSON string representation of the object
print UpdateVaultAccountAssetAddressRequest.to_json()

# convert the object into a dict
update_vault_account_asset_address_request_dict = update_vault_account_asset_address_request_instance.to_dict()
# create an instance of UpdateVaultAccountAssetAddressRequest from a dict
update_vault_account_asset_address_request_form_dict = update_vault_account_asset_address_request.from_dict(update_vault_account_asset_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


