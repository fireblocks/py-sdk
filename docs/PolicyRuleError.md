# PolicyRuleError

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
from fireblocks_client.models.policy_rule_error import PolicyRuleError

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyRuleError from a JSON string
policy_rule_error_instance = PolicyRuleError.from_json(json)
# print the JSON string representation of the object
print PolicyRuleError.to_json()

# convert the object into a dict
policy_rule_error_dict = policy_rule_error_instance.to_dict()
# create an instance of PolicyRuleError from a dict
policy_rule_error_form_dict = policy_rule_error.from_dict(policy_rule_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


