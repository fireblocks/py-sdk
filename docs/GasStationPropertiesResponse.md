# GasStationPropertiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **object** |  | [optional] 
**configuration** | [**GasStationConfigurationResponse**](GasStationConfigurationResponse.md) |  | [optional] 

## Example

```python
from fireblocks.models.gas_station_properties_response import GasStationPropertiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GasStationPropertiesResponse from a JSON string
gas_station_properties_response_instance = GasStationPropertiesResponse.from_json(json)
# print the JSON string representation of the object
print(GasStationPropertiesResponse.to_json())

# convert the object into a dict
gas_station_properties_response_dict = gas_station_properties_response_instance.to_dict()
# create an instance of GasStationPropertiesResponse from a dict
gas_station_properties_response_from_dict = GasStationPropertiesResponse.from_dict(gas_station_properties_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


