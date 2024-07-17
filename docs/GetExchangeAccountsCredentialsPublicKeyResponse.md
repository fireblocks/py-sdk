# GetExchangeAccountsCredentialsPublicKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | Public key string | 

## Example

```python
from fireblocks.models.get_exchange_accounts_credentials_public_key_response import GetExchangeAccountsCredentialsPublicKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetExchangeAccountsCredentialsPublicKeyResponse from a JSON string
get_exchange_accounts_credentials_public_key_response_instance = GetExchangeAccountsCredentialsPublicKeyResponse.from_json(json)
# print the JSON string representation of the object
print(GetExchangeAccountsCredentialsPublicKeyResponse.to_json())

# convert the object into a dict
get_exchange_accounts_credentials_public_key_response_dict = get_exchange_accounts_credentials_public_key_response_instance.to_dict()
# create an instance of GetExchangeAccountsCredentialsPublicKeyResponse from a dict
get_exchange_accounts_credentials_public_key_response_from_dict = GetExchangeAccountsCredentialsPublicKeyResponse.from_dict(get_exchange_accounts_credentials_public_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


