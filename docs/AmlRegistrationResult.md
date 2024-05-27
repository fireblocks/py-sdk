# AmlRegistrationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**timestamp** | **float** |  | [optional] 

## Example

```python
from fireblocks_client.models.aml_registration_result import AmlRegistrationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AmlRegistrationResult from a JSON string
aml_registration_result_instance = AmlRegistrationResult.from_json(json)
# print the JSON string representation of the object
print AmlRegistrationResult.to_json()

# convert the object into a dict
aml_registration_result_dict = aml_registration_result_instance.to_dict()
# create an instance of AmlRegistrationResult from a dict
aml_registration_result_form_dict = aml_registration_result.from_dict(aml_registration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


