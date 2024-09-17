# CreateSigningKeyDtoProofOfOwnership

An object containing proof of ownership for the signing key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message to be signed by the key as proof of ownership. 64 to 1024 bytes in hexadecimal format. | 
**signature** | **str** | The signature of the message. 64 bytes in hexadecimal format. | 

## Example

```python
from fireblocks.models.create_signing_key_dto_proof_of_ownership import CreateSigningKeyDtoProofOfOwnership

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSigningKeyDtoProofOfOwnership from a JSON string
create_signing_key_dto_proof_of_ownership_instance = CreateSigningKeyDtoProofOfOwnership.from_json(json)
# print the JSON string representation of the object
print(CreateSigningKeyDtoProofOfOwnership.to_json())

# convert the object into a dict
create_signing_key_dto_proof_of_ownership_dict = create_signing_key_dto_proof_of_ownership_instance.to_dict()
# create an instance of CreateSigningKeyDtoProofOfOwnership from a dict
create_signing_key_dto_proof_of_ownership_from_dict = CreateSigningKeyDtoProofOfOwnership.from_dict(create_signing_key_dto_proof_of_ownership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


