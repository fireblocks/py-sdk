# ExecutionRequestBaseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | [**Side**](Side.md) |  | 
**base_amount** | **str** | Amount in baseAssetId. BUY &#x3D; base amount to receive; SELL &#x3D; base amount to sell. | 
**base_asset_id** | **str** | The asset you receive on BUY / give on SELL. | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Counter asset used to pay/receive | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_request_base_details import ExecutionRequestBaseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionRequestBaseDetails from a JSON string
execution_request_base_details_instance = ExecutionRequestBaseDetails.from_json(json)
# print the JSON string representation of the object
print(ExecutionRequestBaseDetails.to_json())

# convert the object into a dict
execution_request_base_details_dict = execution_request_base_details_instance.to_dict()
# create an instance of ExecutionRequestBaseDetails from a dict
execution_request_base_details_from_dict = ExecutionRequestBaseDetails.from_dict(execution_request_base_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


