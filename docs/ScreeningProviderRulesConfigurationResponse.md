# ScreeningProviderRulesConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**amount_usd** | **float** |  | [optional] 
**amount** | **float** |  | [optional] 
**asset** | **str** |  | [optional] 
**action** | **str** |  | 

## Example

```python
from fireblocks_client.models.screening_provider_rules_configuration_response import ScreeningProviderRulesConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningProviderRulesConfigurationResponse from a JSON string
screening_provider_rules_configuration_response_instance = ScreeningProviderRulesConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(ScreeningProviderRulesConfigurationResponse.to_json())

# convert the object into a dict
screening_provider_rules_configuration_response_dict = screening_provider_rules_configuration_response_instance.to_dict()
# create an instance of ScreeningProviderRulesConfigurationResponse from a dict
screening_provider_rules_configuration_response_from_dict = ScreeningProviderRulesConfigurationResponse.from_dict(screening_provider_rules_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


