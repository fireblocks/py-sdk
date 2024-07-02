# RegisterNewAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockchain_id** | **str** | Native asset ID of the blockchain | 
**address** | **str** | Asset address. - EVM-based chains: token contract address - Stellar (XLM): issuer address - Algorand (ALGO): asset ID - TRON (TRX): token contract address - NEAR: token address - Solana: token&#39;s mint account address  | 
**symbol** | **str** | Required for Stellar only, asset code is expected. | [optional] 

## Example

```python
from fireblocks.models.register_new_asset_request import RegisterNewAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterNewAssetRequest from a JSON string
register_new_asset_request_instance = RegisterNewAssetRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterNewAssetRequest.to_json())

# convert the object into a dict
register_new_asset_request_dict = register_new_asset_request_instance.to_dict()
# create an instance of RegisterNewAssetRequest from a dict
register_new_asset_request_from_dict = RegisterNewAssetRequest.from_dict(register_new_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


