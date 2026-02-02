# TRLinkJwkPublicKey

JSON Web Key (JWK) format public key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Key type | 
**e** | **str** | RSA public exponent | 
**use** | **str** | Public key use (encryption) | 
**kid** | **str** | Key ID | 
**n** | **str** | RSA modulus | 

## Example

```python
from fireblocks.models.tr_link_jwk_public_key import TRLinkJwkPublicKey

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkJwkPublicKey from a JSON string
tr_link_jwk_public_key_instance = TRLinkJwkPublicKey.from_json(json)
# print the JSON string representation of the object
print(TRLinkJwkPublicKey.to_json())

# convert the object into a dict
tr_link_jwk_public_key_dict = tr_link_jwk_public_key_instance.to_dict()
# create an instance of TRLinkJwkPublicKey from a dict
tr_link_jwk_public_key_from_dict = TRLinkJwkPublicKey.from_dict(tr_link_jwk_public_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


