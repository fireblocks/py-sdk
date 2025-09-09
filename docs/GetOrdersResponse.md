# GetOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OrderSummary]**](OrderSummary.md) |  | 
**total** | **int** | Total number of orders matching the query. | 
**next** | **str** | A cursor for the next page of results, if available. | [optional] 

## Example

```python
from fireblocks.models.get_orders_response import GetOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrdersResponse from a JSON string
get_orders_response_instance = GetOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrdersResponse.to_json())

# convert the object into a dict
get_orders_response_dict = get_orders_response_instance.to_dict()
# create an instance of GetOrdersResponse from a dict
get_orders_response_from_dict = GetOrdersResponse.from_dict(get_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


