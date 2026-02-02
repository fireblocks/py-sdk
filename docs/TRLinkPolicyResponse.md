# TRLinkPolicyResponse

TRLink policy response containing pre-screening, post-screening, and missing TRM rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_screening_rules** | [**List[TRLinkPreScreeningRule2]**](TRLinkPreScreeningRule2.md) | Pre-screening rules that determine whether transactions should be screened | 
**post_screening_rules** | [**List[TRLinkPostScreeningRule2]**](TRLinkPostScreeningRule2.md) | Post-screening rules that determine actions based on screening results | 
**missing_trm_rules** | [**List[TRLinkMissingTrmRule2]**](TRLinkMissingTrmRule2.md) | Rules for handling transactions when TRM screening data is unavailable | 

## Example

```python
from fireblocks.models.tr_link_policy_response import TRLinkPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkPolicyResponse from a JSON string
tr_link_policy_response_instance = TRLinkPolicyResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkPolicyResponse.to_json())

# convert the object into a dict
tr_link_policy_response_dict = tr_link_policy_response_instance.to_dict()
# create an instance of TRLinkPolicyResponse from a dict
tr_link_policy_response_from_dict = TRLinkPolicyResponse.from_dict(tr_link_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


