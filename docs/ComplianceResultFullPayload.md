# ComplianceResultFullPayload

The result of the Compliance AML/Travel Rule screening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aml** | [**List[ComplianceScreeningResultFullPayload]**](ComplianceScreeningResultFullPayload.md) | The end result of the AML screening. | [optional] 
**tr** | [**List[ComplianceScreeningResultFullPayload]**](ComplianceScreeningResultFullPayload.md) | The result of the Travel Rule screening. | [optional] 
**aml_list** | [**List[ComplianceScreeningResultFullPayload]**](ComplianceScreeningResultFullPayload.md) | The list of all results of the AML screening. | [optional] 
**status** | **str** | Status of compliance result screening. | [optional] 
**aml_registration** | [**List[AmlRegistrationResultFullPayload]**](AmlRegistrationResultFullPayload.md) | The results of the AML address registration. | [optional] 

## Example

```python
from fireblocks.models.compliance_result_full_payload import ComplianceResultFullPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceResultFullPayload from a JSON string
compliance_result_full_payload_instance = ComplianceResultFullPayload.from_json(json)
# print the JSON string representation of the object
print(ComplianceResultFullPayload.to_json())

# convert the object into a dict
compliance_result_full_payload_dict = compliance_result_full_payload_instance.to_dict()
# create an instance of ComplianceResultFullPayload from a dict
compliance_result_full_payload_from_dict = ComplianceResultFullPayload.from_dict(compliance_result_full_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


