# AssignVaultsToLegalEntityResponse

Response after assigning vault accounts to a legal entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_count** | **int** | Number of vault accounts successfully assigned | 

## Example

```python
from fireblocks.models.assign_vaults_to_legal_entity_response import AssignVaultsToLegalEntityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignVaultsToLegalEntityResponse from a JSON string
assign_vaults_to_legal_entity_response_instance = AssignVaultsToLegalEntityResponse.from_json(json)
# print the JSON string representation of the object
print(AssignVaultsToLegalEntityResponse.to_json())

# convert the object into a dict
assign_vaults_to_legal_entity_response_dict = assign_vaults_to_legal_entity_response_instance.to_dict()
# create an instance of AssignVaultsToLegalEntityResponse from a dict
assign_vaults_to_legal_entity_response_from_dict = AssignVaultsToLegalEntityResponse.from_dict(assign_vaults_to_legal_entity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


