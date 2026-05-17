# UsdcGatewayWalletStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The USDC Gateway wallet identifier | 
**status** | **str** | Current activation status of the USDC Gateway wallet | 

## Example

```python
from fireblocks.models.usdc_gateway_wallet_status_response import UsdcGatewayWalletStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsdcGatewayWalletStatusResponse from a JSON string
usdc_gateway_wallet_status_response_instance = UsdcGatewayWalletStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UsdcGatewayWalletStatusResponse.to_json())

# convert the object into a dict
usdc_gateway_wallet_status_response_dict = usdc_gateway_wallet_status_response_instance.to_dict()
# create an instance of UsdcGatewayWalletStatusResponse from a dict
usdc_gateway_wallet_status_response_from_dict = UsdcGatewayWalletStatusResponse.from_dict(usdc_gateway_wallet_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


