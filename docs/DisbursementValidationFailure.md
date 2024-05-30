# DisbursementValidationFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from fireblocks.models.disbursement_validation_failure import DisbursementValidationFailure

# TODO update the JSON string below
json = "{}"
# create an instance of DisbursementValidationFailure from a JSON string
disbursement_validation_failure_instance = DisbursementValidationFailure.from_json(json)
# print the JSON string representation of the object
print(DisbursementValidationFailure.to_json())

# convert the object into a dict
disbursement_validation_failure_dict = disbursement_validation_failure_instance.to_dict()
# create an instance of DisbursementValidationFailure from a dict
disbursement_validation_failure_from_dict = DisbursementValidationFailure.from_dict(disbursement_validation_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


