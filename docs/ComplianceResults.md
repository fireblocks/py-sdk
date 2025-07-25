# ComplianceResults

The result of the Compliance AML/Travel Rule screening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aml** | [**ComplianceScreeningResult**](ComplianceScreeningResult.md) |  | [optional] 
**tr** | [**ComplianceScreeningResult**](ComplianceScreeningResult.md) |  | [optional] 
**aml_list** | [**List[ComplianceScreeningResult]**](ComplianceScreeningResult.md) | The list of all results of the AML screening. | [optional] 
**status** | [**ComplianceResultStatusesEnum**](ComplianceResultStatusesEnum.md) |  | [optional] 
**aml_registration** | [**AmlRegistrationResult**](AmlRegistrationResult.md) |  | [optional] 

## Example

```python
from fireblocks.models.compliance_results import ComplianceResults

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceResults from a JSON string
compliance_results_instance = ComplianceResults.from_json(json)
# print the JSON string representation of the object
print(ComplianceResults.to_json())

# convert the object into a dict
compliance_results_dict = compliance_results_instance.to_dict()
# create an instance of ComplianceResults from a dict
compliance_results_from_dict = ComplianceResults.from_dict(compliance_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


