# UpdateVaultAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Account Name | [optional] 

## Example

```python
from fireblocks.models.update_vault_account_request import UpdateVaultAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVaultAccountRequest from a JSON string
update_vault_account_request_instance = UpdateVaultAccountRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateVaultAccountRequest.to_json())

# convert the object into a dict
update_vault_account_request_dict = update_vault_account_request_instance.to_dict()
# create an instance of UpdateVaultAccountRequest from a dict
update_vault_account_request_from_dict = UpdateVaultAccountRequest.from_dict(update_vault_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


