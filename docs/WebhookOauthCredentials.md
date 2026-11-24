# WebhookOauthCredentials

A stored OAuth 2.0 client credential set, referenced by webhooks through their `webhookOauthId`. Deliveries for a webhook that references one carry `Authorization: Bearer {token}`, using a token fetched from `url` and cached until it expires, so your authorization server sees far fewer token requests than deliveries. Secret material is never returned: `clientSecret` is absent from this schema entirely, and the `customJwtClaims` and `customBodyParams` fields are reduced to their names, without the configured values. Extra token request headers are a separate resource, referenced by `webhookCustomHeadersId`. The key pairs of `private_key_jwt` credentials are never returned here either; their public halves are published at the URL in `jwksUri`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the OAuth credentials. Pass this as a webhook&#39;s &#x60;webhookOauthId&#x60; to attach them. | 
**name** | **str** | The label given to this credential set. | 
**client_id** | **str** | OAuth client ID used to authenticate with the token endpoint. | 
**url** | **str** | Token endpoint URL. | 
**auth_method** | **str** | How the client credentials are presented to the token endpoint: &#x60;client_secret_basic&#x60;, &#x60;client_secret_post&#x60;, &#x60;client_secret_jwt&#x60; or &#x60;private_key_jwt&#x60;. Credentials created without this field report &#x60;client_secret_basic&#x60;, which is what they use. | [default to 'client_secret_basic']
**signing_alg** | [**WebhookOauthSigningAlg**](WebhookOauthSigningAlg.md) | Algorithm of the key pairs, and of the assertions signed with them. Present only when &#x60;authMethod&#x60; is &#x60;private_key_jwt&#x60;. Which key is signing is never returned; each assertion names it in its &#x60;kid&#x60; header. Defaults to &#x60;RS256&#x60; on create only. | [optional] 
**custom_jwt_claims** | **List[str]** | Names of the additional claims placed in the JWT assertion. Claim values are write-only and are never returned. Absent when no custom claims are configured. | [optional] 
**custom_body_params** | **List[str]** | Names of the additional parameters added to the token request body. Parameter values are write-only and are never returned. Absent when no custom parameters are configured. | [optional] 
**webhook_custom_headers_id** | **str** | The id of the set of custom headers added to **the token request sent to the authorization server** — not to the webhook delivery. Absent when the token request adds none. Header values are write-only and are never returned; read the header names from &#x60;/v1/webhooks_settings/custom_headers/{webhookCustomHeadersId}&#x60;. | [optional] 
**webhook_mtls_id** | **str** | The id of the mTLS configuration presented to the token endpoint. Absent when the token request does not use mTLS. Read the certificate from &#x60;/v1/webhooks_settings/mtls/{id}&#x60;. | [optional] 
**created_at** | **int** | The date and time the OAuth credentials were created, in milliseconds. | 
**updated_at** | **int** | The date and time the OAuth credentials were last updated, in milliseconds. | 
**jwks_uri** | **str** | The public URL of these credentials&#39; JWKS. Register it as the client&#39;s jwks_uri on your authorization server. Present for private_key_jwt only. | [optional] [readonly] 

## Example

```python
from fireblocks.models.webhook_oauth_credentials import WebhookOauthCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOauthCredentials from a JSON string
webhook_oauth_credentials_instance = WebhookOauthCredentials.from_json(json)
# print the JSON string representation of the object
print(WebhookOauthCredentials.to_json())

# convert the object into a dict
webhook_oauth_credentials_dict = webhook_oauth_credentials_instance.to_dict()
# create an instance of WebhookOauthCredentials from a dict
webhook_oauth_credentials_from_dict = WebhookOauthCredentials.from_dict(webhook_oauth_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


