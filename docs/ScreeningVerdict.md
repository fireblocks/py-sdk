# ScreeningVerdict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verdict** | **str** |  | 
**execution_operation_id** | **str** |  | 
**account** | [**Destination**](Destination.md) |  | 
**asset_id** | **str** |  | 
**amount** | **str** |  | 
**matched_rule** | [**ScreeningVerdictMatchedRule**](ScreeningVerdictMatchedRule.md) |  | [optional] 

## Example

```python
from fireblocks.models.screening_verdict import ScreeningVerdict

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningVerdict from a JSON string
screening_verdict_instance = ScreeningVerdict.from_json(json)
# print the JSON string representation of the object
print(ScreeningVerdict.to_json())

# convert the object into a dict
screening_verdict_dict = screening_verdict_instance.to_dict()
# create an instance of ScreeningVerdict from a dict
screening_verdict_from_dict = ScreeningVerdict.from_dict(screening_verdict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


