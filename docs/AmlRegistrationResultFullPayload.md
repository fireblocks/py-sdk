# AmlRegistrationResultFullPayload

The results of the AML address registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**timestamp** | **float** |  | [optional] 

## Example

```python
from fireblocks.models.aml_registration_result_full_payload import AmlRegistrationResultFullPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AmlRegistrationResultFullPayload from a JSON string
aml_registration_result_full_payload_instance = AmlRegistrationResultFullPayload.from_json(json)
# print the JSON string representation of the object
print(AmlRegistrationResultFullPayload.to_json())

# convert the object into a dict
aml_registration_result_full_payload_dict = aml_registration_result_full_payload_instance.to_dict()
# create an instance of AmlRegistrationResultFullPayload from a dict
aml_registration_result_full_payload_from_dict = AmlRegistrationResultFullPayload.from_dict(aml_registration_result_full_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


