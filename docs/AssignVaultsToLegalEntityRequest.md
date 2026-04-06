# AssignVaultsToLegalEntityRequest

Request body to assign vault accounts to a legal entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_ids** | **List[str]** | List of vault account IDs to assign to the legal entity | 

## Example

```python
from fireblocks.models.assign_vaults_to_legal_entity_request import AssignVaultsToLegalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignVaultsToLegalEntityRequest from a JSON string
assign_vaults_to_legal_entity_request_instance = AssignVaultsToLegalEntityRequest.from_json(json)
# print the JSON string representation of the object
print(AssignVaultsToLegalEntityRequest.to_json())

# convert the object into a dict
assign_vaults_to_legal_entity_request_dict = assign_vaults_to_legal_entity_request_instance.to_dict()
# create an instance of AssignVaultsToLegalEntityRequest from a dict
assign_vaults_to_legal_entity_request_from_dict = AssignVaultsToLegalEntityRequest.from_dict(assign_vaults_to_legal_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


