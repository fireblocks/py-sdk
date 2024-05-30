# UnmanagedWallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**customer_ref_id** | **str** |  | [optional] 
**assets** | [**List[WalletAsset]**](WalletAsset.md) |  | 

## Example

```python
from fireblocks_client.models.unmanaged_wallet import UnmanagedWallet

# TODO update the JSON string below
json = "{}"
# create an instance of UnmanagedWallet from a JSON string
unmanaged_wallet_instance = UnmanagedWallet.from_json(json)
# print the JSON string representation of the object
print(UnmanagedWallet.to_json())

# convert the object into a dict
unmanaged_wallet_dict = unmanaged_wallet_instance.to_dict()
# create an instance of UnmanagedWallet from a dict
unmanaged_wallet_from_dict = UnmanagedWallet.from_dict(unmanaged_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


