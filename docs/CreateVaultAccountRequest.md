# CreateVaultAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Account Name | [optional] 
**hidden_on_ui** | **bool** | Optional - if true, the created account and all related transactions will not be shown on Fireblocks console | [optional] 
**customer_ref_id** | **str** | Optional - Sets a customer reference ID | [optional] 
**auto_fuel** | **bool** | Optional - Sets the autoFuel property of the vault account | [optional] 

## Example

```python
from fireblocks_client.models.create_vault_account_request import CreateVaultAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVaultAccountRequest from a JSON string
create_vault_account_request_instance = CreateVaultAccountRequest.from_json(json)
# print the JSON string representation of the object
print CreateVaultAccountRequest.to_json()

# convert the object into a dict
create_vault_account_request_dict = create_vault_account_request_instance.to_dict()
# create an instance of CreateVaultAccountRequest from a dict
create_vault_account_request_form_dict = create_vault_account_request.from_dict(create_vault_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


