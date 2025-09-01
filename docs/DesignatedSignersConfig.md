# DesignatedSignersConfig

Designated signers configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of designated signers | 
**users** | **List[str]** | List of user IDs | [optional] 
**groups** | **List[str]** | List of policy group IDs | [optional] 

## Example

```python
from fireblocks.models.designated_signers_config import DesignatedSignersConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DesignatedSignersConfig from a JSON string
designated_signers_config_instance = DesignatedSignersConfig.from_json(json)
# print the JSON string representation of the object
print(DesignatedSignersConfig.to_json())

# convert the object into a dict
designated_signers_config_dict = designated_signers_config_instance.to_dict()
# create an instance of DesignatedSignersConfig from a dict
designated_signers_config_from_dict = DesignatedSignersConfig.from_dict(designated_signers_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


