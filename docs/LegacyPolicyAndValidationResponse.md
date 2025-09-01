# LegacyPolicyAndValidationResponse

Policy validation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**LegacyPolicyResponse**](LegacyPolicyResponse.md) |  | 
**validation** | [**LegacyPolicyValidation**](LegacyPolicyValidation.md) |  | 

## Example

```python
from fireblocks.models.legacy_policy_and_validation_response import LegacyPolicyAndValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyAndValidationResponse from a JSON string
legacy_policy_and_validation_response_instance = LegacyPolicyAndValidationResponse.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyAndValidationResponse.to_json())

# convert the object into a dict
legacy_policy_and_validation_response_dict = legacy_policy_and_validation_response_instance.to_dict()
# create an instance of LegacyPolicyAndValidationResponse from a dict
legacy_policy_and_validation_response_from_dict = LegacyPolicyAndValidationResponse.from_dict(legacy_policy_and_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


