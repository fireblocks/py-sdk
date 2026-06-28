# CreateMultipleVaultAccountsJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the job. Possible values - Success, In Progress, Error, Pending Approval, Canceled | 
**vault_accounts** | **Dict[str, Dict[str, str]]** | Mapping between VaultAccountId to a mapping of asset to address, and the vault account name | [optional] 
**tag_ids** | **List[str]** | List of tag IDs successfully attached to each of the created vault accounts | [optional] 
**error_message** | **str** |  | [optional] 
**approval_request_id** | **str** | Approval request ID if the job has protected tags to attach to the vault accounts | [optional] 

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


