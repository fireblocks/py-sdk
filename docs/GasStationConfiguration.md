# GasStationConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas_threshold** | **str** |  | [optional] 
**gas_cap** | **str** |  | [optional] 
**max_gas_price** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.gas_station_configuration import GasStationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GasStationConfiguration from a JSON string
gas_station_configuration_instance = GasStationConfiguration.from_json(json)
# print the JSON string representation of the object
print(GasStationConfiguration.to_json())

# convert the object into a dict
gas_station_configuration_dict = gas_station_configuration_instance.to_dict()
# create an instance of GasStationConfiguration from a dict
gas_station_configuration_from_dict = GasStationConfiguration.from_dict(gas_station_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


