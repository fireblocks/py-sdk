# CreateVaultAccountAssetAddressRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | (Optional) Attach a description to the new address | [optional] 
**customer_ref_id** | **str** | Optional - Sets a customer reference ID | [optional] 

## Example

```python
from fireblocks_client.models.create_vault_account_asset_address_request import CreateVaultAccountAssetAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVaultAccountAssetAddressRequest from a JSON string
create_vault_account_asset_address_request_instance = CreateVaultAccountAssetAddressRequest.from_json(json)
# print the JSON string representation of the object
print CreateVaultAccountAssetAddressRequest.to_json()

# convert the object into a dict
create_vault_account_asset_address_request_dict = create_vault_account_asset_address_request_instance.to_dict()
# create an instance of CreateVaultAccountAssetAddressRequest from a dict
create_vault_account_asset_address_request_form_dict = create_vault_account_asset_address_request.from_dict(create_vault_account_asset_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


