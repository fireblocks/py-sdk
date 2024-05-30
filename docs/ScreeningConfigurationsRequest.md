# ScreeningConfigurationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_screening_during_service_outages** | **bool** | Flag to enable or disable bypass screening during service outages. | [optional] 
**inbound_transaction_delay** | **float** | Inbound transaction delay in seconds. | [optional] 
**outbound_transaction_delay** | **float** | Outbound transaction delay in seconds. | [optional] 

## Example

```python
from fireblocks_client.models.screening_configurations_request import ScreeningConfigurationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningConfigurationsRequest from a JSON string
screening_configurations_request_instance = ScreeningConfigurationsRequest.from_json(json)
# print the JSON string representation of the object
print(ScreeningConfigurationsRequest.to_json())

# convert the object into a dict
screening_configurations_request_dict = screening_configurations_request_instance.to_dict()
# create an instance of ScreeningConfigurationsRequest from a dict
screening_configurations_request_from_dict = ScreeningConfigurationsRequest.from_dict(screening_configurations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


