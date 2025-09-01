# LegacyPolicyRuleRawMessageSigning

Raw message signing configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | [optional] 
**derivation_path** | [**LegacyPolicyRuleRawMessageSigningDerivationPath**](LegacyPolicyRuleRawMessageSigningDerivationPath.md) |  | [optional] 

## Example

```python
from fireblocks.models.legacy_policy_rule_raw_message_signing import LegacyPolicyRuleRawMessageSigning

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyRuleRawMessageSigning from a JSON string
legacy_policy_rule_raw_message_signing_instance = LegacyPolicyRuleRawMessageSigning.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyRuleRawMessageSigning.to_json())

# convert the object into a dict
legacy_policy_rule_raw_message_signing_dict = legacy_policy_rule_raw_message_signing_instance.to_dict()
# create an instance of LegacyPolicyRuleRawMessageSigning from a dict
legacy_policy_rule_raw_message_signing_from_dict = LegacyPolicyRuleRawMessageSigning.from_dict(legacy_policy_rule_raw_message_signing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


