# GetConnectedAccountsCredentialsPublicKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | RSA public key (PEM) used to encrypt credential payloads sent to POST /connected_accounts. | 

## Example

```python
from fireblocks.models.get_connected_accounts_credentials_public_key_response import GetConnectedAccountsCredentialsPublicKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetConnectedAccountsCredentialsPublicKeyResponse from a JSON string
get_connected_accounts_credentials_public_key_response_instance = GetConnectedAccountsCredentialsPublicKeyResponse.from_json(json)
# print the JSON string representation of the object
print(GetConnectedAccountsCredentialsPublicKeyResponse.to_json())

# convert the object into a dict
get_connected_accounts_credentials_public_key_response_dict = get_connected_accounts_credentials_public_key_response_instance.to_dict()
# create an instance of GetConnectedAccountsCredentialsPublicKeyResponse from a dict
get_connected_accounts_credentials_public_key_response_from_dict = GetConnectedAccountsCredentialsPublicKeyResponse.from_dict(get_connected_accounts_credentials_public_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


