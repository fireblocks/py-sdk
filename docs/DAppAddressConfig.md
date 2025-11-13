# DAppAddressConfig

dApp address configuration for policy rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_whitelisted** | **List[str]** | Globally whitelisted addresses | 
**tenant_whitelisted** | **List[str]** | Tenant whitelisted addresses | 
**urls** | **List[str]** | Allowed all address | 
**operator** | [**PolicyOperator**](PolicyOperator.md) |  | 

## Example

```python
from fireblocks.models.d_app_address_config import DAppAddressConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DAppAddressConfig from a JSON string
d_app_address_config_instance = DAppAddressConfig.from_json(json)
# print the JSON string representation of the object
print(DAppAddressConfig.to_json())

# convert the object into a dict
d_app_address_config_dict = d_app_address_config_instance.to_dict()
# create an instance of DAppAddressConfig from a dict
d_app_address_config_from_dict = DAppAddressConfig.from_dict(d_app_address_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


