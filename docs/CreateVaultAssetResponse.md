# CreateVaultAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**legacy_address** | **str** |  | [optional] 
**enterprise_address** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**eos_account_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**activation_tx_id** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.create_vault_asset_response import CreateVaultAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVaultAssetResponse from a JSON string
create_vault_asset_response_instance = CreateVaultAssetResponse.from_json(json)
# print the JSON string representation of the object
print(CreateVaultAssetResponse.to_json())

# convert the object into a dict
create_vault_asset_response_dict = create_vault_asset_response_instance.to_dict()
# create an instance of CreateVaultAssetResponse from a dict
create_vault_asset_response_from_dict = CreateVaultAssetResponse.from_dict(create_vault_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


