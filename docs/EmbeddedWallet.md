# EmbeddedWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wallet_id** | **str** | walletId | 
**enabled** | **bool** | enabled | 

## Example

```python
from fireblocks.models.embedded_wallet import EmbeddedWallet

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWallet from a JSON string
embedded_wallet_instance = EmbeddedWallet.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWallet.to_json())

# convert the object into a dict
embedded_wallet_dict = embedded_wallet_instance.to_dict()
# create an instance of EmbeddedWallet from a dict
embedded_wallet_from_dict = EmbeddedWallet.from_dict(embedded_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


