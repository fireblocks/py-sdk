# CreateMultipleAccountsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count | 
**base_asset_ids** | **List[str]** | Array of base asset IDs | 
**names** | **List[str]** | Names to assign to vault accounts. if vaultAccountNamesStartingIndex or prefix is used it&#39;ll fail | [optional] 
**vault_account_names_starting_index** | **int** | Copy vault accounts names starting from this index. If names array is used it&#39;ll fail | [optional] 
**prefix** | **str** | When copying from existing vault accounts (vaultAccountNamesStartingIndex) then adding a prefix to the names. If names array is used it&#39;ll fail | [optional] 

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


