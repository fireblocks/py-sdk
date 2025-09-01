# LegacyPolicyValidation

Policy validation object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Validation status | 
**check_result** | [**LegacyPolicyCheckResult**](LegacyPolicyCheckResult.md) |  | 

## Example

```python
from fireblocks.models.legacy_policy_validation import LegacyPolicyValidation

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyValidation from a JSON string
legacy_policy_validation_instance = LegacyPolicyValidation.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyValidation.to_json())

# convert the object into a dict
legacy_policy_validation_dict = legacy_policy_validation_instance.to_dict()
# create an instance of LegacyPolicyValidation from a dict
legacy_policy_validation_from_dict = LegacyPolicyValidation.from_dict(legacy_policy_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


