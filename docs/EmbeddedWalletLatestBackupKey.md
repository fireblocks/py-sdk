# EmbeddedWalletLatestBackupKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | deviceId | 
**public_key** | **str** | publicKey | 
**key_id** | **str** | keyId | 
**algorithm** | **str** | algorithm | 

## Example

```python
from fireblocks.models.embedded_wallet_latest_backup_key import EmbeddedWalletLatestBackupKey

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletLatestBackupKey from a JSON string
embedded_wallet_latest_backup_key_instance = EmbeddedWalletLatestBackupKey.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletLatestBackupKey.to_json())

# convert the object into a dict
embedded_wallet_latest_backup_key_dict = embedded_wallet_latest_backup_key_instance.to_dict()
# create an instance of EmbeddedWalletLatestBackupKey from a dict
embedded_wallet_latest_backup_key_from_dict = EmbeddedWalletLatestBackupKey.from_dict(embedded_wallet_latest_backup_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


