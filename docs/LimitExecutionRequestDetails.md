# LimitExecutionRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**LimitTypeEnum**](LimitTypeEnum.md) |  | 
**price** | **str** | Limit price for the order | 
**time_in_force** | [**TimeInForce**](TimeInForce.md) |  | 
**side** | [**Side**](Side.md) |  | 
**base_amount** | **str** | Amount in baseAssetId. BUY &#x3D; base amount to receive; SELL &#x3D; base amount to sell. | 
**base_asset_id** | **str** | The asset you receive on BUY / give on SELL. | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Counter asset used to pay/receive | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 

## Example

```python
from fireblocks.models.limit_execution_request_details import LimitExecutionRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LimitExecutionRequestDetails from a JSON string
limit_execution_request_details_instance = LimitExecutionRequestDetails.from_json(json)
# print the JSON string representation of the object
print(LimitExecutionRequestDetails.to_json())

# convert the object into a dict
limit_execution_request_details_dict = limit_execution_request_details_instance.to_dict()
# create an instance of LimitExecutionRequestDetails from a dict
limit_execution_request_details_from_dict = LimitExecutionRequestDetails.from_dict(limit_execution_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


