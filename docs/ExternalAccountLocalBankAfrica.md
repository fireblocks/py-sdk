# ExternalAccountLocalBankAfrica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_redirect_url** | **str** | URL to redirect the end user back to after they complete the payment on the bank/mobile provider page (e.g., the merchant checkout page) | [optional] 

## Example

```python
from fireblocks.models.external_account_local_bank_africa import ExternalAccountLocalBankAfrica

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalAccountLocalBankAfrica from a JSON string
external_account_local_bank_africa_instance = ExternalAccountLocalBankAfrica.from_json(json)
# print the JSON string representation of the object
print(ExternalAccountLocalBankAfrica.to_json())

# convert the object into a dict
external_account_local_bank_africa_dict = external_account_local_bank_africa_instance.to_dict()
# create an instance of ExternalAccountLocalBankAfrica from a dict
external_account_local_bank_africa_from_dict = ExternalAccountLocalBankAfrica.from_dict(external_account_local_bank_africa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


