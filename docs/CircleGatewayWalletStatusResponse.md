# CircleGatewayWalletStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | The Circle Gateway wallet identifier | 
**status** | **str** | Current activation status of the Circle Gateway wallet | 

## Example

```python
from fireblocks.models.circle_gateway_wallet_status_response import CircleGatewayWalletStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CircleGatewayWalletStatusResponse from a JSON string
circle_gateway_wallet_status_response_instance = CircleGatewayWalletStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CircleGatewayWalletStatusResponse.to_json())

# convert the object into a dict
circle_gateway_wallet_status_response_dict = circle_gateway_wallet_status_response_instance.to_dict()
# create an instance of CircleGatewayWalletStatusResponse from a dict
circle_gateway_wallet_status_response_from_dict = CircleGatewayWalletStatusResponse.from_dict(circle_gateway_wallet_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


