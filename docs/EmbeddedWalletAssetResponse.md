# EmbeddedWalletAssetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**symbol** | **str** | The asset symbol | 
**name** | **str** | The asset name | 
**decimals** | **float** | Number of decimals | 
**network_protocol** | **str** | Netowrk protocol of the blockchain (BTC, ETH) | 
**testnet** | **bool** | Is in testnet | 
**has_fee** | **bool** | Has fee | 
**base_asset** | **str** | Base asset symbol BTC_TEST, ETH_TEST5) | 
**eth_network** | **str** |  | [optional] 
**eth_contract_address** | **str** |  | [optional] 
**issuer_address** | **str** | The address of the issuer of this token. Will be part of the identifier of this token on chain. | [optional] 
**blockchain_symbol** | **str** | Name of blockchain | [optional] 
**deprecated** | **bool** | Is blockchain deprecated | [optional] 
**coin_type** | **float** | Unique identifier of an asset (0 for BTC, 60 for ETH, etc.) | 
**blockchain** | **str** | The blockchain native asset id which the token is deployed on | 
**blockchain_display_name** | **str** | Name of blockchain | [optional] 
**algorithm** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.embedded_wallet_asset_response import EmbeddedWalletAssetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletAssetResponse from a JSON string
embedded_wallet_asset_response_instance = EmbeddedWalletAssetResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletAssetResponse.to_json())

# convert the object into a dict
embedded_wallet_asset_response_dict = embedded_wallet_asset_response_instance.to_dict()
# create an instance of EmbeddedWalletAssetResponse from a dict
embedded_wallet_asset_response_from_dict = EmbeddedWalletAssetResponse.from_dict(embedded_wallet_asset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


