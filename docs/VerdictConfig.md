# VerdictConfig

Verdict configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Verdict action | 
**approvers** | [**ApproversConfig**](ApproversConfig.md) |  | [optional] 
**designated_signers** | [**DesignatedSignersConfig**](DesignatedSignersConfig.md) |  | [optional] 

## Example

```python
from fireblocks.models.verdict_config import VerdictConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VerdictConfig from a JSON string
verdict_config_instance = VerdictConfig.from_json(json)
# print the JSON string representation of the object
print(VerdictConfig.to_json())

# convert the object into a dict
verdict_config_dict = verdict_config_instance.to_dict()
# create an instance of VerdictConfig from a dict
verdict_config_from_dict = VerdictConfig.from_dict(verdict_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


