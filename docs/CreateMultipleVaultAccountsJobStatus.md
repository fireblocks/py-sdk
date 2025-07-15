# CreateMultipleVaultAccountsJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**vault_accounts** | **Dict[str, Dict[str, str]]** | Mapping between VaultAccountId to a mapping of asset to address | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.create_multiple_vault_accounts_job_status import CreateMultipleVaultAccountsJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleVaultAccountsJobStatus from a JSON string
create_multiple_vault_accounts_job_status_instance = CreateMultipleVaultAccountsJobStatus.from_json(json)
# print the JSON string representation of the object
print(CreateMultipleVaultAccountsJobStatus.to_json())

# convert the object into a dict
create_multiple_vault_accounts_job_status_dict = create_multiple_vault_accounts_job_status_instance.to_dict()
# create an instance of CreateMultipleVaultAccountsJobStatus from a dict
create_multiple_vault_accounts_job_status_from_dict = CreateMultipleVaultAccountsJobStatus.from_dict(create_multiple_vault_accounts_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


