# GasStationConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_threshold** | **str** |  | [optional] 
**gas_cap** | **str** |  | [optional] 
**max_gas_price** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.gas_station_configuration_response import GasStationConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GasStationConfigurationResponse from a JSON string
gas_station_configuration_response_instance = GasStationConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(GasStationConfigurationResponse.to_json())

# convert the object into a dict
gas_station_configuration_response_dict = gas_station_configuration_response_instance.to_dict()
# create an instance of GasStationConfigurationResponse from a dict
gas_station_configuration_response_from_dict = GasStationConfigurationResponse.from_dict(gas_station_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


