# TRLinkProviderResultWithRule

Provider response and matched rule wrapper for TRLink screening results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_response** | **object** | Raw provider response | [optional] 
**matched_rule** | [**TRLinkPostScreeningRule**](TRLinkPostScreeningRule.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_provider_result_with_rule import TRLinkProviderResultWithRule

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkProviderResultWithRule from a JSON string
tr_link_provider_result_with_rule_instance = TRLinkProviderResultWithRule.from_json(json)
# print the JSON string representation of the object
print(TRLinkProviderResultWithRule.to_json())

# convert the object into a dict
tr_link_provider_result_with_rule_dict = tr_link_provider_result_with_rule_instance.to_dict()
# create an instance of TRLinkProviderResultWithRule from a dict
tr_link_provider_result_with_rule_from_dict = TRLinkProviderResultWithRule.from_dict(tr_link_provider_result_with_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


