# RevokeWebhookOauthKeyResponse

The key that was revoked. It is no longer published at the `jwksUri` of the credentials. Fetch the JWKS from there for the current public keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | The &#x60;kid&#x60; of the key revoked. When the request carried no &#x60;kid&#x60;, this is the key Fireblocks was signing with. It is the SHA-256 fingerprint of the public key&#39;s DER (SPKI) encoding, in lowercase hex. | 

## Example

```python
from fireblocks.models.revoke_webhook_oauth_key_response import RevokeWebhookOauthKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeWebhookOauthKeyResponse from a JSON string
revoke_webhook_oauth_key_response_instance = RevokeWebhookOauthKeyResponse.from_json(json)
# print the JSON string representation of the object
print(RevokeWebhookOauthKeyResponse.to_json())

# convert the object into a dict
revoke_webhook_oauth_key_response_dict = revoke_webhook_oauth_key_response_instance.to_dict()
# create an instance of RevokeWebhookOauthKeyResponse from a dict
revoke_webhook_oauth_key_response_from_dict = RevokeWebhookOauthKeyResponse.from_dict(revoke_webhook_oauth_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


