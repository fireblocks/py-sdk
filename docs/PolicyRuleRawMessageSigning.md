# PolicyRuleRawMessageSigning

Raw message signing configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | [optional] 
**derivation_path** | [**PolicyRuleRawMessageSigningDerivationPath**](PolicyRuleRawMessageSigningDerivationPath.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.policy_rule_raw_message_signing import PolicyRuleRawMessageSigning

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleRawMessageSigning from a JSON string
policy_rule_raw_message_signing_instance = PolicyRuleRawMessageSigning.from_json(json)
# print the JSON string representation of the object
print PolicyRuleRawMessageSigning.to_json()

# convert the object into a dict
policy_rule_raw_message_signing_dict = policy_rule_raw_message_signing_instance.to_dict()
# create an instance of PolicyRuleRawMessageSigning from a dict
policy_rule_raw_message_signing_form_dict = policy_rule_raw_message_signing.from_dict(policy_rule_raw_message_signing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


