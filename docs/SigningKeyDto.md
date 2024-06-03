# SigningKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | External signing key id set by Fireblocks. | 
**signing_device_key_id** | **str** | The ID, name or label of the key specified on the customer&#39;s signing device. | 
**public_key_pem** | **str** | PEM encoded public key | 
**algorithm** | **str** | Algorithm and curve used for the signature. Can be: ECDSA_SECP256K1 or EDDSA_ED25519 | 
**enabled** | **bool** | True if the signing key is enabled | 
**vault_account_id** | **float** | Id of the vault account which this key is linked to | 
**agent_user_id** | **str** | Id of user that represent agent servers that can sign with the key | 
**created_at** | **float** | Creation date (timestamp) in milliseconds. | 

## Example

```python
from fireblocks.models.signing_key_dto import SigningKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of SigningKeyDto from a JSON string
signing_key_dto_instance = SigningKeyDto.from_json(json)
# print the JSON string representation of the object
print(SigningKeyDto.to_json())

# convert the object into a dict
signing_key_dto_dict = signing_key_dto_instance.to_dict()
# create an instance of SigningKeyDto from a dict
signing_key_dto_from_dict = SigningKeyDto.from_dict(signing_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


