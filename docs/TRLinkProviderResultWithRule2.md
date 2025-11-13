# TRLinkProviderResultWithRule2

Provider response and matched rule wrapper for TRLink screening results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_response** | **object** | Raw provider response | [optional] 
**matched_rule** | [**ScreeningTRLinkPostScreeningRule**](ScreeningTRLinkPostScreeningRule.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_provider_result_with_rule2 import TRLinkProviderResultWithRule2

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkProviderResultWithRule2 from a JSON string
tr_link_provider_result_with_rule2_instance = TRLinkProviderResultWithRule2.from_json(json)
# print the JSON string representation of the object
print(TRLinkProviderResultWithRule2.to_json())

# convert the object into a dict
tr_link_provider_result_with_rule2_dict = tr_link_provider_result_with_rule2_instance.to_dict()
# create an instance of TRLinkProviderResultWithRule2 from a dict
tr_link_provider_result_with_rule2_from_dict = TRLinkProviderResultWithRule2.from_dict(tr_link_provider_result_with_rule2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


