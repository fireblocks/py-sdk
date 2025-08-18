# DvnConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvn_addresses** | **List[str]** | Array of required DVN Ethereum addresses that sign ULN messages. | 
**optional_dvn_addresses** | **List[str]** | Array of optional DVN Ethereum addresses that sign ULN messages. | [optional] 
**optional_threshold** | **float** | Minimum number of DVN signatures required (M-of-N). | 

## Example

```python
from fireblocks.models.dvn_config import DvnConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DvnConfig from a JSON string
dvn_config_instance = DvnConfig.from_json(json)
# print the JSON string representation of the object
print(DvnConfig.to_json())

# convert the object into a dict
dvn_config_dict = dvn_config_instance.to_dict()
# create an instance of DvnConfig from a dict
dvn_config_from_dict = DvnConfig.from_dict(dvn_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


