# LegacyPolicyRuleError

Rule validation result error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error message | 
**error_code** | **float** | error code | 
**error_code_name** | **str** | error code name | 
**error_field** | **str** | The field which the error relates to * operator - transaction initiator * operators - transaction initiators * authorizationGroups - transaction authorizer groups * designatedSigner - transaction signer * designatedSigners - transaction signers * contractMethods - contract methods * amountAggregation - transaction amount aggregation configuration * src - transaction source asset configuration * dst - transaction destination asset configuration  | 

## Example

```python
from fireblocks.models.legacy_policy_rule_error import LegacyPolicyRuleError

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleError from a JSON string
legacy_policy_rule_error_instance = LegacyPolicyRuleError.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleError.to_json())

# convert the object into a dict
legacy_policy_rule_error_dict = legacy_policy_rule_error_instance.to_dict()
# create an instance of LegacyPolicyRuleError from a dict
legacy_policy_rule_error_from_dict = LegacyPolicyRuleError.from_dict(legacy_policy_rule_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


