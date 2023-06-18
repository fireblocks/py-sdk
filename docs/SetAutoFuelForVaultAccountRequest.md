# SetAutoFuelForVaultAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_fuel** | **bool** | Auto Fuel | [optional] 

## Example

```python
from fireblocks_client.models.set_auto_fuel_for_vault_account_request import SetAutoFuelForVaultAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAutoFuelForVaultAccountRequest from a JSON string
set_auto_fuel_for_vault_account_request_instance = SetAutoFuelForVaultAccountRequest.from_json(json)
# print the JSON string representation of the object
print SetAutoFuelForVaultAccountRequest.to_json()

# convert the object into a dict
set_auto_fuel_for_vault_account_request_dict = set_auto_fuel_for_vault_account_request_instance.to_dict()
# create an instance of SetAutoFuelForVaultAccountRequest from a dict
set_auto_fuel_for_vault_account_request_form_dict = set_auto_fuel_for_vault_account_request.from_dict(set_auto_fuel_for_vault_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


