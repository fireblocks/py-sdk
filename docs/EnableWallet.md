# EnableWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the wallet should be enabled or disabled | 

## Example

```python
from fireblocks.models.enable_wallet import EnableWallet

# TODO update the JSON string below
json = "{}"
# create an instance of EnableWallet from a JSON string
enable_wallet_instance = EnableWallet.from_json(json)
# print the JSON string representation of the object
print(EnableWallet.to_json())

# convert the object into a dict
enable_wallet_dict = enable_wallet_instance.to_dict()
# create an instance of EnableWallet from a dict
enable_wallet_from_dict = EnableWallet.from_dict(enable_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


