# Exposure

Vault allocation exposure item (Morpho MetaMorpho allocation slice).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Contract address of the exposure token on-chain. | 
**amount** | **str** | Human-readable token amount (raw on-chain value scaled by 10^decimals). | 
**symbol** | **str** | Human-readable ticker (e.g. USDC). | [optional] 
**decimals** | **int** | Token decimals used when interpreting on-chain amounts. | [optional] 
**asset_id** | **str** | Fireblocks legacy asset identifier (e.g. USDC_ETH, PYUSD); only present when resolved via asset-service. | [optional] 
**amount_usd** | **str** | USD notional value of the exposure amount. | [optional] 

## Example

```python
from fireblocks.models.exposure import Exposure

# TODO update the JSON string below
json = "{}"
# create an instance of Exposure from a JSON string
exposure_instance = Exposure.from_json(json)
# print the JSON string representation of the object
print(Exposure.to_json())

# convert the object into a dict
exposure_dict = exposure_instance.to_dict()
# create an instance of Exposure from a dict
exposure_from_dict = Exposure.from_dict(exposure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


