# SetAutoFuelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_fuel** | **bool** | Auto Fuel | [optional] 

## Example

```python
from fireblocks_client.models.set_auto_fuel_request import SetAutoFuelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAutoFuelRequest from a JSON string
set_auto_fuel_request_instance = SetAutoFuelRequest.from_json(json)
# print the JSON string representation of the object
print(SetAutoFuelRequest.to_json())

# convert the object into a dict
set_auto_fuel_request_dict = set_auto_fuel_request_instance.to_dict()
# create an instance of SetAutoFuelRequest from a dict
set_auto_fuel_request_from_dict = SetAutoFuelRequest.from_dict(set_auto_fuel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


