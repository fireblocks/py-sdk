# LegacyPolicyResponse

Response object for policy operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[LegacyPolicyRule]**](LegacyPolicyRule.md) | A set of policy rules | 
**metadata** | [**LegacyPolicyMetadata**](LegacyPolicyMetadata.md) |  | 

## Example

```python
from fireblocks.models.legacy_policy_response import LegacyPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPolicyResponse from a JSON string
legacy_policy_response_instance = LegacyPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(LegacyPolicyResponse.to_json())

# convert the object into a dict
legacy_policy_response_dict = legacy_policy_response_instance.to_dict()
# create an instance of LegacyPolicyResponse from a dict
legacy_policy_response_from_dict = LegacyPolicyResponse.from_dict(legacy_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


