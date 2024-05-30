# VaultWalletAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**customer_ref_id** | **str** |  | [optional] 
**address_format** | **str** |  | [optional] 
**legacy_address** | **str** |  | [optional] 
**enterprise_address** | **str** |  | [optional] 
**bip44_address_index** | **int** |  | [optional] 
**user_defined** | **bool** |  | [optional] 

## Example

```python
from fireblocks.models.vault_wallet_address import VaultWalletAddress

# TODO update the JSON string below
json = "{}"
# create an instance of VaultWalletAddress from a JSON string
vault_wallet_address_instance = VaultWalletAddress.from_json(json)
# print the JSON string representation of the object
print(VaultWalletAddress.to_json())

# convert the object into a dict
vault_wallet_address_dict = vault_wallet_address_instance.to_dict()
# create an instance of VaultWalletAddress from a dict
vault_wallet_address_from_dict = VaultWalletAddress.from_dict(vault_wallet_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


