# TokenLinkDtoTokenMetadata

The token's metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** | The Fireblocks&#x60; asset id | 
**name** | **str** | Collection name | [optional] 
**symbol** | **str** | Collection symbol | [optional] 
**network_protocol** | **str** | The network protocol of the token | [optional] 
**total_supply** | **str** | The total supply of the token | [optional] 
**holders_count** | **float** | The number of holders of the token | [optional] 
**type** | **str** | The type of the token | [optional] 
**contract_address** | **str** | The address of the token contract | 
**issuer_address** | **str** | In case of Stellar or Ripple, the address of the issuer of the token | [optional] 
**testnet** | **bool** | Is it deployed on testnet or to mainnet | [optional] 
**blockchain** | **str** | The blockchain native asset id which the token is deployed on | [optional] 
**decimals** | **float** | The number of decimals of the token | [optional] 
**vault_account_id** | **str** | The vault account ID that initiated the request to issue the token | [optional] 
**fb_collection_id** | **str** | Fireblocks collection id | 
**standard** | **str** | Collection contract standard | [optional] 
**blockchain_descriptor** | **str** | Collection&#39;s blockchain | 
**id** | **str** | The deployed contract ID | 
**blockchain_id** | **str** | The blockchain ID | 
**contract_template_id** | **str** | The contract template ID | 

## Example

```python
from fireblocks.models.token_link_dto_token_metadata import TokenLinkDtoTokenMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TokenLinkDtoTokenMetadata from a JSON string
token_link_dto_token_metadata_instance = TokenLinkDtoTokenMetadata.from_json(json)
# print the JSON string representation of the object
print(TokenLinkDtoTokenMetadata.to_json())

# convert the object into a dict
token_link_dto_token_metadata_dict = token_link_dto_token_metadata_instance.to_dict()
# create an instance of TokenLinkDtoTokenMetadata from a dict
token_link_dto_token_metadata_from_dict = TokenLinkDtoTokenMetadata.from_dict(token_link_dto_token_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


