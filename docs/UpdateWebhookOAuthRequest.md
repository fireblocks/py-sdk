# UpdateWebhookOAuthRequest

A partial update. Every field is optional and an omitted field is left as it is, so `{ \"clientSecret\": \"new-secret\" }` rotates the secret and changes nothing else. A rotation applies to every webhook referencing these credentials.  The three custom maps merge: a key with a value is upserted, a key with `null` is deleted, a key you leave out is untouched. Because `null` inside a map means delete, none of the three is nullable as a whole — `customJwtClaims: null` and friends are rejected with a `400`. Clear a map by naming each key with a `null` value. `mtlsClientSignedCert` is a scalar, so `null` there does remove it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A label for this credential set. Omit to leave it unchanged. | [optional] 
**client_id** | **str** | OAuth client ID. Omit to leave it unchanged. | [optional] 
**client_secret** | **str** | A new OAuth client secret. Limited to 480 bytes when UTF-8 encoded, so a secret using non-ASCII characters fits fewer than 480 of them. Write-only — never returned in any response. Send this on its own to rotate the secret without changing anything else. Omit to leave it unchanged. | [optional] 
**url** | **str** | Token endpoint URL. HTTPS on port 443 only, and the host must resolve publicly. Omit to leave it unchanged. | [optional] 
**auth_method** | **str** | &#x60;client_secret_basic&#x60;, &#x60;client_secret_post&#x60; or &#x60;client_secret_jwt&#x60;. Omit to leave it unchanged — it does not revert to the default. | [optional] 
**custom_jwt_claims** | **Dict[str, object]** | A delta applied to the JWT assertion claims. A claim with a value is added or replaced, a claim with &#x60;null&#x60; is deleted, and a claim you leave out is untouched. So &#x60;{ \&quot;aud\&quot;: \&quot;https://auth.example.com\&quot;, \&quot;resource\&quot;: null }&#x60; sets &#x60;aud&#x60;, drops &#x60;resource&#x60;, and changes nothing else. Send &#x60;customJwtClaims: null&#x60; to clear every claim in one call. That does not collide with a &#x60;null&#x60; value on a name: one names the claim to delete, the other names the whole field. Same rules as on create: any JSON type except &#x60;null&#x60;, &#x60;iss&#x60;/&#x60;sub&#x60;/&#x60;jti&#x60;/&#x60;iat&#x60;/&#x60;exp&#x60; reserved, names case-sensitive, resulting set under 16 KB, values write-only. | [optional] 
**custom_body_params** | **Dict[str, Optional[str]]** | A delta applied to the token request body parameters. A parameter with a value is added or replaced, a parameter with &#x60;null&#x60; is deleted, and one you leave out is untouched. So &#x60;{ \&quot;scope\&quot;: \&quot;payments.read\&quot;, \&quot;audience\&quot;: null }&#x60; sets &#x60;scope&#x60;, drops &#x60;audience&#x60;, and changes nothing else. Send &#x60;customBodyParams: null&#x60; to clear every parameter in one call. That does not collide with a &#x60;null&#x60; value on a name: one names the parameter to delete, the other names the whole field. Same rules as on create: string values only, &#x60;grant_type&#x60;/&#x60;client_id&#x60;/&#x60;client_secret&#x60;/ &#x60;client_assertion&#x60;/&#x60;client_assertion_type&#x60; reserved, names case-sensitive, resulting set under 16 KB, values write-only. | [optional] 
**custom_headers** | **Dict[str, Optional[str]]** | A delta applied to the token request headers — not the webhook delivery headers. A header with a value is added or replaced, a header with &#x60;null&#x60; is deleted, and one you leave out is untouched. So &#x60;{ \&quot;X-Api-Key\&quot;: \&quot;new-key\&quot;, \&quot;X-Tenant\&quot;: null }&#x60; rotates &#x60;X-Api-Key&#x60;, drops &#x60;X-Tenant&#x60;, and changes nothing else. Send &#x60;customHeaders: null&#x60; to clear every header in one call. That does not collide with a &#x60;null&#x60; value on a name: one names the header to delete, the other names the whole field. Names are case-insensitive, so a &#x60;null&#x60; under one casing deletes a header stored under another, and names are stored and returned lowercased. Same rules as on create: string values only, &#x60;Content-Type&#x60;/&#x60;Authorization&#x60;/ &#x60;Content-Length&#x60;/&#x60;Host&#x60; reserved, resulting set under 16 KB, values write-only. | [optional] 
**mtls_client_signed_cert** | **str** | PEM-encoded client certificate for mTLS. Must be a valid X.509 certificate inside its validity window. Omit to leave it unchanged, or send &#x60;null&#x60; to remove it. | [optional] 

## Example

```python
from fireblocks.models.update_webhook_o_auth_request import UpdateWebhookOAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookOAuthRequest from a JSON string
update_webhook_o_auth_request_instance = UpdateWebhookOAuthRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookOAuthRequest.to_json())

# convert the object into a dict
update_webhook_o_auth_request_dict = update_webhook_o_auth_request_instance.to_dict()
# create an instance of UpdateWebhookOAuthRequest from a dict
update_webhook_o_auth_request_from_dict = UpdateWebhookOAuthRequest.from_dict(update_webhook_o_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


