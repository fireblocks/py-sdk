# ArsConfigResponse

ARS (Address Registry Screening) configuration for the tenant: active flag and last update time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether ARS is active for the tenant | [optional] 
**last_update** | **datetime** | Last update timestamp of the configuration | [optional] 

## Example

```python
from fireblocks.models.ars_config_response import ArsConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArsConfigResponse from a JSON string
ars_config_response_instance = ArsConfigResponse.from_json(json)
# print the JSON string representation of the object
print(ArsConfigResponse.to_json())

# convert the object into a dict
ars_config_response_dict = ars_config_response_instance.to_dict()
# create an instance of ArsConfigResponse from a dict
ars_config_response_from_dict = ArsConfigResponse.from_dict(ars_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


