# EmbeddedWalletLatestBackupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passphrase_id** | **str** | passphraseId | 
**created_at** | **float** | createdAt | 
**keys** | [**List[EmbeddedWalletLatestBackupKey]**](EmbeddedWalletLatestBackupKey.md) | keys | 

## Example

```python
from fireblocks.models.embedded_wallet_latest_backup_response import EmbeddedWalletLatestBackupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletLatestBackupResponse from a JSON string
embedded_wallet_latest_backup_response_instance = EmbeddedWalletLatestBackupResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletLatestBackupResponse.to_json())

# convert the object into a dict
embedded_wallet_latest_backup_response_dict = embedded_wallet_latest_backup_response_instance.to_dict()
# create an instance of EmbeddedWalletLatestBackupResponse from a dict
embedded_wallet_latest_backup_response_from_dict = EmbeddedWalletLatestBackupResponse.from_dict(embedded_wallet_latest_backup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


