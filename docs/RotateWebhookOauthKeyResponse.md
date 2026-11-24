# RotateWebhookOauthKeyResponse

The key that was rotated out. It stays published at the `jwksUri` of the credentials for 30 days. Fetch the JWKS from there for the current public keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | The &#x60;kid&#x60; of the key rotated out, the one Fireblocks was signing with until now. It is the SHA-256 fingerprint of the public key&#39;s DER (SPKI) encoding, in lowercase hex. | 

## Example

```python
from fireblocks.models.rotate_webhook_oauth_key_response import RotateWebhookOauthKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RotateWebhookOauthKeyResponse from a JSON string
rotate_webhook_oauth_key_response_instance = RotateWebhookOauthKeyResponse.from_json(json)
# print the JSON string representation of the object
print(RotateWebhookOauthKeyResponse.to_json())

# convert the object into a dict
rotate_webhook_oauth_key_response_dict = rotate_webhook_oauth_key_response_instance.to_dict()
# create an instance of RotateWebhookOauthKeyResponse from a dict
rotate_webhook_oauth_key_response_from_dict = RotateWebhookOauthKeyResponse.from_dict(rotate_webhook_oauth_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


