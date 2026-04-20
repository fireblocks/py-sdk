# ScreeningPolicyAmount

Amount specification with range and currency type (screening policy rules – BYORK, TRLink, etc.)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**ScreeningPolicyAmountRange**](ScreeningPolicyAmountRange.md) |  | 
**currency** | [**ScreeningPolicyCurrency**](ScreeningPolicyCurrency.md) |  | 

## Example

```python
from fireblocks.models.screening_policy_amount import ScreeningPolicyAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningPolicyAmount from a JSON string
screening_policy_amount_instance = ScreeningPolicyAmount.from_json(json)
# print the JSON string representation of the object
print(ScreeningPolicyAmount.to_json())

# convert the object into a dict
screening_policy_amount_dict = screening_policy_amount_instance.to_dict()
# create an instance of ScreeningPolicyAmount from a dict
screening_policy_amount_from_dict = ScreeningPolicyAmount.from_dict(screening_policy_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


