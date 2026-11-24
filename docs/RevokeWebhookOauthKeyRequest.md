# RevokeWebhookOauthKeyRequest

Which key to revoke. Omit `kid`, or send an empty body, to revoke the key Fireblocks is signing with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | The &#x60;kid&#x60; of the key to revoke, as the JWKS at &#x60;jwksUri&#x60; lists it: the signing key, its successor, a key rotated out and still published, or a key left behind by a &#x60;signingAlg&#x60; change within its 30 days. Omit to revoke the signing key; &#x60;null&#x60; is refused rather than read as omitted. Required on credentials that no longer use &#x60;private_key_jwt&#x60;. | [optional] 

## Example

```python
from fireblocks.models.revoke_webhook_oauth_key_request import RevokeWebhookOauthKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeWebhookOauthKeyRequest from a JSON string
revoke_webhook_oauth_key_request_instance = RevokeWebhookOauthKeyRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeWebhookOauthKeyRequest.to_json())

# convert the object into a dict
revoke_webhook_oauth_key_request_dict = revoke_webhook_oauth_key_request_instance.to_dict()
# create an instance of RevokeWebhookOauthKeyRequest from a dict
revoke_webhook_oauth_key_request_from_dict = RevokeWebhookOauthKeyRequest.from_dict(revoke_webhook_oauth_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


