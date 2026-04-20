# ScreeningPolicyAmountRange

Minimum and maximum amount range specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **str** | Minimum amount (inclusive) | [optional] 
**max** | **str** | Maximum amount (inclusive) | [optional] 

## Example

```python
from fireblocks.models.screening_policy_amount_range import ScreeningPolicyAmountRange

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningPolicyAmountRange from a JSON string
screening_policy_amount_range_instance = ScreeningPolicyAmountRange.from_json(json)
# print the JSON string representation of the object
print(ScreeningPolicyAmountRange.to_json())

# convert the object into a dict
screening_policy_amount_range_dict = screening_policy_amount_range_instance.to_dict()
# create an instance of ScreeningPolicyAmountRange from a dict
screening_policy_amount_range_from_dict = ScreeningPolicyAmountRange.from_dict(screening_policy_amount_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


