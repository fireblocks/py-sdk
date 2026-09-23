# ScreeningInput

What the caller wants screened, and how.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**ScreeningOperationEnum**](ScreeningOperationEnum.md) |  | 
**payload** | [**List[ScreeningPayload]**](ScreeningPayload.md) | The screening subjects. Up to 100 per request — the provider&#39;s own batch limit for address screening — so a bulk check does not need one call per address. | 

## Example

```python
from fireblocks.models.screening_input import ScreeningInput

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningInput from a JSON string
screening_input_instance = ScreeningInput.from_json(json)
# print the JSON string representation of the object
print(ScreeningInput.to_json())

# convert the object into a dict
screening_input_dict = screening_input_instance.to_dict()
# create an instance of ScreeningInput from a dict
screening_input_from_dict = ScreeningInput.from_dict(screening_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


