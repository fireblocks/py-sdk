# EditGasStationConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates whether editing the gas station configuration was successful | 

## Example

```python
from fireblocks.models.edit_gas_station_configuration_response import EditGasStationConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditGasStationConfigurationResponse from a JSON string
edit_gas_station_configuration_response_instance = EditGasStationConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(EditGasStationConfigurationResponse.to_json())

# convert the object into a dict
edit_gas_station_configuration_response_dict = edit_gas_station_configuration_response_instance.to_dict()
# create an instance of EditGasStationConfigurationResponse from a dict
edit_gas_station_configuration_response_from_dict = EditGasStationConfigurationResponse.from_dict(edit_gas_station_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


