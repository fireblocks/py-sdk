# CircleGatewayWalletInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The Circle Gateway wallet identifier | 
**type** | **str** | The Circle Gateway provider identifier | 
**status** | **str** | Current activation status of the Circle Gateway wallet | 
**symbol** | **str** | The token symbol supported by this wallet (e.g. USDC) | 
**asset_ids** | **List[str]** | Fireblocks asset IDs available for this wallet | 

## Example

```python
from fireblocks.models.circle_gateway_wallet_info_response import CircleGatewayWalletInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CircleGatewayWalletInfoResponse from a JSON string
circle_gateway_wallet_info_response_instance = CircleGatewayWalletInfoResponse.from_json(json)
# print the JSON string representation of the object
print(CircleGatewayWalletInfoResponse.to_json())

# convert the object into a dict
circle_gateway_wallet_info_response_dict = circle_gateway_wallet_info_response_instance.to_dict()
# create an instance of CircleGatewayWalletInfoResponse from a dict
circle_gateway_wallet_info_response_from_dict = CircleGatewayWalletInfoResponse.from_dict(circle_gateway_wallet_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


