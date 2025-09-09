# ExecutionResponseBaseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | Side of the order | [default to 'BUY']
**base_amount** | **str** | Amount to convert | 
**base_asset_id** | **str** | Source asset identifier | 
**base_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 
**quote_asset_id** | **str** | Target asset identifier | 
**quote_asset_rail** | [**TransferRail**](TransferRail.md) |  | [optional] 

## Example

```python
from fireblocks.models.execution_response_base_details import ExecutionResponseBaseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionResponseBaseDetails from a JSON string
execution_response_base_details_instance = ExecutionResponseBaseDetails.from_json(json)
# print the JSON string representation of the object
print(ExecutionResponseBaseDetails.to_json())

# convert the object into a dict
execution_response_base_details_dict = execution_response_base_details_instance.to_dict()
# create an instance of ExecutionResponseBaseDetails from a dict
execution_response_base_details_from_dict = ExecutionResponseBaseDetails.from_dict(execution_response_base_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


