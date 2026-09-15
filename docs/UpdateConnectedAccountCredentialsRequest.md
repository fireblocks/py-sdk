# UpdateConnectedAccountCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creds** | **bytearray** | Base64-encoded RSA-encrypted credential blob (the new secret). Encrypt using the public key from GET /connected_accounts/credentials/public_key. | 
**api_key** | **str** | The new account-level API key. Mandatory for credential update. | 

## Example

```python
from fireblocks.models.update_connected_account_credentials_request import UpdateConnectedAccountCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConnectedAccountCredentialsRequest from a JSON string
update_connected_account_credentials_request_instance = UpdateConnectedAccountCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateConnectedAccountCredentialsRequest.to_json())

# convert the object into a dict
update_connected_account_credentials_request_dict = update_connected_account_credentials_request_instance.to_dict()
# create an instance of UpdateConnectedAccountCredentialsRequest from a dict
update_connected_account_credentials_request_from_dict = UpdateConnectedAccountCredentialsRequest.from_dict(update_connected_account_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


