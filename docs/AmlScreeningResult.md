# AmlScreeningResult

The result of the AML screening.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**payload** | **object** |  | [optional] 

## Example

```python
from fireblocks_client.models.aml_screening_result import AmlScreeningResult

# TODO update the JSON string below
json = "{}"
# create an instance of AmlScreeningResult from a JSON string
aml_screening_result_instance = AmlScreeningResult.from_json(json)
# print the JSON string representation of the object
print AmlScreeningResult.to_json()

# convert the object into a dict
aml_screening_result_dict = aml_screening_result_instance.to_dict()
# create an instance of AmlScreeningResult from a dict
aml_screening_result_form_dict = aml_screening_result.from_dict(aml_screening_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


