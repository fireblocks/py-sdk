# PublishPolicyRulesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[PolicyRule]**](PolicyRule.md) | Policy rules to publish | [optional] 

## Example

```python
from fireblocks_client.models.publish_policy_rules_request import PublishPolicyRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPolicyRulesRequest from a JSON string
publish_policy_rules_request_instance = PublishPolicyRulesRequest.from_json(json)
# print the JSON string representation of the object
print PublishPolicyRulesRequest.to_json()

# convert the object into a dict
publish_policy_rules_request_dict = publish_policy_rules_request_instance.to_dict()
# create an instance of PublishPolicyRulesRequest from a dict
publish_policy_rules_request_form_dict = publish_policy_rules_request.from_dict(publish_policy_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


