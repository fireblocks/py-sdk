# CreateMultipleDepositAddressesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_account_id** | **int** | Existing Vault account ID to add deposit addresses to | 
**asset_id** | **str** | asset ID | 
**count** | **int** | Count of deposit addresses to issue | 
**descriptions** | **List[str]** | Desctiptions of the newly created addresses | [optional] 
**vault_account_to_copy_desc_from** | **int** | Existing Vault Account ID to copy deposit addresses descriptions from in case no descriptions were provided | [optional] 
**vault_account_to_copy_desc_from_index** | **int** | Existing length within the vault account to copy deposit addresses descriptions from | [optional] 

## Example

```python
from fireblocks.models.create_multiple_deposit_addresses_request import CreateMultipleDepositAddressesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleDepositAddressesRequest from a JSON string
create_multiple_deposit_addresses_request_instance = CreateMultipleDepositAddressesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateMultipleDepositAddressesRequest.to_json())

# convert the object into a dict
create_multiple_deposit_addresses_request_dict = create_multiple_deposit_addresses_request_instance.to_dict()
# create an instance of CreateMultipleDepositAddressesRequest from a dict
create_multiple_deposit_addresses_request_from_dict = CreateMultipleDepositAddressesRequest.from_dict(create_multiple_deposit_addresses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


