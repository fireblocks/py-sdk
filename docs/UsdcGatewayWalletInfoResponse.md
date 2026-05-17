# UsdcGatewayWalletInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The USDC Gateway wallet identifier | 
**type** | **str** | The USDC Gateway provider identifier | 
**status** | **str** | Current activation status of the USDC Gateway wallet | 
**symbol** | **str** | The token symbol supported by this wallet (e.g. USDC) | 
**asset_ids** | **List[str]** | Fireblocks asset IDs available for this wallet | 

## Example

```python
from fireblocks.models.usdc_gateway_wallet_info_response import UsdcGatewayWalletInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsdcGatewayWalletInfoResponse from a JSON string
usdc_gateway_wallet_info_response_instance = UsdcGatewayWalletInfoResponse.from_json(json)
# print the JSON string representation of the object
print(UsdcGatewayWalletInfoResponse.to_json())

# convert the object into a dict
usdc_gateway_wallet_info_response_dict = usdc_gateway_wallet_info_response_instance.to_dict()
# create an instance of UsdcGatewayWalletInfoResponse from a dict
usdc_gateway_wallet_info_response_from_dict = UsdcGatewayWalletInfoResponse.from_dict(usdc_gateway_wallet_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


