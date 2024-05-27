# AssetMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The Fireblocks&#x60; asset id | 
**name** | **str** | The name of the token | [optional] 
**symbol** | **str** | The symbol of the token | [optional] 
**network_protocol** | **str** | The network protocol of the token | [optional] 
**total_supply** | **str** | The total supply of the token | [optional] 
**holders_count** | **float** | The number of holders of the token | [optional] 
**type** | **str** | The type of the token | [optional] 
**contract_address** | **str** | The address of the token contract | [optional] 
**issuer_address** | **str** | In case of Stellar or Ripple, the address of the issuer of the token | [optional] 
**testnet** | **bool** | Is it deployed on testnet or to mainnet | [optional] 
**blockchain** | **str** | The blockchain native asset id which the token is deployed on | [optional] 
**decimals** | **float** | The number of decimals of the token | [optional] 
**vault_account_id** | **str** | The id of the vault account that initiated the request to issue the token. Will be empty if token was issued outside of Fireblocks. | [optional] 

## Example

```python
from fireblocks_client.models.asset_metadata_dto import AssetMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMetadataDto from a JSON string
asset_metadata_dto_instance = AssetMetadataDto.from_json(json)
# print the JSON string representation of the object
print AssetMetadataDto.to_json()

# convert the object into a dict
asset_metadata_dto_dict = asset_metadata_dto_instance.to_dict()
# create an instance of AssetMetadataDto from a dict
asset_metadata_dto_form_dict = asset_metadata_dto.from_dict(asset_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


