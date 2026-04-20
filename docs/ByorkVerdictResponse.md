# ByorkVerdictResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ByorkVerdictResponseStatusEnum**](ByorkVerdictResponseStatusEnum.md) |  | 
**message** | **str** | Human-readable message | 

## Example

```python
from fireblocks.models.byork_verdict_response import ByorkVerdictResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ByorkVerdictResponse from a JSON string
byork_verdict_response_instance = ByorkVerdictResponse.from_json(json)
# print the JSON string representation of the object
print(ByorkVerdictResponse.to_json())

# convert the object into a dict
byork_verdict_response_dict = byork_verdict_response_instance.to_dict()
# create an instance of ByorkVerdictResponse from a dict
byork_verdict_response_from_dict = ByorkVerdictResponse.from_dict(byork_verdict_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


