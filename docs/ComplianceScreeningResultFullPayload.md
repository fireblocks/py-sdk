# ComplianceScreeningResultFullPayload

The result of the Travel Rule screening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**payload** | **object** | The payload of the screening result. The payload is a JSON object that contains the screening result. The payload is different for each screening provider.  | [optional] 
**bypass_reason** | **str** |  | [optional] 
**screening_status** | **str** |  | [optional] 
**timestamp** | **float** |  | [optional] 

## Example

```python
from fireblocks.models.compliance_screening_result_full_payload import ComplianceScreeningResultFullPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceScreeningResultFullPayload from a JSON string
compliance_screening_result_full_payload_instance = ComplianceScreeningResultFullPayload.from_json(json)
# print the JSON string representation of the object
print(ComplianceScreeningResultFullPayload.to_json())

# convert the object into a dict
compliance_screening_result_full_payload_dict = compliance_screening_result_full_payload_instance.to_dict()
# create an instance of ComplianceScreeningResultFullPayload from a dict
compliance_screening_result_full_payload_from_dict = ComplianceScreeningResultFullPayload.from_dict(compliance_screening_result_full_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


