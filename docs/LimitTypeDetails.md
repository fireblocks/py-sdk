# LimitTypeDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Order type for limit orders | 
**time_in_force** | [**TimeInForce**](TimeInForce.md) |  | 
**limit_price** | **str** | Price for limit orders | 

## Example

```python
from fireblocks.models.limit_type_details import LimitTypeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LimitTypeDetails from a JSON string
limit_type_details_instance = LimitTypeDetails.from_json(json)
# print the JSON string representation of the object
print(LimitTypeDetails.to_json())

# convert the object into a dict
limit_type_details_dict = limit_type_details_instance.to_dict()
# create an instance of LimitTypeDetails from a dict
limit_type_details_from_dict = LimitTypeDetails.from_dict(limit_type_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


