# CreateMultipleAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count | 
**base_asset_ids** | **List[str]** | Array of base asset IDs | 
**names** | **List[str]** | Names to assign to vault accounts. if vaultAccountNamesStartingIndex or prefix is used it&#39;ll fail | [optional] 
**vault_account_names_starting_index** | **int** | Copy vault accounts names starting from this index. If names array is used it&#39;ll fail | [optional] 
**prefix** | **str** | When copying from existing vault accounts (vaultAccountNamesStartingIndex) then adding a prefix to the names. If names array is used it&#39;ll fail | [optional] 
**tag_ids** | **List[str]** | Optional list of tag IDs to attach to all created vault accounts | [optional] 
**vault_type** | **str** | Type of vault accounts to create. The default type is MPC. KEY_LINK creates Key Link vault accounts. It requires a Key Link workspace. With autoAssign set to true, the vault accounts are bound to the workspace&#39;s Key Link signing keys, assigned automatically from the available keys, and only one KEY_LINK bulk creation with autoAssign set to true can run per workspace at a time. With autoAssign set to false (the default), the vault accounts are created without keys. With KEY_LINK, names, vaultAccountNamesStartingIndex, prefix and tagIds work as they do for MPC, and baseAssetIds may be empty to create vault accounts without wallets.  | [optional] [default to 'MPC']
**auto_assign** | **bool** | Applicable only when vaultType is KEY_LINK. For MPC, this parameter is ignored. If set to true, keys are assigned to every created vault account. If there are not enough available keys to assign, the request returns an error and no vault accounts are created. If set to false, the vault accounts are created without any keys, and baseAssetIds must be empty because wallets can only be created for vault accounts that have keys.  | [optional] [default to False]

## Example

```python
from fireblocks.models.create_multiple_accounts_request import CreateMultipleAccountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleAccountsRequest from a JSON string
create_multiple_accounts_request_instance = CreateMultipleAccountsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMultipleAccountsRequest.to_json())

# convert the object into a dict
create_multiple_accounts_request_dict = create_multiple_accounts_request_instance.to_dict()
# create an instance of CreateMultipleAccountsRequest from a dict
create_multiple_accounts_request_from_dict = CreateMultipleAccountsRequest.from_dict(create_multiple_accounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


