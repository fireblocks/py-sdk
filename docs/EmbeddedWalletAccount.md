# EmbeddedWalletAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account | 
**wallet_id** | **str** | Unique identifier of the Non-Custodial Wallet (UUID) | 

## Example

```python
from fireblocks.models.embedded_wallet_account import EmbeddedWalletAccount

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletAccount from a JSON string
embedded_wallet_account_instance = EmbeddedWalletAccount.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletAccount.to_json())

# convert the object into a dict
embedded_wallet_account_dict = embedded_wallet_account_instance.to_dict()
# create an instance of EmbeddedWalletAccount from a dict
embedded_wallet_account_from_dict = EmbeddedWalletAccount.from_dict(embedded_wallet_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


