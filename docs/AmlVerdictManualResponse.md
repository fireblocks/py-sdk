# AmlVerdictManualResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from fireblocks.models.aml_verdict_manual_response import AmlVerdictManualResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AmlVerdictManualResponse from a JSON string
aml_verdict_manual_response_instance = AmlVerdictManualResponse.from_json(json)
# print the JSON string representation of the object
print(AmlVerdictManualResponse.to_json())

# convert the object into a dict
aml_verdict_manual_response_dict = aml_verdict_manual_response_instance.to_dict()
# create an instance of AmlVerdictManualResponse from a dict
aml_verdict_manual_response_from_dict = AmlVerdictManualResponse.from_dict(aml_verdict_manual_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


